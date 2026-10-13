"""GYRS Portal UI/UX screenshot + explain PDF generator (job portal only, no tenders, no OJAS).

Captures desktop screenshots of every portal surface (Home, All Jobs, Job Detail,
Auth, User Dashboard, Skills, Admin Dashboard/Jobs/Add-Job) with demo sessions
injected via localStorage (no manual login needed), then renders an explained
A4 PDF gallery via Chromium print.
"""
import base64
import io
import os

import fitz  # PyMuPDF — PDF page raster check (kept for tooling)
from PIL import Image  # slice tall screenshots into exact-fit print pages
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000"
ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets", "portal_v2")
PDF_PATH = os.path.join(ROOT, "GYRS_Portal_UI_UX.pdf")
HTML_TMP = os.path.join(ROOT, "temp_portal_pdf.html")

os.makedirs(ASSETS, exist_ok=True)

USER_SEED_JS = """() => {
  localStorage.setItem("gyrs_session", JSON.stringify({email:"priya@example.com",role:"user"}));
  try {
    const users = JSON.parse(localStorage.getItem("gyrs_users")) || [];
    const i = users.findIndex(u => u.email === "priya@example.com");
    if (i >= 0) {
      users[i].skills = ["computer","gujarati typing","record keeping","ccc","typing 30wpm"];
      users[i].saved = ["gpssb-talati-2026","hc-assistant-2026","gsrtc-helper-2026"];
      users[i].applied = ["police-constable-2026"];
      localStorage.setItem("gyrs_users", JSON.stringify(users));
    }
  } catch(e) {}
}"""

ADMIN_SEED_JS = """() => {
  localStorage.setItem("gyrs_session", JSON.stringify({email:"admin@gyrs.in",role:"admin"}));
  localStorage.setItem("gyrs_activity", JSON.stringify([
    {t:"13/10/2026, 2:30:00 pm", msg:"Downloaded report: gyrs-jobs-report.csv"},
    {t:"13/10/2026, 2:20:00 pm", msg:"Added job: Staff Nurse Class-III (GSSSB/202627/192)"},
    {t:"13/10/2026, 2:05:00 pm", msg:"Blocked user: demo@example.com"}
  ]));
}"""

# (shot_id, url, seed_js, click_selector, title, about, ux)
SHOTS = [
    ("01-home", "/", None, None,
     "Home — Job Discovery Gateway",
     "Hero with trust pill + live vacancy count, 3-part search (keyword, board, qualification), trending pills, Top Recruitment Boards strip, live job cards with vacancies / salary / eligibility / deadline, eligibility calculator, 3-step how-it-works and live stats.",
     "One screen answers: what jobs exist, am I eligible, how do I apply. Every card routes inward to its own Job Detail page; the candidate never leaves the portal until the final official Apply click."),
    ("02-jobs", "/jobs/", None, None,
     "All Jobs — Filterable Listing",
     "Keyword + district + sort bar, popular-filter pills, live result counter, sticky filter sidebar (urgency toggle, board, qualification, category, pay scale), WhatsApp alerts card, rich bilingual job cards with metric matrix and syllabus links.",
     "Filters narrow results without reload friction; urgency toggle surfaces closing-soon posts first so no deadline is missed."),
    ("03-job-detail", "/job-detail/?id=police-constable-2026", None, None,
     "Job Detail — Notification, Documents, Eligibility",
     "Full metric grid (vacancies, qualification, salary, location, age, fees, dates), match % for logged-in users, Save / Mark-as-Applied, tabbed Notification text + PDF download, Documents checklist, and interactive age/category eligibility checker.",
     "The single source of truth per recruitment: green Apply button opens only the recruiting board's own official website in a new tab. GYRS never collects applications or fees."),
    ("04-dashboard", "/dashboard/", USER_SEED_JS, None,
     "User Dashboard — Profile, CV Match, Tracking",
     "KPI cards (matched / saved / applied / skills), editable profile, CV upload + paste-text skill analyser, CV-scored recommended jobs, saved-jobs and applied-jobs lists.",
     "Uploading a CV instantly re-scores every job by skill overlap; missing skills point the candidate to the Skills page to unlock more opportunities."),
    ("05-skills", "/skills/", None, None,
     "Skills — Upgrade to Unlock Jobs",
     "Catalog cards (CCC, typing, ITI, nursing, GPSC prep, PET fitness, Tally+GST, Excel) each listing the recruitments they unlock, with one-click Add to my profile.",
     "Closes the loop: a locked job shows which skill unlocks it, and adding the skill immediately raises the dashboard match score."),
    ("06-admin-dash", "/admin/", ADMIN_SEED_JS, None,
     "Admin — Dashboard with Filters, Charts, Reports",
     "Global search + board + status + closing-window filters driving KPI cards, vacancies-by-board and jobs-by-status charts, and a closing-soon action list with CSV export.",
     "Production control room: filter to any slice (e.g. Police + closing in 7 days) and download exactly that slice for reminder campaigns."),
    ("07-admin-jobs", "/admin/", ADMIN_SEED_JS, '#panel aside button[data-v="jobs"]',
     "Admin — Manage Jobs",
     "Searchable, status-filterable jobs table with views/clicks telemetry, status pills and per-row View / Edit / Duplicate / Status-toggle / Delete plus one-click jobs CSV export.",
     "Full lifecycle in one table: draft → publish → close, duplicate repeat recruitments, and audit performance without leaving the page."),
    ("08-admin-add", "/admin/", ADMIN_SEED_JS, '#panel aside button[data-v="add"]',
     "Admin — Add / Edit Job (All Fields)",
     "Every field a posting needs: title, board, advt no, posts, qualification, age band, salary, location, fees, start/last/exam dates, skills, notification text, documents checklist, official Apply URL, notification PDF file picker + URL, and publish status.",
     "Saving publishes instantly to Home, All Jobs and candidate dashboards; every change is written to the Activity Log."),
]

