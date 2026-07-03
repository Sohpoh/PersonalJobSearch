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

## Meta
`metacareers.com/jobsearch/` supports real query-param filtering
(`teams[n]=`, `roles[n]=`, `sort_by_new=true`). Results paginate 10 at a time
via a "Show more" button / "Page X of Y" counter. Each card links to
`/profile/job_details/<id>`, which redirects to the canonical
`/profile/job_details/<id>/` detail page — read that page's "Minimum
Qualifications" heading, not the title: titles here are frequently generic
("Software Engineer, Machine Learning ...", "Software Engineer - Backend,
Standalone Apps Team") but the postings under "Standalone Apps Team" in
particular have consistently required 12+ years of experience regardless of
title. No posted-date shown on cards or detail pages.

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
matching job (90+ for a 5-team filter) in one flat list in the DOM — no
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
