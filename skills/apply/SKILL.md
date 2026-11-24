---
name: apply
description: Approval-gated job application. Fills LinkedIn Easy Apply or an external ATS from sourced answers only, shows a field-by-field review, submits only on SUBMIT, then updates tracker, LinkedIn job tracker and HR outreach. Use in a MODE: APPLY thread.
---

# Prompt E: Apply

Take the job from the kickoff and list its job folder. The FINAL resume and cover letter are Google Docs the user formats and exports to PDF themselves. Open their contents only if a form question needs a fact (as text). **Do no resume work.**

## Preconditions (stop and say which one fails)
- The user's **latest message in this thread** is exactly `APPROVED TO APPLY - <Company> - <Role>`, matching this job.
- The FINAL resume Doc exists (and FINAL cover letter if Step 4b required one). Ask once whether the formatted PDFs are ready; the user uploads them.
- The job is still open.

## Apply
1. Open the job link in Chrome; note Easy Apply vs external portal. If the portal needs sign-in or an account, ask the user to do it and wait.
2. Fill fields **only** from the Master Resume, FINAL resume, Application Answers and answers in this thread. For resume / cover-letter uploads, stop and ask the user to upload their PDFs, saying which file goes where. If there's a cover-letter field but no letter, run **cover-letter** now without asking.
3. For any question without a sourced answer (CTC, notice period, visa, relocation, years with a tool, diversity questions, essays): **stop and ask. Never guess or pick a default.**
4. Before Submit, show a **review table**: `Field | Value | Source`, including uploaded files. If the job page lists a hiring contact, put the draft HR message (**hr-outreach**) under it.
5. Wait for `SUBMIT`, click Submit **once**, capture the confirmation.

## After submitting
- Tracker: Status `Applied`, applied date, resume and cover-letter links, application type, any reference number.
- Save an **Application Record** in the job folder: date, link, field values, confirmation.
- Move the job to Applied (**linkedin-tracker-sync**).
- Send the HR message (**hr-outreach**).
- If master-resume additions from this job are pending, remind the user once.

Stop and describe anything unexpected (CAPTCHA, assessment, login wall, error, payment or ID request); never work around it. Never type passwords, solve CAPTCHAs, create accounts or accept terms for the user.
