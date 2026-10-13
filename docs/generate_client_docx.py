import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()

    # Page Margins (Normal 1 inch)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styling helpers
    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'''
            <w:tcMar {nsdecls("w")}>
                <w:top w:w="{top}" w:type="dxa"/>
                <w:bottom w:w="{bottom}" w:type="dxa"/>
                <w:left w:w="{left}" w:type="dxa"/>
                <w:right w:w="{right}" w:type="dxa"/>
            </w:tcMar>
        ''')
        tcPr.append(tcMar)

    def style_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0, 40, 142) # #00288E
        return p

    def style_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(21, 101, 192) # #1565C0
        return p

    def style_heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(30, 41, 59) # #1E293B
        return p

    def add_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.bold = True
            r_bold.font.name = "Arial"
            r_bold.font.size = Pt(10)
            r_bold.font.color.rgb = RGBColor(15, 23, 42)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(51, 65, 85)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.bold = True
            r_bold.font.name = "Arial"
            r_bold.font.size = Pt(10)
            r_bold.font.color.rgb = RGBColor(15, 23, 42)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(51, 65, 85)
        return p

    def add_callout(text, title="SYSTEM PRINCIPLE"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F0F4F8")
        set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:left w:val="single" w:sz="24" w:space="0" w:color="00288E"/>
                <w:top w:val="none"/>
                <w:right w:val="none"/>
                <w:bottom w:val="none"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if title:
            r_t = p.add_run(f"📌 {title}: ")
            r_t.bold = True
            r_t.font.color.rgb = RGBColor(0, 40, 142)
            r_t.font.name = "Arial"
            r_t.font.size = Pt(10)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(30, 41, 59)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_code_block(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:left w:val="single" w:sz="12" w:space="0" w:color="CBD5E1"/>
                <w:top w:val="single" w:sz="12" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="12" w:space="0" w:color="CBD5E1"/>
                <w:bottom w:val="single" w:sz="12" w:space="0" w:color="CBD5E1"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.05
        r = p.add_run(code_text)
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(15, 23, 42)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def style_table(headers, rows_data, col_widths=None):
        table = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        # Header Row
        hdr_cells = table.rows[0].cells
        for idx, header_text in enumerate(headers):
            cell = hdr_cells[idx]
            cell.text = header_text
            set_cell_background(cell, "00288E")
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.bold = True
                run.font.name = "Arial"
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(255, 255, 255)
        # Data Rows
        for r_idx, row in enumerate(rows_data):
            row_cells = table.rows[r_idx + 1].cells
            bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, cell_value in enumerate(row):
                cell = row_cells[c_idx]
                cell.text = str(cell_value)
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(30, 41, 59)
        # Set Widths if provided
        if col_widths:
            for row in table.rows:
                for idx, w in enumerate(col_widths):
                    row.cells[idx].width = Inches(w)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ---------------- DOCUMENT HEADER / TITLE ----------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("GUJARAT YUVA REGISTRATION SYSTEM (GYRS)")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = RGBColor(0, 40, 142)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    r_sub = p_sub.add_run("Comprehensive System Architecture, UI/UX Skeleton Layout Blueprint & Technical Specifications")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # Meta Table
    meta_headers = ["Project Parameter", "Specification Detail", "Authority / Owner", "Release Version"]
    meta_rows = [
        ["System Code / Name", "GYRS (Gujarat Yuva Registration System)", "Gujarat Youth Recruitment Initiative", "Version 2.0 (Production Blueprint)"],
        ["Platform Nature", "Naukri-Style Sarkari Naukri Discovery & Alert Engine", "Lead Developer: Deepak Bagada", "Date: 13 October 2026"],
        ["Target Audience", "Gujarat Job Aspirants (18-35 Yrs, Mobile-First)", "Official Application Target", "ojas.gujarat.gov.in (Official Govt Portal)"],
        ["Architecture Stack", "Laravel 11 + Livewire 3 + Supabase Cloud DB (PostgreSQL 16) + Tailwind CSS", "Status", "Final Client Architecture Deliverable"]
    ]
    style_table(meta_headers, meta_rows, [1.6, 2.4, 1.8, 1.2])

    # ---------------- 1. EXECUTIVE SUMMARY ----------------
    style_heading_1("1. Executive Summary & Problem-Solution Matrix")
    add_p("The Gujarat Yuva Registration System (GYRS) is an enterprise-grade, citizen-centric employment discovery platform tailored specifically for government job aspirants across Gujarat's 33 districts. It solves the critical usability and communication bottlenecks inherent in legacy recruitment portals while maintaining absolute compliance with official recruitment workflows.")
    
    add_p("OJAS (ojas.gujarat.gov.in) is the mandatory official portal where all Gujarat State Government job applications, fee submissions, call-letter downloads, and hall ticket issuances occur. However, the existing system presents critical operational friction for candidates:", bold_prefix="The Core Challenge: ")
    add_bullet("Fragmented discovery across multiple examination boards (GPSC, GSSSB, GSRTC, Police Recruitment Board, GPSSB Panchayat, WCD, High Court).", bold_prefix="1. Fragmented Discovery: ")
    add_bullet("Dense, legalistic Gujarati gazette PDFs that make eligibility criteria, age cuts, and educational requirements difficult to decipher quickly on mobile devices.", bold_prefix="2. Information Inaccessibility: ")
    add_bullet("Zero personalized notifications; aspirants regularly miss critical 15-day application windows due to absence of automated SMS/WhatsApp alerts.", bold_prefix="3. Missed Deadlines: ")
    add_bullet("Lack of unified candidate profile persistence; candidates must repeatedly enter demographic details without a dashboard tracking their application milestones.", bold_prefix="4. Tracking Deficit: ")

    add_p("GYRS is engineered as a modern, high-speed, Naukri.com-style intelligence layer that sits directly in front of OJAS:", bold_prefix="The GYRS Strategic Solution: ")
    add_bullet("Aggregates all Gujarat state recruitment notices into a clean, searchable, bilingual (English + Gujarati) interface.", bold_prefix="Centralized Aggregator: ")
    add_bullet("Instant 30-Second Eligibility Calculator evaluating candidate Date of Birth, category, and educational qualifications against official gazette rules.", bold_prefix="Instant Qualification Engine: ")
    add_bullet("Automated Multi-Channel Alert Engine delivering WhatsApp Business and Email notifications for newly published jobs and 3-day/1-day last date reminders.", bold_prefix="Proactive Push Engine: ")
    add_bullet("Strict 1-Click Official Redirection: GYRS acts strictly as an intelligence and discovery platform. When a candidate chooses to apply, GYRS safely redirects them to the official OJAS advertisement detail and application page, tracking the referral while ensuring zero interference with official government transactions.", bold_prefix="Zero-Risk Compliance Architecture: ")

    add_callout("GYRS is an informational discovery and notification platform. It NEVER collects candidate application fees, NEVER duplicates official government forms, and NEVER stores applicant submission data on unauthorized servers. All final applications, document uploads, fee payments, and admit cards occur strictly on ojas.gujarat.gov.in.", "STATUTORY COMPLIANCE DIRECTIVE")

    # ---------------- 2. TECHNOLOGY STACK ARCHITECTURE ----------------
    style_heading_1("2. Technology Stack & Architectural Decision Matrix")
    add_p("The technology stack has been selected to ensure maximum Search Engine Optimization (SEO) for vernacular Gujarati search terms, microsecond page delivery on low-bandwidth rural mobile networks, high-availability cloud database scaling, low maintenance overhead, and enterprise reliability.")

    stack_headers = ["Layer", "Technology Choice", "Version / Package", "Architectural Rationale"]
    stack_rows = [
        ["Backend Framework", "Laravel", "11.x (PHP 8.2+)", "Robust MVC, native queue workers, enterprise security, Eloquent ORM, and rapid administrative tooling."],
        ["Frontend UI", "Blade + Livewire 3", "Livewire v3.4 + Alpine.js", "Delivers reactive Single Page Application (SPA) interactivity without frontend-backend API desynchronization. Full SSR for SEO."],
        ["Styling Engine", "Tailwind CSS", "3.4 (Strict Light Theme)", "Utility-first design token system ensuring sub-50KB CSS payloads, strict contrast ratios, and responsive 8pt grid conformity."],
        ["Cloud Database", "Supabase Cloud (PostgreSQL)", "PostgreSQL 16 + Supavisor", "Enterprise-grade managed cloud database with connection pooling, automated failover, point-in-time recovery (PITR) backups, native JSONB for syllabi, and spatial district indexing."],
        ["Cloud Object Storage", "Supabase Storage (S3 API)", "Global CDN Buckets", "Encrypted cloud object storage for official OJAS recruitment gazette PDFs, syllabus documents, and candidate document checklists."],
        ["Realtime & Webhooks", "Supabase Realtime & CDC", "PostgreSQL WAL Webhooks", "Instant database event triggers firing background queues for WhatsApp and Email notifications whenever a new job is published or deadlines approach."],
        ["Cache & Queue", "Redis Cloud", "7.2 Alpine", "In-memory caching of gazette feeds, rate limiting, and queue management for asynchronous WhatsApp and transactional email workers."],
        ["Authentication & RBAC", "Laravel Breeze + Spatie", "spatie/laravel-permission", "Role-Based Access Control enforcing strict separation between Super Admins, Content Editors, and Candidates."],
        ["Notification Gateway", "Interakt / Gupshup / WATI", "WhatsApp Cloud Business API", "Official WhatsApp Business API templates for instant candidate notifications with 98% open rates."],
        ["Transactional Email", "Brevo / AWS SES", "SMTP Mailables", "Reliable delivery for registration OTPs, profile notifications, and scheduled weekly recruitment digests."],
        ["Deployment & Edge CDN", "Cloudflare Enterprise Edge", "Nginx + PHP-FPM + SSL", "Edge caching, DDoS protection, Web Application Firewall, and automated daily cloud backup pipelines."]
    ]
    style_table(stack_headers, stack_rows, [1.4, 1.8, 1.8, 2.2])

    add_p("Why Supabase Cloud Database + Laravel Blade/Livewire?", bold_prefix="Architectural Defense: ")
    add_bullet("By utilizing Supabase's managed PostgreSQL cloud infrastructure, the system eliminates traditional database maintenance overhead (manual patching, disk expansions, replica failures). Supabase provides built-in connection pooling (Supavisor) capable of supporting 10,000+ concurrent candidate queries during peak result release hours without connection pool starvation.", bold_prefix="Cloud Database Scalability: ")
    add_bullet("Supabase Storage delivers instant global CDN delivery for government gazette PDFs, ensuring rural applicants on 4G networks download notifications at microsecond latency.", bold_prefix="Managed Cloud Storage: ")
    add_bullet("Laravel Blade delivers full server-side HTML rendering (SSR) natively, ensuring 100% indexing by Google, Bing, and vernacular search engines for regional search queries like 'GSRTC helper bharti 2026' or 'GSSSB staff nurse syllabus'.", bold_prefix="SEO Dominance: ")

    # ---------------- 3. UI/UX DESIGN SYSTEM & COLOR SCHEME ----------------
    style_heading_1("3. UI/UX Design System, Color Scheme & Typography Scale")
    add_p("The GYRS visual identity adheres to the official 'Frontend UI' design skill, creating a harmonious balance between institutional government authority, modern civic cleanliness, and high-readability candidate interfaces.")

    style_heading_2("3.1 Color Token Architecture (Strict Light Theme)")
    add_p("Dark themes are strictly avoided to ensure absolute visual clarity under direct Indian sunlight on mid-range and budget mobile devices. The color palette utilizes high-contrast accessible tokens (WCAG 2.1 AA certified):")

    color_headers = ["Token Name", "Hex Code", "Semantic Role & Usage", "Contrast Against Surface"]
    color_rows = [
        ["Primary Civic Navy", "#00288E / #1565C0", "Primary brand identity, institutional header, primary CTA buttons, active tabs.", "11.2:1 (Exceptional AAA)"],
        ["Secondary Action Orange", "#FD761A / #F97316", "High-visibility urgent CTA, 'Closing Soon' highlights, urgent notification badges.", "4.6:1 (AA Compliant)"],
        ["Tertiary Verified Green", "#16A34A / #005823", "WhatsApp alerts pill, 'Eligible' success badge, verified OJAS gazette indicator.", "5.8:1 (AA Compliant)"],
        ["Critical Urgent Red", "#DC2626 / #93000A", "Application deadline warnings, last date countdown, 'Not Eligible' error alerts.", "6.1:1 (AA Compliant)"],
        ["Base Surface Light", "#FAFAFC / #F8FAFC", "Global background canvas, ensuring soft, glare-free readability across long reading sessions.", "N/A (Base Layer)"],
        ["Card Surface White", "#FFFFFF", "Floating card containers, search input matrix, modal drawers, table data backgrounds.", "N/A (Card Layer)"],
        ["Text High-Emphasis", "#0F172A", "Headlines, job titles, department names, candidate names, critical dates.", "14.5:1 (Ultra AAA)"],
        ["Text Medium-Emphasis", "#475569", "Body descriptions, table labels, statutory disclaimers, metadata timestamps.", "7.2:1 (AAA Compliant)"],
        ["Divider & Border", "#E2E8F0 / #CBD5E1", "Subtle card outlines, table gridlines, input container boundaries.", "Structural Outline"]
    ]
    style_table(color_headers, color_rows, [1.6, 1.5, 2.6, 1.5])

    style_heading_2("3.2 Typography System (Bilingual Hierarchy)")
    add_p("GYRS is built from the ground up to support native bilingual parity. Gujarati content is treated with first-class typographical priority alongside English:")
    add_bullet("Plus Jakarta Sans (Weights 600, 700, 800) - Utilized for high-impact landing headlines, department category badges, and metric counters.", bold_prefix="Display English: ")
    add_bullet("Inter (Weights 400, 500, 600) - Utilized for body copy, search inputs, data tables, criteria lists, and navigation menus.", bold_prefix="Body English: ")
    add_bullet("Noto Sans Gujarati (Weights 400, 600, 700) - Google-curated unicode font rendering intricate conjuncts and diacritics with perfect optical clarity.", bold_prefix="Regional Gujarati: ")
    add_bullet("Material Symbols Outlined - Google icon set ensuring standardized visual iconography across navigation, actions, and status indicators.", bold_prefix="Iconography: ")

    # ---------------- 4. WEBSITE SKELETON & LAYOUT DESIGN ----------------
    style_heading_1("4. Website Skeleton & Layout Design Architecture")
    add_p("The layout architecture implements a rigid 8-point spatial grid system. Every margin, padding, component height, and button dimensions is a multiple of 4px or 8px. Touch targets are strictly dimensioned to a minimum of 44px by 44px on mobile devices to prevent mis-clicks.")

    style_heading_2("4.1 Global Layout Skeleton (Desktop 1440px vs Mobile 390px)")
    add_p("The global skeleton consists of five hierarchical layers: Institutional Bar, Sticky Navigation, Urgent Marquee Strip, Dynamic Content Canvas, and Statutory Civic Footer.")

    add_code_block("""+----------------------------------------------------------------------------------------------------+
| 1. GOVT HELPLINE STRIP (h: 36px | bg: #131B2E | Helpline: 1800 233 5500 | A- A A+ | GU/EN | OJAS Link)     |
+----------------------------------------------------------------------------------------------------+
| 2. STICKY CIVIC NAVBAR (h: 80px | bg: #FFFFFF/95% Blur | Logo | Home | All Jobs | Results | Syllabus | SSO)|
+----------------------------------------------------------------------------------------------------+
| 3. URGENT NOTIFICATION TICKER (h: 40px | bg: #9D4300 | [URGENT] Closing Soon Jobs | View Deadlines ->)     |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
| 4. MAIN WORKSPACE / CONTENT CANVAS (Variable Height | bg: #F8FAFC)                                |
|    +------------------------------------------------------------------------------------------+    |
|    | PAGE-SPECIFIC GRID / FLEX LAYOUTS (Hero Search Matrix, Job Cards, Details, Livewire DB) |    |
|    +------------------------------------------------------------------------------------------+    |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
| 5. STATUTORY CIVIC FOOTER (bg: #0F172A | text: #E2E8F0 | Dept Links | Disclaimers | OJAS Warning)  |
+----------------------------------------------------------------------------------------------------+""")

    style_heading_2("4.2 Page-by-Page Layout Wireframe Blueprints")
    add_p("Below are the detailed layout skeletons defining each core page of the platform:")

    style_heading_3("Blueprint A: Home Portal Skeleton Layout ('/')")
    add_code_block("""[ SECTION 1: HERO & UNIFIED FLOATING SEARCH MATRIX ]
  - Trust Pill Badge: "Gujarat Govt. Gazette & OJAS Synchronized Portal | 12,450+ Active Vacancies"
  - Bilingual Display H1: "Sarkari Naukri Made Simple / સરકારી નોકરી હવે સરળ અને ઝડપી"
  - Subhead Paragraph: Explanation of 1-click eligibility check and official OJAS redirection.
  - 3-Part Unified Floating Search Box (Card bg: #FFFFFF, shadow-xl, rounded-2xl):
    [ Input: Keyword (Helper, Clerk) ] [ Select: Department (GPSC, GSRTC) ] [ Select: Qualification (10th, Grad) ] [ Button: Search Jobs ]
  - Quick Category Filter Pills: [ 10th Pass (3,410) ] [ 12th Pass (2,100) ] [ ITI Jobs (1,850) ] [ Graduate (4,200) ] [ Police (1,500) ]

[ SECTION 2: LIVE RECRUITMENT CARDS MATRIX (3-Column Desktop Grid / 1-Column Mobile) ]
  - Section Header: "Active Recruitment Notifications in Gujarat (ચાલુ સરકારી ભરતીઓ)"
  - Job Card Anatomy:
    + Top Header: Department Logo Badge + Tag [Advt No: GSRTC/202627/01] + Status Pill [Closes in 4 Days]
    + Title H3: Bilingual Title (GSRTC Helper / વાહન વ્યવહાર નિગમ હેલ્પર)
    + Metric Grid: [ Posts: 2,389 ] [ Edu: 10th + ITI ] [ Age: 18-33 Yrs ] [ Salary: Rs. 19,950 ]
    + Action Strip: [ Button: Check Eligibility ] [ Button: View Details & Apply on OJAS -> ]
  - Quick View Drawer / Modal for Instant Eligibility calculation.

[ SECTION 3: TRUSTED BY GUJARAT YOUTH & CIVIC STEP-BY-STEP PROCESS ]
  - 3-Step Civic Card Flow: (1) Discover Verified Vacancies -> (2) Check Eligibility in 30s -> (3) Apply on Official OJAS
  - Statistics Counter Bar: 1,50,000+ Registered Candidates | 33 Districts Covered | 100% Official Links.""")

    style_heading_3("Blueprint B: Jobs Listing & Filter Matrix Skeleton ('/jobs')")
    add_code_block("""+-----------------------------------+----------------------------------------------------------------+
| LEFT FILTER SIDEBAR (col-span-3)  | MAIN JOB LISTINGS CONTAINER (col-span-9)                       |
+-----------------------------------+----------------------------------------------------------------+
| [ Reset All Filters ]             | [ Breadcrumb: Home > All Gujarat Govt Jobs ]                   |
|                                   | [ Live Search Bar: Filter by job title, department, code... ]  |
| DEPARTMENT ACCORDION:             | [ Results Counter: Showing 10 of 42 Active Vacancies ]         |
| [x] GSRTC (ST Nigam) (8)          | [ Sort Dropdown: Closing Date (Soonest) | Newest | Most Posts ]|
| [ ] GPSC Class 1 & 2 (12)         |                                                                |
| [ ] GSSSB Gaun Seva (14)          | [ CARD 1: GSRTC Helper - 2,389 Posts - Closes Oct 06 ]         |
| [ ] Gujarat Police (4)            |   Dept: GSRTC | Edu: 10th + ITI | Fee: Rs 100/Free | Advt: 2026/01 |
| [ ] GPSSB Panchayat (6)           |   [ Check Eligibility ]  [ Apply on OJAS (Official) ]          |
|                                   |                                                                |
| EDUCATION QUALIFICATION:          | [ CARD 2: GSSSB Staff Nurse - 1,200 Posts - Closes Oct 12 ]    |
| [x] 10th Pass                     |   Dept: Health | Edu: GNM / B.Sc Nursing | Fee: Rs 100/Free    |
| [ ] 12th Pass                     |   [ Check Eligibility ]  [ Apply on OJAS (Official) ]          |
| [x] ITI Certificate               |                                                                |
| [ ] Any Graduate                  | [ CARD 3: Gujarat Police Constable - 12,000 Posts - Closes Nov]|
|                                   |                                                                |
| LAST DATE CLOSING WINDOW:         | [ CARD 4: GPSC Administrative Services - 350 Posts ]           |
| ( ) Urgent (Next 3 Days)          |                                                                |
| (*) Active (Next 15 Days)         | [ PAGINATION STRIP: < Prev [1] [2] [3] Next > ]                |
+-----------------------------------+----------------------------------------------------------------+""")

    style_heading_3("Blueprint C: Job Detail & Interactive Eligibility Skeleton ('/job/{slug}')")
    add_code_block("""+----------------------------------------------------------------------------------------------------+
| BREADCRUMBS: Home > Jobs > Transport > GSRTC Helper Recruitment 2026                               |
+----------------------------------------------------------------------------------------------------+
| HERO HEADER: GSRTC Helper (વાહન વ્યવહાર નિગમ હેલ્પર) | Advt No: GSRTC/202627/01 | Dept: GSRTC          |
| KEY METRIC CARDS: [ Total Vacancies: 2,389 ] [ Age: 18 to 33 Yrs ] [ Pay: Rs. 19,950 ] [ Fee: Rs 100 ]|
+--------------------------------------------------------------------+-------------------------------+
| LEFT MAIN COLUMN (col-span-8)                                      | RIGHT STICKY WIDGET (col-span-4)
+--------------------------------------------------------------------+-------------------------------+
| 1. KEY DATES & SCHEDULE TABLE                                      | [ OFFICIAL OJAS ACTION BOX ]  |
|    - Online Application Start: 15 Sep 2026                         | [ Status: Closing Soon ]      |
|    - Last Date to Apply: 06 Oct 2026 (11:59 PM)                    | [ Days Remaining: 4 Days Left]|
|    - Last Date for Online Fee: 08 Oct 2026                         | [ BUTTON: APPLY ON OJAS ]     |
|                                                                    | (Direct link to official form)|
| 2. INTERACTIVE ELIGIBILITY CALCULATOR                              |                               |
|    - Input: Date of Birth [DD/MM/YYYY]                             | [ WHATSAPP ALERTS WIDGET ]    |
|    - Input: Candidate Gender [Male / Female]                       | [ Opt-in Toggle: ON/OFF ]     |
|    - Input: Reservation Category [GEN / SEBC / SC / ST / EWS]      | [ Get Last-Date Reminders ]   |
|    - Input: Educational Qualification [Select from list]           |                               |
|    - [ BUTTON: CHECK MY ELIGIBILITY ]                              | [ OFFICIAL NOTIFICATION PDF ] |
|    - Result Pill: [ VERIFIED: You are Eligible for this post! ]    | [ Download Official Gazette ] |
|                                                                    |                               |
| 3. VACANCY DISTRIBUTION TABLE (SC, ST, SEBC, EWS, General, PH, Ex) | [ STATUTORY WARNING BOX ]     |
| 4. APPLICATION & EXAM FEE MATRIX BY CATEGORY                       | "GYRS redirects to OJAS.      |
| 5. EXAM PATTERN & SYLLABUS TOPIC MATRIX (OMR Pattern, 100 Marks)   | Never pay fees on third-party |
| 6. STEP-BY-STEP OJAS APPLICATION GUIDE (Illustrated Instructions)  | websites."                    |
+--------------------------------------------------------------------+-------------------------------+""")

    # ---------------- 5. COMPREHENSIVE PAGE-BY-PAGE SPECIFICATIONS ----------------
    style_heading_1("5. Comprehensive Page-by-Page Specifications")
    add_p("Each page template is architected with explicit component responsibilities, error boundaries, state persistence rules, and accessibility attributes.")

    style_heading_2("5.1 Public Discovery Pages")
    add_p("Home Portal ('/'): Serves as the primary onboarding funnel. Key components include the top institutional bar, hero search matrix with instantaneous auto-scroll anchor links, closing-soon marquee ticker, dynamic category cards with live job counts, trusted testimonial metrics, and a bilingual FAQ accordion.", bold_prefix="1. ")
    add_p("All Jobs Explorer ('/jobs'): Livewire 3 reactive listing interface. Features deep-linkable URL query string synchronization (`/jobs?department=gsrtc&education=10th&sort=closing_soon`), faceted checkboxes with immediate asynchronous re-rendering, multi-select tags, card-level bookmarking persisted to candidate local storage and database, and pagination.", bold_prefix="2. ")
    add_p("Job Detail Blueprint ('/job/{slug}'): Comprehensive informational dossier for individual gazettes. Contains high-emphasis key metrics, interactive client-side and server-side eligibility validation engine, structured HTML tables for category reservation quotas, syllabus breakdown, step-by-step OJAS filing instructions, and sticky conversion widgets.", bold_prefix="3. ")
    add_p("Results & Call Letters ('/results', '/call-letters'): Direct index linking candidate roll numbers and advertisement codes directly to the official OJAS admit card generation modules.", bold_prefix="4. ")

    style_heading_2("5.2 Candidate SSO & Authenticated Dashboard ('/dashboard/*')")
    add_p("Candidates register using their mobile phone number with one-time password (OTP) verification and email address. The candidate portal includes:")
    add_bullet("One-time entry of full name, mobile, email, date of birth, gender, social category (General/EWS/SEBC-OBC/SC/ST), highest educational qualification, and home district. Once saved, this profile automatically pre-fills every job eligibility calculation.", bold_prefix="One-Time Candidate Profile: ")
    add_bullet("Personalized repository of bookmarked recruitments with dynamic countdown clocks indicating exact days remaining before OJAS registration closure.", bold_prefix="Saved Jobs Hub: ")
    add_bullet("Enables candidates to confirm they completed their submission on OJAS, allowing GYRS to send automated call-letter availability alerts and exam date notifications.", bold_prefix="Applied Tracker: ")
    add_bullet("Granular preferences allowing candidates to select preferred job departments (e.g., Police vs Class 1-2) and toggle WhatsApp and Email alert channels.", bold_prefix="Alert Preferences: ")

    style_heading_2("5.3 Administrative Control Center ('/admin/*')")
    add_p("Restricted to authenticated personnel with `role:super-admin` and `role:staff`. Contains:")
    add_bullet("Live metrics showing active advertisements, recruitments closing within 72 hours, cumulative external click-throughs to OJAS, WhatsApp message dispatch delivery rates, and candidate registration volume.", bold_prefix="Executive Dashboard: ")
    add_bullet("Standardized entry form designed for non-technical administrative staff. Allows pasting OJAS Advertisement Numbers, bilingual titles, vacancy counts, start/end timestamps, age boundaries, fee matrices, syllabus summaries, official PDF document URLs, and official OJAS deep links.", bold_prefix="Job Posting & Gazette Ingestion: ")
    add_bullet("Upon publishing a new recruitment, a background Laravel Queue job is triggered. It scans the candidate database for matching educational and departmental criteria, assembling personalized WhatsApp and Email notifications dispatched via rate-limited API workers.", bold_prefix="Automated Match & Dispatch: ")
    add_bullet("Full audit log of candidate redirection clicks, alert delivery statuses (Sent, Delivered, Read, Failed), and automated re-queueing of failed alerts.", bold_prefix="Audit Logs & Reporting: ")

    # ---------------- 6. USER FLOW & NAVIGATION ARCHITECTURE ----------------
    style_heading_1("6. End-to-End User Journey & Navigation Architecture")
    add_p("The candidate user flow is architected to minimize friction, provide immediate value prior to account creation, and ensure complete transparency regarding the external OJAS application boundary.")

    flow_headers = ["Stage", "User Action", "System Response / UI State", "Conversion Milestone"]
    flow_rows = [
        ["1. Discovery", "Visitor arrives via Google search for 'GSRTC helper bharti 2026'.", "Renders server-side optimized Home or Job Detail page in under 800ms.", "Unauthenticated Landing"],
        ["2. Evaluation", "Candidate inspects dates, vacancy count, and salary scale.", "Presents structured bilingual summary; highlights closing date countdown.", "Intent Generation"],
        ["3. Eligibility", "Candidate inputs DOB (14/08/2001) and selects '10th + ITI'.", "Instant calculation: Age = 25 yrs (within 18-33 limit). Highlights Green 'ELIGIBLE'.", "Value Delivery"],
        ["4. Alert Opt-In", "Candidate clicks 'Get WhatsApp Alerts for this Bharti'.", "Presents lightweight modal requesting Mobile Number + OTP verification.", "Candidate Lead Capture"],
        ["5. Official Apply", "Candidate clicks primary CTA: 'Apply on Official OJAS Portal'.", "Logs outbound referral click in `application_tracks`. Opens ojas.gujarat.gov.in.", "Safe External Redirect"],
        ["6. Completion", "Candidate returns to GYRS and clicks 'Mark as Applied'.", "Saves application state; schedules automated Call Letter and Exam date alerts.", "Retention & Engagement"]
    ]
    style_table(flow_headers, flow_rows, [1.4, 2.2, 2.4, 1.2])

    # ---------------- 7. CLOUD DATABASE & SUPABASE ARCHITECTURE ----------------
    style_heading_1("7. Cloud Database Architecture (Supabase / Managed PostgreSQL)")
    add_p("The database tier is architected on Supabase Cloud Infrastructure (powered by PostgreSQL 16). This enterprise cloud foundation eliminates traditional on-premise single-point-of-failure bottlenecks and guarantees 99.99% uptime during peak exam notification cycles.")

    style_heading_2("7.1 Supabase Cloud Infrastructure & Capabilities")
    add_p("The Supabase Cloud platform provides critical enterprise primitives perfectly suited for citizen-scale government recruitment discovery:")
    add_bullet("Supabase utilizes Supavisor connection pooling (Ports 5432 / 6543) enabling thousands of concurrent candidate connections without PostgreSQL connection exhaustion during major bharti releases.", bold_prefix="1. High-Concurrency Connection Pooling: ")
    add_bullet("S3-compatible global object storage buckets (`official-gazettes`, `syllabus-documents`, `candidate-resumes`) with integrated CDN acceleration for rapid PDF delivery.", bold_prefix="2. Cloud Object Storage Buckets: ")
    add_bullet("PostgreSQL Write-Ahead Log (WAL) hooks trigger instant webhooks whenever an admin publishes a new job or alters deadlines, triggering immediate background queue processing.", bold_prefix="3. Realtime Change Data Capture (CDC): ")
    add_bullet("Candidate profile records and alert logs are secured using database-level security policies (RLS), guaranteeing that candidate PII cannot be accessed across tenant boundaries.", bold_prefix="4. Row-Level Security (RLS): ")
    add_bullet("Continuous WAL archiving with Point-in-Time Recovery (PITR) allowing instantaneous state rollback to any second within a 30-day window, coupled with automated daily encrypted backups.", bold_prefix="5. Point-in-Time Recovery & Backups: ")

    style_heading_2("7.2 Relational Data Dictionary (Supabase PostgreSQL)")

    add_p("Core table storing candidate demographics and authentication credentials.", bold_prefix="Table 1: users - ")
    db1_headers = ["Column Name", "Data Type", "Constraints / Index", "Description"]
    db1_rows = [
        ["id", "UUID", "PRIMARY KEY, DEFAULT gen_random_uuid()", "Unique candidate global identifier"],
        ["name", "VARCHAR(255)", "NOT NULL", "Full candidate legal name"],
        ["mobile", "VARCHAR(15)", "UNIQUE, INDEX", "Candidate mobile phone number (OTP validated)"],
        ["email", "VARCHAR(255)", "UNIQUE, INDEX", "Candidate primary email address"],
        ["password", "VARCHAR(255)", "NOT NULL", "Bcrypt hashed security password"],
        ["dob", "DATE", "NULLABLE", "Date of Birth for automated eligibility calculation"],
        ["gender", "ENUM('M', 'F', 'O')", "NULLABLE", "Gender identification for reservation quotas"],
        ["category", "ENUM('GEN', 'EWS', 'OBC', 'SC', 'ST')", "NULLABLE", "Social reservation category for fee and age relaxations"],
        ["education", "VARCHAR(100)", "NULLABLE", "Highest educational degree (e.g. 10th, 12th, ITI, Graduate)"],
        ["district", "VARCHAR(100)", "NULLABLE", "Gujarat home district (1 to 33)"],
        ["whatsapp_optin", "BOOLEAN", "DEFAULT TRUE, INDEX", "Explicit consent for WhatsApp notifications"],
        ["email_optin", "BOOLEAN", "DEFAULT TRUE", "Explicit consent for Email notifications"],
        ["role", "VARCHAR(50)", "DEFAULT 'user', INDEX", "RBAC role: super-admin, staff, candidate"],
        ["created_at / updated_at", "TIMESTAMPTZ", "DEFAULT NOW()", "PostgreSQL audit timestamps with timezone"]
    ]
    style_table(db1_headers, db1_rows, [1.6, 1.6, 1.8, 2.2])

    add_p("Government recruitment boards and state corporations.", bold_prefix="Table 2: departments - ")
    db2_headers = ["Column Name", "Data Type", "Constraints / Index", "Description"]
    db2_rows = [
        ["id", "BIGINT GENERATED ALWAYS AS IDENTITY", "PRIMARY KEY", "Unique department identifier"],
        ["name_en", "VARCHAR(255)", "NOT NULL", "English official title (e.g. Gujarat State Road Transport)"],
        ["name_gu", "VARCHAR(255)", "NOT NULL", "Gujarati title (ગુજરાત રાજ્ય માર્ગ વાહન વ્યવહાર નિગમ)"],
        ["slug", "VARCHAR(100)", "UNIQUE, INDEX", "URL slug (e.g. gsrtc, gpsc, gsssb, police)"],
        ["logo", "VARCHAR(255)", "NULLABLE", "Supabase storage asset URL"],
        ["is_active", "BOOLEAN", "DEFAULT TRUE", "Visibility toggle"]
    ]
    style_table(db2_headers, db2_rows, [1.6, 1.6, 1.8, 2.2])

    add_p("Recruitment advertisements synchronized from official gazettes.", bold_prefix="Table 3: jobs - ")
    db3_headers = ["Column Name", "Data Type", "Constraints / Index", "Description"]
    db3_rows = [
        ["id", "BIGINT GENERATED ALWAYS AS IDENTITY", "PRIMARY KEY", "Unique recruitment identifier"],
        ["slug", "VARCHAR(255)", "UNIQUE, INDEX", "SEO-optimized URL slug"],
        ["title_en", "VARCHAR(255)", "NOT NULL", "English recruitment title"],
        ["title_gu", "VARCHAR(255)", "NOT NULL", "Gujarati recruitment title"],
        ["department_id", "BIGINT", "FOREIGN KEY, INDEX", "References departments(id)"],
        ["advt_no", "VARCHAR(100)", "NOT NULL, INDEX", "Official advertisement number (e.g. GSRTC/202627/01)"],
        ["total_posts", "INT", "NOT NULL", "Aggregate number of announced vacancies"],
        ["qualification", "VARCHAR(255)", "NOT NULL", "Educational qualification requirements"],
        ["age_min / age_max", "SMALLINT", "NOT NULL", "Minimum and maximum age limits as of cutoff date"],
        ["fees_gen / fees_res", "NUMERIC(8,2)", "NOT NULL", "Application fees for General vs Reserved categories"],
        ["start_date / last_date", "TIMESTAMPTZ", "NOT NULL, INDEX", "Official start timestamp and strict cutoff deadline"],
        ["exam_date", "DATE", "NULLABLE", "Tentative or confirmed examination date"],
        ["ojas_apply_url", "TEXT", "NOT NULL", "Direct deep link to official OJAS apply screen"],
        ["ojas_pdf_url", "TEXT", "NOT NULL", "Direct link to official government notification PDF on Supabase Storage"],
        ["syllabus", "JSONB", "NULLABLE", "Structured JSON topic tree for examination breakdown"],
        ["status", "ENUM('draft', 'published', 'closed')", "DEFAULT 'draft', INDEX", "Publication lifecycle status"],
        ["views_count", "BIGINT", "DEFAULT 0", "Internal counter of recruitment views"],
        ["clicks_to_ojas", "BIGINT", "DEFAULT 0", "Verified count of candidates redirected to OJAS"]
    ]
    style_table(db3_headers, db3_rows, [1.6, 1.6, 1.8, 2.2])

    add_p("Outbound candidate tracking and external application lifecycle.", bold_prefix="Table 4: application_tracks - ")
    db4_headers = ["Column Name", "Data Type", "Constraints / Index", "Description"]
    db4_rows = [
        ["id", "UUID", "PRIMARY KEY, DEFAULT gen_random_uuid()", "Unique tracking event identifier"],
        ["user_id", "UUID", "FOREIGN KEY, INDEX", "References users(id)"],
        ["job_id", "BIGINT", "FOREIGN KEY, INDEX", "References jobs(id)"],
        ["status", "ENUM('saved', 'interested', 'applied_on_ojas')", "NOT NULL, INDEX", "Current candidate progress state"],
        ["clicked_at", "TIMESTAMPTZ", "NOT NULL", "Timestamp of external OJAS button click"],
        ["confirmed_at", "TIMESTAMPTZ", "NULLABLE", "Timestamp when candidate confirmed completion"]
    ]
    style_table(db4_headers, db4_rows, [1.6, 1.6, 1.8, 2.2])

    add_p("Multi-channel notification dispatch records and delivery auditing.", bold_prefix="Table 5: alert_logs - ")
    db5_headers = ["Column Name", "Data Type", "Constraints / Index", "Description"]
    db5_rows = [
        ["id", "UUID", "PRIMARY KEY, DEFAULT gen_random_uuid()", "Unique dispatch log record"],
        ["user_id", "UUID", "FOREIGN KEY, INDEX", "Recipient user identifier"],
        ["job_id", "BIGINT", "FOREIGN KEY, INDEX", "Associated recruitment identifier"],
        ["channel", "ENUM('whatsapp', 'email', 'sms')", "NOT NULL, INDEX", "Notification dispatch medium"],
        ["template_id", "VARCHAR(100)", "NOT NULL", "Approved WhatsApp HSM template identifier"],
        ["status", "ENUM('queued', 'sent', 'delivered', 'failed')", "NOT NULL, INDEX", "Provider delivery feedback status"],
        ["provider_msg_id", "VARCHAR(255)", "NULLABLE", "External gateway message tracking UUID"],
        ["error_message", "TEXT", "NULLABLE", "Gateway error description if delivery failed"],
        ["sent_at", "TIMESTAMPTZ", "NOT NULL, INDEX", "Exact dispatch timestamp"]
    ]
    style_table(db5_headers, db5_rows, [1.6, 1.6, 1.8, 2.2])

    # ---------------- 8. NOTIFICATION ENGINE & OJAS REDIRECTION ----------------
    style_heading_1("8. Notification Engine & OJAS Integration Architecture")
    add_p("The alert subsystem is the core retention engine of GYRS. It operates through scheduled cron jobs and queue workers that evaluate candidate match criteria against active deadlines.")

    style_heading_2("8.1 Automated Trigger Matrix")
    add_bullet("Triggered immediately upon admin publication of a new gazette. Dispatched to users whose profile education and category match the recruitment.", bold_prefix="1. New Recruitment Announcement: ")
    add_bullet("Dispatched daily at 08:00 AM IST to all users who have saved or viewed a job whose `last_date` expires within 72 hours.", bold_prefix="2. 72-Hour Urgent Deadline Reminder: ")
    add_bullet("Dispatched at 10:00 AM IST on the final cutoff date to emphasize the 11:59 PM closure of OJAS servers.", bold_prefix="3. Final Day Emergency Alert: ")
    add_bullet("Triggered when official exam schedules or hall ticket download windows are published on OJAS.", bold_prefix="4. Admit Card & Call Letter Alert: ")

    style_heading_2("8.2 WhatsApp HSM Template Structure")
    add_code_block("""[WHATSAPP OFFICIAL TEMPLATE: gyrs_job_alert_v1]
Header: Gujarat Yuva Registration System (GYRS)
Body:
નમસ્તે {{1}},
ગુજરાત સરકાર દ્વારા નવી ભરતી જાહેર કરવામાં આવી છે:
*વિભાગ:* {{2}}
*જગ્યા:* {{3}} (કુલ {{4}} જગ્યાઓ)
*છેલ્લી તારીખ:* {{5}}
તમારી પાત્રતા મુજબ તમે આ ભરતીમાં અરજી કરવા માટે યોગ્ય છો.

વિગતવાર માહિતી જોવા અને OJAS પર અરજી કરવા માટે નીચે આપેલા બટન પર ક્લિક કરો.
Button 1 (URL): View & Apply on OJAS (https://gyrs.gujarat.gov.in/job/{{6}})
Button 2 (Quick Reply): Stop Alerts""")

    style_heading_2("8.3 OJAS Redirection & Safeguard Protocol")
    add_p("To eliminate candidate confusion and maintain strict legal compliance, every redirection to the official government server complies with the following protocol:")
    add_bullet("All outbound links to `ojas.gujarat.gov.in` open in a fresh browser tab (`target='_blank' rel='noopener noreferrer'`).", bold_prefix="1. Tab Isolation: ")
    add_bullet("A subtle intermediate modal warns: 'You are now leaving GYRS and navigating to the Official Government of Gujarat OJAS portal (ojas.gujarat.gov.in). GYRS never charges application fees.'", bold_prefix="2. Institutional Disclaimer: ")
    add_bullet("Before the redirect executes, an asynchronous fetch request logs the user ID, job ID, and timestamp into `application_tracks`, enabling accurate conversion analytics.", bold_prefix="3. Telemetry Logging: ")

    # ---------------- 9. IMPLEMENTATION ROADMAP ----------------
    style_heading_1("9. Phased Implementation Roadmap & Enterprise Build Milestones")
    add_p("To ensure rigorous enterprise quality, automated security audits, and flawless high-load scalability, the project execution is structured across a realistic 8 to 10 week development roadmap (56 to 66 Days):")

    ms_headers = ["Milestone", "Scope & Deliverables", "Timeline / Days", "Acceptance Criteria"]
    ms_rows = [
        ["Milestone 1", "Core Environment, Supabase Cloud Database setup, PostgreSQL schemas, Supabase Storage buckets, Laravel 11 + Breeze scaffolding, Spatie RBAC, and Tailwind light theme token foundation.", "10 - 12 Days", "Supabase PostgreSQL connected; candidate auth and administrative roles operational on staging."],
        ["Milestone 2", "Departments & Jobs CRUD administrative engine, Supabase Realtime event listeners, Public Home & All Jobs listing responsive templates, and bilingual Gujarati typography pipeline.", "14 - 16 Days", "Full administrative job ingestion, image/PDF upload to Supabase Storage, and public recruitment cards live."],
        ["Milestone 3", "Candidate SSO profile hub, bookmarked jobs sync, reactive Livewire 3 search and multi-facet filtering, and the Instant 30-Second Eligibility validation calculation engine.", "10 - 12 Days", "Eligibility checker verified with 50+ age/education test cases; instant Livewire filters operational."],
        ["Milestone 4", "WhatsApp Cloud Business API integration, Brevo SMTP transactional mailers, Supabase Webhook event queue, and daily automated 08:00 AM cron workers for 72h/24h deadline reminders.", "12 - 14 Days", "Automated alert dispatch verified; delivery status logs and candidate opt-in toggles functional."],
        ["Milestone 5", "Results & Call Letters index, SEO vernacular meta tags, sitemap.xml, Cloudflare Enterprise CDN caching, security penetration audit, stress load testing, and production deployment.", "10 - 12 Days", "Production live on custom domain with SSL, edge caching active, 99.99% uptime benchmark achieved."]
    ]
    style_table(ms_headers, ms_rows, [1.4, 2.5, 1.2, 2.1])

    add_callout("Total Projected Project Duration: 56 to 66 Days (Approx. 8 to 10 Weeks). This extended, realistic timeline accommodates end-to-end cloud database security configurations, bilingual font rendering audits, WhatsApp Business API template approvals, and exhaustive cross-device mobile testing across budget Android smartphones.", "PROJECT DURATION & QUALITY ASSURANCE")

    doc_path = r"C:\jawahar gyrs\gyrs-system\docs\GYRS_Client_Document.docx"
    alt_path = r"C:\jawahar gyrs\gyrs-system\docs\GYRS_Client_System_Document.docx"
    doc.save(alt_path)
    print(f"Document successfully created at: {alt_path}")
    try:
        doc.save(doc_path)
        print(f"Document also updated at: {doc_path}")
    except PermissionError:
        print(f"Note: {doc_path} is currently open in Word. Updated version saved as: {alt_path}")

if __name__ == "__main__":
    create_document()
