# MetaCurious Website

Hugo-based website for MetaCurious.ca.

## Overview

This site is built with [Hugo](https://gohugo.io/), a fast static site generator, using the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. The site automatically deploys to GitHub Pages when pull requests are merged to the `main` branch.

## Quick Start

### Viewing the Site

The live site is available at: `https://<username>.github.io/<repository>/`

**Note:** Replace `<username>` and `<repository>` with your GitHub username and repository name.

### Making Content Changes

**⚠️ Important: Always use pull requests for changes. Do not push directly to `main`.**

1. Create a branch for your changes
2. Make your edits and commit them
3. Open a pull request
4. Review the PR preview deployment (automatically created)
5. Merge the PR when ready
6. The site will automatically rebuild and deploy after merging

### Adding New Content

```bash
# Create a new page
hugo new content/my-page.md
```

**Important:** After creating a new page, you'll need to add it to the site navigation (menu) or link to it from another page for visitors to access it. See `hugo.toml` to add menu items, or add links in your content Markdown files.

## Contact Form Setup

The contact form requires a Formspree endpoint to be configured.

📋 **Quick Setup Guide**: [SETUP_CONTACT_FORM.md](SETUP_CONTACT_FORM.md)

## Local Development

To preview changes locally before pushing:

### Prerequisites

- [Hugo v0.146.0 or higher](https://gohugo.io/installation/) (extended version required)

### Running Locally

```bash
# Install theme dependencies (first time only)
git submodule update --init --recursive

# Start local server with live reload
hugo server -D

# Site will be available at http://localhost:1313/
```

#### Troubleshooting
If changes aren't appearing in the browser, try `hugo server -D --disableFastRender` to force a full rebuild on each change (slower but more reliable).

## Site Structure

- `content/` - Markdown content files (edit these to update site content)
- `layouts/` - HTML templates (custom styling and structure)
- `static/` - Static assets (images, favicon)
- `assets/` - CSS and other processed assets
- `hugo.toml` - Site configuration (title, menu, theme settings)
- `themes/PaperMod/` - Hugo theme (via git submodule)

## Deployment

Deployment is automatic via GitHub Actions:
- **⚠️ Important**: All changes must go through pull requests (pushing directly to `main` is not allowed)
- PR preview deployments are automatically created for review
- When a PR is merged to `main`, GitHub Actions builds and deploys to GitHub Pages
- Site updates within 1-2 minutes

No manual deployment steps required.
