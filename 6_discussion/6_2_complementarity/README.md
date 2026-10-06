# 6.2 Complementarity of Image and FEA Sequences

[Up one level](../README.md) · [Repository README](../../README.md)

[dynamic_fusion_correctness_groups.ipynb](dynamic_fusion_correctness_groups.ipynb) produces Figure 5 and the descriptive results used in Section 6.2. It reads the shared [static](../../4_static_facial_expression_recognition/static_test_predictions.csv) and [dynamic](../../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv) prediction CSVs; no raw datasets or checkpoints are needed. Follow the [shared execution setup](../../env/README.md).

## Results and outputs

Start with [section_6_2_summary.md](section_6_2_summary.md). The notebook computes:

- Multimodal correctness within the four unimodal correctness groups, plotted in [Figure 5](figures/dynamic_fusion_correctness_groups.pdf).
- Dynamic class-wise precision, recall, and F1, using each modality's native evaluation unit, plus fusion recall differences.
- Dominant multimodal confusion pairs and their share of all errors.
- Static–dynamic changes in unimodal correctness overlap.

The six numerical exports are in [tables/](tables/). The summary links to each table.

Image and Multimodal use 756 view predictions; FEA-only metrics deduplicate to 378 reenactments. Correctness overlaps pair each FEA prediction with both image views. Conditional fusion outcomes are descriptive, and the prediction-selection oracle is not a strict ceiling on learned fusion.

The [Section 5.3.1 overlap analysis](../../5_dynamic_facial_expression_recognition/5_3_multimodal/5_3_1_complementarity/README.md) describes the unimodal overlap before evaluating fusion. Paired accuracy comparisons are in [significance-tests](../significance-tests/README.md), while coefficient profiles and annotation agreement are in [Section 6.3](../6_3_interpreting/README.md).
