# ISO/IEC 27001:2022 Self-Assessment: SmartDesk

A self-directed risk assessment of SmartDesk, an AI ticket-triage training
application that I designed and taught as a trainer and Scrum master at EARTech.

**Status:** desk-based self-assessment. Not a certified audit, not a tested ISMS,
and not a claim of ISO 27001 conformity. Scores are my own judgement.

## What is included
- Report (PDF): scope, method, risk results, treatments, limitations.
- Workbook (Excel): asset register, 15 risks with residual scores, Statement of
  Applicability for all 93 Annex A controls, clause 4-10 gap analysis.
- Evidence: screenshots of the branch ruleset, secret scanning and CI checks.

## Headline results
- 10 assets, 15 risks (5 High, 9 Medium, 1 Low before treatment).
- SoA: 7 implemented, 27 partially implemented, 20 gaps, 39 excluded.
- Three risks reduced through a reviewed pull request: debug mode (R02),
  unpinned dependencies (R07) and secret exposure (R08).

## Evidence in the source repository
- Project: https://github.com/enzupiechaczek/smartdesk-ai-ticket-triage
- Fixes: pull request #55

## Limitations
I designed SmartDesk and trained its contributors, so I assessed my own work.
An independent reviewer is needed for a real internal audit (clause 9.2).
