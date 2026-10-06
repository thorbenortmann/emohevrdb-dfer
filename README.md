# EmoHeVRDB DFER

Code, saved experiment results, prediction exports, and analyses accompanying **Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB**, by Thorben Ortmann, Qi Wang, and Larissa Putzar.

The folders follow the submitted revised article. Static baselines provide the reference for the dynamic image, FEA, and multimodal experiments. FEA denotes the headset's facial expression activation coefficients.

## Navigate by paper section

| Paper section | Entry point | Contents |
|---|---|---|
| 3 — EmojiHeroVR and EmoHeVRDB | [Study and database](3_emojiherovr_and_emohevrdb/README.md) | Construction pipeline and links to the game, annotation procedure, participant splits, and benchmark subsets. |
| 4 — Static FER | [Static baselines](4_static_facial_expression_recognition/README.md) | Baseline sources, model downloads, static prediction collection, and the shared static CSV. |
| 5 — Dynamic FER | [Dynamic experiments](5_dynamic_facial_expression_recognition/README.md) | Image and FEA sequence models, optimized and unoptimized order controls, complementarity, and fusion. |
| 6 — Discussion | [Discussion analyses](6_discussion/README.md) | Model comparisons, temporal FEA analysis, fusion correctness groups, error-associated FEA profiles, and human annotation agreement. |
| Supplemental Material | [Supplement index](supplemental_material/README.md) | Confusion matrices and pointers to the analyses supporting supplemental figures and tables. |

Supplemental outputs are kept with their producing analyses where appropriate. The shared [confusion-matrix notebook](supplemental_material/confusion_matrices.ipynb) spans human ratings and static/dynamic baselines.

## Reading results and reproducing analyses

Start with the relevant section README, then open its notebooks, reports, and saved result tables. Prediction-based comparisons use two shared exports:

- [Static test predictions](4_static_facial_expression_recognition/static_test_predictions.csv), produced by [the static collector](4_static_facial_expression_recognition/collect_static_test_predictions.ipynb).
- [Dynamic test predictions](5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv), produced by [the dynamic collector](5_dynamic_facial_expression_recognition/collect_dynamic_test_predictions.ipynb).

Both exports contain the same 756 view-level sample IDs from 378 reenactments and eight test participants. `sample_id` identifies a camera view; `reenactment_id` links its central and side views. Image and Multimodal results use 756 view predictions. FEA results use 378 reenactment predictions; the CSV repeats each FEA prediction on both matching view rows for alignment. Deduplicate FEA rows when reporting its native sample counts. Class IDs follow `Anger, Disgust, Fear, Happiness, Neutral, Sadness, Surprise`.

Reusing these CSVs requires no model inference. Regenerating predictions or retraining requires the corresponding external datasets and model checkpoints. Follow each notebook's path configuration and execution instructions. Static inference uses the [TensorFlow 2.15 environment](4_static_facial_expression_recognition/env/README.md); the [root environment definitions](env/) support the dynamic experiments. Lightweight analysis notebooks list their own dependencies.

## Data and models

Obtain EmoHeVRDB through the [database repository's access instructions](https://github.com/thorbenortmann/emoji-hero-vr-database#request-access-to-emohevrdb). Use the published subsets:

| Subset | Input |
|---|---|
| SI | Static 224 × 224 RGB images from the central and side cameras. |
| SFEA | One synchronized 63-coefficient FEA vector per reenactment. |
| DI | Sequences of 30 RGB images per camera view. |
| DFEA | Sequences of 30 synchronized 63-coefficient FEA vectors per reenactment. |

SFEA and DFEA CSV exports supply the static and dynamic FEA inputs. Image and multimodal inference additionally use SI and DI, respectively. Set the external dataset paths in the relevant notebooks. Model download links are documented beside their experiments; static checkpoint links are in [Section 4's model links](4_static_facial_expression_recognition/models/put_static_models_here).

Labels describe posed facial-expression categories. Human raters judged one selected central-view reference image per reenactment; other views and modalities inherit that label. The paired views are not independent reenactments. FEAs are vendor-defined estimates rather than validated FACS action-unit measurements, and sequence positions are not annotated onset, apex, or offset phases.

## Related work and repositories

The study/database and static image baseline were introduced in [ACII 2024](https://doi.org/10.1109/ACII63134.2024.00014); the static FEA and multimodal baselines were reported in [AIxVR 2025](https://doi.org/10.1109/AIxVR63409.2025.00048). Their original implementations are maintained in [emoji-hero-vr-database](https://github.com/thorbenortmann/emoji-hero-vr-database) and [emohevrdb-sfer](https://github.com/thorbenortmann/emohevrdb-sfer).

`99_misc/`, when present on a revision or archive branch, contains historical exploratory analyses. Use the numbered sections and supplement index to reproduce the reported results.

## Citation and license

Please cite the article when using this code. The entry below identifies the submitted manuscript; replace it with the published bibliographic record when available.

```bibtex
@unpublished{ortmann2026dynamic,
  author = {Ortmann, Thorben and Wang, Qi and Putzar, Larissa},
  title  = {Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB},
  year   = {2026},
  note   = {Revised manuscript submitted to IEEE Transactions on Affective Computing, Special Issue 'Best of ACII 2024'}
}
```

See [LICENSE](LICENSE) for the code, documentation, and linked model files. EmoHeVRDB has separate access and usage terms described by the database repository.
