---
name: job-search
description: Searches a user-maintained list of company career sites for recently posted job openings that match their resume, using live browser automation (Playwright) to navigate each site's search and filters. Learns each site's navigation quirks (how to search, filter, paginate, where posted-dates show up) and saves them to a separate notes file so future runs don't re-explore blind. Saves a dated markdown report of matches and never re-surfaces a job already shown in a past run. Use this whenever the user asks to check for new job postings, scan their tracked companies, run their job search, or look for openings at specific companies on the list — even if phrased casually like "anything new at the companies I'm tracking", "check my job list", "see if there are new roles at Anthropic/Google/Meta", or "run my weekly job check."
---

# Job Search

Checks each company on the user's tracked list for recently posted roles that
genuinely fit their resume, and writes a dated report. This is meant to be run
repeatedly (e.g. weekly) — treat every run as building on the last one, not
starting from scratch.

## Before you start

Find these files in the current working directory (they hold user state, not
skill logic, so they live alongside the resume rather than inside this skill
folder):

- **Resume**: a file matching `resume`/`cv` (case-insensitive) with extension
  `.docx`, `.pdf`, `.md`, or `.txt`. If more than one candidate exists or none
  is found, ask the user which file to use.
- **`resume_profile.md`**: the working profile judged against — see Step 1.
  Create it from the resume if missing.
- **`companies.md`**: the list of companies to check — just a name and a URL
  per company. This is user-maintained; don't write anything back into it.
  If it doesn't exist, create it from the template below and ask the user to
  add at least one company before continuing.
- **`site_notes.md`**: skill-maintained notes on how to navigate/filter each
  company's site, keyed by the same company name used in `companies.md`. This
  file is where learned navigation notes live — never `companies.md`. Create
  it from the template below if missing.
- **`seen_jobs.json`**: dedup log, `{}` if new.
- **`reports/`**: directory where dated reports land; create it if missing.

`companies.md` template (user edits this — just name + URL):

```markdown
# Companies to Search

## <Company Name>
<careers page URL>
```

`site_notes.md` template (skill edits this — do not ask the user to fill it in):

```markdown
# Site Notes

## <Company Name>
<learned notes go here after the first successful run>
```

## Step 1 — Build the resume profile

**If `resume_profile.md` already exists, read it and use it as-is** — it has
two sections, both of which matter for Step 5:
- **"Resume"**: a plain transcription of the resume's actual content.
- **"Additional Preferences"**: things the user has added that the resume
  itself doesn't state (e.g. locations they're open to, roles to avoid,
  comp/remote preferences). Weigh these as real constraints, not soft hints —
  e.g. a stated location list narrows where a match can be, not just a nice-
  to-have.

Don't silently regenerate or overwrite this file.

**If it doesn't exist yet** (first run, or the user says the resume changed
and asks you to refresh it), derive the "Resume" section from the resume:
- `.pdf` / `.md` / `.txt`: read directly.
- `.docx`: the plain `Read` tool cannot open binary `.docx` files. Run
  `scripts/extract_docx_text.py <path-to-resume>` and read its stdout instead.

Write `resume_profile.md` with a **"Resume" section that's a plain
transcription** of the resume's actual content — education, work experience
with its bullets, projects, skills, certifications — organized clearly but
not interpreted or judged. Don't add conclusions like "not a fit for X" or
"seniority level: Y" into this section; it's a record of what's on the
resume, not an analysis of it. Below it, add an **"Additional Preferences"**
section (empty or with a prompt for the user to fill in) for anything not on
the resume. Do the reasoning about seniority, fit, and exclusions fresh in
Step 5 each time, from this raw content — that way it stays available to
reconsider rather than being locked in as a stale judgment call.

## Step 2 — Determine the recency window

Default to the last 7 days. If the user's request mentions a different window
("last two weeks", "since yesterday"), use that instead.

## Step 3 — Visit each company

Use the Playwright tools (`browser_navigate`, `browser_snapshot`,
`browser_click`, `browser_type`, `browser_select_option`, `browser_wait_for`,
etc.) — not `fetch`/`curl` — since these sites are JS-rendered and often need
interaction (search boxes, filter panels, "load more" buttons) to reveal
listings.

