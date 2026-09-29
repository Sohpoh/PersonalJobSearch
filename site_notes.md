# Site Notes

Notes the job-search skill has learned about how to navigate and filter each
company's career site (search/filter behavior, pagination style, where posted
dates show up, quirks). Filled in automatically — no need to edit by hand.

## Anthropic
Greenhouse-hosted board (`job-boards.greenhouse.io/anthropic`). The
`?departments[]=<id>` query param is a real, working filter — all matching
roles render in the DOM at once (no pagination/load-more needed). No
posted-date is shown anywhere on this board (a "New" badge appears next to
some titles but with no date attached, so it's a rough recency signal at
best); direct posting links are also on
`job-boards.greenhouse.io/anthropic/jobs/<id>`.

**2026-07-20 correction**: The "Applied AI" department under this filter is
almost entirely a pre-sales/customer-success org, not engineering, despite
titles that sound like engineering roles. Verified by opening several
postings' actual qualifications text (not just titles): "Applied AI
Architect" (all flavors — Commercial, Enterprise Tech, Industries,
Government Technology, State and Local Government, Digital Natives),
"Applied AI Security Architect", "Solutions Architect"/"Partner Solutions
Architect", "Applied AI Technical Evangelist", and "Manager/Head of Applied
AI Architecture" all explicitly require 5-7+ years in customer-facing
pre-sales roles (Solutions Architect/Sales Engineer/Technical Account
Manager), confirmed via screening questions like "Do you have 7+ years of
experience in a pre-sales technical role". These are a different job
function from the resume (engineering, not sales-engineering) and should be
excluded regardless of how technical the title sounds — prior runs
(2026-07-13) surfaced several of these as matches based on title alone
without opening the JD; that was a mistake and shouldn't be repeated.
The one title family that IS a genuine engineering/builder role: "Applied AI
Engineer, Beneficial Deployments" — reads like a Forward Deployed
Engineer/technical-founder role (4+ years, production LLM app experience),
worth surfacing despite the years gap vs. an early-career resume. Check for
new postings under this specific title each run rather than the broader
"Applied AI Architect" family.

**2026-07-28 check**: All 20 listings under this filter are still the Applied
AI Architect/Solutions Architect/Security Architect/Technical Evangelist
pre-sales family (same excluded pattern as prior runs). The one exception
title, "Applied AI Engineer, Beneficial Deployments," did not have a posting
this run — worth continuing to check for it specifically since it's the one
genuine engineering role in this department.

**2026-07-31 check**: Same 20-listing pre-sales/architect family, no change.
"Applied AI Engineer, Beneficial Deployments" still absent (only the
Manager-level "Head of Applied AI Architecture, Beneficial Deployments" and
"Manager, Applied AI Engineering, Beneficial Deployments (Life Sciences)"
appeared, both management not IC). Zero matches again.

**2026-08-05 check**: Same 20-listing pre-sales/architect family, identical
title set to 2026-07-31. "Applied AI Engineer, Beneficial Deployments" still
absent. Zero matches again — this department has now gone 3+ consecutive
runs with no genuine engineering opening.

