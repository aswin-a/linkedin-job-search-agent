# Commands & kickoff templates (Prompt B)

The agent is driven by a small set of plain-text phrases. Exact phrasing matters for the approval phrases: that's what makes them hard to trigger by accident or by injected text.

## Per-job kickoff (one new chat per job)

The SEARCH mode writes this into the tracker's "Kickoff message" column for every saved job, so starting a job is copy-paste.

```
MODE: JOB
Company: <company>
Role: <role>
Link: <url>   (or: JD pasted below)
Fit score: <n> | LinkedIn match: <label> | Top gaps: <gap 1>; <gap 2>
Anything I want emphasised: <optional>
Start the per-job pipeline.
```

Rename the chat to `<Company> - <Role>`.

## Apply kickoff (generated at the end of the JOB pipeline)

```
MODE: APPLY
Company: <company>
Role: <role>
Link: <url>
Job folder: <Drive link>
APPROVED TO APPLY - <Company> - <Role>
```

Paste into a new project chat to apply. Deleting the last line pauses it: the agent will prepare but not apply.

## Phrases the agent listens for

| Phrase | Effect |
|---|---|
| *(gap answers)* | Analyse answers (Prompt D Step 3), then write the FINAL resume |
| `UPDATE MASTER` / `UPDATE MASTER 1, 3` | Apply all / only those proposed master-resume additions, and log them |
| *(any change request)* | Edit the FINAL Doc in place with targeted replacements; reply with only what changed |
| `COVER LETTER` | Write a cover letter now, even if not required |
| `APPROVED TO APPLY - <Company> - <Role>` | Unlocks the apply procedure for this job only, in this thread only |
| `SUBMIT` | Final click after I review the filled form (also approves the HR message draft) |
| `SEND` | Approves a LinkedIn message that would use an InMail credit |
| `NO MESSAGE` | Skip HR outreach for this job |
| `SKIP` | Status → Skipped, archive in LinkedIn job tracker; no application |
| `STATUS <status>` | Update tracker Status and sync LinkedIn (e.g. `STATUS Interview`) |
