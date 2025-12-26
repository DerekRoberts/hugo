# Contact Form Setup - Quick Guide

The repository uses a Formspree endpoint configured via GitHub Secrets.

## Setup

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
