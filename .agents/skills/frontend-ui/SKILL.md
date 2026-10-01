---
name: Frontend UI
description: Build or rebuild proper user-friendly frontend UI - accessible, mobile-first, light theme, working navigation and interactions
---

# Frontend UI

Build proper, user-friendly web UI. Use for: new pages, UI rebuild, UX cleanup, making Stitch output production-friendly.

## Rules (always follow)

1. **Mobile-first responsive** - single column on mobile, sidebar/drawer filters, min touch target 44px.
2. **Light theme** - bg `#F8FAFC`, cards `#FFFFFF`, primary `#1565C0`, CTA `#F97316`, success `#16A34A`, danger `#DC2626`, text `#0F172A` / `#475569`, borders `#E2E8F0`.
3. **Working navigation** - every nav link goes somewhere real. Breadcrumbs on inner pages. Sticky header. Full footer with disclaimer.
4. **Real interactions, no dead buttons** - search filters the list, toggles persist (localStorage), forms validate, countdowns show days left. If backend missing, use inline JS data.
5. **Accessibility** - semantic tags (`header/main/nav/footer`), labels on all inputs, focus-visible styles, alt text, lang attribute, Gujarati via Noto Sans Gujarati.
6. **Bilingual** - English + Gujarati titles together, never lorem ipsum, Indian names / ₹ prices / real dates.
7. **Performance** - Tailwind CDN ok for preview, system-font fallback, images lazy + with dimensions.

## Workflow

1. Read `references/ux-checklist.md`, apply every item.
2. Structure: `index.html` (home) + folder per page (`jobs/index.html`) for clean URLs. Shared header/footer markup copied per page (static, no build step).
3. Job data: one inline JS array per page (same 6 jobs everywhere: title EN+GU, dept, posts, qualification, last date, fees, OJAS url).
4. Must-have components per page type:
   - Home: gov helpline bar, hero search (working — jumps to /jobs with query), closing-soon strip, job cards, how-it-works, footer.
   - Listing: filter sidebar (dept/qualification checkboxes that actually filter), sort by closing soon, save buttons (localStorage).
   - Detail: dates/fees/eligibility tables, working eligibility checker (DOB + education → result), green "Apply on OJAS" external button, WhatsApp/Email toggles, related jobs.
5. Test: serve locally, click every link/button, check 360px mobile width.

## Output

Tell user: files changed, what now works (list interactions), what still needs backend (Laravel per PROJECT_DOC.md).
