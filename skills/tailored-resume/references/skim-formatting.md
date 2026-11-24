# Skim-friendly formatting (FINAL resume)

Reference for **tailored-resume** Step 4 and the Step 5 skim test. The deterministic parts of these rules are checked by [`evals/check_resume_format.py`](../../../evals/check_resume_format.py).

**Goal:** a recruiter reading only the **bold text, job titles and each role's first bullet** sees within 10 seconds that the candidate meets the top must-haves. Bold points to proof; it never adds content.

## Bold
- At most one 2–6 word phrase per bullet, preferably the quantified result that proves a must-have (e.g. "…holding **99.5% uptime**").
- Only bullets that map to a must-have or top-5 keyword: about half per role, never all.
- Summary: ≤ 2 phrases. Name bold. Role lines: title bold, company/dates regular. Section headings bold.
- ~8–14 bold phrases in total.

## Never bold
Whole bullets, >1 phrase per bullet, Core Skills, Education, Certifications, dates, company names, contact details, soft words ("strong", "cross-functional", "stakeholders", "team", "successfully"), or anything unsupported. Bold is the only emphasis: no italics, underline, colour, caps or symbols.

## Skim order
Summary line 1 mirrors the JD's title and seniority (as far as true), then years and domain. Each role leads with the bullet matching the #1 must-have. Bullets: verb first, 1–2 lines, numerals, one idea each. Recent roles 4–6 bullets; older 2–3. Single column; dates after ` | `.

## Basic formatting only
- Create the Doc in **one** Drive create call from simple HTML: `<h1>` name, `<p>` contact, `<h2>` sections, `<p>` role lines with `<b>` title, `<ul><li>` bullets, `<b>` skim phrases. No CSS, fonts, spacing or page settings.
- Don't restyle, read back, preview, screenshot or export.
- Length by word count: ~450–550 words per page.
