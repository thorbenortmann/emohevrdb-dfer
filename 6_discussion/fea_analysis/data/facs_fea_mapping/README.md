# FACS–FEA mapping for EmoHeVRDB

Version **1.2.1** — 2026-09-20

This directory contains a project-canonical **semantic crosswalk** between the 63 facial expression activation (FEA) channels used by EmoHeVRDB and movements described by the Facial Action Coding System (FACS), plus a paper-specific mapping for the Action Units (AUs) listed in the current manuscript's Table 1.

## Files

- `fea_to_facs_all_63.csv` — one row for each of the 63 EmoHeVRDB FEA channels.
- `paper_aus_to_fea.csv` — one row for each of the 20 unique AUs occurring in the manuscript's Table 1, including upper/lower-face assignment, expression categories, and corresponding FEA channels.
- `facs_fea_mapping.json` — structured representation of both views, source metadata, reverse mappings, coverage summaries, and caveats.

## Scope

EmoHeVRDB was recorded with the Meta XR Core SDK Face Tracking API, version 59.0. The 63 stored feature names and their order match the 63-entry `XrFaceExpressionFB` enum of the OpenXR `XR_FB_face_tracking` extension (indices 0–62). The supplied repository snapshot also contains saved static and dynamic test-set notebook outputs showing the same 63 features in the same order.

Newer Meta SDK references expose additional tongue-related expressions. Those newer channels are **not** part of EmoHeVRDB and are intentionally excluded from this mapping.

## Naming conventions

The same face-expression channel appears under several official identifiers depending on the API layer. This project keeps the short **PascalCase** name as its canonical identifier because it matches both the existing EmoHeVRDB feature columns and the public Unity `OVRFaceExpressions.FaceExpression` enum member.

For example, the same channel is represented as:

| Layer | Identifier |
| --- | --- |
| EmoHeVRDB / canonical project key | `BrowLowererL` |
| Meta Unity API member | `OVRFaceExpressions.FaceExpression.BrowLowererL` |
| Meta lower-level plugin value | `OVRPlugin.FaceExpression2.Brow_Lowerer_L` |
| OpenXR enum constant | `XR_FACE_EXPRESSION_BROW_LOWERER_L_FB` |

Meta's current Unity documentation explicitly defines the PascalCase member in terms of the underscore-separated lower-level value (for example, `BrowLowererL = OVRPlugin.FaceExpression2.Brow_Lowerer_L`). Thus, the two Meta spellings are not competing names invented by this project; they refer to different API layers.

Accordingly:

- `fea_name` remains the stable key used in EmoHeVRDB CSVs, analysis code, and the mapping tables.
- `meta_unity_member`, `meta_plugin_value`, and `openxr_enum` are provided as explicit aliases in `fea_to_facs_all_63.csv` and `facs_fea_mapping.json`.
- The paper and supplementary tables should normally use the compact PascalCase form in code font (for example, `BrowLowererL`) unless the API layer itself is being discussed.
- The underscore-separated Meta form should be used when referring specifically to `OVRPlugin.FaceExpression2`.
- The `XR_FACE_EXPRESSION_*_FB` form should be used when referring specifically to the OpenXR `XrFaceExpressionFB` enum.

The current Meta documentation contains additional tongue-related expressions. They are outside the scope of EmoHeVRDB's 63-channel schema and therefore do not receive project keys in these files.

## Interpretation

This mapping must **not** be read as an official Meta-to-FACS conversion or as evidence that a Meta coefficient is a validated FACS measurement. Meta describes its expression enum as FACS-based, but the API exposes vendor-defined blendshape coefficients intended primarily to drive facial animation. The mapping here therefore uses movement-name and movement-description correspondence only.

In particular:

