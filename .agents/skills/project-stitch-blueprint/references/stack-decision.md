# Stack Decision Guide

Use this to pick ONE concrete stack when user has no preference.

## 1. Default choice (admin-heavy SME, India - e.g. Ojas type projects)

**Laravel 11 + Blade + Livewire + MySQL 8 + Laravel Breeze/Auth + Shared VPS/cPanel**
- Why: fast to build, easy admin panel, cheap hosting, Hindi/English content easy, client can manage.
- Use when: business website + admin manages content/users/orders/bookings, SEO needed, budget low.
- Packages: spatie/laravel-permission (roles: admin/staff/user), livewire, maatwebsite/excel for reports.
- Deployment: Hostinger / Hetzner + Forge / cPanel, Cloudflare.

## 2. E-commerce / Booking

Same as above + Razorpay / Stripe + laravel-cashier equivalent.
If 10k+ products, realtime filters: Laravel API + Next.js frontend + MySQL + Redis + Meilisearch.

## 3. SaaS / Dashboard-heavy / SPA

**Laravel 11 API + Next.js 14 (App Router) + PostgreSQL + Clerk/NextAuth + Tailwind + Vercel + Railway/Render**
- Why: great UX, role dashboards, subscriptions.
- Use when: user dashboard complex, charts, realtime.

## 4. Simple static / portfolio / landing

**Next.js or Astro + Tailwind + Markdown CMS / Strapi** - deploy Vercel/Netlify.

## 5. Mobile-app future needed

**Laravel API + Flutter / React Native** - keep API REST from day 1.

## Output format (write into PROJECT_DOC.md)

| Layer | Choice | Version / Note |
|---|---|---|
| Backend | Laravel | 11, PHP 8.2 |
| Frontend | Blade + Livewire + Tailwind | 3.4 |
| DB | MySQL | 8.0 |
| Auth | Breeze + spatie roles | user/admin |
| Storage | S3 / local public | |
| Payment | Razorpay | if needed |
| Deploy | Hetzner/Shared + Cloudflare | |

Always include justification in 2-3 lines.
