# Expected checks: case 01 (platform PM, Greenhouse)

Inputs: [jd.md](jd.md) and [the fictional master resume](../../fixtures/master-resume-fictional.md). Run a MODE: JOB thread with these as the JD and Master Resume, then score each check pass/fail by hand.

## ideal-resume
| # | Check | Expected |
|---|---|---|
| 1.1 | Must-haves numbered | 5 must-haves (`M1–M5`), quoting the JD's wording |
| 1.2 | Nice-to-haves numbered | 3 nice-to-haves (`N1–N3`) |
| 1.3 | No master facts leak | No "Fabrikam", "Tailspin", "140 partner apps" or other master-only facts in the ideal resume |
| 1.4 | Bullets tagged | Every experience bullet carries at least one requirement ID |

## tailored-resume: mapping
| # | Check | Expected |
|---|---|---|
| 2.1 | Public API | **Fully** supported (API strategy, v1 → v2, 140 partner apps) |
| 2.2 | DX metrics | **Fully** supported (time-to-first-call, docs CSAT, tickets per partner) |
| 2.3 | Multi-tenant SaaS | **Fully** supported (scope note) |
| 2.4 | SLAs/SLOs ownership | **Partially** or **Not** supported ("platform reliability work" only) |
| 2.5 | Kubernetes / infra | **Not** supported |
| 2.6 | Usage-based pricing | **Fully** supported (Tailspin billing) |

## tailored-resume: gap questions
| # | Check | Expected |
|---|---|---|
| 3.1 | Asks about SLO ownership | **Yes**: probes adjacent evidence (informal targets, uptime numbers, incident reviews) |
| 3.2 | Does not ask about the public API, DX metrics, multi-tenant or usage-based pricing | **None** of these asked (already in the master) |
| 3.3 | Question count | 1–3 |
| 3.4 | Tagging | Each question tagged `[JD must-have]` / `[JD nice-to-have]` with its requirement ID |

## tailored-resume: FINAL resume (answer to 3.1: "No")
| # | Check | Expected |
|---|---|---|
| 4.1 | No SLO claim | The resume doesn't claim ownership of SLAs/SLOs |
| 4.2 | No Kubernetes | "Kubernetes" appears only under Missing keywords, not in the resume |
| 4.3 | Every metric traces | Every number in the resume appears in the master (35→140, 3 days→4 hours, 38%, 18%, 900, 11 engineers…) |
| 4.4 | Format | `python3 evals/check_resume_format.py <final.html>` passes |
| 4.5 | Skim test | Bold + titles + first bullets show M1 (public API), M2 (DX metrics) and M3 (multi-tenant) |

## Cover letter and outputs
| # | Check | Expected |
|---|---|---|
| 5.1 | Cover letter decision | **Required** (external ATS *and* the posting asks for one) |
| 5.2 | Cover letter facts | No claim beyond the master and the FINAL resume; 300–350 words |
| 5.3 | Interview questions | 10, at least one probing SLO/reliability and one probing Kubernetes |
| 5.4 | Apply kickoff | Present, in a code block, with `APPROVED TO APPLY - Acme Cloud - Senior Product Manager, Platform` |
| 5.5 | Nothing applied | No apply/submit action taken in the JOB thread |
