# 3. EmojiHeroVR and EmoHeVRDB

[Repository home](../README.md)

This section documents the study and database construction summarized in Section 3 of the submitted article. The original game, annotation tools, split procedure, and subset-construction code are maintained in [emoji-hero-vr-database](https://github.com/thorbenortmann/emoji-hero-vr-database), accompanying [ACII 2024](https://doi.org/10.1109/ACII63134.2024.00014).

## Construction pipeline

[pipeline.pdf](pipeline.pdf) is the construction overview used in **main Figure 2**. [pipeline.drawio](pipeline.drawio) is its editable source.

37 participants posed seven expression categories during EmojiHeroVR, producing 2,590 prompted reenactments. Two external cameras recorded central and 45° side views, while the Meta Quest Pro supplied 63 FEA coefficients. FEA recordings were unavailable for one participant.

For each reenactment, the in-game FER model selected a central-view reference image for human annotation. Three raters independently labeled that image, without seeing the prompt. Retaining cases in which at least two raters assigned the prompted category yielded 1,921 reenactments. Participant-disjoint splitting and class balancing of validation/test data then yielded 1,778 reference images. All derived views and subsets inherit their reference image's category and split assignment.

## Implementation and source data

| Topic | Source |
|---|---|
| EmojiHeroVR game | [Game implementation](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/iii_study_preparation/a_the_game_emojiherovr) |
| In-game FER | [Model implementation](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/iii_study_preparation/b_facial_expression_recognition_model) |
| Annotation procedure and results | [Human annotation](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/v_data_annotation), including [the master annotation table](https://github.com/thorbenortmann/emoji-hero-vr-database/blob/main/v_data_annotation/b_results/labels-master-table-analysis_irr.csv) |
| Participant-disjoint splits | [Split construction](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vi_database_construction/a_training_validation_and_test_split) |
| Benchmark subsets and statistics | [Subset construction](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vi_database_construction/b_construction_and_statistics) |
| Dataset access | [Access instructions](https://github.com/thorbenortmann/emoji-hero-vr-database#request-access-to-emohevrdb) |

## Benchmark subsets

The sizes below reproduce **main Table 2**. SI/DI counts are camera-view samples; SFEA/DFEA counts are reenactments.

| Subset | Sample unit | Training | Validation | Test | Total |
|---|---|---:|---:|---:|---:|
| SI | One 224 × 224 RGB image | 2,030 | 770 | 756 | 3,556 |
| SFEA | One 63-coefficient FEA vector | 964 | 385 | 378 | 1,727 |
| DI | One sequence of 30 RGB images | 2,030 | 770 | 756 | 3,556 |
| DFEA | One sequence of 30 FEA vectors | 964 | 385 | 378 | 1,727 |

Each FEA sample is synchronized with one central and one side camera-view sample. Missing face-tracking data affect the training set: 964 FEA reenactments versus 1,015 image-reference reenactments. Validation and test contain 55 and 54 reenactments per class, respectively. The test participants are shared across static and dynamic evaluation.

The reference image is a model-selected annotation candidate, not an independently verified apex frame. DI/DFEA sequences cover approximately one second and are not explicitly aligned to expression phases. FEAs are proprietary facial-movement estimates rather than validated action-unit measurements.

## Analyses in this repository

- [Human-rater confusion matrices](../supplemental_material/confusion_matrices.ipynb) support **supplemental Figure S1**.
- [Human agreement and multimodal errors](../6_discussion/6_3_interpreting/analyze_label_agreement_and_model_errors.ipynb) support the annotation-agreement paragraph in Section 6.3; its local annotation CSV is [here](../6_discussion/6_3_interpreting/labels-master-table-analysis_irr.csv).
- [Static FER](../4_static_facial_expression_recognition/README.md) uses SI/SFEA; [dynamic FER](../5_dynamic_facial_expression_recognition/README.md) uses DI/DFEA.

Dataset-construction details remain in the original repository. This folder holds the article's pipeline figure and navigation to those sources.
