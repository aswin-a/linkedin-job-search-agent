# Job Tracker schema

Google Sheet, tab `Jobs`. One row per job. The agent always finds columns **by header name**, never by letter, so columns can be reordered or added safely. A CSV with these headers is in [jobs-tracker.template.csv](jobs-tracker.template.csv).

| Column | Written by | Notes |
|---|---|---|
| Job ID | SEARCH | Unique id (e.g. LinkedIn job id) for de-duplication |
| Company | SEARCH | |
| Role | SEARCH | |
| Location | SEARCH | |
| Mode | SEARCH | Remote / Hybrid / Onsite |
| Link | SEARCH | Job URL; used for duplicate checks |
| Post Type | SEARCH / JOB | Easy Apply or external ATS name |
| Post Date | SEARCH | |
| Fit score | SEARCH | 0–100 weighted score |
| LinkedIn match | SEARCH / JOB | Exactly as LinkedIn shows it, or `Not shown`. Never inferred |
| Top gaps | SEARCH | Two biggest gaps |
| Status | all | Shortlisted, Saved - low fit, In progress, Resume final, Applied, Interview, Offer, Rejected, Skipped, Withdrawn, Archived. Every change is mirrored to LinkedIn |
| Thread name | JOB | `<Company> - <Role>` |
| Ideal resume | JOB | Drive link |
| Customized resume | JOB | Drive link to FINAL |
| Applied on | APPLY | Date |
| Application type | APPLY | Easy Apply / ATS |
| Follow-up date | manual | |
| Notes | all | Fit breakdown, LinkedIn sync log, HR outreach log |
| Kickoff message | SEARCH | Ready-to-paste `MODE: JOB` kickoff |
| Likely interview questions | JOB | 10 numbered questions in one cell, kept in step with resume edits |
| Cover letter | JOB / APPLY | Drive link, or `not required (<reason>)` |

## Token rule
The agent reads only the rows and columns it needs: `Job ID, Company, Role, Link` for duplicate checks in SEARCH; the single job row in JOB/APPLY threads. It never reads the whole sheet.
