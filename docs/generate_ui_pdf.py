import os
import base64
from playwright.sync_api import sync_playwright

assets_dir = r"C:\jawahar gyrs\gyrs-system\docs\assets"
pdf_path = r"C:\jawahar gyrs\gyrs-system\docs\GYRS_UI_Screenshots.pdf"

def get_base64_image(filename):
    filepath = os.path.join(assets_dir, filename)
    with open(filepath, "rb") as f:
        data = f.read()
    return f"data:image/png;base64,{base64.b64encode(data).decode('utf-8')}"

img_screen_home = get_base64_image("screen_home.png")
img_screen_jobs = get_base64_image("screen_jobs.png")
img_screen_detail_upper = get_base64_image("screen_detail_upper.png")
img_screen_detail_lower = get_base64_image("screen_detail_lower.png")
img_mobile_home = get_base64_image("mobile_home.png")
img_mobile_jobs = get_base64_image("mobile_jobs.png")
img_mobile_detail = get_base64_image("mobile_detail.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GYRS UI & UX Layout Design Specification</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Noto+Sans+Gujarati:wght@400;600;700&display=swap');
  
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #0F172A;
    background: #FFFFFF;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    padding: 12mm 15mm;
    page-break-after: always;
    position: relative;
    overflow: hidden;
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
  }}

  /* Page Header & Footer */
  .doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }}
  .doc-header .brand {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 800;
    font-size: 13px;
    color: #00288E;
    letter-spacing: -0.2px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .doc-header .tag {{
    font-size: 9.5px;
    font-weight: 600;
    color: #475569;
    background: #F1F5F9;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  
  .doc-footer {{
    margin-top: auto;
    border-top: 1px solid #E2E8F0;
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 9px;
    color: #64748B;
  }}

  /* Typography */
  h1, h2, h3, h4 {{
    font-family: 'Plus Jakarta Sans', sans-serif;
  }}
  
  .section-title {{
    font-size: 16px;
    font-weight: 800;
    color: #00288E;
    margin-bottom: 3px;
  }}
  .section-subtitle {{
    font-size: 10px;
    color: #475569;
    margin-bottom: 10px;
    line-height: 1.4;
  }}

  /* Screen Frame */
  .screen-frame {{
    width: 100%;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
    background: #F8FAFC;
    margin-bottom: 10px;
    position: relative;
  }}
  .screen-frame img {{
    width: 100%;
    display: block;
    object-fit: cover;
  }}

  /* Callout grid */
  .callout-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-top: 4px;
  }}
  .callout-card {{
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-left: 3px solid #00288E;
    border-radius: 6px;
    padding: 6px 8px;
  }}
  .callout-card.alt {{
    border-left-color: #FD761A;
  }}
  .callout-card.green {{
    border-left-color: #16A34A;
  }}
  .callout-title {{
    font-size: 9.5px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 2px;
  }}
  .callout-desc {{
    font-size: 8.5px;
    color: #475569;
    line-height: 1.35;
  }}

  /* Cover Page */
  .cover-page {{
    background: linear-gradient(135deg, #001453 0%, #00288E 60%, #1565C0 100%);
    color: #FFFFFF;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 25mm 20mm;
  }}
  .cover-card {{
    background: #061C68;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 16px;
    padding: 34px 28px;
    width: 100%;
    max-width: 170mm;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
  }}
  .cover-logo-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #0A247A;
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 22px;
  }}
  .cover-title {{
    font-size: 26px;
    font-weight: 800;
    line-height: 1.25;
    letter-spacing: -0.5px;
    margin-bottom: 12px;
    color: #FFFFFF;
  }}
  .cover-subtitle {{
    font-size: 13px;
    color: #DDE1FF;
    font-weight: 500;
    line-height: 1.5;
    margin-bottom: 24px;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
  }}
  .cover-divider {{
    height: 1px;
    background: rgba(255, 255, 255, 0.2);
    margin: 20px 0;
  }}
  .cover-meta {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    text-align: left;
    font-size: 10px;
  }}
  .cover-meta-item {{
    background: #051652;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.12);
  }}
  .cover-meta-label {{
    color: #A8B8FF;
    font-size: 9px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 3px;
  }}
  .cover-meta-value {{
    color: #FFFFFF;
    font-weight: 600;
    font-size: 10.5px;
  }}

  /* Swatches */
  .swatch-group {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    margin: 8px 0 14px 0;
  }}
  .swatch-box {{
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
    background: #FFFFFF;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  .swatch-color {{
    height: 28px;
    width: 100%;
  }}
  .swatch-info {{
    padding: 5px;
    font-size: 8px;
  }}
  .swatch-name {{
    font-weight: 700;
    color: #0F172A;
    font-size: 8.5px;
  }}
  .swatch-hex {{
    color: #64748B;
    font-family: monospace;
  }}

  /* Wireframe box */
  .wireframe-container {{
    background: #F8FAFC;
    border: 1px dashed #94A3B8;
    border-radius: 8px;
    padding: 10px;
    font-family: 'Consolas', monospace;
    font-size: 8.5px;
    color: #1E293B;
    line-height: 1.4;
    white-space: pre-wrap;
    margin-bottom: 12px;
  }}

  /* Mobile Grid */
  .mobile-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 6px;
  }}
  .mobile-frame {{
    border: 2px solid #0F172A;
    border-radius: 14px;
    overflow: hidden;
    background: #FFFFFF;
    box-shadow: 0 8px 16px rgba(15, 23, 42, 0.12);
  }}
  .mobile-frame img {{
    width: 100%;
    display: block;
    height: 165mm;
    object-fit: cover;
  }}
  .mobile-label {{
    text-align: center;
    padding: 6px;
    background: #0F172A;
    color: #FFFFFF;
    font-size: 9px;
    font-weight: 700;
  }}

  /* Process steps */
  .process-flow {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 10px;
  }}
  .process-step {{
    display: flex;
    align-items: center;
    gap: 12px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 10px 14px;
  }}
  .step-number {{
    width: 28px;
    height: 28px;
    background: #00288E;
    color: #FFFFFF;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 11px;
    flex-shrink: 0;
  }}
  .step-content {{
    flex: 1;
  }}
  .step-title {{
    font-size: 10.5px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 2px;
  }}
  .step-desc {{
    font-size: 9px;
    color: #475569;
    line-height: 1.35;
  }}
