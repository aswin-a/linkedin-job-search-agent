---
name: tailored-resume
description: Three-way mapping of Ideal Resume x Master Resume x JD, targeted gap questions, then a FINAL tailored resume that is true, ATS-safe and skim-friendly, plus cover-letter decision, fit check and 10 interview questions. Steps 3-5 of the MODE: JOB pipeline.
---

# Prompt D: Customized resume (three-way mapping)

Act as an expert resume strategist and ATS specialist. Three sources, each with one job:

| Source | Truth for |
|---|---|
| **Master Resume** (Project Knowledge; re-read from Drive only after `UPDATE MASTER`) | FACTS |
| **Ideal Resume** from this thread | WORDING, STRUCTURE, KEYWORDS, FORMAT |
| **JD.txt** | PRIORITIES |

**Goal:** turn the ideal resume into a true resume of the user's experience, keeping its phrasing, keywords and structure as far as the facts allow, aligned to the JD.

## Rules
- Never copy master-resume text; carry its meaning into the ideal resume's wording.
- Where the JD and ideal resume use different terms for the same thing, use the JD's term if the experience supports it.
- Never invent experience, tools, metrics or responsibilities; every claim must trace to the master resume or the user's answers. Never add a JD keyword without real experience behind it.
- ATS-safe: standard headings and bullets; no tables, columns or graphics; bold only as SKIM-FRIENDLY FORMATTING allows.

## Step 0: JD analysis
Reuse the ideal-resume analysis and requirement IDs. Add only what's missing: top 15–20 ATS keywords ranked, key responsibilities and valued outcomes, hidden expectations (ownership, stakeholders, scale), and where the ideal resume's emphasis differs from the JD.

## Step 1: Three-way mapping
- **Table 1**, per ideal-resume bullet: point | JD relevance (High/Med/Low + req ID) | match vs master (Fully / Partially / Not supported) | evidence (role + paraphrase) | gap or reason
- **Table 2**: JD requirements the ideal resume misses, and whether the master supports them

Save both in `Mapping and Gap Questions` in the job folder. In chat, one line: how many must-haves are Fully / Partially / Not supported.

## Step 2: Gap questions (only what's needed)
Ask a question only if **all three** hold:
1. the answer could change the resume for a must-have, or for a nice-to-have / high-relevance point that would visibly strengthen it;
2. the Master Resume doesn't already answer it (check every variant, alt bullet, scope note and skill);
3. it hasn't been answered in this thread, the master, or the Change Log.

- Skip low-relevance ideal-only points, things clearly outside the background (mark Not supported), and polish that can be done from known facts.
- Priority: must-haves Partial/Not supported → high-relevance ideal points → nice-to-haves.
- Each question probes: used it, even briefly? similar work elsewhere (academic, internship, freelance, volunteer, side project)? any scale, metric, team size or impact?
- Merge related questions; number, group by section, tag `[JD must-have]` / `[JD nice-to-have]` / `[Ideal resume only]`; yes/no + one line.
- No target number (0–3 is normal for a good match). Max 8; list others as optional.
- If any were asked, **stop and wait**. If none pass, say "No gap questions needed" with one line on why, and go to Step 4.

## Step 3: Analyse answers
For each answer: Yes / Partly / No on whether it supports the point, and why. Flag stretches the user may struggle to defend and suggest safer phrasing; one follow-up if vague. Then list **PROPOSED MASTER RESUME ADDITIONS**, numbered: `Section | Role | Exact text | Source (answer, date)`. Don't edit the master until `UPDATE MASTER`.

## Step 4: FINAL resume (no drafts)
Write once, as FINAL. Run the Step 5 checks before saving.
- Ideal resume's wording, structure and keywords, filled with verified experience; JD terms where supported
- Most JD-relevant points first in each role; unsupported/low-relevance points removed (one-line note)
- Partial matches worded truthfully; no requirement-ID tags; real header details from the master

### Skim-friendly formatting
Goal: a recruiter reading only the **bold text, job titles and each role's first bullet** sees within 10 seconds that the candidate meets the top must-haves. Bold points to proof; it never adds content.

**Bold:**
- At most one 2–6 word phrase per bullet, preferably the quantified result that proves a must-have (e.g. "…holding **99.5% uptime**").
- Only bullets that map to a must-have or top-5 keyword: about half per role, never all.
- Summary: ≤ 2 phrases. Name bold. Role lines: title bold, company/dates regular. Section headings bold.
- ~8–14 bold phrases in total.

**Never bold:** whole bullets, >1 phrase per bullet, Core Skills, Education, Certifications, dates, company names, contact details, soft words ("strong", "cross-functional", "stakeholders", "team", "successfully"), or anything unsupported. Bold is the only emphasis: no italics, underline, colour, caps or symbols.

**Skim order:** summary line 1 mirrors the JD's title and seniority (as far as true), then years and domain. Each role leads with the bullet matching the #1 must-have. Bullets: verb first, 1–2 lines, numerals, one idea each. Recent roles 4–6 bullets; older 2–3. Single column; dates after ` | `.

### Basic formatting only
- Create the Doc in **one** Drive create call from simple HTML: `<h1>` name, `<p>` contact, `<h2>` sections, `<p>` role lines with `<b>` title, `<ul><li>` bullets, `<b>` skim phrases. No CSS, fonts, spacing or page settings.
- Don't restyle, read back, preview, screenshot or export.
- Length by word count: ~450–550 words per page.

Save as `<Company> - <Role> - Customized Resume - FINAL - <date>`.

## Step 4b: Cover letter (decide; never ask)
**Required if:** the posting mentions a cover letter / motivation letter / "why you want to join"; or the application is on an external ATS or careers page (Greenhouse, Lever, Workday, Ashby, SmartRecruiters, iCIMS, SuccessFactors, Taleo, company site); or the form has a cover-letter field. **Not required** for LinkedIn Easy Apply without such a field. If required, run **cover-letter**. Otherwise: `Cover letter: not required (<reason>)`.

## Step 5: Fit check (before saving)
- Keyword coverage: list only **Missing keywords**, noting which could honestly be added later (course, project, certification).
- JD match: strong / moderate / weak + one-line reason; any ATS concerns.
- Skim test: every bold phrase maps to a requirement ID (remove any that don't); bold + titles + first bullets alone show the top 3 must-haves, else fix.
- Write **10 likely interview questions** to the tracker's `Likely interview questions` column: must-haves, gaps and stretches, claims an interviewer would probe (metrics, decisions, trade-offs), logistics. Update if the resume changes.
- End with: file links, JD match, missing keywords, which question numbers hit the thinnest spots, and the **apply kickoff** in a code block (see [agent/commands.md](../../agent/commands.md)).
