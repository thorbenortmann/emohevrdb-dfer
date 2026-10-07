# EmoHeVRDB DFER

Code and saved results accompanying **Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB**, by Thorben Ortmann, Qi Wang, and Larissa Putzar.

The directories follow the article. Start with the section index below, then follow links to the producing notebook, saved report, or numerical table. FEA denotes the headset's facial expression activation coefficients.

## Paper-to-code navigation

| Reported content | Entry point |
| --- | --- |
| Section 3; Figure 2; Table 2: database construction and subsets | [EmojiHeroVR and EmoHeVRDB](3_emojiherovr_and_emohevrdb/README.md) |
| Section 4; Table 3: static baselines and complementarity counts | [Static FER](4_static_facial_expression_recognition/README.md) |
| Sections 5.1–5.2; Tables 4–5: dynamic unimodal results and sequence-order controls | [Dynamic FER](5_dynamic_facial_expression_recognition/README.md) |
| Section 5.3; Figures 3–4; Table 6: overlap and fusion | [Multimodal FER](5_dynamic_facial_expression_recognition/5_3_multimodal/README.md) |
| Section 6; Figure 5; Table 7: fusion outcomes, accuracy comparisons, and error interpretation | [Discussion analyses](6_discussion/README.md) |
| Figures S1–S7; Tables S1–S11 | [Supplemental Material](supplemental_material/README.md) |

Figure 1 and Table 1 are background illustration/reference material in the article, rather than notebook-generated results. AU names and FEA correspondences are indexed in supplemental Tables S1–S2.

## Shared predictions

- [Static test predictions](4_static_facial_expression_recognition/static_test_predictions.csv), produced by the [static collector](4_static_facial_expression_recognition/collect_static_test_predictions.ipynb).
- [Dynamic test predictions](5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv), produced by the [dynamic collector](5_dynamic_facial_expression_recognition/collect_dynamic_test_predictions.ipynb).

Each export contains 756 camera-view rows from the same 378 test reenactments and eight participants. `sample_id` identifies a view; `reenactment_id` links central and side views. Image and Multimodal metrics use both views. FEA metrics use one prediction per reenactment; its prediction is repeated on both view rows for alignment. Class IDs follow Anger, Disgust, Fear, Happiness, Neutral, Sadness, Surprise.

Prediction-based analyses can use these CSVs without model inference. Raw-FEA analyses require the external DFEA data. Retraining or regenerating predictions additionally requires the appropriate datasets and checkpoints.

## Setup and related repositories

- [Environment and dataset layout](env/README.md), including the separate static inference environment.
- [Static checkpoints](4_static_facial_expression_recognition/models/README.md) and [dynamic checkpoints](5_dynamic_facial_expression_recognition/models/README.md).
- [EmoHeVRDB access and construction](https://github.com/thorbenortmann/emoji-hero-vr-database), accompanying [ACII 2024](https://doi.org/10.1109/ACII63134.2024.00014).
- [Original static FEA and multimodal experiments](https://github.com/thorbenortmann/emohevrdb-sfer), accompanying [AIxVR 2025](https://doi.org/10.1109/AIxVR63409.2025.00048).

Labels describe posed expression categories. The paired views share a human-rated reference image and are not independent reenactments. FEAs are vendor-defined estimates, not validated FACS action-unit measurements.

## Citation and license

```bibtex
@unpublished{ortmann2026dynamic,
  author = {Ortmann, Thorben and Wang, Qi and Putzar, Larissa},
  title  = {Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB},
  year   = {2026},
  note   = {Revised manuscript submitted to IEEE Transactions on Affective Computing, Special Issue 'Best of ACII 2024'}
}
```

[LICENSE](LICENSE) covers the code, documentation, and linked models. The paper, dataset, and third-party assets have separate terms.
