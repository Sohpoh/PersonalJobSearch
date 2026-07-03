# Personal Job Search

A Claude Code skill that automates a recurring job search: it visits a
tracked list of company career pages, filters new postings against my
resume, and writes a dated report — skipping anything already surfaced in a
past run.

## Layout

- **`.claude/skills/job-search/`** — the skill itself (`SKILL.md` plus a
  `.docx`-extraction helper script).
- **`companies.md`** — company name + careers-page URL, one per company. This
  is the only file meant to be hand-edited to add/remove companies.
- **`site_notes.md`** — learned navigation quirks per site (pagination style,
  where posted-dates show up), written by the skill so later runs don't
  re-explore each site from scratch.
- **`seen_jobs.json`** — dedup log of jobs already surfaced in a past report.
- **`reports/`** — dated markdown reports (`YYYY-MM-DD.md`) of matched
  postings, each with a one-line reason it matched.

## Requirements

- [Claude Code](https://claude.com/claude-code), since this is a Claude Code
  skill, not a standalone script.
- The **Playwright MCP server** connected to Claude Code — the skill drives
  browser navigation (`browser_navigate`, `browser_snapshot`, `browser_click`,
  etc.) to load JS-rendered career pages, not `fetch`/`curl`.
- Python 3 (stdlib only, no extra packages) — used by
  `scripts/extract_docx_text.py` to pull text out of a `.docx` resume the
  first time `resume_profile.md` is generated. Not needed if your resume is
  already `.pdf`/`.md`/`.txt`, or once `resume_profile.md` exists.

## Not in this repo

`resume_profile.md` and the source resume file are gitignored — they contain
personal contact info and aren't needed for the skill logic to be useful to
someone else.

## Usage

From this directory, ask Claude Code to run the job search (e.g. "check my
job list" or "anything new at the companies I'm tracking") — the skill
triggers automatically. See `.claude/skills/job-search/SKILL.md` for the full
behavior spec.