- FEA coefficients are not converted into FACS occurrence labels or FACS A–E intensity scores.
- Left/right and quadrant-specific Meta channels remain separate; no averaging, summation, threshold, or maximum rule is defined here.
- `ChinRaiserB/T`, the four `LipFunneler*` channels, and the four `LipSuck*` channels are treated as API components of a single AU-related movement.
- `JawThrust`, `JawSideways*`, `CheekPuff*`, and `CheekSuck*` are mapped to FACS **Action Descriptors** (AD29, AD30, AD34, AD35), not to muscle-based AUs.
- `EyesLookLeft/Right/Up/Down*` are linked conservatively to FACS eye-position codes 61–64. They are not treated as calibrated gaze measurements.
- `MouthLeft` and `MouthRight` remain without a unique single FACS code.
- `EyesClosedL/R` are linked semantically to AU43. Current Meta documentation also notes that `EyesClosed` and `EyesLookDown` coefficients can interact when eye-following blendshapes are valid, which is another reason not to interpret the raw value as a validated AU43 intensity.

## Paper-specific AU mapping

The current manuscript table contains **20 unique AUs** across anger, disgust, fear, happiness, sadness, and surprise. Of these, **17 have at least one dedicated semantic FEA correspondence** in the 63-channel schema. Three do not:

- **AU11 — Nasolabial Deepener**
- **AU25 — Lips Part**
- **AU27 — Mouth Stretch**

For AU25 and AU27, the absence of a dedicated channel should be preserved explicitly. `JawDrop` must not be used as a validated substitute for AU27, and `1 - LipsToward` must not be used as a validated AU25 measure. FACS 2002 explicitly distinguishes AU25, AU26, and AU27.

The expression-category and upper/lower-face assignments in `paper_aus_to_fea.csv` reproduce the current manuscript's Table 1. They describe AUs involved across alternative typical configurations; they do not imply that every listed AU must occur in every display of that category.

## FACS-version notes

The crosswalk is intended to use **FACS 2002** terminology. Historical sources can be misleading for the eye region. In FACS 2002, the former 1978 AU41 and AU42 eyelid-lowering actions were folded into degrees of AU43, and the former AU44 squint action was folded into AU7. The files therefore do not introduce separate AU41/AU42/AU44 mappings for Meta eye channels.

## Sources

1. Meta Horizon OS Developers, *Face Tracking for Movement SDK for Unity*:  
   https://developers.meta.com/horizon/documentation/unity/move-face-tracking/
2. Meta Horizon OS Developers, *OVRFaceExpressions reference (Unity SDK v205)*:  
   https://developers.meta.com/horizon/reference/unity/v205/class_o_v_r_face_expressions/
3. Khronos OpenXR, *XrFaceExpressionFB*:  
   https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrFaceExpressionFB.html
4. J. F. Cohn, Z. Ambadar, and P. Ekman, *Observer-Based Measurement of Facial Expression with the Facial Action Coding System* (2007):  
   https://www.jeffcohn.net/wp-content/uploads/2020/01/Cohn-chapter-2007.pdf
5. Correia-Caeiro et al., *CalliFACS: The common marmoset Facial Action Coding System* (used only as a peer-reviewed secondary cross-check for human Action Descriptor labels):  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC9113598/
6. Historical CMU FACS reference (used only as a historical code/name cross-check):  
   https://www.cs.cmu.edu/~face/facs.htm
7. Ekman, Friesen, and Hager, *Facial Action Coding System, Investigator's Guide* (2002), especially Table 10-1 for the manuscript's emotion-category AU table.

## Repository cross-check

The supplied `2026-09-20-emohevrdb-dfer` snapshot was checked at the two saved prediction-collection notebooks:

- `6_discussion/significance-tests/static-significance-tests/collect_static_test_predictions.ipynb`
- `6_discussion/significance-tests/dynamic-significance-tests/collect_dynamic_test_predictions.ipynb`

Both saved outputs contain exactly 63 FEA columns in the same order as `fea_to_facs_all_63.csv`.

This is a schema consistency check only. It does not independently validate Meta's per-channel tracking accuracy or establish numerical equivalence between FEAs and FACS coding.
