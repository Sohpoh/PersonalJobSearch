# Site Notes

Notes the job-search skill has learned about how to navigate and filter each
company's career site (search/filter behavior, pagination style, where posted
dates show up, quirks). Filled in automatically — no need to edit by hand.

## Anthropic
Greenhouse-hosted board (`job-boards.greenhouse.io/anthropic`). The
`?departments[]=<id>` query param is a real, working filter — all matching
roles render in the DOM at once (no pagination/load-more needed). No
posted-date is shown anywhere on this board, so recency can't be verified;
treat matches as date-unknown. Direct posting links are also on
`job-boards.greenhouse.io/anthropic/jobs/<id>`.

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
