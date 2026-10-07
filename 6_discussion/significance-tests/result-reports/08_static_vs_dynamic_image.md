# Static Image vs. Dynamic Image

**A:** Static Image. **B:** Dynamic Image. **Δ = B − A**, in percentage points (pp).

**Source:** [static_image_vs_dynamic_image_significance_tests.ipynb](../dynamic-significance-tests/static_image_vs_dynamic_image_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Static and Dynamic Image predictions correspond one-to-one for Central and Side. The paired view-level differences are averaged within each reenactment. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 69.84% (528/756 correct) |
| B accuracy | 72.75% (550/756 correct) |
| Δ; 95% CI | **+2.91 pp; [-0.79, 6.61] pp** |
| Primary p | **0.129288** |
| Main result | **Not significant at α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 452 | 59.79% |
| Only A correct | 76 | 10.05% |
| Only B correct | 98 | 12.96% |
| Both wrong | 130 | 17.20% |

Relative to A, B corrects **98** errors and introduces **76** errors; net **+22** correct view predictions (+2.91 pp). B retains 452/528 (85.61%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 1.551 | 377 | 0.121791 | Not significant |

### 4. Secondary view comparisons

No secondary significance tests. View accuracies are descriptive.

| View | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: |
| Central | 72.75 | 73.02 | +0.26 |
| Side | 66.93 | 72.49 | +5.56 |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 76.60 | 82.98 | +6.38 |
| 8 | 54 | 59.26 | 55.56 | -3.70 |
| 10 | 46 | 48.91 | 61.96 | +13.04 |
| 13 | 46 | 80.43 | 80.43 | +0.00 |
| 15 | 48 | 68.75 | 71.88 | +3.12 |
| 18 | 43 | 80.23 | 86.05 | +5.81 |
| 23 | 53 | 69.81 | 77.36 | +7.55 |
| 27 | 41 | 78.05 | 68.29 | -9.76 |

Participants favoring B/A/tied: **5/2/1**; median Δ: **+4.47 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

The positive pooled estimate is not significant and does not establish equivalence. The Side-view gain is descriptively larger; no view-specific static–dynamic significance or interaction test was performed.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
