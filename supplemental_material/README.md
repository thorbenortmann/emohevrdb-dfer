# Supplemental Material

[Repository README](../README.md) · [Environment setup](../env/README.md)

This README maps all seven figures and eleven tables in the submitted Supplemental Material to their sources. Analyses remain beside the main-article section they support. The shared [confusion-matrix notebook](confusion_matrices.ipynb) stays here because it covers human annotation and both static and dynamic baselines.

## Reference tables

| Supplemental section | Table | Source |
| --- | --- | --- |
| 1. FACS Action Unit Reference | S1: AU numbers and names | Reference table compiled from the FACS manual in the submitted manuscript; no analysis notebook. |
| 2. Meta Quest Pro FEA Coefficients | S2: 63 coefficients and semantic AU correspondences | Reference table in the submitted manuscript. The machine-readable [FEA/FACS mapping](../6_discussion/6_3_interpreting/facs_fea_mapping.json) documents the correspondences used by the Section 6.3 analysis. |

FEA coefficients are proprietary facial-movement estimates. Semantic correspondences do not establish validated AU measurements.

## Human annotation and baseline results

| Supplemental section | Item | Producer and saved output |
| --- | --- | --- |
| 3. Human-Rater Annotation Results | Figure S1 | [confusion_matrices.ipynb](confusion_matrices.ipynb): [all annotations](figures/confusion_matrices/human_rater.pdf) and [retained benchmark](figures/confusion_matrices/filtered_human_rater.pdf). |
| 4. Class-Wise Baseline Results | Table S3: static precision, recall, and F1 | [Section 4 baseline sources](../4_static_facial_expression_recognition/README.md#reported-baselines). The shared [static predictions](../4_static_facial_expression_recognition/static_test_predictions.csv) support recomputation. |
| 4. Class-Wise Baseline Results | Figure S2: static confusion matrices | [confusion_matrices.ipynb](confusion_matrices.ipynb): [Image](figures/confusion_matrices/si.pdf), [FEA](figures/confusion_matrices/sfea.pdf), and [Multimodal](figures/confusion_matrices/smul.pdf). |
| 4. Class-Wise Baseline Results | Figure S3: dynamic confusion matrices | [confusion_matrices.ipynb](confusion_matrices.ipynb): [Image](figures/confusion_matrices/di.pdf), [FEA](figures/confusion_matrices/dfea.pdf), and [Multimodal](figures/confusion_matrices/dmul.pdf). |

The confusion-matrix notebook plots embedded count matrices; it does not load prediction CSVs or run model inference. Run it from this directory using the [shared environment](../env/README.md). It exports PDF and PNG panels to `figures/confusion_matrices/`. Figure assembly and subcaptions belong to the manuscript.

Rows represent reference categories and columns assigned or predicted categories. Cells show counts and row-normalized percentages on a common 0–100% color scale. Class order is Anger, Disgust, Fear, Happiness, Neutral, Sadness, Surprise.

Human-rater matrices contain 7,770 ratings for all 2,590 reenactments and 5,334 ratings for the final 1,778 benchmark reenactments. The latter is conditioned on agreement-based retention and subsequent benchmark selection; it does not measure annotation performance before filtering. See [Section 3](../3_emojiherovr_and_emohevrdb/README.md) for annotation provenance and construction.

Model matrices contain 756 camera-view predictions for Image and Multimodal, and 378 reenactment predictions for FEA. The FEA prediction is repeated across both views in the shared CSVs, so retain one row per reenactment when reconstructing FEA matrices. Dynamic predictions are stored in [Section 5](../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv).

## Experimental configuration

Supplemental Section 5 documents the selected dynamic baselines. The tables describe settings implemented in these notebooks; they are not generated analysis outputs.

| Tables | Content | Implementation |
| --- | --- | --- |
| S4–S6 | Image augmentation, architecture, and five-phase training schedule | [efficientnetv2_lstm.ipynb](../5_dynamic_facial_expression_recognition/5_1_image/efficientnetv2_lstm.ipynb); [Section 5.1 documentation](../5_dynamic_facial_expression_recognition/5_1_image/README.md). |
| S7–S8 | FEA architecture and training configuration | [lstm.ipynb](../5_dynamic_facial_expression_recognition/5_2_fea/lstm.ipynb); [Section 5.2 documentation](../5_dynamic_facial_expression_recognition/5_2_fea/README.md). |
| S9–S11 | Multimodal image augmentation, fusion-head architecture, and training configuration | [intermediate_fusion_cross_attention.ipynb](../5_dynamic_facial_expression_recognition/5_3_multimodal/5_3_3_intermediate/intermediate_fusion_cross_attention.ipynb); [Section 5.3.3 documentation](../5_dynamic_facial_expression_recognition/5_3_multimodal/5_3_3_intermediate/README.md). |

Environment and dataset placement are documented in [env/README.md](../env/README.md). Checkpoint links and inference filenames are in [Section 5 models](../5_dynamic_facial_expression_recognition/models/README.md).

## Temporal variation and error interpretation

| Supplemental section | Figure | Producer and saved output |
| --- | --- | --- |
| 6. FEA-Sequence Trajectories | S4: largest-increase positions | [fea_temporal_analysis.ipynb](../6_discussion/6_1_temporal/fea_temporal_analysis.ipynb); [heatmap](../6_discussion/6_1_temporal/figures/fea_temporal_analysis/largest_increase_heatmap.pdf). |
| 6. FEA-Sequence Trajectories | S5: six category trajectories | Same notebook; [panel links and method](../6_discussion/6_1_temporal/README.md#saved-figures). |
| 7. Interpreting Persistent Error Patterns | S6: category-level FEA profiles | [multimodal_fea_analysis.ipynb](../6_discussion/6_3_interpreting/multimodal_fea_analysis.ipynb); [profile figure](../6_discussion/6_3_interpreting/outputs/multimodal_fea_analysis/03_category_profiles_compact.pdf). |
| 7. Interpreting Persistent Error Patterns | S7: confused-minus-correct FEA differences | Same notebook; [contrast figure](../6_discussion/6_3_interpreting/outputs/multimodal_fea_analysis/04_confused_minus_correct_compact.pdf). |

Run these notebooks from their respective Section 6 directories. [Section 6.1](../6_discussion/6_1_temporal/README.md) documents the raw-DFEA trajectory analysis; [Section 6.3](../6_discussion/6_3_interpreting/README.md) documents the profile inputs, grouped coefficients, and exported numerical tables.

Temporal and category-level summaries pool retained training, validation, and test sequences. Error contrasts use test predictions only. The trajectories are not aligned to annotated expression phases, and error-associated coefficient differences do not establish causal model reliance.
