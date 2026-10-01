"""Jobs filter fix + responsive audit fixes (all pages). Design untouched."""
PAGES = ["index.html", "jobs/index.html", "job-detail/index.html"]

GLOBAL_CSS = """<style>
/* GYRS responsive audit fixes */
html, body { overflow-x: clip; }
img { max-width: 100%; }
.gyrsTableWrap { overflow-x: auto; -webkit-overflow-scrolling: touch; }
.gyrsTableWrap table { min-width: 480px; }
@media (max-width: 400px) {
  #gyrsFilterCard div.grid-cols-2 { grid-template-columns: 1fr !important; }
}
#gyrsFilterCard label { min-height: 44px; }
#gyrsFilterCard input[type="checkbox"] { width: 20px; height: 20px; flex-shrink: 0; }
#gyrsFilterBtn { display: none; }
@media (max-width: 1023.5px) {
  #gyrsFilterBtn { display: flex; }
  #gyrsFilterAside.gyrsHide { display: none; }
}
@media (min-width: 1024px) {
  #gyrsFilterAside.gyrsHide { display: flex !important; }
}
</style>
"""

JOBS_JS = """<script>
/* GYRS jobs: working filters + mobile collapsible sidebar */
(function(){
  var h2 = null;
  Array.prototype.forEach.call(document.querySelectorAll("h2"), function(x){
    if ((x.textContent || "").indexOf("Filters") > -1) h2 = x;
  });
  if (!h2) return;
  var card = h2.closest("div");
  if (card) card.id = "gyrsFilterCard";
  var aside = h2.closest("aside");
  if (aside) aside.id = "gyrsFilterAside";

  var boxes = Array.prototype.slice.call(card.querySelectorAll('input[type="checkbox"]'));
  var toggle = null, resetBtn = null;
  boxes.forEach(function(b){
    var lbl = (b.closest("label") ? b.closest("label").textContent : "") || "";
    if (/Closing/i.test(lbl)) toggle = b;
  });
  Array.prototype.forEach.call(card.querySelectorAll("button"), function(x){
    if ((x.textContent || "").trim().indexOf("Reset All") === 0) resetBtn = x;
  });
  var articles = Array.prototype.slice.call(document.querySelectorAll("article"));
  var MONTHS = {jan:0,feb:1,mar:2,apr:3,may:4,jun:5,jul:6,aug:7,sep:8,oct:9,nov:10,dec:11};

  function daysOf(text){
    var m = text.match(/Closes in (\\d+)\\s*Day/i);
    if (m) return parseInt(m[1], 10);
    m = text.match(/Closes\\s+(\\d{1,2})\\s+([A-Za-z]+)\\s+(\\d{4})/);
    if (m) {
      var d = new Date(parseInt(m[3],10), MONTHS[m[2].slice(0,3).toLowerCase()], parseInt(m[1],10), 23, 59, 59);
      return Math.ceil((d - Date.now()) / 864e5);
    }
    return 999;
  }
  function deptKey(label){
    label = label.toLowerCase();
    if (label.indexOf("gsssb") > -1) return "gsssb";
    if (label.indexOf("police") > -1) return "police|lrd";
    if (label.indexOf("gpsc") > -1 && label.indexOf("gpssb") === -1) return "gpsc";
    if (label.indexOf("gsrtc") > -1) return "gsrtc";
    if (label.indexOf("gpssb") > -1 || label.indexOf("panchayat") > -1) return "gpssb|panchayat";
    if (label.indexOf("forest") > -1) return "forest";
    return null;
  }
  function qualKey(label){
    label = label.toLowerCase();
    if (label.indexOf("10th") > -1) return "10th";
    if (label.indexOf("12th") > -1) return "12th";
    if (label.indexOf("iti") > -1) return "iti";
    if (label.indexOf("diploma") > -1) return "diploma";
    if (label.indexOf("post graduate") > -1) return "post graduate";
    if (label.indexOf("graduate") > -1) return "graduate";
    return null;
  }
  function activeFilters(){
    var dept = [], qual = [];
    boxes.forEach(function(b){
      if (!b.checked || b === toggle) return;
      var lbl = b.closest("label") ? b.closest("label").textContent : "";
      var d = deptKey(lbl), q = qualKey(lbl);
      if (d) dept.push(d); else if (q) qual.push(q);
    });
    return { dept: dept, qual: qual, urgent: toggle ? toggle.checked : false };
  }
  var emptyBox = document.createElement("div");
  emptyBox.style.cssText = "display:none;background:#fff;border:1px solid #E2E8F0;border-radius:16px;padding:32px;text-align:center;color:#475569;";
  emptyBox.innerHTML = "<p style='font-weight:700;color:#0F172A;'>No jobs match these filters.</p>" +
    "<button id='gyrsEmptyClear' style='margin-top:8px;color:#1565C0;font-weight:700;text-decoration:underline;min-height:44px;'>Clear all filters</button>";

  function render(){
    var f = activeFilters(), shown = 0;
    articles.forEach(function(a){
      var t = a.textContent || "";
      var okD = !f.dept.length || f.dept.some(function(k){ return new RegExp(k, "i").test(t); });
      var okQ = !f.qual.length || f.qual.some(function(k){ return t.toLowerCase().indexOf(k) > -1; });
      var okU = !f.urgent || daysOf(t) <= 7;
      var show = okD && okQ && okU;
      a.style.display = show ? "" : "none";
      if (show) shown++;
    });
    if (!emptyBox.parentNode && articles.length) articles[0].parentNode.insertBefore(emptyBox, articles[0]);
    emptyBox.style.display = shown ? "none" : "block";
    var n = f.dept.length + f.qual.length + (f.urgent ? 1 : 0);
    var btn = document.getElementById("gyrsFilterBtn");
    if (btn) btn.querySelector("span:last-child").textContent = n ? "Filters \\u2022 " + n + " active" : "Filters";
  }
  boxes.forEach(function(b){ b.addEventListener("change", render); });
  function resetAll(){ boxes.forEach(function(b){ b.checked = false; }); render(); }
  if (resetBtn) resetBtn.addEventListener("click", resetAll);
  document.addEventListener("click", function(e){
    if (e.target && e.target.id === "gyrsEmptyClear") resetAll();
  });

  /* collapsible sidebar on mobile */
  if (aside && !document.getElementById("gyrsFilterBtn")) {
    var btn = document.createElement("button");
    btn.id = "gyrsFilterBtn"; btn.type = "button";
    btn.style.cssText = "align-items:center;justify-content:center;gap:8px;width:100%;min-height:48px;background:#fff;border:1px solid #E2E8F0;border-radius:14px;font-weight:700;color:#0F172A;margin-bottom:12px;";
    btn.innerHTML = "<span>\\u2630</span><span>Filters</span>";
    aside.parentNode.insertBefore(btn, aside);
    var mq = window.matchMedia("(max-width:1023.5px)");
    function sync(){ aside.classList.toggle("gyrsHide", mq.matches); }
    if (mq.addEventListener) mq.addEventListener("change", sync);
    sync();
    btn.addEventListener("click", function(){ aside.classList.toggle("gyrsHide"); });
  }
  render();
})();
</script>
</body>"""

TABLE_JS = """<script>
/* wrap tables for horizontal scroll on small screens */
(function(){
  Array.prototype.forEach.call(document.querySelectorAll("table"), function(t){
    if (t.parentNode && !t.parentNode.classList.contains("gyrsTableWrap")) {
      var w = document.createElement("div");
      w.className = "gyrsTableWrap";
      t.parentNode.insertBefore(w, t); w.appendChild(t);
    }
  });
})();
</script>
</body>"""

for path in PAGES:
    with open(path, encoding="utf-8") as f:
        h = f.read()
    assert "gyrsTableWrap" not in h, path
    h = h.replace("</head>", GLOBAL_CSS + "</head>", 1)
    h = h.replace("</body>", TABLE_JS, 1)
    if "jobs/" in path:
        assert "gyrsFilterBtn" not in h, path
        h = h.replace("</body>", JOBS_JS, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(h)
    print("audit fixes:", path)
