#!/usr/bin/env python3
"""
Test script for the RSS feed migration functionality.
Creates sample blog posts to verify the migration script works correctly.
"""

import sys
from pathlib import Path
from datetime import datetime

# Add the scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from migrate_rss_feed import (
    sanitize_filename,
    html_to_markdown_simple,
    extract_categories_and_tags,
    create_hugo_post
)


class MockEntry:
    """Mock RSS entry for testing."""
    def __init__(self, title, content, date=None, link='', tags=None):
        self.title = title
        self.link = link
        self.summary = content
        self.published_parsed = date.timetuple() if date else None
        if tags:
            self.tags = [{'term': tag} for tag in tags]
    
    def get(self, key, default=None):
        """Support dict-like access."""
        return getattr(self, key, default)


def test_sanitize_filename():
    """Test filename sanitization."""
    print("Testing sanitize_filename...")
    
    tests = [
        ("Hello World", "hello-world"),
        ("Test Post #1!", "test-post-1"),
        ("Multiple   Spaces", "multiple-spaces"),
        ("Special-Characters!@#$%", "special-characters"),
    ]
    
    for input_str, expected in tests:
        result = sanitize_filename(input_str)
        status = "✓" if result == expected else "✗"
        print(f"  {status} '{input_str}' -> '{result}' (expected: '{expected}')")


def test_html_to_markdown():
    """Test HTML to Markdown conversion."""
    print("\nTesting html_to_markdown_simple...")
    
    tests = [
        ("<p>Simple paragraph</p>", "Simple paragraph"),
        ("<strong>Bold text</strong>", "**Bold text**"),
        ("<em>Italic text</em>", "*Italic text*"),
        ("<a href='https://example.com'>Link</a>", "[Link](https://example.com)"),
    ]
    
    for html_input, expected in tests:
        result = html_to_markdown_simple(html_input)
        status = "✓" if expected in result else "✗"
        print(f"  {status} HTML -> Markdown conversion")


def test_create_hugo_post():
    """Test Hugo post creation."""
    print("\nTesting create_hugo_post...")
    
    # Create a temporary output directory
    output_dir = Path("/tmp/test_hugo_migration")
    output_dir.mkdir(exist_ok=True)
    
    # Create mock entries
    entries = [
        MockEntry(
            title="Test Leadership Post",
            content="<p>This is a <strong>test post</strong> about leadership coaching.</p>",
            date=datetime(2024, 1, 15),
            link="https://www.metacurious.ca/test-post",
            tags=["leadership", "coaching"]
        ),
        MockEntry(
            title="Social Justice in Action",
            content="<h2>Introduction</h2><p>Discussing social justice initiatives.</p>",
            date=datetime(2024, 2, 20),
            link="https://www.metacurious.ca/social-justice",
            tags=["social justice", "community"]
        ),
    ]
    
    created_files = []
    for entry in entries:
        try:
            filepath = create_hugo_post(entry, output_dir)
            created_files.append(filepath)
            print(f"  ✓ Created: {filepath.name}")
            
            # Verify file content
            with open(filepath, 'r') as f:
                content = f.read()
                if "---" in content and "title:" in content and "date:" in content:
                    print(f"    ✓ Valid front matter")
                else:
                    print(f"    ✗ Invalid front matter")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\n  Created {len(created_files)} test files in {output_dir}")
    
    # Show sample file content
    if created_files:
        print("\n  Sample file content:")
        print("  " + "="*58)
        with open(created_files[0], 'r') as f:
            lines = f.readlines()[:15]  # Show first 15 lines
            for line in lines:
                print(f"  {line.rstrip()}")
        print("  " + "="*58)


def main():
    """Run all tests."""
    print("="*60)
    print("RSS Migration Script Tests")
    print("="*60)
    
    try:
        test_sanitize_filename()
        test_html_to_markdown()
        test_create_hugo_post()
        
        print("\n" + "="*60)
        print("All tests completed!")
        print("="*60)
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
