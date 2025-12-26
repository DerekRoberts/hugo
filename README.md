# MetaCurious Website

Hugo-based website for MetaCurious.ca.

## Overview

This site is built with [Hugo](https://gohugo.io/), a fast static site generator, and automatically deploys to GitHub Pages when pull requests are merged to the `main` branch.

## Quick Start

### Viewing the Site

The live site is available at: `https://<username>.github.io/<repository>/`

**Note:** Replace `<username>` and `<repository>` with your GitHub username and repository name.

### Making Content Changes

Content files are in the `content/` directory:
- `content/_index.md` - Homepage
- `content/coach.md` - About page
- `content/services.md` - Services page
- `content/contact.md` - Contact page

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

### Building for Production

```bash
# Build the site
hugo --minify
```

The built site will be in the `public/` directory (this directory is git-ignored).

## Site Structure

- `content/` - Markdown content files (edit these to update site content)
- `layouts/` - HTML templates (custom styling and structure)
- `static/` - Static assets (images, favicon)
- `assets/` - CSS and other processed assets
- `hugo.toml` - Site configuration (title, menu, theme settings)
- `themes/PaperMod/` - Hugo theme (via git submodule)

## Theme

This site uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, which provides:
- Clean, minimalist design
- Dark/light mode toggle
- Mobile-responsive layout
- Fast performance

## Deployment

Deployment is automatic via GitHub Actions:
- **⚠️ Important**: All changes must go through pull requests (pushing directly to `main` is not allowed)
- PR preview deployments are automatically created for review
- When a PR is merged to `main`, GitHub Actions builds and deploys to GitHub Pages
- Site updates within 1-2 minutes

No manual deployment steps required. All changes should go through pull requests.

## License

Apache License 2.0 - See LICENSE file for details
