# Static Multimodal vs. Dynamic Multimodal

**A:** Static Multimodal. **B:** Dynamic Multimodal. **Δ = B − A**, in percentage points (pp).

**Source:** [static_multimodal_vs_dynamic_multimodal_significance_tests.ipynb](../dynamic-significance-tests/static_multimodal_vs_dynamic_multimodal_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Static and Dynamic Multimodal predictions correspond one-to-one for Central and Side. The paired view-level differences are averaged within each reenactment. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 80.42% (608/756 correct) |
| B accuracy | 81.61% (617/756 correct) |
| Δ; 95% CI | **+1.19 pp; [-1.98, 4.37] pp** |
| Primary p | **0.494278** |
| Main result | **Not significant at α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 552 | 73.02% |
| Only A correct | 56 | 7.41% |
| Only B correct | 65 | 8.60% |
| Both wrong | 83 | 10.98% |

Relative to A, B corrects **65** errors and introduces **56** errors; net **+9** correct view predictions (+1.19 pp). B retains 552/608 (90.79%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 0.722 | 377 | 0.470472 | Not significant |

### 4. Secondary view comparisons

No secondary significance tests. View accuracies are descriptive.

| View | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: |
| Central | 83.60 | 81.75 | -1.85 |
| Side | 77.25 | 81.48 | +4.23 |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 77.66 | 86.17 | +8.51 |
| 8 | 54 | 74.07 | 70.37 | -3.70 |
| 10 | 46 | 64.13 | 72.83 | +8.70 |
| 13 | 46 | 90.22 | 89.13 | -1.09 |
| 15 | 48 | 82.29 | 78.12 | -4.17 |
| 18 | 43 | 93.02 | 96.51 | +3.49 |
| 23 | 53 | 80.19 | 85.85 | +5.66 |
| 27 | 41 | 84.15 | 75.61 | -8.54 |

Participants favoring B/A/tied: **4/4/0**; median Δ: **+1.20 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

The pooled difference is not significant and does not establish equivalence. Participants split 4–4. Descriptively, Dynamic accuracy decreases for Central and increases for Side; no view-specific static–dynamic significance or interaction test was performed.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