errors = []


def capture(pw):
    browser = pw.chromium.launch()
    results = []
    for shot_id, url, seed_js, click, title, about, ux in SHOTS:
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        if seed_js:
            ctx.add_init_script(f"({seed_js})()")
        page = ctx.new_page()
        page.on("pageerror", lambda e, s=shot_id: errors.append(f"{s}: {e}"))
        page.on("console", lambda m, s=shot_id: errors.append(f"{s} console-{m.type}: {m.text}") if m.type == "error" else None)
        page.goto(BASE + url, wait_until="networkidle")
        page.wait_for_timeout(1200)
        if click:
            page.click(click)
            page.wait_for_timeout(800)
        path = os.path.join(ASSETS, shot_id + ".png")
        page.screenshot(path=path, full_page=True)
        print(f"shot {shot_id} -> {os.path.getsize(path)} bytes", flush=True)
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        results.append((shot_id, title, about, ux, b64))
        ctx.close()
    browser.close()
    return results


SLICE_H = 1950  # source px per full print page; 1950px @1440w prints ~246mm tall
FIRST_H = 1300  # first chunk shares its page with the section intro (~164mm)


def slice_png(path):
    """Split a tall screenshot into page-sized chunks; returns list of b64 PNGs.

    First chunk is shorter so it shares its page with the section intro;
    the rest are full-page sized. Nothing is cropped on any side.
    """
    img = Image.open(path)
    W, H = img.size
    bounds = []
    first = min(FIRST_H, H)
    bounds.append((0, first))
    y = first
    while y < H:
        bounds.append((y, min(y + SLICE_H, H)))
        y += SLICE_H
    if len(bounds) > 1 and bounds[-1][1] - bounds[-1][0] < 500:
        bounds[-1] = (max(0, bounds[-1][1] - SLICE_H), bounds[-1][1])  # merge sliver upward
    out = []
    for a, b in bounds:
        buf = io.BytesIO()
        img.crop((0, a, W, b)).save(buf, format="PNG")
        out.append(base64.b64encode(buf.getvalue()).decode())
    return out


