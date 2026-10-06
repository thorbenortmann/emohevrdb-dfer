# 4. Static Facial Expression Recognition

[Repository home](../README.md)

This section provides the static Image, FEA, and Multimodal reference baselines summarized in Section 4 of the submitted article. Original training material remains in the [ACII 2024 database repository](https://github.com/thorbenortmann/emoji-hero-vr-database) and the [AIxVR 2025 static FER repository](https://github.com/thorbenortmann/emohevrdb-sfer). This folder collects their frozen models' aligned test predictions for reuse in the dynamic comparisons.

## Reported baselines

The results reproduce **main Table 3**. F1 is reported in percent; macro and support-weighted F1 coincide because each modality's test set is class-balanced.

| Modality | Model | Correct / test samples | Accuracy (%) | F1 (%) | Original training material |
|---|---|---:|---:|---:|---|
| Image | EfficientNet-B0 | 528 / 756 views | 69.84 | 70.06 | [Image baseline](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vii_baseline/b_training_c_results/emohevrdb) |
| FEA | Multilayer perceptron | 271 / 378 reenactments | 71.69 | 71.10 | [FEA baseline](https://github.com/thorbenortmann/emohevrdb-sfer/tree/main/iii_unimodal_facial_expression_recognition/b_c_training_results) |
| Multimodal | Intermediate fusion with cross-attention | 608 / 756 views | 80.42 | 80.22 | [Multimodal baseline](https://github.com/thorbenortmann/emohevrdb-sfer/tree/main/iv_multimodal_facial_expression_recognition/b_training_and_results) |

The FEA MLP has Dense layers of 128 and 64 units with ReLU activation and 0.2 dropout, followed by seven softmax outputs. The multimodal model combines frozen image and FEA feature extractors with cross-attention and a classification head.

## Files and outputs

| File or directory | Purpose |
|---|---|
| [collect_static_test_predictions.ipynb](collect_static_test_predictions.ipynb) | Load published SI/SFEA test data, run frozen static models, remap legacy class outputs, validate results, and export predictions. |
| [static_test_predictions.csv](static_test_predictions.csv) | Shared static prediction input for subsequent comparisons and analyses. |
| [models/put_static_models_here](models/put_static_models_here) | Checkpoint download links; the collector expects `image_model.keras`, `fea_model.keras`, and `multimodal_model.keras` in this directory. |
| [env/README.md](env/README.md) | TensorFlow 2.15 inference environment and Docker/Jupyter setup. |

The CSV has one row per image-view test sample: 756 rows from 378 reenactments and eight participants. `sample_id` identifies the view and `reenactment_id` links the two views. It contains metadata, predictions, and seven probabilities for each model. Its `image_path` column records the inference source location and is not needed by downstream prediction analyses. Raw FEA vectors are omitted.

The FEA prediction is repeated on the two view rows for alignment. Use one row per reenactment when computing FEA-native confusion matrices or sample counts: 54 test samples per class, versus 108 for Image/Multimodal. Canonical class IDs follow `Anger, Disgust, Fear, Happiness, Neutral, Sadness, Surprise`.

## Reproduce the prediction export

1. Obtain the published SI image test set and SFEA CSV test set through [the database access procedure](https://github.com/thorbenortmann/emoji-hero-vr-database#request-access-to-emohevrdb).
2. Download the three checkpoints and save them under `models/` as `image_model.keras`, `fea_model.keras`, and `multimodal_model.keras` (see [the model links](models/put_static_models_here)).
3. Start [the static environment](env/README.md), or use a compatible TensorFlow/Keras 2.15 environment.
4. Open the collector from this Section 4 directory. Its `MODEL_ROOT = Path('./models')` and CSV export are relative to the working directory. Set `DATASET_ROOT` to your mounted dataset location; the current default is `/workspace/datasets/emohevrdb`, containing `emoji-hero-vr-db-si/test_set/` and `emoji-hero-vr-db-sfea-as-csv/test_set.csv`.
5. Run all cells. Verify 528 correct Image predictions, 542 correct FEA view rows (equivalent to 271/378 reenactments), and 608 correct Multimodal predictions before replacing the shared CSV. The export is written as `static_test_predictions.csv` in the working directory.

No retraining is required. The collector preserves the legacy models' preprocessing and converts their output order (`Neutral, Happiness, Sadness, Surprise, Fear, Disgust, Anger`) to canonical order. Further scaling or class reordering changes the inputs or meaning of the saved predictions.

## Complementarity and downstream analyses

At the view level, the static unimodal correctness groups comprise **414 both correct**, **128 FEA-only correct**, **114 Image-only correct**, and **100 both incorrect**. Selecting a correct unimodal prediction whenever either is correct yields an oracle accuracy of **656/756 = 86.77%**. This measures prediction-selection potential, not a strict ceiling for a learned fusion model. These counts follow from the shared static CSV and are also saved in the linked Section 6.2 overlap table.

| Reported content | Analysis or output |
|---|---|
| Static class-wise precision, recall, and F1 — supplemental Table S3 | [Original baseline training reports](#reported-baselines); the shared CSV supports recomputation of class-wise metrics. |
| Static confusion matrices — supplemental Figure S2 | [Shared confusion-matrix notebook](../supplemental_material/confusion_matrices.ipynb) and [SI](../supplemental_material/figures/confusion_matrices/si.pdf), [SFEA](../supplemental_material/figures/confusion_matrices/sfea.pdf), [Multimodal](../supplemental_material/figures/confusion_matrices/smul.pdf) panels. |
| Static paired model comparisons — main Table 7 | [Static significance notebooks](../6_discussion/significance-tests/static-significance-tests/README.md). The paper reports FEA→Multimodal and Image→Multimodal; Image→FEA remains an additional repository comparison. |
| Static–dynamic comparisons — main Table 7 | [Static–dynamic comparison notebooks](../6_discussion/significance-tests/dynamic-significance-tests/README.md). |
| Change in static/dynamic correctness overlap — Section 6.2 | [Complementarity notebook](../6_discussion/6_2_complementarity/dynamic_fusion_correctness_groups.ipynb) and [overlap table](../6_discussion/6_2_complementarity/tables/static_dynamic_unimodal_overlap.csv). |

The static CSV is the common input to these prediction-based analyses; their producers and outputs remain beside their respective paper sections.
