# Statistical Significance Tests — Summary

Nine paired comparisons of fitted FER models on 378 reenactments from eight participants. Image/Multimodal accuracies use 756 view predictions; FEA uses 378 predictions. Δ = B − A; positive values favor B. See the [Statistical Comparison Plan](../statistical_comparison_plan.md) and linked reports for methods and detailed tables.

## Primary comparisons

| Comparison (A vs. B) | A (%) | B (%) | Δ (pp) | 95% CI (pp) | Primary p | Main result |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Static Image vs. Static FEA](01_static_image_vs_fea.md) | 69.84 | 71.69 | +1.85 | [-3.31, 6.88] | 0.493626 | Not significant |
| [Static FEA vs. Static Multimodal](02_static_fea_vs_multimodal.md) | 71.69 | 80.42 | +8.73 | [4.63, 12.83] | 0.000044 | Significant: B higher (nominal) |
| [Static Image vs. Static Multimodal](03_static_image_vs_multimodal.md) | 69.84 | 80.42 | +10.58 | [7.54, 13.76] | 1e-06 | Significant: B higher (nominal) |
| [Dynamic Image vs. Dynamic FEA](04_dynamic_image_vs_fea.md) | 72.75 | 78.31 | +5.56 | [1.06, 10.05] | 0.016963 | Significant: B higher (nominal) |
| [Dynamic FEA vs. Dynamic Multimodal](05_dynamic_fea_vs_multimodal.md) | 78.31 | 81.61 | +3.31 | [0.26, 6.48] | 0.043552 | Significant: B higher (nominal; borderline) |
| [Dynamic Image vs. Dynamic Multimodal](06_dynamic_image_vs_multimodal.md) | 72.75 | 81.61 | +8.86 | [5.69, 12.04] | 1e-06 | Significant: B higher (nominal) |
| [Static FEA vs. Dynamic FEA](07_static_vs_dynamic_fea.md) | 71.69 | 78.31 | +6.61 | [2.91, 10.58] | 0.001264 | Significant: B higher (nominal) |
| [Static Image vs. Dynamic Image](08_static_vs_dynamic_image.md) | 69.84 | 72.75 | +2.91 | [-0.79, 6.61] | 0.129288 | Not significant |
| [Static Multimodal vs. Dynamic Multimodal](09_static_vs_dynamic_multimodal.md) | 80.42 | 81.61 | +1.19 | [-1.98, 4.37] | 0.494278 | Not significant |

Eight primary p-values use a two-sided centered reenactment bootstrap; Static vs. Dynamic FEA uses exact McNemar. All CIs are paired percentile-bootstrap intervals. Bootstrap: 1,000,000 draws per distribution, seed 42, batch 10,000; p = (K + 1)/(B + 1). Values near 10⁻⁶ are the simulation floor. All nine sensitivity t-tests agree with the primary significance decisions.

## Main trends for the paper

Significance below refers to the planned primary tests at the nominal 5% level, without a joint correction across the nine comparisons.

- **Multimodal FER achieves the highest accuracy in both settings.** It significantly outperforms Image FER by **10.58 pp in Static** and **8.86 pp in Dynamic**. This advantage is descriptively consistent across participants: **all eight participants** have higher Multimodal than Image accuracy in both settings.

- **Dynamic FEA clearly outperforms Static FEA.** Accuracy increases from **71.69% to 78.31%** (**+6.61 pp**, exact McNemar p = **0.001264**). Dynamic FEA corrects **41 reenactments** that Static FEA misclassifies, while losing **16** that Static FEA classifies correctly; **255** are correct for both. The improvement therefore reflects more corrections than losses, rather than simply adding correct predictions without introducing new errors.

- **The Dynamic models do not show a statistically significant overall gain for Image or Multimodal FER.** Image accuracy increases by **2.91 pp** (p = **0.129288**), and Multimodal accuracy by **1.19 pp** (p = **0.494278**). Both point estimates favor Dynamic, but the tests provide insufficient evidence for an overall difference. They do not establish equivalence between Static and Dynamic performance.

- **FEA has a clearer advantage over Image FER in the Dynamic setting.** Static FEA exceeds Static Image by **1.85 pp**, without a significant difference (p = **0.493626**). Dynamic FEA exceeds Dynamic Image by **5.56 pp**, which is nominally significant (p = **0.016963**). This pattern is descriptive evidence of a larger Dynamic advantage; the difference between the two modality effects was not itself tested.

- **Multimodal FER exceeds FEA in both settings, but its Dynamic advantage is smaller and less consistent.** The Static gain is **8.73 pp** (p = **0.000044**), with **six of eight participants** favoring Multimodal. The Dynamic gain is **3.31 pp**, with a borderline primary p-value (**0.043552**) and an even participant split: **four improve and four deteriorate**. The Dynamic result therefore supports only a small, heterogeneous advantage over FEA.

- **Descriptive view results suggest that the Dynamic–Static gains are concentrated in the Side view.** For Image FER, the changes are **+0.26 pp Central** versus **+5.56 pp Side**. For Multimodal FER, they are **−1.85 pp Central** versus **+4.23 pp Side**. These view-specific Static–Dynamic differences and their contrast were not tested inferentially.

- **The secondary tests provide additional evidence for Static Multimodal FER.** After Holm correction, it outperforms Static FEA for both Central and Side views, and its Central-view accuracy exceeds its Side-view accuracy. No secondary comparison remains significant in the other three test families.

- **The primary and sensitivity analyses agree across all nine comparisons.** The sensitivity t-tests yield the same significance decisions as the primary tests. This agreement does not address the unmodeled dependence between reenactments from the same participant.

## Correctness changes between Static and Dynamic

| Modality | Unit; N | Both correct | Static only | Dynamic only | Both wrong | Net gain |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| FEA | Reenactment; 378 | 255 | 16 | 41 | 66 | +25 |
| Image | View sample; 756 | 452 | 76 | 98 | 130 | +22 |
| Multimodal | View sample; 756 | 552 | 56 | 65 | 83 | +9 |

All three Dynamic models both correct previous errors and lose some previously correct predictions. These counts describe overlap, not an additional significance test. View samples within a reenactment are dependent. “Both wrong” may include different incorrect classes. The individual reports contain analogous modality-overlap tables, secondary tests, and all eight participant rows.

## Inferential scope

Primary significance is nominal at α = 0.05: no joint correction across the nine primary tests. Holm adjustment applies separately within four families of three secondary McNemar tests. The analyses retain both views within reenactments but do not adjust for dependence among reenactments from the same participant or model-training variability. Participant tables are descriptive; conclusions concern these fitted models and test data and do not isolate temporal modeling from other model differences.
