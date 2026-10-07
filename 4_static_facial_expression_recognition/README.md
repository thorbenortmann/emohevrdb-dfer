# 4. Static Facial Expression Recognition

[Repository README](../README.md)

This section collects aligned test predictions from the frozen static baselines. Original training material remains in the database and static-FER repositories linked below.

## Baselines — Table 3

| Model | Correct / samples | Accuracy (%) | F1 (%) | Original training results |
| --- | ---: | ---: | ---: | --- |
| Image: EfficientNet-B0 | 528 / 756 views | 69.84 | 70.06 | [Image baseline](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vii_baseline/b_training_c_results/emohevrdb) |
| FEA: MLP | 271 / 378 reenactments | 71.69 | 71.10 | [FEA baseline](https://github.com/thorbenortmann/emohevrdb-sfer/tree/main/iii_unimodal_facial_expression_recognition/b_c_training_results) |
| Multimodal: intermediate fusion | 608 / 756 views | 80.42 | 80.22 | [Multimodal baseline](https://github.com/thorbenortmann/emohevrdb-sfer/tree/main/iv_multimodal_facial_expression_recognition/b_training_and_results) |

Macro and support-weighted F1 coincide on these class-balanced test sets.

## Reproduction and downstream outputs

[collect_static_test_predictions.ipynb](collect_static_test_predictions.ipynb) loads the three frozen models, aligns SI/SFEA samples, remaps the legacy class order, and exports [static_test_predictions.csv](static_test_predictions.csv). Its **Test results and static complementarity** section calculates Table 3, class-wise metrics for Table S3, and the overlap counts discussed in Section 4.3.

To regenerate predictions, follow the [static environment setup](env/README.md) and [checkpoint instructions](models/README.md), then run the collector from this directory. The included CSV supports downstream analyses without inference; its schema and evaluation units are documented in the [repository README](../README.md#shared-predictions).

| Reported content | Analysis or output |
| --- | --- |
| Section 4.3: unimodal overlap | Collector; also [static_dynamic_unimodal_overlap.csv](../6_discussion/6_2_complementarity/tables/static_dynamic_unimodal_overlap.csv) |
| Table S3: class-wise precision, recall, and F1 | Collector's class-wise table and original training reports above |
| Figure S2: confusion matrices | [Shared plotting notebook](../supplemental_material/confusion_matrices.ipynb); [supplement index](../supplemental_material/README.md#figures) |
| Table 7: static and static–dynamic comparisons | [Paired comparisons](../6_discussion/significance-tests/README.md) |

Static overlap comprises 414 jointly correct, 128 FEA-only correct, 114 Image-only correct, and 100 jointly incorrect view cases. The prediction-selection oracle is 656/756 = 86.77%; it describes coverage by either unimodal prediction rather than a strict fusion ceiling.
