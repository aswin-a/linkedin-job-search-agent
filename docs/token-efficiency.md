# Token efficiency

A per-job pipeline touches a JD, two resumes, a mapping, a sheet, a browser and Drive. Without discipline, context fills up fast and each turn gets slower and more expensive. These rules came from running the agent and watching where tokens went.

| Rule | Why |
|---|---|
| Reference docs (master resume, procedures, profile, answers) live in **Project Knowledge**; re-fetched only after `UPDATE MASTER` or when I say a file changed | Avoids re-reading the same 20 KB every thread |
| Tracker read **by column / single row**, never the whole sheet | The sheet grows with every job |
| Browser pages read **as text**; screenshots only as fallback | Text is far cheaper than images |
| Docs created in **one Drive call from simple HTML**; no read-back, preview, PDF export or base64 | Formatting and PDF are done by me, once, at the end |
| Edits are **targeted text replacements**; the reply lists only what changed | No full-document rewrites |
| **Never print documents in chat**: link + 1–2 line summary | Chat stays small; the files are the deliverable |
| **One job per thread** | Context holds one JD and one mapping only |
| Every turn ends with `Current step \| Waiting on \| Next step` | Lets me resume a thread without scrolling |
