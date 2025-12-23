#!/usr/bin/env python3
"""
Script to migrate blog posts from metacurious.ca RSS feed to Hugo markdown format.

Usage:
    python scripts/migrate_rss_feed.py

Requirements:
    pip install feedparser python-dateutil
"""

import feedparser
import os
import re
from datetime import datetime
from pathlib import Path
import html


def sanitize_filename(title):
    """Convert title to a safe filename."""
    # Remove or replace special characters
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces with hyphens
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')


def html_to_markdown_simple(html_content):
    """
    Convert simple HTML to Markdown.
    For complex conversions, consider using html2text library.
    """
    if not html_content:
        return ""
    
    # Unescape HTML entities
    content = html.unescape(html_content)
    
    # Remove HTML tags for simple conversion (basic approach)
    # For production, consider using html2text library
    content = re.sub(r'<br\s*/?>', '\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<p>', '\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'</p>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.IGNORECASE)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content, flags=re.IGNORECASE)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.IGNORECASE)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content, flags=re.IGNORECASE)
    content = re.sub(r'<a href="(.*?)">(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE)
    content = re.sub(r'<h1>(.*?)</h1>', r'# \1\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h2>(.*?)</h2>', r'## \1\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'<h3>(.*?)</h3>', r'### \1\n\n', content, flags=re.IGNORECASE)
    
    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Clean up extra whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()


def extract_categories_and_tags(entry):
    """Extract categories and tags from RSS entry."""
    categories = []
    tags = []
    
    if hasattr(entry, 'tags'):
        for tag in entry.tags:
            if tag.get('term'):
                # Simple heuristic: longer terms are categories, shorter are tags
                term = tag['term']
                if len(term.split()) > 2:
                    categories.append(term)
                else:
                    tags.append(term)
    
    # If no clear distinction, put everything in tags
    if not categories and tags:
        categories = tags[:1] if tags else []
        tags = tags[1:] if len(tags) > 1 else []
    
    return categories, tags


def create_hugo_post(entry, output_dir):
    """Create a Hugo markdown post from an RSS feed entry."""
    
    # Extract post information
    title = entry.get('title', 'Untitled')
    link = entry.get('link', '')
    
    # Get publication date
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        pub_date = datetime(*entry.published_parsed[:6])
    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
        pub_date = datetime(*entry.updated_parsed[:6])
    else:
        pub_date = datetime.now()
    
    date_str = pub_date.strftime('%Y-%m-%d')
    
    # Get content
    if hasattr(entry, 'content') and entry.content:
        content = entry.content[0].value
    elif hasattr(entry, 'summary'):
        content = entry.summary
    else:
        content = entry.get('description', '')
    
    # Convert HTML to Markdown
    markdown_content = html_to_markdown_simple(content)
    
    # Extract categories and tags
    categories, tags = extract_categories_and_tags(entry)
    
    # Create filename
    filename = sanitize_filename(title)
    if not filename:
        filename = pub_date.strftime('%Y-%m-%d')
    
    filepath = output_dir / f"{filename}.md"
    
    # Handle duplicate filenames
    counter = 1
    while filepath.exists():
        filepath = output_dir / f"{filename}-{counter}.md"
        counter += 1
    
    # Create front matter
    front_matter = f"""---
title: "{title}"
date: {date_str}
draft: false
"""
    
    if tags:
        front_matter += f"tags: {tags}\n"
    
    if categories:
        front_matter += f"categories: {categories}\n"
    
    if link:
        front_matter += f"original_url: \"{link}\"\n"
    
    front_matter += "---\n\n"
    
    # Combine front matter and content
    full_content = front_matter + markdown_content
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Created: {filepath.name}")
    return filepath


def migrate_feed(feed_url, output_dir):
    """
    Fetch RSS feed and convert all entries to Hugo posts.
    
    Args:
        feed_url: URL of the RSS feed
        output_dir: Directory where markdown files will be created
    """
    print(f"Fetching RSS feed from: {feed_url}")
    
    # Parse the feed
    feed = feedparser.parse(feed_url)
    
    if feed.bozo:
        print(f"Warning: Feed parsing encountered issues: {feed.bozo_exception}")
    
    if not feed.entries:
        print("No entries found in the feed.")
        return
    
    print(f"Found {len(feed.entries)} entries in the feed.")
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Process each entry
    created_files = []
    for i, entry in enumerate(feed.entries, 1):
        print(f"\nProcessing entry {i}/{len(feed.entries)}: {entry.get('title', 'Untitled')}")
        try:
            filepath = create_hugo_post(entry, output_path)
            created_files.append(filepath)
        except Exception as e:
            print(f"Error processing entry: {e}")
            continue
    
    print(f"\n{'='*60}")
    print(f"Migration complete!")
    print(f"Created {len(created_files)} blog posts in {output_dir}")
    print(f"{'='*60}")


def main():
    """Main function."""
    # Configuration - can be overridden by environment variables
    FEED_URL = os.environ.get('FEED_URL', 'https://www.metacurious.ca/feed')
    OUTPUT_DIR = os.environ.get('OUTPUT_DIR', 'content/blog')
    
    # Get the script's directory and construct absolute path
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / OUTPUT_DIR
    
    print("="*60)
    print("MetaCurious Blog Migration Script")
    print("="*60)
    print(f"Feed URL: {FEED_URL}")
    print(f"Output Directory: {output_dir}")
    print("="*60)
    
    try:
        migrate_feed(FEED_URL, output_dir)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have the required dependencies installed:")
        print("  pip install feedparser python-dateutil")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