def build_pdf(shots):
    def section(shot_id, title, about, ux):
        parts = slice_png(os.path.join(ASSETS, shot_id + ".png"))
        first = f"""
        <div class="firstpage">
          <div class="doc-header"><div class="brand">GYRS JOB PORTAL — UI/UX</div><div class="tag">{title}</div></div>
          <h2 class="section-title">{title}</h2>
          <div class="about"><b>What this screen does:</b> {about}</div>
          <div class="ux"><b>UX note:</b> {ux}</div>
          <div class="sframe"><img src="data:image/png;base64,{parts[0]}"/></div>
          <div class="minifoot"><span>GYRS Job Portal — full-screen capture, nothing cropped</span><span>{title} · 1/{len(parts)}</span></div>
        </div>"""
        rest = "".join(f"""
        <div class="spage">
          <div class="minihead"><span>GYRS JOB PORTAL</span><span>{title} · {i + 1}/{len(parts)}</span></div>
          <div class="sframe"><img src="data:image/png;base64,{b}"/></div>
          <div class="minifoot"><span>GYRS Job Portal — full-screen capture, nothing cropped</span><span>{title}</span></div>
        </div>""" for i, b in enumerate(parts[1:], start=1))
        return first + rest

    pages = "".join(section(s, t, a, u) for s, t, a, u, _ in shots)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
      @page {{ size: A4 portrait; margin: 0; }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{ font-family: Arial, sans-serif; color: #0F172A; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
      .page {{ width: 210mm; min-height: 297mm; padding: 12mm 14mm 10mm 14mm; page-break-after: always; display: flex; flex-direction: column; background: #fff; }}
      .page.single {{ height: 297mm; overflow: hidden; }}
      .cover {{ background: linear-gradient(135deg,#001453,#00288E 60%,#1565C0); color: #fff; justify-content: center; align-items: center; text-align: center; }}
      .cover h1 {{ font-size: 28px; margin: 14px 0; }}
      .cover p {{ color: #DDE1FF; font-size: 13px; max-width: 150mm; line-height: 1.6; }}
      .cover .pill {{ display: inline-block; border: 1px solid rgba(255,255,255,.4); border-radius: 999px; padding: 6px 16px; font-size: 11px; font-weight: bold; letter-spacing: 1px; }}
      .doc-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; margin-bottom: 8px; }}
      .brand {{ font-weight: 800; font-size: 12px; color: #00288E; }}
      .tag {{ font-size: 9px; font-weight: 700; color: #475569; background: #F1F5F9; padding: 3px 8px; border-radius: 4px; text-transform: uppercase; }}
      .section-title {{ font-size: 16px; color: #00288E; margin-bottom: 8px; break-inside: avoid; break-after: avoid; }}
      .intro {{ padding: 12mm 14mm 6mm 14mm; break-inside: avoid; page-break-after: avoid; }}
      .firstpage {{ width: 210mm; height: 297mm; padding: 10mm 14mm 8mm 14mm; page-break-after: always; overflow: hidden; background: #fff; }}
      .firstpage .sframe {{ margin-top: 6px; }}
      .spage {{ width: 210mm; height: 297mm; padding: 8mm 14mm 8mm 14mm; page-break-after: always; overflow: hidden; background: #fff; }}
      .minihead {{ display: flex; justify-content: space-between; align-items: center; font-size: 9px; font-weight: 800; color: #00288E; border-bottom: 2px solid #E2E8F0; padding-bottom: 4px; margin-bottom: 4px; text-transform: uppercase; }}
      .sframe {{ border: 1px solid #CBD5E1; border-radius: 8px; overflow: hidden; }}
      .sframe img {{ width: 100%; height: auto; display: block; }}
      .minifoot {{ display: flex; justify-content: space-between; font-size: 8.5px; color: #64748B; border-top: 1px solid #E2E8F0; padding-top: 4px; margin-top: 4px; }}
      .about {{ margin-top: 8px; font-size: 10px; line-height: 1.5; color: #334155; background: #F8FAFC; border-left: 3px solid #00288E; border-radius: 6px; padding: 7px 10px; break-inside: avoid; }}
      .ux {{ margin-top: 6px; font-size: 10px; line-height: 1.5; color: #334155; background: #FFF7ED; border-left: 3px solid #FD761A; border-radius: 6px; padding: 7px 10px; break-inside: avoid; }}
      .doc-footer {{ margin-top: auto; border-top: 1px solid #E2E8F0; padding-top: 6px; display: flex; justify-content: space-between; font-size: 9px; color: #64748B; }}
      .lede {{ font-size: 10.5px; color: #475569; line-height: 1.5; margin-bottom: 8px; }}
      .skel {{ background: #F8FAFC; border: 1px dashed #94A3B8; border-radius: 8px; padding: 9px 11px; font-family: Consolas, monospace; font-size: 8.4px; line-height: 1.45; color: #1E293B; white-space: pre; overflow: hidden; margin-bottom: 8px; }}
      .flow {{ display: flex; flex-direction: column; gap: 8px; margin-top: 8px; }}
      .step {{ display: flex; gap: 10px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 9px 12px; font-size: 10px; }}
      .n {{ width: 26px; height: 26px; border-radius: 50%; background: #00288E; color: #fff; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    </style></head><body>
      <div class="page single"><div class="doc-header"><div class="brand">GYRS JOB PORTAL — BLUEPRINT</div><div class="tag">Page 01 · Layout Skeleton</div></div>
        <h2 class="section-title">Portal Layout Skeleton</h2>
        <p class="lede">Structural blueprint behind every screen in this document. The global shell (sticky header, content zone, footer note) is identical on candidate and admin surfaces, so navigation is never re-learned. Each page below it fills the content zone with its own blocks.</p>
        <div class="skel">GLOBAL SHELL — used by every page
+--------------------------------------------------------------------+
| HEADER (sticky, min-h 64px): [GYRS *] Home All-Jobs Skills .. [☰]  |
+--------------------------------------------------------------------+
| CONTENT ZONE (max-w-6xl, white rounded-2xl cards on slate bg)       |
|   -- page blocks plug in here, tables scroll inside cards --       |
+--------------------------------------------------------------------+
| FOOTER NOTE: apply only on board official sites · GYRS takes       |
| no applications and no fees                                        |
+--------------------------------------------------------------------+</div>
        <div class="skel">HOME (/)                          | ALL JOBS (/jobs/)
[H1 + trust pill + live count]      | [search | district | sort]
[search: keyword|board|qualif][Go]  | sidebar: urgency/board/qualif
[trending pills + boards strip]     | cards: badge advt deadline
[job cards: metrics + View &amp; Apply]   | title · grid · [View &amp; Apply]
[eligibility calc + how-it-works]   |
DETAIL (/job-detail/?id=..)         | DASHBOARD (/dashboard/)
[badges + H1 + match %]             | KPI row: matched/saved/applied
[metric grid x8]                    | [profile form | CV analyser]
[Apply official][Save][Applied]     | [match-ranked jobs][saved|done]
[tabs: notification|docs|eligib.]   |
SKILLS (/skills/)                   | ADMIN (/admin/)
[card: level · time]                | sidebar: dash jobs users apps
[unlocks: job pills] [+ Add]        | filter bar -&gt; KPI x4 -&gt; charts
                                    | tables -&gt; add-job form -&gt; reports</div>
        <div class="about"><b>How to read:</b> every screenshot page that follows is one of these blocks filled with real data. Nothing sits outside the shell — that is what keeps mobile free of overlaps: one sticky header with a hamburger menu, one content column, tables scrolling inside their cards.</div>
        <div class="doc-footer"><span>GYRS Job Portal — layout skeleton</span><span>job portal only · apply on board sites</span></div>
      </div>
      {pages}
      <div class="page single"><div class="doc-header"><div class="brand">GYRS JOB PORTAL — UI/UX</div><div class="tag">End-to-end flow</div></div>
        <h2 class="section-title">How the portal flows together</h2>
        <div class="flow">
          <div class="step"><div class="n">1</div><div><b>Discover</b> — Home search / All Jobs filters surface the right recruitments with vacancies, salary and deadlines visible up front.</div></div>
          <div class="step"><div class="n">2</div><div><b>Verify</b> — Job Detail tabs show the official notification, documents checklist and an eligibility checker before any commitment.</div></div>
          <div class="step"><div class="n">3</div><div><b>Apply externally</b> — The green Apply button opens that board's own official website. GYRS never takes applications or fees.</div></div>
          <div class="step"><div class="n">4</div><div><b>Track & upskill</b> — Dashboard tracks saved/applied, scores CV skill-match per job, and Skills unlocks blocked opportunities.</div></div>
          <div class="step"><div class="n">5</div><div><b>Operate</b> — Admin filters, edits, publishes, exports CSV reports and audits every action in the Activity Log.</div></div>
        </div>
        <div class="doc-footer"><span>GYRS Job Portal</span><span>generated from live localhost build</span></div>
      </div>
    </body></html>"""
    with open(HTML_TMP, "w", encoding="utf-8") as f:
        f.write(html)

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file:///" + HTML_TMP.replace("\\", "/"), wait_until="networkidle")
        pg.wait_for_timeout(1200)
        pg.pdf(path=PDF_PATH, format="A4", print_background=True, prefer_css_page_size=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        b.close()
    print(f"PDF -> {PDF_PATH} ({os.path.getsize(PDF_PATH)} bytes)")


if __name__ == "__main__":
    with sync_playwright() as pw:
        shots = capture(pw)
    build_pdf(shots)
    if errors:
        print("CONSOLE/PAGE ERRORS:")
        for e in errors:
            print(" -", e[:300])
    else:
        print("No console/page errors on captured pages.")
