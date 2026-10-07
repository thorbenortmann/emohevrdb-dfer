# Static FEA vs. Static Multimodal

**A:** Static FEA. **B:** Static Multimodal. **Δ = B − A**, in percentage points (pp).

**Source:** [static_fea_vs_multimodal_significance_tests.ipynb](../static-significance-tests/static_fea_vs_multimodal_significance_tests.ipynb); matching CSVs in `../static-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Image/Multimodal correctness is averaged across two views per reenactment; FEA contributes one binary outcome. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 71.69% (271/378 correct) |
| B accuracy | 80.42% (608/756 correct) |
| Δ; 95% CI | **+8.73 pp; [4.63, 12.83] pp** |
| Primary p | **0.000044** |
| Main result | **Significant at nominal α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. The same FEA prediction is paired with each view and counted twice here. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 495 | 65.48% |
| Only A correct | 47 | 6.22% |
| Only B correct | 113 | 14.95% |
| Both wrong | 101 | 13.36% |

Relative to A, B corrects **113** errors and introduces **47** errors; net **+66** correct view predictions (+8.73 pp). B retains 495/542 (91.33%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 4.165 | 377 | 0.000039 | Significant |

### 4. Secondary view comparisons

Exact two-sided McNemar on 378 pairs per row; Holm correction across these three tests. Δ is second minus first. Discordants: first-only / second-only correct.

| Comparison | Accuracies (%) | Δ (pp) | Discordants | Raw p | Holm p | Significant after Holm? |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| FEA vs. Central Multimodal | 71.69 / 83.60 | +11.90 | 18 / 63 | 5.2e-07 | 1.56e-06 | Yes |
| FEA vs. Side Multimodal | 71.69 / 77.25 | +5.56 | 29 / 50 | 0.023820 | 0.023820 | Yes |
| Central Multimodal vs. Side Multimodal | 83.60 / 77.25 | -6.35 | 41 / 17 | 0.002233 | 0.004465 | Yes |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 57.45 | 77.66 | +20.21 |
| 8 | 54 | 66.67 | 74.07 | +7.41 |
| 10 | 46 | 78.26 | 64.13 | -14.13 |
| 13 | 46 | 80.43 | 90.22 | +9.78 |
| 15 | 48 | 64.58 | 82.29 | +17.71 |
| 18 | 43 | 90.70 | 93.02 | +2.33 |
| 23 | 53 | 83.02 | 80.19 | -2.83 |
| 27 | 41 | 51.22 | 84.15 | +32.93 |

Participants favoring B/A/tied: **6/2/0**; median Δ: **+8.60 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

Multimodal accuracy is higher overall and in both view-specific comparisons. Central Multimodal also exceeds Side Multimodal after Holm correction. The larger Central-view gain is descriptive; no interaction test was performed.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
