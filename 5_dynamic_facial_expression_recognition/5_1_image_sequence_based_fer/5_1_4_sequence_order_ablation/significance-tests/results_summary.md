# Image Sequence-Order Ablation: Significance Tests

## Scope and analysis

The Image analysis compares the **Ordered LSTM** against the independently optimized **Shuffled LSTM** and **Mean Aggregation** controls on the held-out test set.

- **756 view-level samples** from **378 reenactments**
- **2 views per reenactment:** Central and Side
- **8 test participants**
- Primary inference: **two-sided centered paired cluster bootstrap over reenactments**, keeping Central and Side together
- **1,000,000 bootstrap resamples**
- **95% unadjusted bootstrap confidence intervals**
- **Holm correction across the two Image primary tests**, α = .05
- Sensitivity analysis: one-sample t-test on the 378 reenactment-level paired differences
- Participant-level results are descriptive; additional dependence between reenactments from the same participant is not modeled

## Primary results

| Comparison | Ordered | Alternative | Difference | 95% CI | Raw p | Holm-adjusted p |
|---|---:|---:|---:|---:|---:|---:|
| Ordered vs. Shuffled | 72.75% | 61.90% | **+10.85 pp** | [7.28, 14.42] | ≈ 1×10⁻⁶ | **≈ 2×10⁻⁶** |
| Ordered vs. Mean | 72.75% | 60.85% | **+11.90 pp** | [7.94, 15.87] | ≈ 1×10⁻⁶ | **≈ 2×10⁻⁶** |

Both Holm-adjusted tests are significant at **α = .05**. Both raw p-values reach the Monte Carlo floor of 1 / (1,000,000 + 1): no extreme null-bootstrap draws occurred. These are resolution-limited estimates, not precisely resolved tail probabilities.

## Additional checks

| Comparison | Sensitivity t-test | Participant consistency |
|---|---:|---:|
| Ordered vs. Shuffled | t(377) = 5.876, p = 9.23×10⁻⁹ | **8/8** favor Ordered; median difference **+12.86 pp** |
| Ordered vs. Mean | t(377) = 5.945, p = 6.30×10⁻⁹ | **8/8** favor Ordered; median difference **+12.36 pp** |

Central / Side accuracies were **73.02% / 72.49%** for Ordered, **62.96% / 60.85%** for Shuffled, and **60.32% / 61.38%** for Mean.

## Interpretation

Ordered Image FER outperforms both controls by approximately **11–12 percentage points**, with significant Holm-adjusted tests and positive differences for all eight test participants. This supports a benefit of chronological sequence modeling beyond access to multiple frames in the evaluated models. Independent optimization, and the different aggregation architecture of Mean, mean that these comparisons do not isolate temporal order as the only experimental difference.
