# Static FEA vs. Dynamic FEA

**A:** Static FEA. **B:** Dynamic FEA. **Δ = B − A**, in percentage points (pp).

**Source:** [static_fea_vs_dynamic_fea_significance_tests.ipynb](../dynamic-significance-tests/static_fea_vs_dynamic_fea_significance_tests.ipynb); matching CSVs in `../dynamic-significance-tests/statistical_results/`.

## Test setup

378 paired reenactments from eight participants. Each condition contributes one binary FEA outcome per reenactment. Primary test: exact two-sided McNemar. 95% CI: ordinary paired percentile bootstrap. Bootstrap settings: 1,000,000 draws per distribution, seed 42, batch 10,000.

## Results

### 1. Primary comparison

| Quantity | Result |
| --- | --- |
| A accuracy | 71.69% (271/378 correct) |
| B accuracy | 78.31% (296/378 correct) |
| Δ; 95% CI | **+6.61 pp; [2.91, 10.58] pp** |
| Primary p | **0.001264** |
| Main result | **Significant at nominal α = 0.05** |

### 2. Paired correctness overlap (descriptive)

Counts use **378 reenactments**. “Both wrong” does not require the same incorrect class.

| Paired outcome | Count | Share |
| --- | ---: | ---: |
| Both correct | 255 | 67.46% |
| Only A correct | 16 | 4.23% |
| Only B correct | 41 | 10.85% |
| Both wrong | 66 | 17.46% |

Relative to A, B corrects **41** errors and introduces **16** errors; net **+25** correct reenactments (+6.61 pp). B retains 255/271 (94.10%) of A’s correct outcomes. The gain therefore includes both corrections and losses, rather than only additional correct outcomes.

### 3. Sensitivity check

| Test | t | df | p | Decision |
| --- | ---: | ---: | ---: | --- |
| Two-sided one-sample t-test on paired differences | 3.356 | 377 | 0.000871 | Significant |

### 4. Secondary view comparisons

None; FEA has no camera-specific prediction.

### 5. Participant heterogeneity (descriptive)

| Participant | Reenactments | A (%) | B (%) | Δ (pp) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 47 | 57.45 | 72.34 | +14.89 |
| 8 | 54 | 66.67 | 72.22 | +5.56 |
| 10 | 46 | 78.26 | 80.43 | +2.17 |
| 13 | 46 | 80.43 | 93.48 | +13.04 |
| 15 | 48 | 64.58 | 62.50 | -2.08 |
| 18 | 43 | 90.70 | 100.00 | +9.30 |
| 23 | 53 | 83.02 | 79.25 | -3.77 |
| 27 | 41 | 51.22 | 68.29 | +17.07 |

Participants favoring B/A/tied: **6/2/0**; median Δ: **+7.43 pp**. Pooled effects weight reenactments equally; the median summarizes eight participant effects.

## Interpretation and scope

Dynamic FEA has higher accuracy: 41 reenactments are correct only for Dynamic versus 16 only for Static. Six of eight participants favor Dynamic FEA.

Primary p-values are not jointly adjusted across nine comparisons. Reenactment-level tests do not account for dependence among reenactments from the same participant or model-training variability. Participant tables and overlap counts are descriptive.
