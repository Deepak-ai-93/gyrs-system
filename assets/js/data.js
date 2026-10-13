/* GYRS shared seed data + localStorage helpers (static demo, no backend) */
(function () {
  const JOBS_KEY = "gyrs_jobs";
  const TENDERS_KEY = "gyrs_tenders";
  const USERS_KEY = "gyrs_users";
  const SESSION_KEY = "gyrs_session";

  const SEED_JOBS = [
    { id: "gsrtc-helper-2026", title_en: "GSRTC Helper", title_gu: "વાહન વ્યવહાર નિગમ હેલ્પર", dept: "GSRTC", advt_no: "GSRTC/202627/84", posts: 2389, qualification: "10th Pass + ITI", age_min: 18, age_max: 33, fees_gen: 500, fees_res: 250, salary: "₹19,950 / Month", location: "All Gujarat Depots", start_date: "2026-09-15", last_date: "2026-10-06", exam_date: "2026-11-29", apply_url: "https://gsrtc.in", pdf_url: "#", skills: ["fitting", "wiring", "mechanic basics", "safety"], notification: "GSRTC Central Office Ranip invites online applications for Helper cadre. Selection via OMR exam + document verification. Apply only on the GSRTC official website.", documents: ["SSC marksheet", "ITI certificate", "Caste certificate", "Photo + signature", "Domicile proof"], status: "published", views: 45210, clicks: 8930 },
    { id: "gsssb-staff-nurse-2026", title_en: "Staff Nurse Class-III", title_gu: "સ્ટાફ નર્સ વર્ગ-૩", dept: "GSSSB", advt_no: "GSSSB/202627/192", posts: 1200, qualification: "GNM / B.Sc Nursing", age_min: 21, age_max: 38, fees_gen: 500, fees_res: 250, salary: "₹26,000 Fix Pay", location: "Civil Hospitals Gujarat", start_date: "2026-09-10", last_date: "2026-10-12", exam_date: "2026-12-05", apply_url: "https://gsssb.gujarat.gov.in", pdf_url: "#", skills: ["patient care", "anatomy", "pharmacology", "first aid"], notification: "GSSSB Health Department recruitment for Staff Nurse. Requires Gujarat Nursing Council registration. Apply only on the GSSSB official website.", documents: ["GNM/B.Sc certificate", "Nursing Council registration", "Caste/EWS cert", "Photo + signature"], status: "published", views: 31200, clicks: 6100 },
    { id: "gpsc-class12-2026", title_en: "GPSC Class 1 & 2 Gazetted", title_gu: "ગુજરાત વહીવટી સેવા", dept: "GPSC", advt_no: "GPSC/202627/01", posts: 388, qualification: "Any Graduate", age_min: 21, age_max: 35, fees_gen: 100, fees_res: 0, salary: "Level 10 (₹56,100+)", location: "Across Gujarat", start_date: "2026-09-01", last_date: "2026-10-20", exam_date: "2027-01-17", apply_url: "https://gpsc.gujarat.gov.in", pdf_url: "#", skills: ["polity", "history", "current affairs", "essay writing"], notification: "GPSC Gazetted services incl. Dy. Collector, Dy.SP, Mamlatdar. Prelims + Mains + Interview. Apply only on the GPSC official website.", documents: ["Degree certificate", "Caste/EWS cert", "Photo + signature", "ID proof"], status: "published", views: 58900, clicks: 12400 },
    { id: "police-constable-2026", title_en: "Police Constable & PSI", title_gu: "પોલીસ કોન્સ્ટેબલ", dept: "Police (LRD)", advt_no: "LRD/202627/12", posts: 8450, qualification: "12th Pass / Graduate", age_min: 18, age_max: 34, fees_gen: 100, fees_res: 0, salary: "₹26,000 / Month", location: "All Units Gujarat", start_date: "2026-09-20", last_date: "2026-10-15", exam_date: "2026-12-12", apply_url: "https://police.gujarat.gov.in", pdf_url: "#", skills: ["running", "physical fitness", "gk", "reasoning"], notification: "LRD Police recruitment incl. constable, jail constable, SRPF. PET/PST + written exam. Apply only on the Police recruitment official website.", documents: ["HSC marksheet", "Caste cert", "Physical certificate", "Photo + signature"], status: "published", views: 72400, clicks: 18900 },
    { id: "gpssb-talati-2026", title_en: "Talati cum Mantri", title_gu: "તલાટી કમ મંત્રી", dept: "GPSSB", advt_no: "GPSSB/202627/05", posts: 1860, qualification: "12th Pass + CCC", age_min: 18, age_max: 35, fees_gen: 100, fees_res: 0, salary: "₹26,000 / Month", location: "All 33 Districts", start_date: "2026-09-12", last_date: "2026-10-18", exam_date: "2026-12-20", apply_url: "https://gpssb.gujarat.gov.in", pdf_url: "#", skills: ["computer basics", "gujarati typing", "record keeping", "ccc"], notification: "Village Panchayat Secretary Class-3. OMR exam + computer proficiency. Apply only on the GPSSB official website.", documents: ["HSC marksheet", "CCC certificate", "Caste cert", "Photo + signature"], status: "published", views: 39800, clicks: 9200 },
    { id: "hc-assistant-2026", title_en: "High Court Assistant", title_gu: "હાઇકોર્ટ આસિસ્ટન્ટ", dept: "High Court", advt_no: "RC/1434/2026", posts: 1478, qualification: "Any Graduate + Typing", age_min: 21, age_max: 35, fees_gen: 500, fees_res: 250, salary: "₹19,900 - ₹63,200", location: "Ahmedabad + District Courts", start_date: "2026-09-25", last_date: "2026-10-30", exam_date: "2027-01-10", apply_url: "https://gujarathighcourt.nic.in", pdf_url: "#", skills: ["typing 30wpm", "english", "computer", "legal basics"], notification: "High Court subordinate courts assistant cadre. Elimination + mains + typing test. Apply only on the High Court official website.", documents: ["Degree certificate", "Typing certificate", "Caste cert", "Photo + signature"], status: "published", views: 27400, clicks: 5400 }
  ];

  const SEED_TENDERS = [
    { id: "tender-road-ahmedabad", title: "Ahmedabad City Road Resurfacing (Package 4)", authority: "AUDA", tender_no: "AUDA/ENG/2026/44", value: "₹4.2 Cr", emd: "₹4,20,000", location: "Ahmedabad", publish_date: "2026-09-20", deadline: "2026-10-14", docs: ["GST certificate", "Work experience", "Bank solvency", "PF registration"], apply_url: "https://www.nprocure.com", status: "live" },
    { id: "tender-water-surat", title: "Surat Water Supply Pipeline Laying", authority: "SMC", tender_no: "SMC/WS/2026/12", value: "₹8.6 Cr", emd: "₹8,60,000", location: "Surat", publish_date: "2026-09-18", deadline: "2026-10-16", docs: ["Contractor licence", "Turnover cert", "Machinery list", "GST certificate"], apply_url: "https://www.nprocure.com", status: "live" },
    { id: "tender-school-repair", title: "Govt School Building Repair – Rajkot Zone", authority: "SSA Gujarat", tender_no: "SSA/RJT/2026/09", value: "₹1.8 Cr", emd: "₹1,80,000", location: "Rajkot", publish_date: "2026-09-22", deadline: "2026-10-10", docs: ["Registration cert", "Past work orders", "Labour licence"], apply_url: "https://www.nprocure.com", status: "live" },
    { id: "tender-it-hardware", title: "Supply of Computer Hardware – Secretariat", authority: "GIL", tender_no: "GIL/HW/2026/21", value: "₹2.5 Cr", emd: "₹2,50,000", location: "Gandhinagar", publish_date: "2026-09-25", deadline: "2026-10-20", docs: ["OEM authorization", "GST + PAN", "Turnover cert"], apply_url: "https://www.nprocure.com", status: "live" },
    { id: "tender-bus-amc", title: "GSRTC Bus Depot Equipment AMC", authority: "GSRTC", tender_no: "GSRTC/TECH/2026/07", value: "₹95 Lakh", emd: "₹95,000", location: "Vadodara", publish_date: "2026-09-15", deadline: "2026-10-08", docs: ["Service credentials", "GST cert", "Rate list"], apply_url: "https://www.nprocure.com", status: "closing-soon" },
    { id: "tender-hospital-equip", title: "Hospital Equipment Supply – Civil Hospital", authority: "Health Dept", tender_no: "HLT/EQP/2026/33", value: "₹3.1 Cr", emd: "₹3,10,000", location: "Ahmedabad", publish_date: "2026-09-28", deadline: "2026-10-25", docs: ["Drug licence", "OEM authorization", "ISO cert"], apply_url: "https://www.nprocure.com", status: "live" }
  ];

  const SKILLS = [
    { id: "ccc", name: "CCC Computer Course", jobs: ["Talati cum Mantri", "High Court Assistant"], level: "Beginner", duration: "3 months" },
    { id: "typing", name: "Gujarati + English Typing 30 WPM", jobs: ["High Court Assistant", "GPSC Class 1-2"], level: "Practice", duration: "2 months" },
    { id: "iti", name: "ITI Fitter / Electrician", jobs: ["GSRTC Helper"], level: "Certificate", duration: "1-2 years" },
    { id: "nursing", name: "GNM / B.Sc Nursing", jobs: ["Staff Nurse Class-III"], level: "Degree", duration: "3-4 years" },
    { id: "gpsc-prep", name: "GPSC Prelims + Mains Prep", jobs: ["GPSC Class 1-2"], level: "Advanced", duration: "6-12 months" },
    { id: "pet", name: "Police PET/PST Fitness", jobs: ["Police Constable & PSI"], level: "Physical", duration: "3 months" },
    { id: "tally-gst", name: "Tally + GST Assistant", jobs: ["Tender billing / Private accounts"], level: "Beginner", duration: "2 months" },
    { id: "data-entry", name: "Data Entry + Excel", jobs: ["Talati", "High Court Assistant"], level: "Beginner", duration: "1 month" }
  ];

  const SKILL_VOCAB = ["fitting", "wiring", "mechanic", "nursing", "patient care", "typing", "computer", "ccc", "excel", "tally", "gst", "polity", "history", "current affairs", "running", "fitness", "gk", "reasoning", "anatomy", "pharmacology", "first aid", "record keeping", "legal", "essay"];

  function read(key, fallback) {
    try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; }
    catch (e) { return fallback; }
  }
  function write(key, val) { localStorage.setItem(key, JSON.stringify(val)); }

  function seed() {
    if (!localStorage.getItem(JOBS_KEY)) write(JOBS_KEY, SEED_JOBS);
    if (!localStorage.getItem(TENDERS_KEY)) write(TENDERS_KEY, SEED_TENDERS);
    if (!localStorage.getItem(USERS_KEY)) {
      write(USERS_KEY, [
        { name: "Admin", email: "admin@gyrs.in", mobile: "9999999999", password: "admin123", role: "admin", education: "Any Graduate", category: "GEN", district: "Gandhinagar", skills: [], saved: [], applied: [], blocked: false },
        { name: "Priya Patel", email: "priya@example.com", mobile: "9876543210", password: "user123", role: "user", education: "12th Pass", category: "SEBC", district: "Ahmedabad", skills: ["computer", "gujarati typing"], saved: ["gsrtc-helper-2026"], applied: [], blocked: false }
      ]);
    }
  }

  function matchScore(userSkills, job) {
    if (!userSkills || !userSkills.length) return 0;
    const js = (job.skills || []).map(s => s.toLowerCase());
    const us = userSkills.map(s => s.toLowerCase());
    let hit = 0;
    js.forEach(j => { if (us.some(u => j.includes(u) || u.includes(j))) hit++; });
    return js.length ? Math.round((hit / js.length) * 100) : 0;
  }

  window.GYRS = {
    seed, SKILLS, SKILL_VOCAB,
    getJobs: () => read(JOBS_KEY, SEED_JOBS),
    saveJobs: (j) => write(JOBS_KEY, j),
    getTenders: () => read(TENDERS_KEY, SEED_TENDERS),
    saveTenders: (t) => write(TENDERS_KEY, t),
    getUsers: () => read(USERS_KEY, []),
    saveUsers: (u) => write(USERS_KEY, u),
    session: () => read(SESSION_KEY, null),
    setSession: (s) => s ? write(SESSION_KEY, s) : localStorage.removeItem(SESSION_KEY),
    currentUser: function () { const s = this.session(); if (!s) return null; return this.getUsers().find(u => u.email === s.email) || null; },
    matchScore
  };
  seed();
})();
