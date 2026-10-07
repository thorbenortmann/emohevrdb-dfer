# Dynamic Image vs. Dynamic FEA

**A:** Dynamic Image. **B:** Dynamic FEA. **Δ = B − A**, in percentage points (pp).

**Source:** [dynamic_image_vs_fea_significance_tests.ipynb](../dynamic-significance-tests/dynamic_image_vs_fea_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Image/Multimodal correctness is averaged across two views per reenactment; FEA contributes one binary outcome. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 72.75% (550/756 correct) |
| B accuracy | 78.31% (296/378 correct) |
| Δ; 95% CI | **+5.56 pp; [1.06, 10.05] pp** |
| Primary p | **0.016963** |
| Main result | **Significant at nominal α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. The same FEA prediction is paired with each view and counted twice here. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 476 | 62.96% |
| Only A correct | 74 | 9.79% |
| Only B correct | 116 | 15.34% |
| Both wrong | 90 | 11.90% |

Relative to A, B corrects **116** errors and introduces **74** errors; net **+42** correct view predictions (+5.56 pp). B retains 476/550 (86.55%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 2.416 | 377 | 0.016154 | Significant |

### 4. Secondary view comparisons

Exact two-sided McNemar on 378 pairs per row; Holm correction across these three tests. Δ is second minus first. Discordants: first-only / second-only correct.

| Comparison | Accuracies (%) | Δ (pp) | Discordants | Raw p | Holm p | Significant after Holm? |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Central vs. FEA | 73.02 / 78.31 | +5.29 | 36 / 56 | 0.047012 | 0.100080 | No |
| Side vs. FEA | 72.49 / 78.31 | +5.82 | 38 / 60 | 0.033360 | 0.100080 | No |
| Central vs. Side | 73.02 / 72.49 | -0.53 | 38 / 36 | 0.907561 | 0.907561 | No |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 82.98 | 72.34 | -10.64 |
| 8 | 54 | 55.56 | 72.22 | +16.67 |
| 10 | 46 | 61.96 | 80.43 | +18.48 |
| 13 | 46 | 80.43 | 93.48 | +13.04 |
| 15 | 48 | 71.88 | 62.50 | -9.38 |
| 18 | 43 | 86.05 | 97.67 | +11.63 |
| 23 | 53 | 77.36 | 79.25 | +1.89 |
| 27 | 41 | 68.29 | 70.73 | +2.44 |

Participants favoring B/A/tied: **6/2/0**; median Δ: **+7.03 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

FEA exceeds pooled Image accuracy at nominal significance. Neither individual view comparison survives Holm correction.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
