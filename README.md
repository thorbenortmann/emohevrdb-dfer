# EmoHeVRDB DFER

Code, saved experiment runs, predictions, and analyses accompanying **Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB**, by Thorben Ortmann, Qi Wang, and Larissa Putzar.

The repository follows the revised article structure: the study and database are combined in Section 3, static FER is Section 4, dynamic FER is Section 5, and Discussion is Section 6. Documentation reflects the September 21, 2026 repository snapshot.

## Navigate by paper section

| Section | Entry point | Contents |
|---|---|---|
| 3 | [EmojiHeroVR and EmoHeVRDB](3_emojiherovr_and_emohevrdb/README.md) | Game, study, annotation, splits, and dataset construction; links to the original repository. |
| 4 | [Static facial expression recognition](4_static_facial_expression_recognition/README.md) | Original Image, FEA, and Multimodal baselines and current comparison analyses. |
| 5 | [Dynamic facial expression recognition](5_dynamic_facial_expression_recognition/README.md) | Model training, fusion variants, sequence-order ablations, prediction trajectories, and environment. |
| 6 | [Discussion analyses](6_discussion/README.md) | Significance tests, multimodal error analysis, FEA patterns, annotation agreement, and signal/prediction trajectories. |

Start with a section README and follow its experiment links. Each experiment points to its notebooks, saved reports, and relevant result files. Generated-output directories are linked directly and do not require additional README layers.

## Reading and running

- To **read results**, follow the report links in the experiment READMEs.
- To **inspect methods**, open the corresponding notebook; saved outputs document the supplied runs.
- To **rerun an analysis**, inspect its input paths and run it from its containing directory unless the notebook specifies otherwise. Prediction analysis can use existing CSVs; new inference or training requires the external datasets and model files.

Dynamic Image and Multimodal evaluation uses 756 view predictions from 378 reenactments; FEA evaluation uses one prediction per reenactment. Both views belong to the same reenactment. FEAs are vendor-defined coefficients, and sequence positions are not annotated onset/apex/offset phases.

## Related work and repositories

The journal contribution builds on [ACII 2024](https://doi.org/10.1109/ACII63134.2024.00014) and [AIxVR 2025](https://doi.org/10.1109/AIxVR63409.2025.00048). Inherited implementation material remains in [emoji-hero-vr-database](https://github.com/thorbenortmann/emoji-hero-vr-database) and [emohevrdb-sfer](https://github.com/thorbenortmann/emohevrdb-sfer).

## Referencing

If you reference this repository or use the code, please cite the journal paper:

```bibtex
@unpublished{ortmann2026dynamic,
  author       = {Ortmann, Thorben and Wang, Qi and Putzar, Larissa},
  title        = {Dynamic Facial Expression Recognition under Partial Occlusion by Head-Mounted Displays on EmoHeVRDB},
  year         = {2026},
  note         = {Invited submission to the Special Issue 'Best of ACII 2024' of IEEE Transactions on Affective Computing. Under review}
}
```
