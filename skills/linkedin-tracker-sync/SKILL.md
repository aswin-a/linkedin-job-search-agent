---
name: linkedin-tracker-sync
description: Mirror a job's Status change in the Google Sheet tracker to LinkedIn's job tracker (Saved / Applied / Interview / Archive) in the same turn. Use on every status change in any mode.
---

# LinkedIn tracker sync

The Google Sheet is the source of truth. When a job's Status changes there, make the same change at `linkedin.com/jobs-tracker` in the same turn.

| Sheet status | LinkedIn stage |
|---|---|
| Shortlisted / Saved - low fit / In progress / Resume final | Saved |
| Applied | Applied (overflow menu → Change stage → Applied → Update; Easy Apply often does this itself, so just confirm) |
| Interview (any round) | Interview |
| Offer | Interview (LinkedIn has no Offer stage); note the offer in the sheet |
| Rejected / Skipped / Withdrawn / Archived / posting closed | Archive (overflow menu → Archive) |

## Rules
- These changes are reversible, so **no approval needed**. Never Delete or Unsave.
- Match title, company and location before changing. If the job is in no list, save it from its link first.
- Confirm LinkedIn's notice (e.g. "Moved to Applied"), then add `LinkedIn tracker: <stage> (<date>)` to the sheet's Notes.
- On a CAPTCHA, login wall or error: stop and tell the user; the sheet stays the source of truth.
