# Stitch Single-Prompt Template

Output file: `./STITCH_PROMPT.md` - ONE code block to paste into stitch.google.com.

Template (fill brackets, keep under ~150 lines):

```text
Build a complete premium responsive web app UI prototype for "{PROJECT NAME}" - {one-liner}. Target audience: {audience} in India.

PAGES (generate all as clickable screens with navbar linking):
1. Home - hero with headline + CTA [Book Now / Shop Now], trust badges, stats, featured services/products (cards with image, price, rating), testimonials, CTA banner, footer
2. About - story, mission, team 3 members, values
3. Services/Shop - grid of 6-8 items with filter + search + sort UI
4. Detail page - gallery, price, description, reviews, related items, sticky Book/Buy button
5. Contact - form (name, phone, message), map placeholder, WhatsApp button, address/hours
6. Login/Register - tabs, phone+OTP + email options
7. User Dashboard - sidebar (Overview, My Bookings/Orders, Profile, Support), stats cards, table
8. Admin Dashboard - sidebar (Overview, Users, Content/Pages, Orders/Bookings, Payments, Reports, Settings), KPI cards, charts placeholder, recent table, status badges

DESIGN SYSTEM:
- Style: modern premium, clean, generous whitespace, rounded-2xl cards, soft shadows
- Colors: primary {e.g. #0E7C5B emerald}, accent {e.g. #F59E0B amber}, background #F8FAF9 light / #0B1210 dark toggle, text #111827
- Font: Plus Jakarta Sans / Inter, bold headings
- Mobile-first responsive, sticky navbar, full footer with links + socials
- Components: buttons, badges, inputs, tables, modals, toasts, empty states

RULES:
- Use REAL realistic {domain, e.g. grocery / clinic / coaching} content with Indian names, ₹ prices, phone +91-..., no lorem ipsum
- Consistent header/footer/theme across all screens
- Make all buttons/flows clickable prototype
- Light mode default with dark mode support
```

Adapt domain words (products vs services vs courses) to project type. Always include User + Admin dashboards.
