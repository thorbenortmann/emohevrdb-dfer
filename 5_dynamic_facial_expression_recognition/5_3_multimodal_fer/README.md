# 5.3 Multimodal FER

[Up one level](../README.md) · [Repository home](../../README.md)

These experiments combine image sequences and FEA sequences for dynamic FER.

## Experiments

| Experiment | Entry point | Purpose |
|---|---|---|
| 5.3.1 Complementarity | [Unimodal prediction overlap](5_3_1_complementarity_analysis/README.md) | Both-correct, Image-only, FEA-only, and both-wrong cases. |
| 5.3.3 Late fusion | [Late-fusion variants](5_3_3_late_fusion/README.md) | Average and cross-attention fusion. |
| 5.3.4 Intermediate fusion | [Intermediate cross-attention fusion](5_3_4_intermediate_fusion/README.md) | Canonical dynamic Multimodal result: **81.61%**. |

Numbering follows the existing experiment folders; there is no separate dataset-construction directory for Subsection 5.3.2 in this snapshot.

## Detailed comparisons

- [Dynamic model significance tests](../../6_discussion/significance-tests/dynamic-significance-tests/README.md).
- [Multimodal error and fusion analysis](../../6_discussion/multimodal-analysis/README.md), including what fusion preserves, corrects, and loses within the four unimodal correctness groups.
