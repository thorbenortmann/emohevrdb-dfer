# 3. EmojiHeroVR and EmoHeVRDB

[Repository README](../README.md)

The game, annotation tools, participant splits, and subset-construction code are maintained in [emoji-hero-vr-database](https://github.com/thorbenortmann/emoji-hero-vr-database).

## Paper outputs and sources

| Content | Source |
| --- | --- |
| Figure 2: database construction pipeline | [pipeline.pdf](pipeline.pdf); editable [pipeline.drawio](pipeline.drawio) |
| Study/game implementation | [EmojiHeroVR](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/iii_study_preparation/a_the_game_emojiherovr) and [in-game FER](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/iii_study_preparation/b_facial_expression_recognition_model) |
| Annotation counts and agreement | [Annotation results](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/v_data_annotation) |
| Participant-disjoint split | [Split construction](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vi_database_construction/a_training_validation_and_test_split) |
| Table 2: benchmark subset sizes | [Subset construction and statistics](https://github.com/thorbenortmann/emoji-hero-vr-database/tree/main/vi_database_construction/b_construction_and_statistics) |
| Figure S1: human-rater matrices | [Confusion-matrix notebook](../supplemental_material/confusion_matrices.ipynb) |

The study produced 2,590 prompted reenactments from 37 participants. Agreement-based filtering retained 1,921; participant splitting and validation/test balancing yielded 1,778 reference images. One participant had no FEA recordings, leaving 1,727 FEA reenactments. Three raters labeled each selected central-view image; corresponding views and modalities inherit its category and split.

## Benchmark subsets — Table 2

| Subset | Input per sample | Training | Validation | Test | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| SI | One 224 × 224 RGB image | 2,030 | 770 | 756 | 3,556 |
| SFEA | One 63-coefficient vector | 964 | 385 | 378 | 1,727 |
| DI | 30 RGB frames | 2,030 | 770 | 756 | 3,556 |
| DFEA | 30 observations of 63 coefficients | 964 | 385 | 378 | 1,727 |

SI/DI counts are camera-view samples; SFEA/DFEA counts are reenactments. Each FEA sample pairs with central and side images. Validation and test contain 55 and 54 reenactments per category, respectively.

[Section 4](../4_static_facial_expression_recognition/README.md) uses SI/SFEA; [Section 5](../5_dynamic_facial_expression_recognition/README.md) uses DI/DFEA. [Section 6.3](../6_discussion/6_3_interpreting/README.md) joins annotations to model predictions. Dataset access and placement are documented in [the environment README](../env/README.md).

Reference images are model-selected annotation candidates, not verified apex frames. Sequences cover approximately one second without annotated onset/apex/offset alignment.
