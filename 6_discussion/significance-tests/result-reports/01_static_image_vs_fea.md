# Static Image vs. Static FEA

**A:** Static Image. **B:** Static FEA. **Δ = B − A**, in percentage points (pp).

**Source:** [static_image_vs_fea_significance_tests.ipynb](../static-significance-tests/static_image_vs_fea_significance_tests.ipynb); matching CSVs in `../static-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Image/Multimodal correctness is averaged across two views per reenactment; FEA contributes one binary outcome. Primary test: two-sided centered reenactment bootstrap with inclusive integer boundary counting. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 69.84% (528/756 correct) |
| B accuracy | 71.69% (271/378 correct) |
| Δ; 95% CI | **+1.85 pp; [-3.31, 6.88] pp** |
| Primary p | **0.493626** |
| Main result | **Not significant at α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **756 view-level samples (Central and Side)**. The two views are dependent; inferential tests still use 378 reenactments. The same FEA prediction is paired with each view and counted twice here. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 414 | 54.76% |
| Only A correct | 114 | 15.08% |
| Only B correct | 128 | 16.93% |
| Both wrong | 100 | 13.23% |

Relative to A, B corrects **128** errors and introduces **114** errors; net **+14** correct view predictions (+1.85 pp). B retains 414/528 (78.41%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 0.708 | 377 | 0.479103 | Not significant |

### 4. Secondary view comparisons

Exact two-sided McNemar on 378 pairs per row; Holm correction across these three tests. Δ is second minus first. Discordants: first-only / second-only correct.

| Comparison | Accuracies (%) | Δ (pp) | Discordants | Raw p | Holm p | Significant after Holm? |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Central vs. FEA | 72.75 / 71.69 | -1.06 | 63 / 59 | 0.786058 | 0.786058 | No |
| Side vs. FEA | 66.93 / 71.69 | +4.76 | 51 / 69 | 0.120328 | 0.240656 | No |
| Central vs. Side | 72.75 / 66.93 | -5.82 | 58 / 36 | 0.029766 | 0.089299 | No |

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 76.60 | 57.45 | -19.15 |
| 8 | 54 | 59.26 | 66.67 | +7.41 |
| 10 | 46 | 48.91 | 78.26 | +29.35 |
| 13 | 46 | 80.43 | 80.43 | +0.00 |
| 15 | 48 | 68.75 | 64.58 | -4.17 |
| 18 | 43 | 80.23 | 90.70 | +10.47 |
| 23 | 53 | 69.81 | 83.02 | +13.21 |
| 27 | 41 | 78.05 | 51.22 | -26.83 |

Participants favoring B/A/tied: **4/3/1**; median Δ: **+3.70 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

No significant pooled difference; this does not establish equivalence. No secondary comparison survives Holm correction.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