For each company in `companies.md`:

1. Navigate directly to its URL and **read the listings that are already
   there.** The user's URLs are typically already pre-filtered (search terms,
   team, location, level, etc. baked into the query params) — don't re-search
   or add your own filters on top of what's already loaded. The only reason
   to interact with the page at all is to reveal listings that are already
   part of that filtered set but not yet visible (paginating through the
   pages, clicking "load more," waiting for infinite scroll) — not to change
   what's being filtered for.
2. **If `site_notes.md` already has a section for this company describing
   its pagination/date-display behavior, follow those notes directly**
   instead of re-exploring — that's the point of recording them.
3. **If there's no section yet for this company (or it's empty)**, observe
   as you go:
   - Pagination style: "Next" button, "load more" button, or infinite scroll.
   - Where/how posted-dates appear: exact date, relative ("3 days ago"), or
     not shown at all.
4. Extract candidate listings: title, location, posted date (if any), and a
   direct link to the posting.
5. **Write what you learned back into that company's section in
   `site_notes.md`** (only after a successful pass) so the next run can skip
   the exploration. Add the section if it doesn't exist yet. Keep notes short
   and concrete — e.g. "Postings show relative dates like 'Posted 3 days
   ago'; pagination via 'Show more results' button at the bottom, click until
   it disappears; no date shown at all, recency unverifiable." If the site
   clearly changed and the existing notes no
   longer match what you observe, update them. Never write navigation notes
   into `companies.md` — that file only ever holds names and URLs.
6. If a site has no visible posted-dates at all, don't guess — rely on the
   site's own newest-first ordering, pull from the top, and flag in the
   report that recency is approximate for that company.

Pace requests reasonably; these are ordinary company career pages, not an
API — don't hammer them with rapid repeated navigation.

## Step 4 — Filter to the recency window

Drop listings clearly older than the window from Step 2. Keep listings whose
date is unknown or approximate, but flag them as such.

## Step 5 — Judge fit against the resume

For each remaining candidate, use judgment rather than keyword matching: read
the posting's actual title and qualifications/requirements text, and check it
against `resume_profile.md` from Step 1 — does the role type, seniority, and
required skill set genuinely line up? Titles are frequently generic or
misleading (e.g. a plain "Software Engineer" title requiring 12+ years), so
the qualifications text is what actually decides it, not the title.

**Lean generous, not strict.** The user would rather see a borderline role
and decide for themselves than have it silently filtered out. A posting
asking for somewhat more experience than the resume shows (e.g. 3-4 years
against ~2), or covering most but not all of the required skills, or phrased
as "Senior" without an explicit years requirement, is still worth surfacing
— note the gap in the one-line reason rather than discarding it. Only
discard a posting when the mismatch is clear and substantial: an explicit
double-digit years requirement, a fundamentally different role function
(e.g. sales/solutions-architecture vs. engineering, when the resume shows no
customer-facing background), or a location that doesn't overlap with
anything in "Additional Preferences." When genuinely unsure whether
something clears the bar, include it rather than cut it.

Keep every match with a one-line reason each — including a candid note when
it's a stretch (e.g. "asks for 4 years, resume shows ~2, but skill overlap
is strong").

## Step 6 — Dedup against past runs

Load `seen_jobs.json`. Drop any matched job whose link is already a key in
that file — it was already surfaced in an earlier report.

## Step 7 — Write the report

Save to `reports/<YYYY-MM-DD>.md` (use today's date; if a report for today
already exists, append to it rather than overwriting). Format:

```markdown
# Job Search Report — <date>

## <Company>
- **<Job Title>** — <Location> — <posted date, or "date unknown">
  <link>
  Why it matched: <one line>
```

Group by company; omit companies with no new matches (but still mention in
the chat summary that they were checked and came up empty).

## Step 8 — Update the dedup log

Add every job included in this report to `seen_jobs.json`:

```json
{
  "<job link>": {
    "title": "<title>",
    "company": "<company>",
    "first_seen": "<YYYY-MM-DD>"
  }
}
```

## Step 9 — Summarize in chat

Report which companies were checked, how many new matches were found per
company, and the report file path. Don't paste the full report inline if it's
long — point to the file.
