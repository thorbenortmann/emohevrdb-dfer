# Dynamic Model Checkpoints

[Section 5](../README.md)

The [dynamic collector](../collect_dynamic_test_predictions.ipynb) expects these checkpoints in this directory:

| Model | Local filename | Download |
| --- | --- | --- |
| Ordered Image | `image_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/16vcD4SpQOyqDomiMzXUgq8GjBWGX8buK/view?usp=sharing) |
| Ordered FEA | `fea_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/19mTZPnM31N70cwycBfKGOsrvAMYTWyUD/view?usp=sharing) |
| Multimodal, selected intermediate fusion | `multimodal_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/1dNZoqwNJYnBTb5M9x5xFGNW65CG4cYDD/view?usp=sharing) |


Model files are external to Git. The included prediction CSV supports analyses without these downloads. [Fusion setup](../5_3_multimodal/README.md#model-setup) describes reuse of the ordered checkpoints; sequence-order collectors document their own locations and filenames.