</style>
</head>
<body>

  <!-- ================= PAGE 1: COVER PAGE ================= -->
  <div class="page cover-page">
    <div class="cover-card">
      <div class="cover-logo-pill">
        <span>🏛️ GUJARAT YUVA REGISTRATION SYSTEM</span>
        <span style="opacity:0.4;">|</span>
        <span style="color:#7FFC97;">OJAS INTEGRATED</span>
      </div>
      <h1 class="cover-title">
        UI/UX Architecture &<br>Wireframe Skeleton Catalog
      </h1>
      <p class="cover-subtitle">
        High-definition visual design specification, responsive screen captures, and layout blueprints for the modern Gujarat Government recruitment discovery portal.
      </p>
      
      <div class="cover-divider"></div>
      
      <div class="cover-meta">
        <div class="cover-meta-item">
          <div class="cover-meta-label">Project Code / Name</div>
          <div class="cover-meta-value">GYRS — Gujarat Yuva Registration System</div>
        </div>
        <div class="cover-meta-item">
          <div class="cover-meta-label">Client Authority</div>
          <div class="cover-meta-value">Executive Client Review Deliverable</div>
        </div>
        <div class="cover-meta-item">
          <div class="cover-meta-label">Technology Foundation</div>
          <div class="cover-meta-value">Laravel 11 + Livewire 3 + Supabase Cloud DB + Tailwind</div>
        </div>
        <div class="cover-meta-item">
          <div class="cover-meta-label">Engineering Lead / Date</div>
          <div class="cover-meta-value">Deepak Bagada | 13 October 2026</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= PAGE 2: DESIGN SYSTEM & SKELETON ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">GYRS UI/UX BLUEPRINT</div>
      <div class="tag">Section 1: Foundations</div>
    </div>

    <h2 class="section-title">Design System, Color Scheme & Layout Skeleton</h2>
    <p class="section-subtitle">
      Conforms to the Frontend UI skill guidelines: strict light theme, 8pt responsive spatial grid, accessible color contrast (WCAG 2.1 AA), bilingual Gujarati/English typography, and 44px minimum touch targets.
    </p>

    <!-- Color Tokens -->
    <div style="font-size: 11px; font-weight: 700; color: #00288E; margin-bottom: 4px;">Primary Semantic Color Palette</div>
    <div class="swatch-group">
      <div class="swatch-box">
        <div class="swatch-color" style="background:#00288E;"></div>
        <div class="swatch-info">
          <div class="swatch-name">Civic Navy</div>
          <div class="swatch-hex">#00288E</div>
        </div>
      </div>
      <div class="swatch-box">
        <div class="swatch-color" style="background:#1565C0;"></div>
        <div class="swatch-info">
          <div class="swatch-name">Brand Blue</div>
          <div class="swatch-hex">#1565C0</div>
        </div>
      </div>
      <div class="swatch-box">
        <div class="swatch-color" style="background:#FD761A;"></div>
        <div class="swatch-info">
          <div class="swatch-name">Action Orange</div>
          <div class="swatch-hex">#FD761A</div>
        </div>
      </div>
      <div class="swatch-box">
        <div class="swatch-color" style="background:#16A34A;"></div>
        <div class="swatch-info">
          <div class="swatch-name">Success Green</div>
          <div class="swatch-hex">#16A34A</div>
        </div>
      </div>
      <div class="swatch-box">
        <div class="swatch-color" style="background:#DC2626;"></div>
        <div class="swatch-info">
          <div class="swatch-name">Urgent Red</div>
          <div class="swatch-hex">#DC2626</div>
        </div>
      </div>
    </div>

    <!-- Typography & Tokens -->
    <div style="font-size: 11px; font-weight: 700; color: #00288E; margin-bottom: 4px;">Bilingual Typography & Spatial Rules</div>
    <div class="callout-grid" style="margin-bottom: 12px;">
      <div class="callout-card">
        <div class="callout-title">Plus Jakarta Sans & Inter</div>
        <div class="callout-desc">Clean, institutional sans-serif font pairing ensuring high legibility from 11px metadata to 36px hero display titles.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">Noto Sans Gujarati</div>
        <div class="callout-desc">Curated regional unicode glyphs for native Gujarati job descriptions, qualification criteria, and instructions.</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">8-Point Grid & 44px Touch</div>
        <div class="callout-desc">Standardized padding (space-xs: 4px to space-xl: 40px) with minimum 44px tap targets for error-free mobile navigation.</div>
      </div>
    </div>

    <!-- Wireframe Skeleton -->
    <div style="font-size: 11px; font-weight: 700; color: #00288E; margin-bottom: 4px;">Core Website Layout Skeleton Structure</div>
    <div class="wireframe-container">+------------------------------------------------------------------------------------------------------+
