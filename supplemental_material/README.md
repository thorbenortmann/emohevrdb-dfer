# Supplemental Material

[Repository README](../README.md)

This index maps the seven supplementary figures and eleven tables to their sources. Most analyses remain beside the main-paper section they support. [confusion_matrices.ipynb](confusion_matrices.ipynb) is shared across human annotation and static/dynamic models.

## Figures

| Figure | Content | Producer and saved output |
| --- | --- | --- |
| S1 | Human-rater annotations | [Confusion-matrix notebook](confusion_matrices.ipynb); [all annotations](figures/confusion_matrices/human_rater.pdf), [final benchmark](figures/confusion_matrices/filtered_human_rater.pdf) |
| S2 | Static confusion matrices | Same notebook; [Image](figures/confusion_matrices/si.pdf), [FEA](figures/confusion_matrices/sfea.pdf), [Multimodal](figures/confusion_matrices/smul.pdf) |
| S3 | Dynamic confusion matrices | Same notebook; [Image](figures/confusion_matrices/di.pdf), [FEA](figures/confusion_matrices/dfea.pdf), [Multimodal](figures/confusion_matrices/dmul.pdf) |
| S4 | Largest-increase positions | [Temporal notebook](../6_discussion/6_1_temporal/fea_temporal_analysis.ipynb); [heatmap](../6_discussion/6_1_temporal/figures/fea_temporal_analysis/largest_increase_heatmap.pdf) |
| S5 | Six FEA category trajectories | Same notebook; [panel links](../6_discussion/6_1_temporal/README.md#saved-figures) |
| S6 | Category-level FEA profiles | [FEA-profile notebook](../6_discussion/6_3_interpreting/multimodal_fea_analysis.ipynb); [profile figure](../6_discussion/6_3_interpreting/outputs/multimodal_fea_analysis/03_category_profiles_compact.pdf) |
| S7 | Confused-minus-correct FEA differences | Same notebook; [contrast figure](../6_discussion/6_3_interpreting/outputs/multimodal_fea_analysis/04_confused_minus_correct_compact.pdf) |

The confusion-matrix notebook plots embedded counts and exports PDF/PNG panels to `figures/confusion_matrices/`; it does not load CSVs or perform inference. The six model matrices correspond to the shared [static](../4_static_facial_expression_recognition/static_test_predictions.csv) and [dynamic](../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv) predictions. FEA matrices use 378 reenactments; Image/Multimodal use 756 views. Cells show counts and row percentages on a common 0–100% color scale.

S1 contains 7,770 ratings for all 2,590 reenactments and 5,334 for the final 1,778 benchmark reenactments. The retained matrix is conditioned on agreement filtering and benchmark selection. Annotation provenance is documented in [Section 3](../3_emojiherovr_and_emohevrdb/README.md).

## Tables

| Table | Content | Source |
| --- | --- | --- |
| S1 | FACS AU names | Manuscript reference table compiled from the FACS manual; no analysis notebook |
| S2 | 63 FEA coefficients and semantic AU correspondences | Manuscript reference table; machine-readable [FEA/FACS mapping](../6_discussion/6_3_interpreting/facs_fea_mapping.json) supports the Section 6.3 analysis |
| S3 | Static class-wise precision, recall, and F1 | [Static collector](../4_static_facial_expression_recognition/collect_static_test_predictions.ipynb), **Test results and static complementarity** section; [original baseline reports](../4_static_facial_expression_recognition/README.md#baselines--table-3) |
| S4–S6 | Image augmentation, architecture, and training schedule | [Image training notebook](../5_dynamic_facial_expression_recognition/5_1_image/efficientnetv2_lstm.ipynb) |
| S7–S8 | FEA architecture and training settings | [FEA training notebook](../5_dynamic_facial_expression_recognition/5_2_fea/lstm.ipynb) |
| S9–S11 | Multimodal augmentation, fusion architecture, and training settings | [Intermediate-fusion notebook](../5_dynamic_facial_expression_recognition/5_3_multimodal/5_3_3_intermediate/intermediate_fusion_cross_attention.ipynb) |

S4–S11 describe implemented settings rather than generated analysis outputs. AU correspondences are semantic mappings, not validated AU measurements.

Run notebooks from their containing directories using [the shared setup](../env/README.md). [Section 6.1](../6_discussion/6_1_temporal/README.md) documents temporal inputs/methods; [Section 6.3](../6_discussion/6_3_interpreting/README.md) links the numerical profile and contrast tables. These category summaries pool retained splits, while error contrasts are test-only and describe associations rather than causal feature reliance.
