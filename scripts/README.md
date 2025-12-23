# Scripts Directory

This directory contains utility scripts for managing the Hugo site.

## Available Scripts

### migrate_rss_feed.py

Migrates blog posts from an RSS feed to Hugo markdown format.

**Usage:**
```bash
python scripts/migrate_rss_feed.py
```

**Features:**
- Fetches RSS feed from configurable URL
- Parses feed entries with feedparser
- Converts HTML content to Markdown
- Generates Hugo front matter with metadata
- Handles duplicate filenames
- Creates safe filenames from post titles

**Configuration:**
Edit the script to change:
- `FEED_URL`: Source RSS feed URL (default: https://www.metacurious.ca/feed)
- `OUTPUT_DIR`: Destination directory (default: content/blog)

**Dependencies:**
- feedparser
- python-dateutil

Install with: `pip install -r requirements.txt`

### test_migration.py

Tests the migration script functionality with mock data.

**Usage:**
```bash
python scripts/test_migration.py
```

**What it tests:**
- Filename sanitization
- HTML to Markdown conversion
- Hugo post generation
- Front matter formatting

Creates test files in `/tmp/test_hugo_migration/` for inspection.

## Requirements

All Python dependencies are listed in `requirements.txt`:
- feedparser >= 6.0.0
- python-dateutil >= 2.8.0

## Development

### Adding New Scripts

When adding new scripts:
1. Use Python 3.7+ compatible syntax
2. Add a docstring explaining purpose and usage
3. Update this README
4. Add any new dependencies to requirements.txt
5. Make scripts executable: `chmod +x script_name.py`

### Testing

Always test scripts locally before committing:
```bash
python -m py_compile scripts/your_script.py  # Check syntax
python scripts/your_script.py                # Run the script
```

## Troubleshooting

### Import Errors

If you get import errors:
```bash
pip install --upgrade -r scripts/requirements.txt
```

### Network Issues

If the migration script can't access the RSS feed:
- Check your internet connection
- Verify the feed URL is correct and accessible
- Use the GitHub Actions workflow which has network access

### File Permissions

If you get permission errors:
```bash
chmod +x scripts/*.py
```

## See Also

- [MIGRATION.md](../MIGRATION.md) - Complete migration guide
- [.github/workflows/migrate-content.yml](../.github/workflows/migrate-content.yml) - Automated migration workflow
