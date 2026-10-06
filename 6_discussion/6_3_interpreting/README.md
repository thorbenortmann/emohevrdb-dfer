# 6.3 Interpreting Persistent Error Patterns

[Up one level](../README.md) · [Repository README](../../README.md)

Two complementary notebooks support Section 6.3. They use the shared [dynamic prediction CSV](../../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv) and run independently; no model inference is required. See the [environment README](../../env/README.md) for common setup.

| Notebook | Additional inputs | Paper contribution |
| --- | --- | --- |
| [multimodal_fea_analysis.ipynb](multimodal_fea_analysis.ipynb) | Raw DFEA split CSVs; [facs_fea_mapping.json](facs_fea_mapping.json) | Category profiles and error-associated coefficient differences; supplemental Figures S6–S7 |
| [analyze_label_agreement_and_model_errors.ipynb](analyze_label_agreement_and_model_errors.ipynb) | [labels-master-table-analysis_irr.csv](labels-master-table-analysis_irr.csv) | Human-agreement counts, error rates, equal-class accuracy comparison, and dissenting-label correspondence |

## FEA profiles and error contrasts

Category profiles pool 1,727 retained reenactments across the three splits, weighting sequences equally after averaging their 30 observations. For plotting, 63 coefficients are summarized into 33 explicitly defined movement groups.

Error contrasts use test camera-view predictions for Anger→Disgust, Disgust→Happiness, and Surprise→Fear. Each compares the named confusion with correctly classified cases of the same source category; other errors are excluded. A FEA sequence can contribute to both view rows or to both correctness groups.

Outputs are in [outputs/multimodal_fea_analysis/](outputs/multimodal_fea_analysis/):

- [section_6_3_summary.md](outputs/multimodal_fea_analysis/section_6_3_summary.md): numerical summaries and links to complete tables.
- [03_category_profiles_compact.pdf](outputs/multimodal_fea_analysis/03_category_profiles_compact.pdf): supplemental Figure S6.
- [04_confused_minus_correct_compact.pdf](outputs/multimodal_fea_analysis/04_confused_minus_correct_compact.pdf): supplemental Figure S7.
- CSVs containing raw/grouped profiles, differences, group definitions, counts, and selected contrasts.

FEA/FACS correspondences are semantic mappings. These descriptive differences do not validate FEAs as AU measurements or establish causal model reliance.

## Human annotation agreement

The local annotation file is a complete, unchanged copy of the [upstream CSV at commit `deee4796`](https://github.com/thorbenortmann/emoji-hero-vr-database/blob/deee4796cbdbfbd39ce70e99c7adb8836feee86e/v_data_annotation/b_results/labels-master-table-analysis_irr.csv). It contains 2,590 rows and uses semicolon delimiters. Column adaptation and test-set selection occur in memory; the CSV structure is retained.

The notebook joins annotations to the test predictions and computes 2/3 versus 3/3 agreement results, equal-class accuracy over the six categories represented in both groups, and dissenting-label matches among erroneous predictions. It produces supporting CSVs and [a report](outputs/label_agreement_and_model_errors/label_agreement_and_model_errors_report.md) in [outputs/label_agreement_and_model_errors/](outputs/label_agreement_and_model_errors/), without additional figures.

Three raters judged one selected central-view reference image per reenactment; both camera-view predictions inherit that annotation record. The analysis describes agreement and model errors without relabeling samples.
