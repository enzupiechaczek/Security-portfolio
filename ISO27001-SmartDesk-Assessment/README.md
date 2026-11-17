# ISO/IEC 27001:2022 Self-Assessment: SmartDesk

A self-directed risk assessment of **SmartDesk**, an AI ticket-triage training application that I designed and taught as a trainer and Scrum master at EARTech.

**Status:** desk-based self-assessment. It is not a certified audit, not a tested ISMS, and not a claim of ISO 27001 conformity. Risk scores are my own judgement and should be challenged.

## Files

| File | What it is |
|---|---|
| [Self-assessment report (PDF)](SmartDesk_ISO27001_Self_Assessment_Report.pdf) | Scope, method, risk results, treatments completed, limitations (2 pages) |
| [Risk assessment and SoA workbook (Excel)](SmartDesk_ISO27001_Risk_Assessment_SoA_v4%20%281%29.xlsx) | Scope, 10 assets, 15 risks with residual scores, Statement of Applicability for all 93 Annex A controls, clause 4-10 gap analysis, hypothetical "if deployed" scores |

## Evidence

Screenshots taken on 16-17 November 2026 to support the findings and fixes.

- Advanced Security settings (Dependabot alerts, secret protection, push protection, CodeQL): [page 1](Evidence/Advanced%20security%20settings%20page%201.png), [page 2](Evidence/Advanced%20security%20settings%20page%202.png), [page 3](Evidence/advanced%20security%20settings%20page%203.png), [page 4](Evidence/Advanced%20security%20settings%20page%204.png)
- "Protect Main" branch ruleset: [page 1](Evidence/Protect%20main%20ruleset%20page%201.png), [page 2](Evidence/Protect%20main%20ruleset%20page%202.png), [page 3](Evidence/Protect%20main%20ruleset%20page%203.png)
- Security hardening pull request #55: [page 1](Evidence/Security%20hardening%20%28PR55%29%20page%201.png), [page 2](Evidence/Security%20hardening%20%28PR55%29%20page%202.png)

## Headline results

- 10 assets and 15 risks: 5 High, 9 Medium and 1 Low before treatment.
- Statement of Applicability: 7 implemented, 27 partially implemented, 20 gaps and 39 excluded (93 controls).
- Three risks reduced through a reviewed pull request: debug mode (R02), unpinned dependencies (R07) and secret exposure (R08). A LICENSE and SECURITY.md were also added.

## Source repository

- Project: [smartdesk-ai-ticket-triage](https://github.com/enzupiechaczek/smartdesk-ai-ticket-triage)
- Fixes: [pull request #55](https://github.com/enzupiechaczek/smartdesk-ai-ticket-triage/pull/55)

## Limitations

I designed SmartDesk and trained its contributors, so I assessed my own work. A real internal audit (clause 9.2) needs an independent reviewer. I did not test the running system, and one person owns and reviews the repository, so there is no segregation of duties.
