# Example walkthrough (fictional)

A condensed run for a **fictional** company and role, showing what each turn looks like. "Acme Cloud" and every detail below are made up.

---

### 1. Search

**Me:** `MODE: SEARCH`

**Agent:**
| Rank | Score | LinkedIn match | Company | Role | Location/mode | Top gap |
|---|---|---|---|---|---|---|
| 1 | 82 | High | Acme Cloud | Senior PM - Platform | Bengaluru / Hybrid | Kubernetes depth |
| 2 | 74 | Medium | Northwind | Senior PM - Integrations | Remote (India) | Billing domain |
| 3 | 63 | Not shown | Contoso AI | Lead PM - AI Agents | Chennai / Onsite | Eval tooling |

Skipped 17 (8 excluded titles, 5 below 60, 4 already in tracker).
`Current step: shortlist saved | Waiting on: you | Next step: paste a kickoff from the tracker into a new chat`

---

### 2. Job thread

**Me:** *(pastes kickoff)* `MODE: JOB / Company: Acme Cloud / Role: Senior PM - Platform / ...`

**Agent:**
> Acme Cloud | Senior PM - Platform | Bengaluru (Hybrid) | posted 3 days ago | external ATS (Greenhouse). JD saved → [link]
>
> Ideal resume → [link]. 8+ yrs, Senior; top must-haves: M1 public API strategy, M2 developer experience metrics, M3 multi-tenant platform roadmap.
>
> Mapping → [link]. Must-haves: 5 Fully / 2 Partially / 1 Not supported.
>
> **Gap questions (2)**
> 1. [JD must-have, M4] Have you owned SLAs/SLOs for an API, even informally? Any uptime or latency numbers?
> 2. [JD nice-to-have, N2] Any hands-on Kubernetes or infra work (side project counts)?

**Me:** 1, yes, owned the integration API's 99.5% uptime target. 2, no.

**Agent:**
> 1 → Yes, supports M4. 2 → No; N2 marked Not supported, not added.
>
> **Proposed master additions:** 1. Experience | <Role> | "Owned the 99.5% uptime target for the integration API" | Source: answer, <date>
>
> FINAL resume → [link] · Cover letter (external ATS) → [link] · 10 interview questions written to tracker (Q4 and Q7 hit thinnest spots: N2, M3 scale)
> JD match: **strong**, all top 3 must-haves visible in the skim test. Missing keywords: Kubernetes (could add via a course/project), Terraform.
>
> ```
> MODE: APPLY
> Company: Acme Cloud
> Role: Senior PM - Platform
> Link: <url>
> Job folder: <link>
> APPROVED TO APPLY - Acme Cloud - Senior PM - Platform
> ```

**Me:** `UPDATE MASTER`

---

### 3. Apply thread

**Me:** *(pastes apply kickoff incl. approval line)*

**Agent:** fills the Greenhouse form, pauses for PDF uploads, stops on "Expected CTC" to ask, then shows:

| Field | Value | Source |
|---|---|---|
| Name | … | Master Resume |
| Notice period | … | Application Answers (confirmed in thread) |
| Expected CTC | … | Your answer in this thread |
| Resume | FINAL.pdf (uploaded by you) | |
| Cover letter | CoverLetter.pdf (uploaded by you) | |

Draft HR message to *<Hiring Manager>, Director of Product* (free message): …

**Me:** `SUBMIT`

**Agent:** Submitted (ref #…). Tracker → Applied. LinkedIn tracker → Applied. Messaged <Hiring Manager> (free). Application Record → [link].
`Current step: applied | Waiting on: nothing | Next step: STATUS updates as they come`