| 1. GOVT HELPLINE BAR (h: 36px | bg: #131B2E | Toll-Free: 1800 233 5500 | A- A A+ | Official OJAS Link)       |
+------------------------------------------------------------------------------------------------------+
| 2. STICKY CIVIC NAVBAR (h: 80px | bg: #FFFFFF/95% Blur | Logo | Home | All Jobs | Results | SSO Profile)     |
+------------------------------------------------------------------------------------------------------+
| 3. URGENT MARQUEE TICKER (h: 40px | bg: #9D4300 | 🚨 Closing Soon: GSRTC Helper (2,389 Posts) | Deadlines ->)|
+------------------------------------------------------------------------------------------------------+
| 4. DYNAMIC VIEWPORT WORKSPACE (bg: #F8FAFC)                                                          |
|    - Desktop: 12-Column Responsive Grid (col-span-3 Filter Sidebar + col-span-9 Livewire Cards)      |
|    - Mobile: 1-Column Fluid Stacking with Off-Canvas Filter Drawer & Sticky Bottom Action Bar        |
+------------------------------------------------------------------------------------------------------+
| 5. STATUTORY FOOTER (bg: #0F172A | text: #E2E8F0 | Board Links | Disclaimer: Redirects to ojas.gujarat.gov.in) |
+------------------------------------------------------------------------------------------------------+</div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 2 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 3: SCREEN 1 - HOME PORTAL ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SCREEN 01: HOME PORTAL</div>
      <div class="tag">Desktop Viewport (1440 × 900)</div>
    </div>

    <h2 class="section-title">Home Portal & Unified Floating Search Matrix</h2>
    <p class="section-subtitle">
      Primary candidate onboarding gateway. Combines institutional trust signals with a Naukri-style 3-part floating search engine and closing-soon recruitment cards.
    </p>

    <!-- Screenshot Frame -->
    <div class="screen-frame" style="height: 172mm;">
      <img src="{img_screen_home}" alt="GYRS Home Screen Capture">
    </div>

    <!-- Annotated Callouts -->
    <div class="callout-grid">
      <div class="callout-card">
        <div class="callout-title">1. Govt Helpline & OJAS Link</div>
        <div class="callout-desc">Official 1800 233 5500 support number, font resizer (A- A A+), and direct verification link to ojas.gujarat.gov.in.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">2. 3-Part Unified Search Matrix</div>
        <div class="callout-desc">Simultaneous filtering by Keyword, Department (GSRTC, GPSC, GSSSB), and Qualification (10th, 12th, ITI, Graduate).</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">3. Live Bharti Cards & Urgent Strip</div>
        <div class="callout-desc">Real-time closing date countdowns, vacancy metrics, and instant 1-click eligibility check modals.</div>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 3 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 4: SCREEN 2 - JOBS LISTING ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SCREEN 02: JOBS LISTING</div>
      <div class="tag">Desktop Viewport (1440 × 900)</div>
    </div>

    <h2 class="section-title">Jobs Listing & Multi-Facet Livewire Filter Matrix</h2>
    <p class="section-subtitle">
      Comprehensive examination directory with instant multi-facet filtering. Updates asynchronously without full page reload, powered by Livewire 3.
    </p>

    <!-- Screenshot Frame -->
    <div class="screen-frame" style="height: 172mm;">
      <img src="{img_screen_jobs}" alt="GYRS Jobs Listing Screen Capture">
    </div>

    <!-- Annotated Callouts -->
    <div class="callout-grid">
      <div class="callout-card">
        <div class="callout-title">1. Multi-Facet Filter Sidebar</div>
        <div class="callout-desc">Live checkboxes for Department, Qualification, Social Category, and Closing Window with immediate card updates.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">2. Rich Bilingual Job Cards</div>
        <div class="callout-desc">Displays advertisement number, salary grade (₹19,950), age criteria (18-33 Yrs), and official application fee breakdown.</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">3. OJAS Official Redirect Tag</div>
        <div class="callout-desc">Explicit "Apply on OJAS (Official)" CTA button that tracks clicks and redirects safely to the official government form.</div>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 4 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 5: SCREEN 3 - JOB DETAIL UPPER ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SCREEN 03: JOB DETAIL (UPPER)</div>
      <div class="tag">GSRTC Helper 2026 — Key Metrics & Deadlines</div>
    </div>

    <h2 class="section-title">Job Detail — Overview, Schedule & Vacancy Matrix</h2>
    <p class="section-subtitle">
      High-impact advertisement dossier presenting critical deadlines, trade distributions, and official gazette notification documents.
    </p>

    <!-- Screenshot Frame -->
    <div class="screen-frame" style="height: 172mm;">
      <img src="{img_screen_detail_upper}" alt="GYRS Job Detail Upper Section">
    </div>

    <!-- Annotated Callouts -->
    <div class="callout-grid">
      <div class="callout-card">
        <div class="callout-title">1. Metric Highlights Strip</div>
        <div class="callout-desc">Instant visual counters: 2,389 Total Vacancies, 18-33 Years Age Limit, ₹19,950 Fixed Monthly Pay, ₹100 General Fee.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">2. Critical Schedule Matrix</div>
        <div class="callout-desc">Clear dates for Application Opening, Online Application Cutoff (11:59 PM), and Challan Payment Deadline.</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">3. Category Reservation Table</div>
        <div class="callout-desc">Structured breakdown across General, EWS, SEBC/OBC, SC, ST, Female Reservation, and Ex-Servicemen quotas.</div>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 5 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 6: SCREEN 4 - JOB DETAIL LOWER ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SCREEN 04: JOB DETAIL (LOWER)</div>
      <div class="tag">Interactive Eligibility & Official Redirection</div>
    </div>

    <h2 class="section-title">Eligibility Calculator, Syllabus & OJAS Conversion</h2>
    <p class="section-subtitle">
      Candidate decision engine featuring the 30-second eligibility checker, WhatsApp alert opt-in, syllabus breakdown, and official OJAS redirection.
    </p>

    <!-- Screenshot Frame -->
    <div class="screen-frame" style="height: 172mm;">
      <img src="{img_screen_detail_lower}" alt="GYRS Job Detail Lower Section">
    </div>

    <!-- Annotated Callouts -->
    <div class="callout-grid">
      <div class="callout-card">
        <div class="callout-title">1. Instant Eligibility Checker</div>
        <div class="callout-desc">Validates DOB, gender, caste category, and education against official rules to deliver an instant Green/Red status pill.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">2. WhatsApp & Email Alert Bar</div>
        <div class="callout-desc">One-click toggle sending automated last-date reminders (72h / 24h) and admit card alerts directly to candidate WhatsApp.</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">3. Official OJAS Redirection CTA</div>
        <div class="callout-desc">Primary conversion button redirecting to ojas.gujarat.gov.in AdvtDetails with statutory safety disclaimers.</div>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 6 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 7: SCREEN 5 - MOBILE RESPONSIVE ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SCREEN 05: MOBILE EXPERIENCE</div>
      <div class="tag">Mobile Viewports (390 × 844)</div>
    </div>

    <h2 class="section-title">Mobile-First Responsive Experience & Touch UI</h2>
    <p class="section-subtitle">
      Optimized for budget Android and iOS smartphones across rural and urban Gujarat. Features single-column linear layout, off-canvas drawers, and sticky touch action bars.
    </p>

    <!-- Mobile Grid Frame -->
    <div class="mobile-grid">
      <div class="mobile-frame">
        <div class="mobile-label">MOBILE HOME PORTAL</div>
        <img src="{img_mobile_home}" alt="Mobile Home Screen">
      </div>
      <div class="mobile-frame">
        <div class="mobile-label">MOBILE FILTER DRAWER</div>
        <img src="{img_mobile_jobs}" alt="Mobile Jobs Screen">
      </div>
      <div class="mobile-frame">
        <div class="mobile-label">MOBILE DETAIL & ELIGIBILITY</div>
        <img src="{img_mobile_detail}" alt="Mobile Detail Screen">
      </div>
    </div>

    <!-- Mobile Callouts -->
    <div class="callout-grid" style="margin-top: 10px;">
      <div class="callout-card">
        <div class="callout-title">44px+ Touch Targets</div>
        <div class="callout-desc">Every interactive button, checkbox, and select dropdown complies with minimum 44px tap ergonomics.</div>
      </div>
      <div class="callout-card alt">
        <div class="callout-title">Zero Horizontal Scroll</div>
        <div class="callout-desc">Data tables automatically convert to scrollable touch containers with clear visual swipe indicators.</div>
      </div>
      <div class="callout-card green">
        <div class="callout-title">Sticky Bottom Action Bar</div>
        <div class="callout-desc">The primary 'Apply on OJAS' CTA is permanently docked to the bottom viewport for instant thumb access.</div>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 7 of 8</span>
    </div>
  </div>

  <!-- ================= PAGE 8: SCREEN 6 - SYSTEM USER FLOW ================= -->
  <div class="page">
    <div class="doc-header">
      <div class="brand">SYSTEM ARCHITECTURE</div>
      <div class="tag">End-to-End User Flow & Approval</div>
    </div>

    <h2 class="section-title">Candidate Journey & System Integration Flowchart</h2>
    <p class="section-subtitle">
      Architectural workflow demonstrating candidate onboarding, personalized alert triggers, official government portal handoff, and post-application exam tracking.
    </p>

    <!-- Process Steps -->
    <div class="process-flow">
      <div class="process-step">
        <div class="step-number">1</div>
        <div class="step-content">
          <div class="step-title">Discovery & Search (SEO + Social Channels)</div>
          <div class="step-desc">Candidate lands on GYRS via Google Search, WhatsApp community links, or direct referral. Browses latest Gujarat recruitments.</div>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number">2</div>
        <div class="step-content">
          <div class="step-title">Instant Eligibility Check (30 Seconds)</div>
          <div class="step-desc">Candidate selects DOB and qualification. System calculates age cutoff and category relaxation instantly, displaying Green Verified pill.</div>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number">3</div>
        <div class="step-content">
          <div class="step-title">WhatsApp & Email Alert Subscription</div>
          <div class="step-desc">Candidate opts in for proactive notifications. System schedules automated alerts for 3-day and 1-day closing deadlines.</div>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number">4</div>
        <div class="step-content">
          <div class="step-title">Official Redirection to OJAS Portal</div>
          <div class="step-desc">Candidate clicks 'Apply on OJAS'. GYRS logs referral analytics and redirects safely to ojas.gujarat.gov.in to complete official submission.</div>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number">5</div>
        <div class="step-content">
          <div class="step-title">Admit Card & Call-Letter Tracking</div>
          <div class="step-desc">Candidate marks 'Applied' in GYRS dashboard. System automatically notifies candidate when official OJAS exam hall tickets are released.</div>
        </div>
      </div>
    </div>

    <!-- Statutory Compliance & Official OJAS Boundary -->
    <div style="margin-top: 18px; border-top: 1px solid #E2E8F0; padding-top: 12px;">
      <div style="background: #F0F4F8; border-left: 4px solid #00288E; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px;">
        <div style="font-size: 10.5px; font-weight: 800; color: #00288E; margin-bottom: 3px;">
          ⚖️ Official OJAS Compliance & Public Trust Assurance
        </div>
        <p style="font-size: 9px; color: #334155; line-height: 1.4;">
          GYRS is strictly engineered as a citizen-centric discovery, preparation, and proactive notification platform. 
          All final job applications, fee submissions, quota certificate verifications, and admit card issuances are conducted exclusively 
          on the official Government of Gujarat portal (<strong>ojas.gujarat.gov.in</strong>). GYRS does not duplicate official forms, charge candidate fees, 
          or store sensitive payment credentials.
        </p>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; background: #E0E7FF; padding: 7px 12px; border-radius: 6px; font-size: 9px; color: #1E40AF; font-weight: 700;">
        <span>🚀 Enterprise Delivery Schedule: 56 to 66 Days (8 to 10 Weeks)</span>
        <span>☁️ Cloud Database: Supabase (PostgreSQL 16) + Object Storage</span>
      </div>
    </div>

    <div class="doc-footer">
      <span>Gujarat Yuva Registration System (GYRS)</span>
      <span>Page 8 of 8</span>
    </div>
  </div>

</body>
</html>
"""

html_temp_path = r"C:\jawahar gyrs\gyrs-system\docs\temp_pdf_render.html"
with open(html_temp_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML render source saved to {html_temp_path}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_temp_path}", wait_until="networkidle")
    page.wait_for_timeout(1500)
    
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        prefer_css_page_size=True,
        margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"}
    )
    browser.close()

print(f"PDF successfully rendered and saved to: {pdf_path}")
print(f"PDF size: {os.path.getsize(pdf_path)} bytes")
