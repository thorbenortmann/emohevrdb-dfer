# FEA Sequence-Order Ablation: Significance Tests

## Scope and analysis

The FEA analysis compares the **Ordered LSTM** against the independently optimized **Shuffled LSTM** and **Mean Aggregation** controls on the held-out test set.

- **378 reenactments**, with **1 FEA sequence per reenactment**
- **8 test participants**
- Primary inference: **exact two-sided McNemar test** on paired reenactment-level correctness
- **95% unadjusted paired-bootstrap confidence intervals**, using **1,000,000 resamples**
- **Holm correction across the two FEA primary tests**, α = .05
- Sensitivity analysis: one-sample t-test on paired reenactment-level differences
- Participant-level results are descriptive; additional dependence between reenactments from the same participant is not modeled

## Primary results

| Comparison | Ordered | Alternative | Difference | 95% CI | Raw McNemar p | Holm-adjusted p |
|---|---:|---:|---:|---:|---:|---:|
| Ordered vs. Shuffled | 78.31% | 70.11% | **+8.20 pp** | [4.76, 11.90] | 1.47377×10⁻⁵ | **1.47377×10⁻⁵** |
| Ordered vs. Mean | 78.31% | 69.05% | **+9.26 pp** | [5.82, 12.96] | 3.62458×10⁻⁷ | **7.24916×10⁻⁷** |

Both Holm-adjusted tests are significant at **α = .05**.

## Paired correctness counts

| Comparison | Both correct | Ordered only | Alternative only | Both wrong |
|---|---:|---:|---:|---:|
| Ordered vs. Shuffled | 255 | **41** | **10** | 72 |
| Ordered vs. Mean | 254 | **42** | **7** | 75 |

## Additional checks

| Comparison | Sensitivity t-test | Participant consistency |
|---|---:|---:|
| Ordered vs. Shuffled | t(377) = 4.447, p = 0.00001145 | **7/8** favor Ordered, 1/8 favors Shuffled; median difference **+5.61 pp** |
| Ordered vs. Mean | t(377) = 5.167, p = 3.86×10⁻⁷ | **6/8** favor Ordered, 2/8 tied; median difference **+7.84 pp** |

## Interpretation

Ordered FEA outperforms Shuffled by **8.20 pp** and Mean by **9.26 pp**. Both comparisons remain significant after Holm correction, and the discordant-pair counts and participant summaries favor Ordered overall. This supports a benefit of chronological sequence modeling beyond access to multiple FEA measurements in the evaluated models. Independent optimization, and the different aggregation architecture of Mean, mean that these comparisons do not isolate temporal order as the only experimental difference.