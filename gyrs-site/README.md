# GYRS — Static Preview Site (Vercel)

Stitch UI prototype: Home + Jobs Listing + Job Detail. Pure static HTML.

## Preview locally

```bash
cd gyrs-site
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy to Vercel (2 min, free)

### Option A — Vercel Dashboard (no CLI)
1. Push this folder to GitHub as a repo (root = `gyrs-site/` contents).
2. Go to https://vercel.com/new → Import the repo.
3. Framework Preset: **Other**. Build command: empty. Output: `.`
4. Deploy. You get `https://gyrs-site.vercel.app`.

### Option B — Vercel CLI
```bash
npm i -g vercel
cd gyrs-site
vercel        # preview deploy
vercel --prod # production deploy
```

## Routes

| URL | File |
|---|---|
| `/` | `index.html` (Home) |
| `/jobs` | `jobs/index.html` (Listing) |
| `/job-detail` | `job-detail/index.html` (GSRTC Helper 2026) |

Nav (Home / All Jobs) is wired between pages. OJAS buttons open ojas.gujarat.gov.in in a new tab.
