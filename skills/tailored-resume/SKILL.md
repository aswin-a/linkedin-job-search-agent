---
name: tailored-resume
description: Three-way mapping of Ideal Resume x Master Resume x JD, targeted gap questions, then a FINAL tailored resume that is true, ATS-safe and skim-friendly, plus the cover-letter decision, fit check and 10 likely interview questions. Use when a MODE: JOB thread has an Ideal Resume (pipeline steps 3-5), when the user answers gap questions, or when they request changes to the FINAL resume.
---

# Prompt D: Customized resume (three-way mapping)

| | |
|---|---|
| **Inputs** | Master Resume (Project Knowledge; re-read from Drive only after `UPDATE MASTER`); this thread's Ideal Resume + requirement IDs; `JD.txt`; the user's answers in this thread; the Change Log (to avoid re-asking) |
| **Outputs** | Doc `Mapping and Gap Questions`; gap questions in chat (0–8); proposed master additions (numbered); Doc `Customized Resume - FINAL`; cover letter via **cover-letter** if required; tracker `Customized resume`, `Cover letter`, `Likely interview questions`; apply kickoff in chat |
| **Stop conditions** | After Step 2 if any gap question was asked: **wait for answers**. Never edit the Master Resume until `UPDATE MASTER`. Never apply: the run ends at the apply kickoff |

Act as an expert resume strategist and ATS specialist. Three sources, each with one job:

| Source | Truth for |
|---|---|
| **Master Resume** | FACTS |
| **Ideal Resume** from this thread | WORDING, STRUCTURE, KEYWORDS, FORMAT |
| **JD.txt** | PRIORITIES |

**Goal:** turn the ideal resume into a true resume of the user's experience, keeping its phrasing, keywords and structure as far as the facts allow, aligned to the JD.

## Rules
- Never copy master-resume text; carry its meaning into the ideal resume's wording.
- Where the JD and ideal resume use different terms for the same thing, use the JD's term if the experience supports it.
- Never invent experience, tools, metrics or responsibilities; every claim must trace to the master resume or the user's answers. Never add a JD keyword without real experience behind it.
- ATS-safe: standard headings and bullets; no tables, columns or graphics; bold only as [skim-friendly formatting](references/skim-formatting.md) allows.

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
- Formatting, bolding, skim order and HTML structure: follow [references/skim-formatting.md](references/skim-formatting.md) exactly.

Save as `<Company> - <Role> - Customized Resume - FINAL - <date>`.

## Step 4b: Cover letter (decide; never ask)
**Required if:** the posting mentions a cover letter / motivation letter / "why you want to join"; or the application is on an external ATS or careers page (Greenhouse, Lever, Workday, Ashby, SmartRecruiters, iCIMS, SuccessFactors, Taleo, company site); or the form has a cover-letter field. **Not required** for LinkedIn Easy Apply without such a field. If required, run **cover-letter**. Otherwise: `Cover letter: not required (<reason>)`.

## Step 5: Fit check (before saving)
- Keyword coverage: list only **Missing keywords**, noting which could honestly be added later (course, project, certification).
- JD match: strong / moderate / weak + one-line reason; any ATS concerns.
- Skim test: every bold phrase maps to a requirement ID (remove any that don't); bold + titles + first bullets alone show the top 3 must-haves, else fix.
- Write **10 likely interview questions** to the tracker's `Likely interview questions` column: must-haves, gaps and stretches, claims an interviewer would probe (metrics, decisions, trade-offs), logistics. Update if the resume changes.
- End with: file links, JD match, missing keywords, which question numbers hit the thinnest spots, and the **apply kickoff** in a code block (see [agent/commands.md](../../agent/commands.md)).

## Change requests (pipeline step 6)
Edit the FINAL Doc in place with targeted text replacements; keep the cover letter and interview questions in step; reply with only what changed. Any edit made after `APPROVED TO APPLY` disarms the gate: the user must approve again.
