# How to Migrate Blog Content

This file provides quick instructions for completing the blog content migration.

## Quick Start

The migration tools are now ready. To migrate blog posts from https://www.metacurious.ca/feed:

### Option 1: GitHub Actions (Recommended - Easiest)

1. **Navigate to Actions tab** in this repository
2. **Select "Migrate Blog Content from RSS Feed"** workflow
3. **Click "Run workflow"** button (top right)
4. **Keep defaults** or customize:
   - Feed URL: `https://www.metacurious.ca/feed` (default)
   - Create PR: `true` (recommended)
5. **Click the green "Run workflow"** button

The workflow will automatically:
- ✅ Fetch the RSS feed
- ✅ Convert posts to Hugo markdown format
- ✅ Create a pull request with the changes
- ✅ Show you a summary of migrated posts

**Then:** Review the PR, test locally if needed, and merge!

### Option 2: Local Script (For Developers)

If you prefer to run locally:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run migration
python scripts/migrate_rss_feed.py

# Preview
hugo server -D

# Commit changes
git add content/blog/
git commit -m "chore: migrate blog posts from RSS feed"
git push
```

## What Happens During Migration

The migration script will:

1. **Fetch** the RSS feed from metacurious.ca
2. **Parse** all blog entries 
3. **Convert** HTML content to Markdown
4. **Extract** metadata (title, date, tags, categories)
5. **Create** markdown files in `content/blog/`
6. **Preserve** original URLs for reference

Each migrated post will look like:

```markdown
---
title: "Post Title"
date: 2024-01-15
draft: false
tags: ["tag1", "tag2"]
categories: ["Category"]
original_url: "https://www.metacurious.ca/original-post"
---

Post content in markdown format...
```

## After Migration

1. **Review** migrated posts in the PR or locally
2. **Check** that formatting looks good
3. **Adjust** any posts that need manual tweaks
4. **Merge** the PR or push your changes
5. **Deploy** happens automatically via GitHub Actions

## Need Help?

- 📖 See [MIGRATION.md](MIGRATION.md) for detailed documentation
- 🔧 See [scripts/README.md](scripts/README.md) for script details
- 🤖 See GitHub Actions logs for troubleshooting

## Files Created by This PR

- `scripts/migrate_rss_feed.py` - Main migration script
- `scripts/test_migration.py` - Test suite
- `scripts/requirements.txt` - Python dependencies
- `scripts/README.md` - Scripts documentation
- `.github/workflows/migrate-content.yml` - GitHub Actions workflow
- `MIGRATION.md` - Complete migration guide
- `HOW_TO_MIGRATE.md` - This file

## Questions?

The migration is fully automated and tested. Just run the workflow and review the results!
