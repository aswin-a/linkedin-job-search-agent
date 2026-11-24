---
name: cover-letter
description: Write a one-page, fact-only cover letter for a job from the Master Resume, the FINAL tailored resume and the user's answers. Use when tailored-resume Step 4b decides one is required, when the user says COVER LETTER, or when an application form has a cover-letter field and no letter exists yet.
---

# Cover letter

| | |
|---|---|
| **Inputs** | Master Resume; this job's FINAL resume; `JD.txt` / requirement IDs; the user's answers in this thread (location, availability, work mode) |
| **Outputs** | Doc `<Company> - <Role> - Cover Letter - FINAL - <YYYY-MM-DD>` in the job folder; link in tracker `Cover letter` and the Application Record |
| **Stop conditions** | Location, availability or work-mode fit not confirmed → ask before writing the closing paragraph. Never upload or submit it; the user exports the PDF |

1. **Facts only.** One page, 300–350 words, using only the Master Resume, this job's FINAL resume (keep in step if the resume is edited) and the user's answers. No claim, number or tool beyond those.
2. **Structure:**
   - contact header; date (`DD MMM YYYY`); `Hiring Team, <Company>`
   - opening that links the role's core problem to the closest real experience
   - 1–2 evidence paragraphs mirroring the top must-haves with real metrics
   - one paragraph on technical foundation or a trade-off made
   - close with confirmed location, availability and work-mode fit; sign-off
3. **Save** as `<Company> - <Role> - Cover Letter - FINAL - <YYYY-MM-DD>` in the job folder, in one Drive create call from simple HTML (name in `<b>`, then contact line, date, addressee, salutation, each paragraph and sign-off as separate `<p>`). No styling, read-back, preview or PDF.
4. **Approval:** no separate step. `APPROVED TO APPLY` approves files as they are in Drive; for a letter written at apply time, `SUBMIT` approves it. Record its link in the tracker's `Cover letter` column and the Application Record.
