# Deploy GYRS to Vercel (3 minutes, free)

## Steps

1. Open **https://vercel.com/new** and log in (use your GitHub account).
2. Click **Import** next to `Deepak-ai-93/gyrs-system`.
   - If the repo is not listed, click **Adjust GitHub App Permissions** and give access.
3. In **Configure Project**, set exactly this:
   - **Root Directory:** `gyrs-site` ← click Edit and select it (most important step)
   - **Framework Preset:** `Other`
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty — defaults to `.`)
   - Environment Variables: none needed
4. Click **Deploy**. Wait ~30 seconds.
5. Done — you get a live URL like `https://gyrs-system.vercel.app`.

## URLs on the live site

| Page | URL |
|---|---|
| Home | `/` |
| Jobs | `/jobs` |
| Job Detail | `/job-detail` |

## Redeploy after changes

Just push to GitHub — Vercel auto-redeploys `main`:

```bash
git add -A
git commit -m "update site"
git push
```

## If you see 404 on `/jobs`

Root Directory is not set to `gyrs-site`. Fix: Vercel project →
Settings → General → Root Directory → `gyrs-site` → Save → redeploy
(Redeploy: Deployments tab → ⋯ → Redeploy).
