# 6.3 Interpreting Persistent Error Patterns

[Discussion](../README.md)

Two independent notebooks analyze the shared dynamic predictions without model inference.

## FEA profiles and error contrasts

[multimodal_fea_analysis.ipynb](multimodal_fea_analysis.ipynb) additionally reads raw DFEA split CSVs and [facs_fea_mapping.json](facs_fea_mapping.json). Category profiles pool all 1,727 retained sequences; error contrasts use test views only. Each coefficient is averaged over 30 observations, and 63 coefficients are summarized into 33 explicit movement groups.

| Paper content | Saved output |
| --- | --- |
| Figure S6: category profiles | [03_category_profiles_compact.pdf](outputs/multimodal_fea_analysis/03_category_profiles_compact.pdf) and [category_profiles_grouped.csv](outputs/multimodal_fea_analysis/category_profiles_grouped.csv) |
| Figure S7: Anger→Disgust, Disgust→Happiness, Surprise→Fear contrasts | [04_confused_minus_correct_compact.pdf](outputs/multimodal_fea_analysis/04_confused_minus_correct_compact.pdf) and [confusion_contrasts_grouped.csv](outputs/multimodal_fea_analysis/confusion_contrasts_grouped.csv) |
| Section 6.3: reported category/error-associated means and group counts | [section_6_3_summary.md](outputs/multimodal_fea_analysis/section_6_3_summary.md); complete [numerical exports](outputs/multimodal_fea_analysis/) |

Each contrast compares correctly classified source cases with the named confusion target; other errors are excluded. A FEA sequence may contribute to both views or both groups. Semantic FACS correspondences and descriptive differences do not validate AU measurements or establish causal model reliance.

## Human annotation agreement

[analyze_label_agreement_and_model_errors.ipynb](analyze_label_agreement_and_model_errors.ipynb) joins predictions to [labels-master-table-analysis_irr.csv](labels-master-table-analysis_irr.csv), a complete unchanged semicolon-delimited copy of the [upstream file at commit `deee4796`](https://github.com/thorbenortmann/emoji-hero-vr-database/blob/deee4796cbdbfbd39ce70e99c7adb8836feee86e/v_data_annotation/b_results/labels-master-table-analysis_irr.csv).

[The saved report](outputs/label_agreement_and_model_errors/label_agreement_and_model_errors_report.md) links the Section 6.3 annotation results to these [supporting tables](outputs/label_agreement_and_model_errors/):

- [Agreement-group summary](outputs/label_agreement_and_model_errors/agreement_group_summary.csv): 103/378 = 27.25% of reenactments have 2/3 agreement; their predictions account for 62/139 = 44.60% of errors.
- [Equal-class accuracy](outputs/label_agreement_and_model_errors/equal_class_accuracy_summary.csv): the agreement-group gap decreases from 16.10 to 9.88 pp when weighting the six shared categories equally.
- [Dissenting-label correspondence](outputs/label_agreement_and_model_errors/dissenting_label_correspondence.csv): 49/62 = 79.03% of erroneous 2/3-agreement predictions match the dissenting label.

Three raters judged one central-view reference image per reenactment; both view predictions inherit those annotations. The notebook produces descriptive tables and a report, without additional figures or relabeling.
