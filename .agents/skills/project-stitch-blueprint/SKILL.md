---
name: Project Stitch Blueprint
description: Turn one project idea into full blueprint - stack selection, PROJECT_DOC.md, user/admin flows, flowcharts, and single copy-paste Google Stitch prompt
---

# Project Stitch Blueprint

Turn a single vague project idea into 2 outputs:
1. `PROJECT_DOC.md` - stack, architecture, flowchart, user flow, admin flow
2. `STITCH_PROMPT.md` - single copy-paste prompt for Google Stitch to generate awesome design

## When to use

Use when user says: new project, new website, new app, stitch prompt, project doc, flowchart, PRD, blueprint.

## Workflow

### Step 1 - Collect inputs (ask if missing)

Do NOT assume. Ask via question tool if missing:
- Project name + one-line idea
- Project type: business website / admin panel / e-commerce / SaaS / portfolio / booking / LMS / other
- Preferred stack (if user has none, propose from `references/stack-decision.md`)
- Key features (3-10)
- Roles: user / admin / super-admin? Who manages what?
- Design vibe: modern / minimal / premium / colorful / dark + reference sites + brand color if any

If user gives only one line (e.g. "grocery site"), infer sensible defaults, list assumptions, continue.

### Step 2 - Decide stack

Read `references/stack-decision.md`.
Pick ONE concrete stack: Backend + Frontend + DB + Auth + Storage + Deployment.
Default if user has no preference: Laravel + Blade/Livewire + MySQL (good for admin-heavy Indian SME projects like Ojas). If SPA/SaaS needed: Laravel API + Next.js + MySQL/Postgres.

Record: language versions, packages, auth method, roles, payment if needed.

### Step 3 - Create PROJECT_DOC.md

Read `references/project-doc-template.md`.
Create `./PROJECT_DOC.md` (or `./docs/PROJECT_DOC.md` if docs/ exists) with:
1. Project overview, goals, target users
2. Tech stack table + justification + folder structure
3. Site map / page list (public, user, admin)
4. Mermaid flowcharts: overall system flowchart, user journey, admin journey
5. User management: how user registers, books, pays, tracks
6. Admin management: how admin manages users, content, orders, reports
7. Database tables (name, key fields)
8. API / routes list
9. Milestones / build order

Use Mermaid `graph TD` for flowcharts. Keep it visual and simple.

### Step 4 - Create STITCH_PROMPT.md

Read `references/stitch-prompt-template.md`.
Create `./STITCH_PROMPT.md` - ONE single prompt block user can paste into Google Stitch.

That prompt MUST contain:
- App name, purpose, audience
- Full page list (Home, About, Services, Contact, Login, Dashboard, Admin...)
- For each page: sections + content + actions
- Design system: colors (hex), fonts, spacing, rounded, shadows, light/dark
- UX rules: responsive mobile-first, navbar, footer, empty states, loading
- "Generate all screens as clickable prototype with consistent theme" instruction
- Explicit: "Do NOT use lorem ipsum, write real realistic content for [domain]"

Keep it to 1 prompt, 80-150 lines max. Copy-paste ready with ``` code block.

### Step 5 - Output

Tell user:
- Stack chosen + why (2 lines)
- Files created: `PROJECT_DOC.md`, `STITCH_PROMPT.md`
- How to use: paste STITCH_PROMPT.md into stitch.google.com, then build per PROJECT_DOC.md milestones
- Ask: "Want me to expand DB schema or API next?"

## Rules

- Always create BOTH files. Never only Stitch prompt.
- Real content, no lorem ipsum.
- Flowcharts must be Mermaid, renderable on GitHub.
- Separate User flow vs Admin flow clearly.
- Prefer simple maintainable stack over trendy stack.
