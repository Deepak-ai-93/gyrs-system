# GYRS - Google Stitch Single Prompt (copy-paste)

> Paste the block below into stitch.google.com → Generate → get full clickable prototype. Light theme fixed. Then build in Laravel per PROJECT_DOC.md.

```text
Build a complete premium light-theme responsive web app UI prototype for "GYRS - Gujarat Yuva Registration System" - a Naukri-style portal for all Gujarat government exams where youth discover jobs and get WhatsApp + Email alerts, Apply always redirects to official ojas.gujarat.gov.in. Target: 18-35 Gujarat students, mobile-first, Gujarati + English.

PAGES - generate ALL as clickable screens with sticky top navbar (Home, Jobs, Results, Call Letters, Syllabus, FAQ, Login) linking to each other:

1. Home - top thin gov bar (Gujarat Govt + helpline 1800 233 5500), navbar with GYRS logo, hero with headline "Sarkari Naukri Made Simple" + search bar (keyword + department + qualification like Naukri) + CTA, urgent strip "Closing Soon: GSRTC Helper - 6 Oct 2026, Staff Nurse - 12 Oct 2026", Latest Jobs grid 6 cards (GSRTC Helper 2389 posts, GSSSB Staff Nurse 1200 posts, GPSC Class 1-2, Gujarat Police Constable, Panchayat Clerk, Anganwadi Worker) each with dept logo placeholder, posts, last date badge, fees, Apply button, departments row (GPSC/GSSSB/GSRTC/Police/Panchayat), How it works 3 steps (Search > Check Eligibility > Apply on OJAS), stats (25000+ registered, 350+ exams, 98% alerts on time), testimonials 3 Gujarati students, FAQ 4, full footer with disclaimer "Apply only on ojas.gujarat.gov.in" + links + socials.

2. Jobs Listing - left filters (department checkbox, qualification 10th/12th/ITI/Diploma/Graduate, category, last date, sort by closing soon) + top search + 10 job rows like Naukri with title EN+GU, dept, posts, location Gujarat, salary/Pay scale, last date countdown red, Save + Details buttons, pagination.

3. Job Detail e.g. GSRTC Helper 2026 - title, advt no GSRTC/202627/2389 posts, dates table (start 15 Sep 2026, last 6 Oct 2026, exam Dec 2026), vacancy table, eligibility box (10th pass + age 18-33), fees table (Gen 500 / OBC 250 / SC-ST 0), syllabus accordion, how to apply steps, big green "Apply on OJAS Official Site" + secondary "Save Job" + toggles "WhatsApp Alert ON" "Email Alert ON", "Check My Eligibility" card (enter DOB + education -> Eligible/Not Eligible message), related jobs 3, share WhatsApp button.

4. Results / Call Letters / Syllabus - 3 tabs listing with download buttons linking to OJAS (Prelims Call Letter, Mains Preference, Answer Key Bhavnagar Fire Dept example), notice board list like OJAS.

5. Login/Register - tabs, mobile + OTP + email + password, "One Time Registration" note like OJAS OTR, profile completion progress.

6. User Dashboard - sidebar (Overview, My Saved, My Applied, My Alerts, Profile, Documents), stats cards (Saved 5, Applied 2, Closing Soon 1), table of jobs with last-date + status + Apply on OJAS link, alert toggles for WhatsApp/Email, profile form (name, mobile, email, DOB, gender, category GEN/OBC/SC/ST/EWS, education, district dropdown 33 Gujarat districts), documents checklist (photo/signature/caste cert as per jobupload.aspx rules).

7. Admin Dashboard - sidebar (Overview, Jobs, Users, Alerts Log, Pages, Reports, Settings), KPI cards (Live Jobs 24, Users 12500, Clicks to OJAS 8300, Alerts Sent 45000), chart placeholder, recent jobs table with Edit/Publish/Close, users table, alert log table with Sent/Failed + Resend.

DESIGN SYSTEM - LIGHT ONLY:
- Style: clean govt + modern Naukri, generous whitespace, rounded-2xl cards, soft shadows, no dark mode
- Colors: background #F8FAFC slate-50, cards white #FFFFFF, primary blue #1565C0, accent saffron orange #F97316 for CTA/Apply, success green #16A34A for Eligible/Apply-on-OJAS, danger red #DC2626 for closing date, text #0F172A headings / #475569 body, borders #E2E8F0
- Font: Inter / Plus Jakarta Sans + Noto Sans Gujarati for Gujarati text, bold headings
- Components: sticky navbar, badges for Last Date, countdown chips, tables, forms, toggles, modals, toasts, empty states, mobile bottom nav
- Responsive mobile-first, footer always same

RULES:
- Use REAL realistic Gujarat govt content with advt numbers, ₹ fees, dates Sep-Oct 2026, districts Ahmedabad/Surat/Vadodara/Rajkot/Bhavnagar, phone +91-79-..., Indian names Priya Patel, Rahul Solanki, Amit Shah example
- Gujarati titles alongside English e.g. "GSRTC Helper - હેલ્પર"
- Every Apply button labeled "Apply on OJAS" with external icon, never fake apply form
- Footer disclaimer: "GYRS is help/alert portal. Final application on official ojas.gujarat.gov.in only."
- Make all buttons/flows clickable prototype, consistent header/footer/theme across screens
```

How to use:
1. Copy block above to Stitch, generate, export / download design
2. Build pages in Laravel Blade + Livewire per PROJECT_DOC.md milestones M1-M5
