---
name: hr-outreach
description: Draft, and after an approved application send, one short fact-only LinkedIn message to the hiring contact listed on the job page; free messages only unless the user says SEND. Use when apply builds its review table (draft) and right after a confirmed submission (send). Never contacts anyone else.
---

# HR outreach

| | |
|---|---|
| **Inputs** | The job page's "Meet the hiring team" / "People you can reach out to" contact; FINAL resume; Master Resume; the user's confirmed location, availability and work mode; tracker Notes; the existing LinkedIn conversation with that contact |
| **Outputs** | A draft under the apply review table; one sent message (or a logged skip); a Notes line in the tracker |
| **Stop conditions** | No listed contact → skip. Already messaged → show the earlier message and ask. Submission not confirmed → don't send. Paid / InMail → wait for `SEND`. No Message button → skip. `NO MESSAGE` / `CANCEL` → skip |

1. **Who:** only the job poster or hiring manager shown under "Meet the hiring team" / "People you can reach out to". Never search for others.
2. **Already messaged?** Check tracker Notes for `Messaged <name>` and open the existing LinkedIn conversation with that person. If there's an earlier message from the user, don't send again: show it and ask.
3. **Draft (< 150 words):** subject `<Role> application - <Your Name> (<city>, <availability>)` (in the subject field if there is one, else the first line); that the user applied and how; 2–3 strongest JD-matching facts from the FINAL resume; confirmed location, availability and work-mode fit; an offer to talk; name, phone, email. Facts only from the FINAL resume, Master Resume and the user's answers.
4. **Approval:** show the draft under the apply review table. `SUBMIT` approves it as shown; an edited version from the user is sent instead; `NO MESSAGE` skips it (log "HR message skipped (my choice)").
5. **Cost check**, only after the submission is confirmed: open the composer and read the cost label.
   - "Free message" or 1st-degree connection → send
   - InMail credit or no free label → ask `SEND (uses 1 InMail credit) or CANCEL?` and wait
   - No Message button / blocked → skip and say so
6. Type line breaks with Shift+Enter, check the full text before sending, **never send twice**. If the send result is unclear, check the conversation before doing anything else.
7. Log in Notes: `Messaged <name> (<title>) on LinkedIn <date, time> (free / InMail)` or `No HR contact on job page`.

Never send connection requests or follow people on the user's behalf.
