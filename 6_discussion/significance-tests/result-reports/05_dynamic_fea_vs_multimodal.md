# Dynamic FEA vs. Dynamic Multimodal

**A:** Dynamic FEA. **B:** Dynamic Multimodal. **Δ = B − A**, in percentage points (pp).

**Source:** [dynamic_fea_vs_multimodal_significance_tests.ipynb](../dynamic-significance-tests/dynamic_fea_vs_multimodal_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Image/Multimodal correctness is averaged across two views per reenactment; FEA contributes one binary outcome. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 78.31% (296/378 correct) |
| B accuracy | 81.61% (617/756 correct) |
| Δ; 95% CI | **+3.31 pp; [0.26, 6.48] pp** |
| Primary p | **0.043552** |
| Main result | **Significant at nominal α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. The same FEA prediction is paired with each view and counted twice here. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 560 | 74.07% |
| Only A correct | 32 | 4.23% |
| Only B correct | 57 | 7.54% |
| Both wrong | 107 | 14.15% |

Relative to A, B corrects **57** errors and introduces **32** errors; net **+25** correct view predictions (+3.31 pp). B retains 560/592 (94.59%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 2.057 | 377 | 0.040392 | Significant |

### 4. Secondary view comparisons

Exact two-sided McNemar on 378 pairs per row; Holm correction across these three tests. Δ is second minus first. Discordants: first-only / second-only correct.

| Comparison | Accuracies (%) | Δ (pp) | Discordants | Raw p | Holm p | Significant after Holm? |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| FEA vs. Central Multimodal | 78.31 / 81.75 | +3.44 | 15 / 28 | 0.065994 | 0.197982 | No |
| FEA vs. Side Multimodal | 78.31 / 81.48 | +3.17 | 17 / 29 | 0.103805 | 0.207611 | No |
| Central Multimodal vs. Side Multimodal | 81.75 / 81.48 | -0.26 | 15 / 14 | 1.000000 | 1.000000 | No |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 72.34 | 86.17 | +13.83 |
| 8 | 54 | 72.22 | 70.37 | -1.85 |
| 10 | 46 | 80.43 | 72.83 | -7.61 |
| 13 | 46 | 93.48 | 89.13 | -4.35 |
| 15 | 48 | 62.50 | 78.12 | +15.62 |
| 18 | 43 | 97.67 | 96.51 | -1.16 |
| 23 | 53 | 79.25 | 85.85 | +6.60 |
| 27 | 41 | 70.73 | 75.61 | +4.88 |

Participants favoring B/A/tied: **4/4/0**; median Δ: **+1.86 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

The 3.31 pp Multimodal advantage has borderline nominal evidence (p = 0.043552) and a 4–4 participant split. No secondary comparison survives Holm correction; this is limited evidence for a consistent advantage over FEA.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
