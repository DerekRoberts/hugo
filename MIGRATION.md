# Blog Content Migration Guide

This guide explains how to migrate blog content from the MetaCurious RSS feed to this Hugo site.

## Quick Start: Using GitHub Actions (Recommended)

The easiest way to migrate content is using the automated GitHub Actions workflow:

1. Go to the **Actions** tab in this repository
2. Select **"Migrate Blog Content from RSS Feed"** workflow
3. Click **"Run workflow"**
4. Choose options:
   - Feed URL (default: `https://www.metacurious.ca/feed`)
   - Whether to create a Pull Request (recommended: `true`)
5. Click **"Run workflow"** button

The workflow will:
- Fetch and parse the RSS feed
- Convert posts to Hugo markdown format
- Create a pull request with the migrated content (if selected)
- Provide a summary of changes

**Benefits of this approach:**
- No local setup required
- Works even if the feed requires network access
- Creates a reviewable PR before merging
- Automated and reproducible

## Manual Migration: Local Script

If you prefer to run the migration locally:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Migration Steps

#### 1. Install Dependencies

First, install the required Python packages:

```bash
pip install -r scripts/requirements.txt
```

Or install them individually:

```bash
pip install feedparser python-dateutil
```

#### 2. Run the Migration Script

#### 2. Run the Migration Script

Execute the migration script from the root of the repository:

```bash
python scripts/migrate_rss_feed.py
```

The script will:
- Fetch the RSS feed from https://www.metacurious.ca/feed
- Parse all blog entries
- Convert each entry to Hugo markdown format
- Save them to `content/blog/` directory
- Preserve metadata (title, date, tags, categories, original URL)

#### 3. Review the Migrated Content

After the migration completes, review the newly created blog posts:

```bash
ls -la content/blog/
```

Each post will:
- Have proper Hugo front matter (YAML header)
- Include the original publication date
- Contain tags and categories from the RSS feed
- Link back to the original URL
- Have content converted from HTML to Markdown

#### 4. Preview the Site Locally

Test the migrated content locally:

```bash
hugo server -D
```

Then open your browser to http://localhost:1313/hugo/ to review the blog posts.

#### 5. Adjust Content as Needed

You may want to manually review and adjust:
- Image paths (if images were referenced in the original posts)
- Complex HTML formatting that didn't convert perfectly
- Post slugs/filenames
- Draft status (all posts are set to `draft: false` by default)

#### 6. Commit and Deploy

Once you're satisfied with the migrated content:

```bash
git add content/blog/
git commit -m "chore: migrate blog posts from metacurious.ca RSS feed"
git push
```

The GitHub Actions workflow will automatically build and deploy the updated site.

## Script Features

The migration script (`scripts/migrate_rss_feed.py`) provides:

- **Automatic HTML to Markdown conversion** - Converts common HTML tags to Markdown
- **Safe filename generation** - Creates valid filenames from post titles
- **Duplicate handling** - Automatically handles posts with duplicate titles
- **Metadata preservation** - Extracts and preserves tags, categories, dates
- **Original URL tracking** - Adds `original_url` field to front matter for reference
- **Error handling** - Continues processing even if individual posts fail

## Troubleshooting

### Feed Parsing Issues

If the script reports feed parsing errors:
- Check your internet connection
- Verify the feed URL is accessible: https://www.metacurious.ca/feed
- Look for specific error messages in the script output

### HTML Conversion Issues

For complex HTML that doesn't convert well:
- Manually edit the generated markdown files
- Consider using a more advanced HTML to Markdown library (e.g., `html2text`)

### Missing Dependencies

If you get import errors:
```bash
pip install --upgrade feedparser python-dateutil
```

## Customization

To customize the migration:

1. Edit `scripts/migrate_rss_feed.py`
2. Modify the `FEED_URL` variable to change the source feed
3. Adjust the `OUTPUT_DIR` to change where posts are saved
4. Customize the `html_to_markdown_simple()` function for better HTML conversion

## Manual Migration Alternative

If the automated script doesn't work for your use case, you can manually migrate posts:

1. Visit https://www.metacurious.ca/feed in your browser
2. Copy the content of each blog post
3. Create new files in `content/blog/` using this template:

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
original_url: "https://www.metacurious.ca/original-post"
---

Your post content here...
```

4. Use `hugo new content/blog/post-name.md` to create new posts with proper archetypes

## Additional Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Markdown Guide](https://www.markdownguide.org/)
- [feedparser Documentation](https://feedparser.readthedocs.io/)
