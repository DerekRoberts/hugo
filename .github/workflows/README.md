# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automating the deployment of this Hugo site.

## Workflows

### 1. hugo.yml - Production Deployment

**Triggers:**
- Push to `main` branch
- Manual workflow dispatch

**What it does:**
- Builds the Hugo site with production settings
- Deploys to the root of the `gh-pages` branch
- Preserves PR preview deployments in `pr-*` subdirectories
- Updates the live production site at `https://<username>.github.io/<repository>/`

**Requirements:**
- Repository must have GitHub Pages enabled
- Pages source should be set to the `gh-pages` branch

### 2. pr-preview.yml - PR Preview Deployments

**Triggers:**
- Pull request opened, synchronized (updated), or reopened
- Pull request closed (for cleanup)

**What it does:**

**On PR opened/updated:**
- Builds the Hugo site with PR-specific baseURL
- Deploys to a PR-specific subdirectory on `gh-pages` branch (`pr-<number>/`)
- Posts a comment on the PR with the preview URL
- Updates the existing comment on subsequent pushes (no spam)

**On PR closed/merged:**
- Removes the PR preview directory from `gh-pages` branch
- Posts a cleanup confirmation comment on the PR
- Automatically cleans up resources

**Preview URL format:**
- `https://<username>.github.io/<repository>/pr-<PR_NUMBER>/`

**Requirements:**
- Workflow needs write permissions for `contents` and `pull-requests`
- These permissions are set in the workflow file

## Setup Instructions

### Initial Setup

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select the `gh-pages` branch and `/` (root) folder
   - Save the configuration

2. **Verify Permissions:**
   - The workflows are configured with the necessary permissions
   - No additional setup is needed for permissions

3. **First Deployment:**
   - Push to `main` branch or manually trigger the workflow
   - This will create the `gh-pages` branch and deploy the site

### Using PR Previews

1. **Create a pull request** - The preview workflow automatically triggers
2. **Review the preview** - Click the URL in the PR comment
3. **Make changes** - Push commits to update the preview automatically
4. **Merge or close** - The preview is automatically cleaned up

## Customization

### Hugo Version

Both workflows use Hugo v0.146.0 (extended). To change the version:

```yaml
env:
  HUGO_VERSION: 0.146.0  # Change this value
```

### Base URL

The base URL is automatically determined from the repository:

- Production: `https://<owner>.github.io/<repo>/`
- PR Preview: `https://<owner>.github.io/<repo>/pr-<number>/`

To use a custom domain, update the `CNAME` file in the `static/` directory and configure your DNS settings.

## Troubleshooting

### Workflow fails with "permission denied"

- Ensure the workflow has `contents: write` permission
- Check repository settings → Actions → General → Workflow permissions

### PR preview not accessible

- Wait a few minutes for GitHub Pages to update
- Verify the `gh-pages` branch exists and contains the `pr-*` directory
- Check that GitHub Pages is enabled and set to deploy from `gh-pages` branch

### Preview not cleaned up after PR closed

- Check the Actions tab for the cleanup job logs
- The `gh-pages` branch may need manual cleanup if the workflow failed
- You can manually remove the `pr-*` directory from the branch

### Production deployment overwrites PR previews

- The production workflow is designed to preserve `pr-*` directories
- Check the workflow logs if previews are being removed

## Architecture

Both workflows use a shared `gh-pages` branch strategy:

```
gh-pages/
├── index.html              # Production site (root)
├── assets/
├── ...
├── pr-1/                   # PR #1 preview
│   ├── index.html
│   └── ...
├── pr-2/                   # PR #2 preview
│   ├── index.html
│   └── ...
└── ...
```

This approach:
- ✅ Uses native GitHub Pages (no external services)
- ✅ No additional costs or secrets required
- ✅ Automatic cleanup on PR close
- ✅ Production and previews coexist safely
- ✅ Simple, maintainable, and reliable

## Contributing

When modifying these workflows:

1. Test changes in a fork first
2. Validate YAML syntax before committing
3. Update this README if behavior changes
4. Consider backward compatibility with existing deployments
