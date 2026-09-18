# Static Image vs. Static Multimodal

**A:** Static Image. **B:** Static Multimodal. **Δ = B − A**, in percentage points (pp).

**Source:** [static_image_vs_multimodal_significance_tests.ipynb](../static-significance-tests/static_image_vs_multimodal_significance_tests.ipynb); matching CSVs in `../static-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Both Image and Multimodal contribute Central and Side correctness values. The paired view-level differences are averaged within each reenactment. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 69.84% (528/756 correct) |
| B accuracy | 80.42% (608/756 correct) |
| Δ; 95% CI | **+10.58 pp; [7.54, 13.76] pp** |
| Primary p | **1e-06** |
| Main result | **Significant at nominal α = 0.05** |

The bootstrap p-value is the simulation floor, 1/1,000,001: zero extreme null draws.

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 506 | 66.93% |
| Only A correct | 22 | 2.91% |
| Only B correct | 102 | 13.49% |
| Both wrong | 126 | 16.67% |

Relative to A, B corrects **102** errors and introduces **22** errors; net **+80** correct view predictions (+10.58 pp). B retains 506/528 (95.83%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 6.727 | 377 | 6.46e-11 | Significant |

### 4. Secondary view comparisons

No secondary significance tests. View accuracies are descriptive.

| View | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: |
| Central | 72.75 | 83.60 | +10.85 |
| Side | 66.93 | 77.25 | +10.32 |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 76.60 | 77.66 | +1.06 |
| 8 | 54 | 59.26 | 74.07 | +14.81 |
| 10 | 46 | 48.91 | 64.13 | +15.22 |
| 13 | 46 | 80.43 | 90.22 | +9.78 |
| 15 | 48 | 68.75 | 82.29 | +13.54 |
| 18 | 43 | 80.23 | 93.02 | +12.79 |
| 23 | 53 | 69.81 | 80.19 | +10.38 |
| 27 | 41 | 78.05 | 84.15 | +6.10 |

Participants favoring B/A/tied: **8/0/0**; median Δ: **+11.58 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

Multimodal accuracy exceeds Image accuracy by 10.58 pp, with the same effect direction for all eight participants.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
