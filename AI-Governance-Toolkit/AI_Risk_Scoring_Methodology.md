# AI Risk Scoring Methodology

## Purpose
This document outlines a lightweight, practical methodology for scoring risk across AI systems in an organisation's AI register. It is loosely aligned with NIST SP 800-30 (risk assessment) principles and adapted for AI-specific risk categories referenced in the NIST AI Risk Management Framework (AI RMF).

## AI-Specific Risk Categories
- **Bias**: Model outputs systematically disadvantage certain groups due to skewed training data or design.
- **Hallucination**: Model produces confident but factually incorrect or fabricated outputs.
- **Data Leakage**: Sensitive or proprietary data is exposed through model outputs, logs, or third-party processing.
- **Model Drift**: Model performance degrades over time as real-world data diverges from training data.
- **Explainability Gap**: Decisions or outputs cannot be adequately explained to stakeholders or regulators.

## Scoring Matrix (5x5 Likelihood x Impact)

| Likelihood \ Impact | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Severe (5) |
|---|---|---|---|---|---|
| Rare (1) | 1 | 2 | 3 | 4 | 5 |
| Unlikely (2) | 2 | 4 | 6 | 8 | 10 |
| Possible (3) | 3 | 6 | 9 | 12 | 15 |
| Likely (4) | 4 | 8 | 12 | 16 | 20 |
| Almost Certain (5) | 5 | 10 | 15 | 20 | 25 |

## Risk Rating Bands
- **1-6: Low** — Monitor via standard review cycle.
- **7-14: Medium** — Requires documented mitigation and periodic reassessment.
- **15-25: High** — Requires human-in-the-loop controls, executive sign-off, and frequent review.

## Application to AI Register
Each system in the AI System Register is assigned a Risk Classification (Low/Medium/High) derived from this matrix, considering:
1. Sensitivity of data processed
2. Degree of autonomous decision-making
3. Potential impact of an incorrect or biased output
4. Regulatory exposure (e.g., privacy, financial, consumer protection)
