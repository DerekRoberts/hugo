# PR-Based Deployment Architecture

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         GitHub Repository                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐              ┌──────────────┐                │
│  │  main branch │              │  PR branches │                │
│  └──────┬───────┘              └──────┬───────┘                │
│         │                              │                         │
│         │ push                         │ PR events               │
│         │                              │ (open/sync/close)       │
│         ▼                              ▼                         │
│  ┌──────────────────┐          ┌──────────────────┐            │
│  │  hugo.yml        │          │  pr-preview.yml  │            │
│  │  (Production)    │          │  (PR Preview)    │            │
│  └──────┬───────────┘          └──────┬───────────┘            │
│         │                              │                         │
│         │ builds Hugo site             │ builds Hugo site       │
│         │                              │                         │
│         ▼                              ▼                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │              gh-pages branch                      │          │
│  ├──────────────────────────────────────────────────┤          │
│  │                                                    │          │
│  │  / (root)           Production Site               │          │
│  │  ├── index.html                                   │          │
│  │  ├── assets/                                      │          │
│  │  └── ...                                          │          │
│  │                                                    │          │
│  │  /pr-1/             PR #1 Preview                 │          │
│  │  ├── index.html                                   │          │
│  │  └── ...                                          │          │
│  │                                                    │          │
│  │  /pr-5/             PR #5 Preview                 │          │
│  │  ├── index.html                                   │          │
│  │  └── ...                                          │          │
│  │                                                    │          │
│  └──────────────────────────────────────────────────┘          │
│         │                              │                         │
│         └──────────────┬───────────────┘                        │
│                        │                                         │
└────────────────────────┼─────────────────────────────────────────┘
                         │
                         ▼
                  GitHub Pages
                         │
          ┌──────────────┼──────────────┐
          │              │               │
          ▼              ▼               ▼
   Production       PR Preview     PR Preview
      Site            #1              #5
  (root path)    (/pr-1/)        (/pr-5/)
```

## Event Flow

### Production Deployment (main branch)

```
┌─────────────────┐
│  Push to main   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  hugo.yml runs  │
│  • Checkout     │
│  • Setup Hugo   │
│  • Build site   │
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│  Deploy to gh-pages  │
│  • Clone branch      │
│  • Keep pr-* dirs    │
│  • Copy to root      │
│  • Commit & push     │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  GitHub Pages        │
│  updates production  │
└──────────────────────┘
```

### PR Preview Deployment

```
┌──────────────────┐
│  PR opened/sync  │
└────────┬─────────┘
         │
         ▼
┌─────────────────────┐
│  pr-preview.yml     │
│  • Checkout PR      │
│  • Setup Hugo       │
│  • Build with       │
│    PR-specific URL  │
└────────┬────────────┘
         │
         ▼
┌──────────────────────┐
│  Deploy to gh-pages  │
│  • Clone branch      │
│  • Create pr-N/ dir  │
│  • Copy build there  │
│  • Commit & push     │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  Post PR comment     │
│  with preview URL    │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  GitHub Pages        │
│  serves at /pr-N/    │
└──────────────────────┘
```

### PR Cleanup

```
┌─────────────────┐
│  PR closed      │
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│  pr-preview.yml      │
│  cleanup job         │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  Remove from         │
│  gh-pages branch     │
│  • Checkout branch   │
│  • Delete pr-N/ dir  │
│  • Commit & push     │
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  Post cleanup        │
│  confirmation        │
└──────────────────────┘
```

## URL Structure

| Type | Path | Example URL |
|------|------|-------------|
| Production | `/` | `https://derekroberts.github.io/hugo/` |
| PR Preview #1 | `/pr-1/` | `https://derekroberts.github.io/hugo/pr-1/` |
| PR Preview #5 | `/pr-5/` | `https://derekroberts.github.io/hugo/pr-5/` |
| PR Preview #42 | `/pr-42/` | `https://derekroberts.github.io/hugo/pr-42/` |

## Benefits of This Architecture

✅ **Isolated Environments** - Each PR has its own isolated preview  
✅ **Safe Production** - Production site unaffected by PR changes  
✅ **Native GitHub** - No external services, secrets, or costs  
✅ **Auto Cleanup** - Resources freed when PR closes  
✅ **Predictable URLs** - Easy to find any PR preview  
✅ **Concurrent PRs** - Multiple PR previews can coexist  

## Permissions Required

Both workflows require:
- `contents: write` - To push to gh-pages branch
- `pull-requests: write` - To post comments on PRs

These are configured in the workflow files and use `GITHUB_TOKEN` automatically.
