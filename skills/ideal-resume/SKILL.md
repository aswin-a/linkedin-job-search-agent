---
name: ideal-resume
description: From JD.txt alone, analyse the job and write an "ideal" resume for a fictional perfect-fit candidate, tagged with requirement IDs. Used as the wording/structure template for the tailored resume. Step 2 of the MODE: JOB pipeline.
---

# Prompt C: Ideal Resume

Act as an expert resume writer, recruiter and ATS specialist with 15+ years of hiring for roles like this.

Using **only JD.txt**, create the IDEAL resume: a plausible, perfect-fit candidate who would be shortlisted immediately and score 95%+ in an ATS, with placeholder personal details. **Use nothing from the user's Master Resume.** Don't ask questions; make reasonable assumptions.

> Why: separating "what the perfect answer looks like" from "what's true about me" lets the next step borrow the language and structure without borrowing any facts.

## Step 1: JD analysis
- Top 15 keywords (skills, tools, certifications, methods) by importance
- Seniority, years of experience and education expected
- The 5 core problems this hire must solve
- **Requirements checklist:** number every must-have (`M1, M2…`) and nice-to-have (`N1, N2…`), quoting the JD's exact wording. These IDs are used by every later step.

## Step 2: Build the ideal resume
- 1 page under 8 years of experience, otherwise 2
- Header: `[Full Name] | [City] | [Phone] | [Email] | [LinkedIn]`
- Sections in order: Professional Summary (3 lines), Core Skills, Professional Experience, Projects (if relevant), Education, Certifications
- 2–4 roles with realistic titles progressing toward the target role; placeholder companies like `[Company A]`
- Every bullet: action verb + what was done + tools/methods + quantified, believable result, **tagged with the requirement IDs it covers**, e.g. `(M2, N1)`
- Cover every must-have and nice-to-have, mirroring the JD's wording naturally
- ATS-safe (no tables, columns, icons, images); no clichés or filler; consistent tense and dates

## Step 3: Save
Save the JD analysis and ideal resume as `<Company> - <Role> - Ideal Resume - <date>` in the job folder. In chat give only a 2-line summary (seniority, top 3 must-haves) and the link, then go straight to **tailored-resume**.
