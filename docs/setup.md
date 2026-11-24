# Setup

## Prerequisites
- A Claude plan with Projects
- Claude in Chrome extension, signed in to LinkedIn in that Chrome
- Google Drive connector enabled (Docs + Sheets)

## 1. Create the Drive structure
```
Job Search <year>/
  00_Master/   Master Resume (Doc), Change Log (Doc)
  01_Tracker/  Job Tracker (Sheet, tab "Jobs")
  02_Jobs/
```
Create the tracker headers from [tracker/jobs-tracker.template.csv](../tracker/jobs-tracker.template.csv).

## 2. Fill in the config docs
Create Google Docs from:
- [config/master-resume.template.md](../config/master-resume.template.md): be exhaustive; this is the only fact source
- [config/search-profile.template.md](../config/search-profile.template.md)
- [config/application-answers.template.md](../config/application-answers.template.md)

## 3. Create the Claude Project
1. Paste [agent/system-prompt.md](../agent/system-prompt.md) into the project's custom instructions and replace the `<..._ID>` placeholders with your Drive IDs.
2. Add to Project Knowledge: Master Resume, Search Profile, Application Answers, and the procedures (either the `skills/` files or a single "Prompts A–E" doc combining them).

## 4. Run it
1. New chat: `MODE: SEARCH` → shortlist lands in the tracker with kickoff messages.
2. New chat per job: paste the kickoff from the tracker → answer gap questions → get FINAL resume, cover letter, interview questions and an apply kickoff.
3. Format and export your PDFs from the FINAL Docs.
4. New chat: paste the apply kickoff (with the approval line) → review the filled form → `SUBMIT`.
5. Later: `STATUS Interview`, `SKIP`, etc. keep the sheet and LinkedIn in sync.