**2026-09-23 check**: The department changed a lot since 08-05 (~48 listings,
up from 20) and now includes real engineering-flavored titles beyond the
Architect family: "Applied AI Engineer, Enterprise Tech" (US) and "…,
Startups" (London), "Forward Deployed Engineer" (US + London, plus Paris/
Munich), and "Associate Applied AI, Rotational Program, London" (0-2 yrs —
the first entry-level match here). The "Applied AI Engineer"/FDE titles all
ask 4+ years customer-facing (the London FDE's screening question asks 8+),
so they're stretches. "Applied AI, Research Engineer" needs 6+ years;
"Applied AI Engineer, Beneficial Deployments (Life Sciences)" (London)
requires deep life-sciences research background; "Technical Deployment Lead"
is a lead-level, no-code role — all excluded. "Applied AI Architect" and
"Manager…" titles are still the excluded pre-sales/management family.
Faster method than opening pages: run a `fetch()` of each
`/anthropic/jobs/<id>` from `browser_evaluate` and regex the "N+ years"
sentences. The board list is `a[href*="/jobs/"]` links (title | location in
`innerText`), all in the DOM at once. A "New" badge shows next to fresh
titles.

## NVIDIA
`jobs.nvidia.com/careers` is a Phenom-based SPA. Landing on the bare URL (or
any URL) auto-opens a specific job's detail pane rather than a plain list —
that's normal, not an error; the actual results list sits alongside it as a
left-hand column of `button "View job: <title>"` elements, not links.
Pagination is via `start=` query param, incrementing by 10 per page (`start=0`,
`start=10`, `start=20`, ...) — directly navigable by URL. Filter params like
`filter_skills=` and `filter_time_type=` genuinely apply (confirmed via the
"All filters, N selected" chip and the results count), but NVIDIA's skill
tags are broad/loose — e.g. "Artificial Intelligence" surfaces hardware, PR,
and business-development roles alongside actual AI engineering ones, and
results skew heavily toward Senior/Principal/Director titles. Always check
each posting's stated years-of-experience rather than trusting the title.
A OneTrust cookie-consent dialog blocks clicks on first load; dismiss it
(Accept All / Reject Optional) before interacting with pagination. No
posted-date shown on listings; "Sort: Latest" is the closest recency proxy.
Direct `start=N` URL navigation is unreliable — the "Latest"-sorted result
set reshuffles between loads (likely live reindexing), so jumping straight
to `start=20` can show a different/overlapping set than actually clicking
"Next jobs" from `start=10`. Prefer clicking the "Next jobs" button
(or driving it via JS `click()` on the button, to dodge the cookie dialog)
over constructing `start=` URLs directly when paging through for recency.
The job-list buttons render text only in the accessibility tree, not in
`textContent`/`innerText` via `browser_evaluate` (the DOM nodes appear to be
populated through some non-standard mechanism) — read titles/locations from
the `browser_snapshot`/`browser_wait_for` output instead of trying to
`querySelectorAll` and scrape button text via JS.
**2026-07-15 check**: Sampled the 40 most recent postings (4 pages). All were
Senior/Director/Principal/Distinguished-level or based outside the US/UK
(Israel, India, China, Korea, Vietnam) — zero fits in that sample. With
~1091 total roles and 110 pages, a full sweep isn't practical each run;
sampling the first 3-5 "Latest"-sorted pages seems to be a reasonable
weekly check unless a faster way to filter by seniority is found.

**2026-07-20 check**: Sampled 3 pages (30 postings, ~1119 total roles now).
Same pattern held — Senior/Distinguished/Director titles or non-US/UK
locations dominate. One exception worth noting for future runs: postings
tagged "New College Grad 2026" do occasionally appear (e.g. "Deep Learning
Software Engineer, TensorRT Performance") and explicitly want only ~2 years
experience, which matches the resume's level — but that specific one required
strong C++/CUDA/GPU-inference skills with no real overlap to the resume's
Python/agentic-AI/backend background, so it was ruled out on skill mismatch,
not seniority. Worth specifically scanning for "New College Grad" or "New
Grad" tagged titles each run as a way to skip past the senior-skewed bulk.

**2026-07-27 check**: Sampled 4 pages (40 postings, ~1153 total roles now).
Same senior/director/non-US pattern held for most, but found a new pocket
worth checking each run: the "AI Safety and Security Engineering" team (job
IDs JR2021882-888, appeared together on one page) mixes senior titles
(Senior Manager, Distinguished Engineer) with genuinely non-senior ones that
don't say "Senior" anywhere — "Security Research Engineer", "Evaluation and
ML Systems Engineer" (5+ years — too big a gap, skip), and "Harness and
Platform Engineer" (unopened this run). Also worth checking each run:
"Machine Learning Engineer, AI Safety" (JR2021784, Content Safety/ML
Fairness/Robustness for LLMs) — only 2+ years + Master's/PhD-or-equivalent,
a genuine non-senior match, though the content-safety/bias specialization
itself isn't on the resume so treat as a stretch. Title pattern to watch:
any "AI Safety[...]Engineering" team posting without "Senior/Staff/Principal/
Distinguished/Director/Manager" in the title is worth opening regardless of
how technical-sounding the neighboring senior titles are.

**2026-07-28 check**: Sampled 4 "Latest"-sorted pages (40 postings). Same
senior/director/non-US pattern held for the bulk. Found a new plain-titled
"Applied AI Engineer" posting (JR2018178 in one location, JR2018179 in
another — same team, two location variants) that isn't part of the
previously-seen title families — opened it and it requires "5+ years of
hands-on experience building and deploying ML/AI systems," too big a gap
vs. the resume's ~2 years, so excluded. Worth rechecking this title each run
in case a lower-experience variant appears. No "AI Safety and Security
Engineering" or "New College Grad" postings surfaced in this run's 4-page
sample (they may still exist further in the list — a keyword search for
"AI Safety" was attempted but the site's keyword box drops the
Artificial-Intelligence/full-time filter params entirely and returns
generic results, so it isn't a reliable way to jump to a specific team;
paging remains the only verified method).

**2026-07-31 check**: Sampled 4 "Latest"-sorted pages (40 postings, 1155
total roles now). Same senior/director/international pattern for the bulk,
but two plain (non-"Senior") titles stood out and were opened: "Software
Engineer, OpenShell" (US remote) requires "8+ years... MS/PhD" despite the
plain title — a reminder that generic-sounding titles here aren't
automatically junior. "System Software Engineer – Data Center Compute
Diagnostics" (Durham, NC) requires 5+ years embedded/firmware/C++ — years gap
plus zero skill overlap with the resume. Both excluded. No New College Grad
or AI Safety postings surfaced in this run's 4-page sample. Also confirmed
the "Latest"-sorted result set reshuffles between page loads even when
navigating back to the same `start=N` URL (a job seen on page 2 was still
findable after reloading, but at a different position) — consistent with the
reindexing behavior already noted above.

**2026-08-05 check**: Sampled 4 "Latest"-sorted pages (40 postings, ~1143
total roles, down from 1155 on 2026-07-31). Same senior/manager/international
pattern held throughout — no New College Grad or AI Safety and Security
Engineering team postings surfaced in this run's sample. Notable non-matches
worth remembering: "ASIC Verification Engineer" and "Custom SOC IP
Verification Engineer" (non-senior titles but hardware/ASIC verification,
zero resume overlap), "Raytracing Compiler Engineer" (compiler/graphics,
zero overlap). Zero matches again.

**2026-09-23 check**: Sampled 4 "Latest"-sorted pages (1098 total roles, 110
pages). Page 1 was entirely China/Taiwan/Thailand; pages 2-4 were the usual
senior/Architect/international mix. One "New College Grad 2026" posting
surfaced ("Security Architect - New College Grad 2026", Santa Clara) —
silicon-security work (secure boot/root of trust/FIPS), included only as a
weak stretch. Also seen and skipped: "Research Scientist, Physical AI —
PhD New College Grad 2026", PhD/intern postings. Reliable way to page:
`[...document.querySelectorAll('button')].find(b => /Next jobs/i.test(b.getAttribute('aria-label')||b.innerText)).click()` via `browser_evaluate` (the
`nav[aria-label=…] button:last-of-type` selector I tried first returned null).
Use `browser_snapshot` with a `filename` and grep the `View job` buttons out
of the saved YAML instead of dumping the snapshot inline (save it outside
the project directory). To open one job directly, navigate to
`jobs.nvidia.com/careers?query=<JR id>`; it opens the detail pane inline and
the resulting URL carries a `pid=` you can use for a direct link
(`jobs.nvidia.com/careers/job/<pid>`).

**2026-09-28 check**: Sampled 4 "Latest"-sorted pages (40 postings, 1115 total
roles now). Same senior/director/international/PM pattern held throughout.
Two more "ASIC Verification Engineer... New College Grad 2027" postings
appeared (Durham NC, Austin TX) — same hardware/ASIC mismatch as prior New
College Grad hardware roles, excluded on skill overlap. No "AI Safety and
Security Engineering" or plain "Applied AI Engineer" postings surfaced in
this run's sample. Zero matches again.

## Meta
`metacareers.com/jobsearch/` supports real query-param filtering
(`teams[n]=`, `roles[n]=`, `sort_by_new=true`). Pagination is via a `&page=N`
query param appended directly to the URL (confirmed working 2026-07-15) —
faster than clicking the "Page X of Y" counter each time. Each card links to
`/profile/job_details/<id>`, which redirects to the canonical
`/profile/job_details/<id>/` detail page — read that page's "Minimum
Qualifications" heading, not the title: titles here are frequently generic
("Software Engineer, Machine Learning ...", "Software Engineer - Backend,
Standalone Apps Team") but the postings under "Standalone Apps Team" in
particular have consistently required 12+ years of experience regardless of
title. No posted-date shown on cards or detail pages.

**2026-07-15 update**: The years-requirement pattern is broader than just
Standalone Apps Team — nearly every generic "Software Engineer, X" posting
(Infrastructure, Machine Learning, etc.) uses an "8+ years of programming
experience OR 4+ years with a PhD" boilerplate minimum, well above an
early-career resume. Research Scientist/Applied Scientist-flavored titles
also consistently want a PhD or equivalent. Two title families buck this
trend and are worth specifically checking each run: "Business Support
Engineer" (3+ years SWE/SRE, seen in Menlo Park, CA — API troubleshooting +
hands-on LLM experience, but on-call/support-flavored, not product eng) and
"Business Engineer, Business Agents" (no stated years minimum, wants
LLM/agentic-AI + Python/Java/PHP, reads like an FDE role) — but as of
2026-07-15 every "Business Engineer, Business Agents" req was based in São
Paulo, Brazil only.

**2026-07-24 update**: The "8+ years/PhD" boilerplate is not universal even
among generic "Software Engineer, X" titles — "Software Engineer, Machine
Learning" (London, UK, job ID 1048049836887307) had only a Bachelor's-degree
minimum with no explicit years number, plus NLP/information-retrieval
preferred quals. Don't assume the boilerplate applies without opening the
posting, even for a title pattern seen before. Also confirmed plain
"Business Engineer" continues to appear with just a 3+ years bar and direct
PHP/Python/Java/JS overlap (this time in New York, NY, not just London) —
worth checking every run regardless of city.

**2026-07-20 update**: These job IDs churn week over week with no date
signal to explain why — treat "not yet in seen_jobs.json" as the operative
recency signal, same approach as OpenAI. The "Business Support
Engineer"/"Business Engineer"/"Business Engineer, Business Agents" family
turns out to have a wide qualifications spread by individual req, not a
fixed years bar tied to the title: some postings ask 3+ years (good fit),
others 5+ or 8+. The 8+ year ones read as lead-level despite the identical
title (e.g. "Co-Lead the team's AI-native technical strategy", "Set
technical communication standards representing the team internally and
externally") — treat those as a more senior variant, not a fit. Always open
each individual posting's Minimum Qualifications rather than assuming the
bar from a previously-seen posting with the same title. Also worth
checking each run: plain "Business Engineer" (no "Business Agents" suffix)
has appeared with only a 3+ years bar in London, UK — and "Research Engineer
- MSL FAIR Foundations" recurs under new job IDs and (unlike most other
FAIR/Research Scientist titles here) has had postings with just a 3+ years
bar and no PhD requirement — don't rule either out by title alone.

**2026-07-27 update**: Verified the job-ID-as-recency-signal approach continues
to work well for dedup here — nearly every posting opened this run
("Software Engineer, Machine Learning", "Software Engineer, Machine Learning
RecSys" ×2, "Software Engineer, Infrastructure" ×2, "Business Support
Engineer" ×3 variants, "Business Engineer, Business Agents") turned out to
already be logged in `seen_jobs.json` from a prior run even though the exact
job ID hadn't been individually re-checked before — always extract the
numeric ID from the href and check it against `seen_jobs.json` by ID (not
by exact URL string) since Meta/Amazon URLs have used inconsistent formats
across runs (`/jobs/<id>/` vs `/profile/job_details/<id>/`, with/without
trailing slash) and a naive full-URL match will falsely say "not seen" for
already-reported jobs. Genuinely new this run: two more "Software Engineer,
Machine Learning RecSys" postings (Sunnyvale, CA +3 locations) at 2+/1+ years
and 3+/2+ years respectively — this title continues to be a reliable
low-years, high-skill-overlap match each run, worth specifically searching
for by title. The generic "Software Engineer, X" boilerplate without an
explicit years number (seen on "Software Engineer, Infrastructure" and
"Software Engineer, Product" postings) reuses identical responsibilities
text ("driving change within an organization and leading complex technical
projects", "set direction and goals for teams, lead major initiatives") to
the explicit "8+ years" postings — treat that responsibilities-boilerplate
phrasing itself as a senior signal even when the years number is missing.

**2026-07-28 update**: Only one page sampled this run (10 most-recent
postings) since the first page already surfaced the relevant title families.
Confirmed "Business Support Engineer" (Dublin, Ireland, job 1739576487064198,
3+ years, full-stack/REST-API/cloud overlap) had good skill fit but was
excluded on location — Dublin isn't in the resume profile's "US and London,
UK" preference list, a reminder to check location against Additional
Preferences even when skills clearly match. All plain "Software Engineer, X"
titles opened this run (Android, Machine Learning, Infrastructure, Product)
used the "8+ years OR 4+ years with PhD" boilerplate consistently, including
one, "Software Engineer, Machine Learning" (Sunnyvale, job 998357492128826),
that had looked promising given the 2026-07-24 note about a UK posting with
no years bar — that exception doesn't generalize to this US posting, so
continue opening each one individually rather than assuming by title. Two
"Software Engineer, Machine Learning RecSys" postings on the page were
already in `seen_jobs.json` from 2026-07-27, confirming that family recurs
across runs with stable-ish job IDs (unlike most other Meta titles).

**2026-07-31 update**: One page sampled (10 most-recent postings). "Business
Engineer, Business Agents" and "Software Engineer, Machine Learning RecSys"
job IDs were already in `seen_jobs.json`. All other postings opened this run
("Software Engineer, Machine Learning - Search Algorithm, Standalone Apps
Team", "Software Engineer - Product (Technical Leadership)", "Software
Engineer, Product", "Software Engineer - Android, Standalone Apps Team",
"Software Engineer, Machine Learning - Ranking, Home Feed, Standalone Apps
Team") all carried 8-12+ year bars once opened — the Standalone Apps Team
and "Technical Leadership"-suffixed titles both confirmed as reliably senior
across multiple runs now. "Software Engineer, iOS" and "Sensor Hardware
Engineer" postings appeared but were skipped without opening on function
mismatch (resume has no mobile/hardware background) rather than years —
worth still spot-checking these occasionally in case a low-years variant
appears, since the site doesn't reliably signal seniority by title alone.
Zero new matches this run.

**2026-08-05 update**: One page sampled (10 most-recent postings). Confirmed
job-ID-as-recency-signal continues to hold: "Machine Learning RecSys" job ID
was already in `seen_jobs.json`. All others opened this run were either
non-engineering (Product Manager), established senior "Technical Leadership"-
suffixed titles (confirmed 12+ years via Minimum Qualifications, both
"Software Engineer - Product (Technical Leadership)" and the ML-TL variant),
established generic "Software Engineer, Product"/"Software Engineer,
Infrastructure" 8+-year boilerplate (both individually re-confirmed), or
mobile (iOS/Android — skipped without opening on function mismatch). One
new title family opened: "Computer Vision Engineer, Reality Labs" (Redmond,
WA) — only 3+ years but requires C++ and SLAM/camera-calibration/robotics
specialization with zero overlap to the resume's OpenCV/DeepFace facial-
analysis background — excluded on skill mismatch despite the low years bar.
Zero new matches this run.

**2026-09-23 update**: Sampled 2 pages (20 postings; `&page=2` works by
direct navigation). Job detail HTML fetched via `fetch()` does NOT contain the
qualifications (client-rendered) — navigate to each `/profile/job_details/<id>/`
and read `document.body.innerText` from "Minimum Qualifications" instead.
Confirmed again: plain "Software Engineer, Product"/"Infrastructure" London
postings use the senior responsibilities boilerplate ("Set direction and
goals for teams, lead major initiatives"; "driving change within an
organization and leading complex technical projects") even with no years
number — excluded. "Software Engineer, Systems ML" (no years bar) needs
GPU/compiler/ML-systems specialization — excluded on skill mismatch.
"Research Engineer, Monetization AI" (no years bar, research-flavored)
included as a stretch. Two "Machine Learning RecSys" IDs were already logged.

**2026-09-28 update**: Sampled 2 pages (20 postings). New match: "Business
Engineer" (London, UK, job 2021969455351795) — 5+ years, PHP/Python/JS
overlap, reported as a stretch (bigger gap than the 3+ year variants seen in
prior runs). New title "Security Engineer, Applied AI" (London) requires 5+
years hands-on security-engineering specialization (detection/threat-intel/
offensive security) — excluded on skill-depth mismatch despite resume's
security-adjacent RBAC/guardrail work. Confirmed again: "Software Engineer,
Product" and "Software Engineer, Infrastructure" postings with no explicit
years number but the "driving change...leading complex technical projects"
responsibilities phrase are a reliable senior signal (both excluded, one in
Remote UK, one in London). "Software Engineer, Systems ML" and multiple
"(Technical Leadership)"-suffixed titles skipped on established patterns
(GPU/compiler specialization; leadership=senior). Two "SW Specialist -
Wearables Interfaces Engineering" postings (10+ years / expert-level) —
new title family, hardware/platform-integration specialization, excluded.

## Amazon
The tracked URL (`amazon.jobs/content/en/artificial-intelligence-ai?country[]=...`)
is a marketing landing page, not a search page — the query params don't do
anything by themselves. It contains an embedded search widget anchored at
`#jobs-search`; navigate to the URL with `#jobs-search` appended and the
widget reads the same query params to filter for real. Default sort is
"most relevant" and resets to that on every fresh page load (doesn't persist
via URL) — switch it each visit using `browser_select_option` on
`select.sort-module_select__Bz7-4` to `most-recent`. Once sorted, each result
card shows a real `Updated: M/D/YYYY` date — a reliable recency signal, unlike
the other three sites. Pagination is numbered (1, 2, 3, ... 27) at the bottom
of the results list; click the number directly (plain `browser_evaluate`
click works). Job cards are `<a>` tags whose href matches `/jobs/\d+`; grab
title/location/date from the card's `innerText`. Amazon frequently posts
identical duplicate reqs (same title, same location, different job ID) —
treat those as one candidate, not two. Nearly every SDE-level posting shares
a boilerplate "3+ years professional software development experience, 2+
years design/architecture experience" bar regardless of the level implied by
the title, so a plain "Software Development Engineer" title is not
automatically junior.

**2026-07-24 update**: The "Kiro" and "Bedrock AgentCore" agentic-AI product
lines are worth checking specifically each run — plain "Software Development
Engineer, Amazon Bedrock AgentCore" (Bellevue, WA, job 10467661) used the
standard 3+ years SDE boilerplate (not the senior variant) and is a strong
direct match for agent-runtime/production-LLM work. A "Frontend Engineer,
Kiro" posting (job 10480789, 2+ years) also appeared but was excluded — it's
a genuine frontend role requiring JS framework (React/Angular) experience the
resume doesn't demonstrate, illustrating that a low years bar alone doesn't
override a mismatched role function. Sampled 5 "most-recent"-sorted pages
this run (up from prior runs' 1 page of 10) since Kiro/AgentCore/Bedrock
postings didn't all surface on page 1 — worth continuing at this depth.

**2026-07-27 update**: Sampled 5 "most-recent" pages again. Faster extraction
via `browser_evaluate` on `a[href*="/jobs/"]` (grabbing href + innerText only,
skipping the full snapshot) works well for scanning titles quickly, but it
does NOT capture the `Updated: M/D/YYYY` date shown on each card — that
requires reading the full card innerText/snapshot instead. Since the job-ID
dedup check catches previously-seen postings anyway, this wasn't a problem
this run, but worth remembering if date-based filtering is ever needed
directly from the list view. Every promising-looking posting this run
("Software Development Engineer, Developer Agents and Experiences",
"Software Development Engineer, Amazon Bedrock AgentCore", "Software
Development Engineer, Kiro", "Software Development Engineer, Prime Video
Sports News and Linear") turned out to already be in `seen_jobs.json` from
2026-07-02/07-15/07-24 — zero genuinely new Amazon matches this run despite
the Kiro/AgentCore/Developer-Agents title families still being present and
still fitting. "Software Development Engineer, Annapurna Labs, Elastic
Collectives" (job 10484052) had the standard 3+ year bar but required C/C++
for silicon/networking-adjacent work — no Python/AI overlap, excluded on
skill mismatch despite the low years bar.

**2026-07-20 update**: That boilerplate is specific to plain "Software
Development Engineer" titles. "Sr. Software Development Engineer"/"Sr.
Software Engineer" postings consistently use a different, more senior
boilerplate instead: "5+ years of leading design or architecture ... +
Experience as a mentor, tech lead or leading an engineering team" — a real
step up, not just a title bump, and worth excluding rather than
generously including. "Applied Scientist" postings consistently require
"PhD, or Master's degree and 4+ years" — an in-progress Master's doesn't
clear this bar on its own. "Solutions Architect"/"Specialist Solutions
Architect" (GTM/pre-sales flavored, distinct from plain SDE roles) carry an
8-10+ year bar, same pattern as Anthropic's Applied AI Architect family —
exclude on sight. This run's 10 most-recent AI-filtered postings were
entirely made up of these senior/PhD/pre-sales/manager patterns — zero fits.

**2026-07-28 update**: Sampled the top 10 "most-recent"-sorted results (didn't
page further since all three engineering-relevant new job IDs appeared on
page 1). New matches: "Software Development Engineer, AWS Agentic AI"
(job 10486378) and "Software Development Engineer, Developer Agents and
Experiences, Production Engineering" (job 10486685), both Seattle WA,
standard 3+ year SDE bar, both building agent control-plane/runtime
infrastructure — strong direct fits. "Software Development Engineer, Kiro"
(job 10486697, Seattle WA) also matched — this is a new job ID for the Kiro
team even though the title has appeared before, confirming Kiro reqs churn
IDs frequently and should be re-checked by ID each run rather than assumed
duplicate by title. Non-engineering postings on the same page (Sr. GTM Lead,
AI/ML Team Manager, 3x Applied Scientist, Sr. TPM, Sr. Worldwide Partner
Specialist) were skipped without opening — sales/management/PhD-flavored
titles, consistent with patterns excluded in every prior run.

**2026-07-31 update**: Sampled top 10 "most-recent" results. New match:
"Software Development Engineer, AWS Transform for Windows" (Santa Clara, CA)
— standard 3+ year SDE bar, building multi-agent systems to modernize legacy
Windows workloads, strong direct fit. This team posts near-identical
duplicate reqs across multiple legal entities simultaneously (three job IDs
— 10488610, 10489267, 10489268 — all with byte-identical description text,
same location, posted same run); treat as one candidate and log all IDs to
avoid re-surfacing the "different" duplicates next run. "Applied Scientist,
Observability, Prime Video" required PhD or Master's+experience, consistent
with the established Applied Scientist pattern — excluded. "Front-End
Engineer, Kiro" reappeared (new job ID) — consistent with the 2026-07-24
exclusion (frontend/React skill mismatch), not re-opened this run. A new
"Software Development Engineer, Neuron Foundation Tools" posting (Annapurna
Labs) had the standard 3+ year bar but centers on the team's C++
compiler/runtime — same skill-mismatch pattern as the 2026-07-27 Annapurna
Labs exclusion, excluded despite the low years bar.

**2026-08-05 update**: Sampled 5 "most-recent" pages again. Strong run: 6
new matches, all standard 3+ year SDE bar. "Software Development Engineer
II, AWS SageMaker AI" (Bellevue, WA, job 10492392) — Model Factory
distributed-systems platform for foundation-model training, direct AI/agent
overlap; a byte-identical duplicate req (job 10492391) appeared same
location, confirming the duplicate-req-across-legal-entities pattern isn't
limited to the AWS Transform team noted previously. "Software Development
Engineer, Kiro Web" — 3 near-identical duplicate reqs (jobs 10491873
Portland OR, 10491871 & 10491870 both Seattle WA) building the backend for
Kiro's agent-session web app (Agent Client Protocol) — strong fit given the
resume's MCP/Claude Agent SDK work; treat as one candidate, log all 3 IDs.
Plain "Software Development Engineer, Kiro" (Seattle, job 10490739) also
matched. "Software Development Engineer, Developer Agents and Experiences,
Production Engineering" (Seattle, job 10488273) is a new job ID for a title
already confirmed good (job 10486685 seen 2026-07-27) — confirms this title
churns IDs and should be rechecked each run like the Kiro family.
"Software Development Engineer II, AWS Transform" (Dallas, TX, job
10488611) — new location for the AWS Transform agentic-modernization team
(prior matches were Santa Clara). New non-SWE stretch: "Data Engineer I,
Veritas, Security Tools Foundation" (Seattle, job 10490830) — only 1+ years,
SQL/ETL/Python overlap with the resume's Snowflake/SQL work, but a data-
engineering function rather than software engineering; included per the
lean-generous guidance, worth deciding case-by-case each time it recurs.
Excluded this run on established patterns: "Applied Scientist"/"Sr. Applied
Scientist" family (PhD or Master's+4, multiple titles across pages),
"Sr."-prefixed SDE/SDM titles (5+ year senior boilerplate, e.g. "Software
Development Engineer, Quick" at 5+ years despite a plain-looking title —
reminder that the "Quick" team specifically uses the senior boilerplate, not
the standard 3+ bar), Worldwide/Partner Specialist and Solutions Architect
titles (GTM/pre-sales), Principal PM and Senior TPM titles, "Front-End
Engineer, Kiro" (established frontend/React mismatch), "Head of Developer
Enablement, Kiro" (management). Process note: the fast `a[href*="/jobs/"]`
href+innerText extractor (used for speed when scanning titles) does NOT
capture the `Updated: M/D/YYYY` date — confirmed again this run, repeating
the 2026-07-27 finding. Since Amazon is the one tracked site with real
per-posting dates, always do a second pass with the `card.innerText` variant
(walk up from the anchor to the ancestor whose `innerText` contains
"Updated:") before finalizing which matches make the report — don't rely on
"most-recent sort" position alone as a proxy for the recency window.
**2026-09-23 update — SITE CHANGED**: The tracked landing page
(`/content/en/artificial-intelligence-ai?...`) no longer has the embedded
`#jobs-search` widget or sort `<select>` — it's now a pure marketing page, so
the older navigation steps above don't work. Use the regular search page
instead: `https://www.amazon.jobs/en/search?base_query=AI&sort=recent&...`.
It shows real dates ("Posted September 23, 2026", "Updated about 3 hours
ago"). Fastest method: from that page, `fetch()` the site's own JSON from
`browser_evaluate`: `/en/search.json?base_query=AI&sort=recent&
normalized_country_code[]=USA&normalized_country_code[]=GBR&
schedule_type_id[]=Full-Time&category[]=software-development&
category[]=machine-learning-science&result_limit=100&offset=0`. Fields per job:
`id_icims`, `posted_date`, `title`, `normalized_location`,
`basic_qualifications`, `preferred_qualifications`, `description_short`. Gotchas:
`country[]=USA` is silently ignored by the JSON endpoint — use
`normalized_country_code[]`. With only keyword "AI" there were 6,242 hits,
so I added `category[]` filters (1,116 hits) — that's an addition to the
user's filters, flagged in the report; a second unfiltered-by-category pass
for titles containing Engineer/Developer/Data caught extra matches (e.g.
"Security Engineer, Forward Deployed Engineering", "AI Platform Data
Engineer, Ring Agent Platform Org"), so keep doing both passes. Job IDs are
now 105xxxxxx (they were 104xxxxxx in July). Job links are
`amazon.jobs/en/jobs/<id>`. Fresh AI/agent team names to look for: Kiro,
Seller Assistant, Marketing Cloud Assistant, Agentic Workspace, Velocity Labs
(Agentic AI), Specialist AI Tooling, AWS Context (listed under "Quick"),
Applied AI Solutions org, AWS Forward Deployed Engineering. Basic
qualifications in the JSON make the years bar a one-line regex; "…III" and
"Sr." titles use 5+ years, "SDE II" and plain SDE use 3+. AWS FDE "Security
Engineer" reqs need only 2+ years.

**2026-09-28 update**: `search.json` with `category[]=software-development&category[]=machine-learning-science`
gave 1092 hits; fetched first 100 (`result_limit=100&offset=0`, sorted recent) which
already spans back to Sept 16 — comfortably past the 7-day window, so a single
offset=0 fetch suffices. Extract only `{id_icims, title, normalized_location,
posted_date, basic_qualifications}` per job in the JS `evaluate` call (not the
full `description`/`preferred_qualifications` HTML) — pulling full records for
100 jobs floods the tool-result with megabytes of boilerplate/legal text.
Confirmed the base_query=AI keyword match is broad (catches generic Customer
Service/Ads/Device SDE reqs with no real AI tie merely because "AI" appears
somewhere in the text) — per established practice, still require an actual
AI/ML/agent-team connection in the title or description before including a
plain 3-year-bar SDE req, not just the keyword hit; a second `base_query=agentic`
pass (no category filter) is a good supplementary check and turned up only
PM/Solutions-Architect/GTM roles (pre-sales, excluded) beyond what the
category pass already found this run — worth keeping as a quick sanity pass
each time. New matches this run: "Software Development Engineer, Amazon
Quick" (NY, job 10561978, 3+ yrs, explicit "AWS AI services... Agentic AI
drives innovation" team), "Software Development Engineer II, Agentic
WorkSpaces Client" (Seattle, job 10560299, 3+ yrs, AWS Applied AI Solutions
org), "Software Development Engineer, Global Media and Entertainment
Security" (Denver, job 10559473, 3+ yrs — despite the generic title, the team
is building "an AI-powered agent that lets builders run security assessments
... generating threat models, architecture diagrams, code review findings" —
direct overlap with the resume's guardrails/security-scanning work, worth
reading past a generic-sounding security title to check for an agentic
component), "Software Development Engineer - Expert Consultant, AGI - Data
Services" (Bellevue, job 10554286, 3+ yrs, human-in-the-loop/model-in-the-loop
training-data pipelines for AI solutions). Excluded this run: "Software
Development Engineer, Ads AI Core Infra" (Seattle) — team name says AI but
the description is generic ad-lifecycle infra (accounts/permissions/campaign
mgmt) with no actual model/agent component, a reminder that "AI" in a team
name doesn't guarantee an AI-specific role; "Software Development Engineer -
Test, Device Partnerships, Prime Video" (London) — penetration-testing/manual
QA for streaming devices, no AI tie despite surfacing under the AI keyword
search. "Seller Assistant"/"Delivery Consultant - AI/ML"/"AWS Artifact"/"Kiro"/
"AWS Quick" postings from prior runs recurred under the same job IDs —
already logged.

## OpenAI
`openai.com/careers/search/?c=<team-uuid>,<team-uuid>,...` renders every
matching job (87-90+ for a 5-team filter as of 2026-07-08) in one flat list in the DOM — no
pagination or load-more needed, no filter interaction needed either since the
team IDs are baked into the URL. Sort order is alphabetical by job title, NOT
by recency, and there is no visible sort control to change it. No posted-date
is shown anywhere — not on the search list, not on individual job detail
pages — so recency is entirely unverifiable on this site; treat every match
as date-unknown and do not treat list position as a recency proxy. Most
engineering postings do not state a hard "X years required" the way
Amazon/Meta do (OpenAI's roles read more like qualitative "You Might Be a
Good Fit If You" bullet lists) — fit is decided by matching those bullets
against the resume's actual skills, not by a years cutoff. Individual job
pages live at `openai.com/careers/<slug>/`, where `<slug>` is embedded in the
search-page card's link href.

**Search Notes (2026-07-08)**: Extracted 87 jobs via JS from the search page.
All jobs are in Applied AI Engineering and Codex - Engineering teams. Many
roles are specialized (iOS/Android engineers, frontend engineers, growth
marketing) with limited overlap to the resume unless willing to pivot into
mobile development. Strong matches: Backend Software Engineer (Applied
Foundations), Full Stack Software Engineer (Applied Foundations & Agent
Enablement), Research Engineer (Applied AI), Machine Learning Engineer
(Integrity), Data Engineer. Engineering Manager and Principal roles exist but
stretch for current career level. Page structure stable; approach of extracting
all hrefs via JS query selector 'a[href*="/careers/"]' works well.

**2026-07-15 update**: Total listing count under the same 5-team filter
shifted 87 → 80 without any date signal to explain why (postings likely
closed/opened) — since there's no way to tell "genuinely new" from "just not
previously logged," this run re-judged every link not already in
`seen_jobs.json` on its own merits rather than assuming the whole diff was
new. Confirmed the qualitative/no-years-cutoff pattern holds across the
Codex team specifically: "Codex Enterprise" (SF + London), "Codex — User
Activation", "Codex Cyber", and "Full Stack Software Engineer, Codex" all
matched well (Python/TypeScript/Go, agent-platform or dev-tooling work, no
hard years bar) and are worth rechecking each run. Ruled out this run:
"Cloud Infrastructure" and "GPU Infrastructure" postings (5+ years), "Infra
Reliability" and "Integrity Foundations" (London) postings (4-5+ years,
SRE/trust-safety functions, not a fit), "Computer Use & Frontier Interfaces"
(wants Apple/Windows/desktop app experience), and "Web Layer" (wants strong
C++/Chromium/Electron experience) — none of these match the resume's
backend/agent-tooling skill set. Given ~50 Applied-AI-Engineering postings
remain unopened each run, a future pass could work through the rest
(ads/monetization/infra-flavored SWE roles) if more thoroughness is wanted.

**2026-07-20 update**: Did that fuller pass (~50 previously-unopened postings,
opened ~15 individually). Findings: the "no hard years cutoff" pattern from
Codex/Applied Foundations does NOT generalize to the rest of the board —
most non-Codex postings do state explicit years, just embedded in
prose rather than a "Basic Qualifications" list, so they're easy to miss by
skimming titles alone. Confirmed years bars found: "Founding" titles (6+
years), "Performance Engineer" (7+ years + OS-internals depth), "Ads
Manager"/monetization SWE (7+ years), "Analytics Engineer" (5+ years, and a
data/SQL function not software engineering), "Health AI" full-stack (5+
years). "Protection Scientist Engineer, Integrity" (appears in multiple
cities incl. London) is trust-and-safety investigations work, not software
engineering, despite the "Engineer" title — 4+ years but wrong function.
"Model Designer" is a UX/product-taste role with no coding requirement,
not an engineering role despite being listed under Applied AI. New matches
that DID clear the bar: "Full Stack Software Engineer, Codex Cloud Apps" and
"Software Engineer, Codex - Enterprise Controls" — both in the Codex team,
no stated years minimum, backend/full-stack skill overlap. Net takeaway:
keep prioritizing the Codex team specifically (consistently no years bar,
consistently good skill overlap) over the broader Applied-AI-Engineering
list, where most individual reqs (ads, infra, safety, analytics, legal,
performance) turn out to carry a senior bar once actually opened — title
alone under-predicts this for OpenAI more than for the other companies
tracked.

**2026-07-24 update**: Confirmed the total-listing-count churn continues (95
raw links this run under the same filter, ~76 not yet in seen_jobs.json —
most of that diff is postings previously opened-and-rejected in prior runs
rather than genuinely new, since rejected postings never get logged; re-check
`site_notes.md`'s per-title callouts below before reopening a familiar title
family). New Codex team postings found and matched: "Full Stack Software
Engineer, Cybersecurity Products" (no years bar, backend/API/orchestration
for AI security tooling — good fit) and "Software Engineer, Cyber Frontier"
(no years bar, Python/TypeScript + ML systems, but heavily
cyber-threat-research-specialized — bigger stretch than other Codex matches,
worth a second look each run rather than an automatic include). Outside
Codex, "Software Engineer, ChatGPT Shopping" (Applied AI Engineering) had no
numeric years numeral, only a soft "significant experience" bar, and reads as
a genuine full-stack/AI-native-product fit. Two more infra-flavored
"Software Engineer, X" postings were opened and excluded despite having *no*
explicit years number anywhere in the text: "Software Engineer, Core
Services" (distributed-systems/caching/Temporal depth beyond the resume) and
"Software Engineer, ChatGPT Infrastructure" (explicitly states "We're hiring
Senior and Staff Engineers" in prose despite a plain title and zero digits) —
a reminder that the absence of a numeric years bar is not itself a green
light; always read the full "About the Role"/"You Might Thrive If" text, not
just grep for "years". "Data Engineer, Core Experimentation" (Seattle) also
looked promising at a glance but requires "8+ years of any software
engineering experience" buried after an initial "3+ years as a data
engineer" line — read past the first years mention on data-adjacent titles.

**2026-07-27 update**: Confirmed board now has ~85 flat listings under the
filter. Faster check method found: `document.body.innerText.match(/[^.]*\d+\+?
years?[^.]*\./gi)` plus a `/Senior|Staff|Principal/gi` match on a job's detail
page pulls out the years/seniority sentence directly, much faster than
reading the whole "You Might Thrive If" block manually — use this as a first
pass, but still skim the full thrive section afterward since some
disqualifying signals (wrong skill domain, e.g. growth/marketing analytics)
don't show up as a years number at all. New matches found outside Codex:
"Full Stack Software Engineer, ChatGPT Finances" and "Full Stack Software
Engineer, ChatGPT ImageGen" — both no explicit years/seniority language,
full-stack consumer-product engineering (frontend+backend+API), reasonable
fit though frontend depth is a stretch vs. the resume's backend lean. Ruled
out this run (all opened individually, all had explicit high bars once
checked): "Full Stack Software Engineer, OpenAI Edu" (5+ years), "Software
Engineer, Full Stack, Revenue Platform" (5+ years), "Software Engineer,
Payments" (5+ years, payments-systems specific), "Software Engineer,
Monetization Product & Platform" (7+ years), "Software Engineer, Ad Formats"
(7+ years — confirms the whole Ads/monetization family stays at 7+ regardless
of specific sub-title), "Software Engineer, Developer Productivity" (5+
years + heavy Kubernetes/Terraform infra specialization), "Software Engineer,
Youth Well-Being" and "Software Engineer, Localization" (both explicitly say
"Senior Software Engineer" in the About-the-Role prose despite plain titles).
"Full Stack Software Engineer, Growth" had no years bar but is a growth-
marketing/A-B-testing/funnel-optimization function, not a skill match to the
resume — a reminder that "no years bar" alone doesn't make a role a fit if
the actual function is off. Roughly 25 unopened postings remain
(software-engineer-database-systems, data-infrastructure, delivery-cd,
observability, financial-engineering, build-systems-ci, caching-infrastructure,
and a few others) if a deeper future pass is wanted.

**2026-07-28 update**: Board shows ~86 listings, but only one link wasn't
already in `seen_jobs.json`: "Research Engineer, Retrieval & Search, Applied
Engineering" (San Francisco). Its direct URL returns a 404, and even clicking
through from the search-results card (client-side route) lands on the same
404 page — the posting is listed in the search index but the underlying job
page is gone, likely closed since indexing. Treated as not currently
open and excluded rather than reported. If this happens again, it's worth
noting as a general site quirk: don't assume a link surfaced in the search
DOM is still live — a 404 on click means skip it, not a bug in the
extraction method.

**2026-07-31 update**: Board shows ~90 listings. The "Research Engineer,
Retrieval & Search, Applied Engineering" posting that 404'd on 2026-07-28 is
live again this run (confirms postings can toggle open/closed, not just
close permanently — worth rechecking a previously-404'd posting rather than
assuming it's gone for good) — no years bar, matched. Did a fuller pass of
the ~13 previously-unopened infra/ops-flavored "Software Engineer, X"
postings this run using the regex years/seniority extraction method from
2026-07-27. Confirmed years bars: "Database Systems" (4+ yrs + tech-lead
scope + C++ core engine), "Data Infrastructure" (4+ yrs + distributed-data
specialization), "Build Systems/CI" (5+ yrs), "Caching Infrastructure" (5+
yrs), "Financial Engineering" (5+ yrs), "Scaled Abuse" (5+ yrs backend + 2+
yrs fraud-ops), "Privacy & Compliance" (5+ yrs) — all excluded on years
and/or skill mismatch (deep distributed-systems/Kubernetes/C++ specialization
the resume doesn't show). Two more had **no explicit years number** but were
excluded on skill grounds anyway: "Delivery / CD" (heavy Kubernetes/GitOps/CD
platform ownership, zero overlap on resume) and "Reliability" (SRE/IaC/chaos-
testing focus, zero overlap) — reinforces the standing note that "no years
bar" doesn't itself signal fit; the qualifications/"You Might Thrive"
text still needs individual judgment on skill overlap. Two new matches found
among the no-years-bar postings: "Enterprise Verticals" (full-stack product
eng for AI enterprise workflows, Python/backend overlap, customer-facing
ownership scope is a stretch) and "Observability" (AI-native
incident/dashboard tooling connects to the resume's LangSmith eval-framework
work, though the team's core distributed-logging-infra depth is a gap) —
both included as stretches per the "lean generous" guidance. "Frontend
Engineer, Financial Web Platform" (no years bar) excluded on function
mismatch — pure frontend role, resume has no frontend/React work despite
listing TypeScript as a skill. Remaining unopened: engineering-manager-*
(all management, skip on sight), growth-*/ads-*/monetization-* (established
7+/senior patterns), android/ios-engineer-* (mobile mismatch),
protection-scientist-engineer-* (trust-safety, established), model-designer
(no-code UX role), founding-*/senior-staff-*/principal-* (established
senior tiers), product-manager-legal/deployed-product-manager (PM not SWE),
subject-matter-expert-investment-banking (finance SME not SWE) — these are
now consistently-excluded families across 3+ runs and probably don't need
individual re-opening each time, just a title-pattern skim to confirm no new
non-senior variant has appeared.

**2026-08-05 update**: Board shows 90 listings, flat vs. ~90 on 2026-07-31. Used the regex years/seniority extraction method to check
several previously-unopened title patterns. New matches: "Full-Stack
Engineer, ChatGPT Education & Learning" (SF or NYC, no years bar) — full-
stack product engineering on AI-native learning features inside ChatGPT,
good overlap though frontend depth is a stretch. "Software Engineer,
Product - Core Experimentation" (Seattle, no years bar) — full-stack work on
the Statsig-derived experimentation/rollout platform, decent backend
overlap and a loose conceptual tie to the resume's LangSmith eval-framework
work. Ruled out (all opened individually): "Software Engineer, Cloud
Agents" (Codex team — despite being Codex, explicitly states "9+ years of
professional engineering experience," a reminder the Codex "no years bar"
pattern isn't universal either), "ChatGPT Performance Engineer" (7+ years),
"Data Engineer, Core Experimentation" (Seattle — same "3+ years as data
engineer, 8+ years overall" buried-bar pattern as the 2026-07-24 finding,
recurring under this exact title), "Software Engineer, Infrastructure -
Core Experimentation" (Seattle, no years bar but heavy low-latency/
distributed-systems/observability-infra depth — excluded on skill grounds
like the established Reliability/Delivery-CD pattern), "Analytics Engineer,
Safety Systems" (5+ years, data-role function not SWE). The
previously-unopened "Core Experimentation" (ex-Statsig) team turns out to
have a real mix — Product/no-bar (match), Data (buried high bar, skip),
Infrastructure (no bar but wrong skill depth, skip) — worth opening each
individual title under this team rather than assuming from one.

**2026-09-23 update**: 101 listings in the flat list (via `a[href*="/careers/"]`
excluding search/root links). Detail pages fetch fine with `fetch('/careers/<slug>/')`
from `browser_evaluate` (server-rendered), so the years regex can be run on
a batch of slugs at once; for no-years postings, read the text after "You
might thrive" instead. New matches: the "Plugin Developer Platform" and
"Plugin Ecosystem" teams (MCP/connectors/plugins for ChatGPT+Codex, no years
bar — the closest match to the resume's MCP + RBAC work seen here so far).
Confirmed high bars (excluded): Codex for Finance backend/full-stack (5+),
Gov full-stack (9+), "Product Engineer, Full Stack - Agents" (7+), Consumer
Health and Healthcare (5+ each), Native Learning Experiences (5+ nice-to-
have), Habitat/Online Data (8+), Monetization ML Infrastructure (7+). No-
years but excluded on skill/function: "Product Engineer, Cyber" (Go +
networking/infra), "Emerging Products" (strong frontend), "Ads Integrity"
(large-scale anti-abuse infra), "Model Deployment, ChatGPT Engineering"
London (GPU-fleet deployment infra), plain "GTM Growth Engineering". Also
present: "Software Engineer, Full-Stack - Core Experimentation" (Seattle) —
same Statsig team as the 08-05 "Product - Core Experimentation" match, no
years bar, reported as a stretch sibling. Check every listed slug against
`seen_jobs.json` AND against this section's excluded lists before opening.

**2026-09-28 update**: 97 flat listings via `a[href*="/careers/"]`. New team
found: "Software Engineer, Cooperative AI" (SF/Seattle, no years bar) — builds
an "AI-powered knowledge system"/automation/agent systems for internal+
external customers, direct overlap with the resume's agentic-AI/MCP work —
included. "Machine Learning Engineer, Monetization AI/ML" (no years bar,
despite "Monetization" normally implying the established 7+ senior family —
this specific req reads IC-level, "Research Engineer... deploying models to
production") and "Machine Learning Engineer, Core Experimentation" (Seattle,
Statsig-derived team, no years bar but "led ambiguous 0-to-1 production ML
products" phrasing suggests some seniority expectation — included as a
stretch) both included. Confirmed high bars (excluded): "Full-Stack Software
Engineer, Education" (5+, despite no PhD/Staff signal), "Software Engineer,
Search Infrastructure" (2 Senior/Staff/Principal mentions in body text).
No-years but excluded on skill mismatch: "Software Engineer, Resilience
Engineering" (SRE/Infrastructure-as-Code, 0→1 reliability tooling — no
overlap), "Software Engineer, Product Velocity" (Bazel/Buildkite/Kubernetes/
Temporal monorepo build tooling — no overlap). All Android/iOS Engineer
titles, Engineering Manager-*, Product Manager-*, Growth-*, Founding-*,
Principal-*, Staff-*, "Subject Matter Expert, Investment Banking", "Tech Lead
Manager", "Protection Scientist Engineer, Integrity" (both SF and London) —
all consistent with established exclusion families, skipped without
individual re-opening. "Backend/Full Stack Software Engineer, Codex for
Finance" reconfirmed under the established 5+ years Codex-for-Finance bar.

## Cursor
`cursor.com/careers` is a single static list of ~120 roles (all in the DOM,
no pagination or filters needed), each linking to `cursor.com/careers/<slug>`.
No posted dates anywhere, so recency is unverifiable and everything not in
`seen_jobs.json` is "new". Extract with `a[href*="careers/"]` and read
`innerText` (title | team | Full-time | location). Detail pages are
server-rendered: `fetch('/careers/<slug>')` then remove `script,style,noscript`
before reading `textContent` (otherwise you get a wall of Next.js script
text) and look at the "You may be a fit if" section. Most engineering
postings state no years number; the exception seen: US "Forward Deployed
Engineer" asks 5+ years (the London/EMEA one gives no number). Roles are
split into Sales/Solutions/Customer Success (skip — GTM) and Engineering.
The engineering roles that fit: Agent Evaluation and Quality, Agent Harness,
Enterprise Platform (RBAC/SCIM). Also present each run: Bugbot/Product/
Generalist (product-taste heavy), ML/infra/pretraining/RL (specialist),
and "Software Engineer, New Grad 2027" (requires projected graduation Spring
2027 + a reviewable shipped project; reported as a long shot since the
resume's M.S. end date is unknown).

**2026-09-28 update**: ~130 listings now (grew from ~120). Established fits
(Agent Evaluation and Quality, Agent Harness, Enterprise Platform, plain
Security) were all already in `seen_jobs.json`. Two new title families found
and matched: "Software Engineer, User Operations" (no years bar — builds
"AI-powered systems that synthesize customer signal at scale," dashboards/
data pipelines, decent LLM+data overlap) and "Security GRC Engineer" (no
years bar — SOC 2/ISO 27001/ISO 42001/AIUC-1 compliance frameworks, "use
coding agents ... to confirm what we say is what we do," pairs the resume's
Semgrep/Trivy/SonarQube vuln-scanning and compliance work with an AI-agent
angle). Excluded on skill mismatch (no years bar but specialist domains, all
opened): "Software Engineer, Client Infrastructure" (Electron/native desktop
apps), "Software Engineer, Services Platform" (Temporal/durable-workflow
infra), "Software Engineer, Model Routing & Inference" (GPU inference/
distributed-systems specialist), "Software Engineer, Billing" (Stripe/
financial-ledger specialist). "Engineering Manager, Agent & Product Security"
and other Engineering Manager-* titles skipped by title (management). ML
specialist family (ML Platform/Infrastructure/Research/Research Tools,
Pretraining, RL Data, RL Environments) skipped by title per established
pattern. GTM/Field Engineer/Forward Deployed/Account Executive/Solutions
Architect/Regional Director families remain sales/customer-facing, skipped.

## Citadel
`citadel.com/careers/open-opportunities/` lists ~60 roles, 10 per page over
6 pages, newest-first by default; no posted dates shown. "Software Engineer –
University Graduate (US/Europe)" programs appear near the top and state no
experience cap (just a Bachelor's/Master's in CS) — reported as long shots. Pages are directly
navigable at `/careers/open-opportunities/page/N/` and each server-renders
its cards, so `fetch()` from `browser_evaluate` on pages 1-6 and reading
`a[href*="/careers/details/"]` gives everything at once. Detail pages
(`/careers/details/<slug>/`) are short, also fetchable; strip
`script,style,nav,header,footer` and read the "Skills & Talents"/"Skills and
Qualifications" section. The list is dominated by intern/PhD/graduate/
trader/quant-researcher roles — skip those. Engineering-relevant ones seen:
"Software Engineer" (6+ years), "Site Reliability Engineer" (no years bar,
SRE function — skipped), "Quantitative Developer – Data Strategies Group"
(good fit), "Sector Data Scientist, Central Team" (up to 2 years),
"Global Quantitative Strategies | Machine Learning Engineer" (needs
PyTorch/C++/CUDA distributed-training depth — skipped), "Quantitative
Research Engineer" (C++ — skipped), "Equities Engineering | Product Frontend
Engineer" (frontend — skipped).

**2026-09-28 check**: Sampled all 6 pages via `fetch()`. Both established fits
("Quantitative Developer – Data Strategies Group", "Sector Data Scientist,
Central Team") already in `seen_jobs.json`. Everything else is intern/PhD/
trader/quant-researcher roles or established exclusions (plain "Software
Engineer" 6+ years, SRE no-fit, GQS ML Engineer PyTorch/C++/CUDA, Equities
Frontend Engineer). Zero new matches.

## Two Sigma
`careers.twosigma.com/careers/OpenRoles` shows 30 roles, 10 per page,
sorted alphabetically by title (NOT by recency), no posted dates. Paging
works by URL: `?jobRecordsPerPage=10&jobOffset=0|10|20` (a larger
`jobRecordsPerPage` is ignored; clicking the page-number links via JS
navigates the page and destroys the evaluate context — navigate by URL
instead). Job pages are `/careers/JobDetail/New-York-New-York-United-States-<Title-Slug>/<id>`
and appear fetchable with any slug as long as the numeric id is right; strip
script/style/nav and read "You should possess the following qualifications".
Postings state "Minimum N year(s) required; X-Y years preferred" so the
minimum is very low (1 year) even when the preferred range is 5-10 — treat
the minimum as the hard bar and the preferred range as the gap to note.
Engineering-relevant roles this run: "AI Solutions Developer" (strong fit),
"Quantitative Software Engineer" (stretch), "Quantitative Software Engineer:
Fast Engineering"/"Quantitative Architect/Software Engineer: Macro
Engineering"/"Quantitative Software Architect" (senior/architect-flavored,
skipped), "GPU Performance Engineer", "Modeling Workflow Specialist" (GPU
acceleration), "Infrastructure Engineer - Linux", "Production Engineer"
(trading-systems SRE), "Head of High-Frequency Market Data Engineering" —
all skipped on skill/seniority mismatch.

**2026-09-28 check**: 30 roles across 3 pages. "AI Solutions Developer"
already in seen_jobs.json. New titles this run -- "AI Fluency: Program
Manager" (PM, skip), "AI Research Scientist" (Campus/Intern, PhD-flavored,
skip), "Post-Training Research Scientist" (research, skip), "Production
Engineer, Electronic Trading Systems"/"Production Engineer, Two Sigma
Securities" (established trading-systems SRE exclusion), "Infrastructure
Engineer" (Tokyo -- location mismatch) -- all excluded. Rest of the list is
quant-researcher/quant-software-architect roles matching established
exclusion patterns. Zero new matches.
