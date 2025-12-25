# Contact Form Setup - Quick Guide

## Problem Fixed

The contact form was showing the error: **"Form not configured yet. Please contact us at info@metacurious.ca"**

This happened because the form didn't have a Formspree endpoint configured.

## Solution

The repository has been updated to support configuring the Formspree endpoint via GitHub Secrets (recommended) or directly in `hugo.toml`.

## What You Need to Do

### 1. Create a Formspree Account (Free)

1. Go to [https://formspree.io/register](https://formspree.io/register)
2. Sign up for a free account (50 submissions/month free tier)
3. Verify your email address

### 2. Create a Form in Formspree

1. Log into Formspree
2. Click "New Form" or the "+" button
3. Give it a name like "MetaCurious Contact Form"
4. **Important**: Set the email address where you want to receive messages (e.g., `info@metacurious.ca` or your preferred contact email address)
5. Click "Create Form"

### 3. Get Your Form Endpoint

After creating the form, Formspree will show you an endpoint URL like:
```
https://formspree.io/f/xyzabc123
```

Copy this entire URL.

### 4. Configure the Endpoint in GitHub

**Option A: Using GitHub Secrets (Recommended)**

1. Go to this repository on GitHub
2. Click **Settings** (top menu)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Enter the following:
   - **Name**: `FORMSPREE_ENDPOINT`
   - **Secret**: Paste your Formspree URL (e.g., `https://formspree.io/f/xyzabc123`)
6. Click **Add secret**

**Option B: Direct Configuration in hugo.toml**

Alternatively, edit `hugo.toml` and change:
```toml
formspreeEndpoint = ""
```
to:
```toml
formspreeEndpoint = "https://formspree.io/f/xyzabc123"
```

### 5. Deploy and Test

1. If you used GitHub Secrets (Option A), just merge this PR - the next deployment will automatically use the secret
2. If you edited `hugo.toml` (Option B), commit and push that change
3. Wait for the GitHub Actions workflow to complete
4. Visit your contact page: https://derekroberts.github.io/hugo/contact/
5. Fill out and submit the test form
6. Check your email (and spam folder) for the submission

## How It Works

- The GitHub Actions workflow (`.github/workflows/hugo.yml`) now passes the `FORMSPREE_ENDPOINT` secret as an environment variable
- Hugo reads this during the build and injects it into the contact form template
- The form's `action` attribute is set to your Formspree endpoint
- When users submit the form, it sends to Formspree, which emails you

## Troubleshooting

### Still seeing "Form not configured" error?

1. Check that the `FORMSPREE_ENDPOINT` secret is set correctly in GitHub
2. Make sure you merged this PR and the workflow ran successfully
3. View the HTML source of your deployed contact page and look for `<form ... action="https://formspree.io/f/...">` - the action attribute should be present

### Not receiving emails?

1. Check your spam/junk folder
2. Log into Formspree dashboard to see if submissions are recorded there
3. Verify the email address in Formspree matches where you want to receive messages

### Form showing different error?

1. Open browser developer console (F12)
2. Try submitting the form
3. Check the Console and Network tabs for error details
4. Verify your Formspree form ID is correct

## More Information

For detailed documentation, see [CONTACT_FORM_SETUP.md](./CONTACT_FORM_SETUP.md)

## Summary

✅ **What was changed:**
- Added `formspreeEndpoint` parameter to `hugo.toml`
- Updated contact form template to use the parameter
- Modified GitHub workflow to pass `FORMSPREE_ENDPOINT` secret
- Updated documentation

✅ **What you need to do:**
1. Sign up for Formspree (free)
2. Create a form and set your email
3. Add `FORMSPREE_ENDPOINT` secret in GitHub
4. Deploy and test

That's it! Your contact form will work after these steps.
