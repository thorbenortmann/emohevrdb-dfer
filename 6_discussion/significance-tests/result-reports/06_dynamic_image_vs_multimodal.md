# Dynamic Image vs. Dynamic Multimodal

**A:** Dynamic Image. **B:** Dynamic Multimodal. **Δ = B − A**, in percentage points (pp).

**Source:** [dynamic_image_vs_multimodal_significance_tests.ipynb](../dynamic-significance-tests/dynamic_image_vs_multimodal_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Both Image and Multimodal contribute Central and Side correctness values. The paired view-level differences are averaged within each reenactment. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 72.75% (550/756 correct) |
| B accuracy | 81.61% (617/756 correct) |
| Δ; 95% CI | **+8.86 pp; [5.69, 12.04] pp** |
| Primary p | **1e-06** |
| Main result | **Significant at nominal α = 0.05** |

The bootstrap p-value is the simulation floor, 1/1,000,001: zero extreme null draws.

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 526 | 69.58% |
| Only A correct | 24 | 3.17% |
| Only B correct | 91 | 12.04% |
| Both wrong | 115 | 15.21% |

Relative to A, B corrects **91** errors and introduces **24** errors; net **+67** correct view predictions (+8.86 pp). B retains 526/550 (95.64%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 5.407 | 377 | 1.14e-07 | Significant |

### 4. Secondary view comparisons

No secondary significance tests. View accuracies are descriptive.

| View | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: |
| Central | 73.02 | 81.75 | +8.73 |
| Side | 72.49 | 81.48 | +8.99 |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 82.98 | 86.17 | +3.19 |
| 8 | 54 | 55.56 | 70.37 | +14.81 |
| 10 | 46 | 61.96 | 72.83 | +10.87 |
| 13 | 46 | 80.43 | 89.13 | +8.70 |
| 15 | 48 | 71.88 | 78.12 | +6.25 |
| 18 | 43 | 86.05 | 96.51 | +10.47 |
| 23 | 53 | 77.36 | 85.85 | +8.49 |
| 27 | 41 | 68.29 | 75.61 | +7.32 |

Participants favoring B/A/tied: **8/0/0**; median Δ: **+8.59 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

Multimodal accuracy exceeds Image accuracy by 8.86 pp, with the same effect direction for all eight participants.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
