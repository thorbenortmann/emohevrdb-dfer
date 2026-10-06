# Dynamic model checkpoints

[Up one level](../README.md) · [Repository README](../../README.md)

For [collect_dynamic_test_predictions.ipynb](../collect_dynamic_test_predictions.ipynb), download the models and save them in this directory with these exact filenames:

| Model | Local filename | Download |
| --- | --- | --- |
| Ordered Image | `image_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/16vcD4SpQOyqDomiMzXUgq8GjBWGX8buK/view?usp=sharing) |
| Ordered FEA | `fea_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/19mTZPnM31N70cwycBfKGOsrvAMYTWyUD/view?usp=sharing) |
| Multimodal, selected intermediate fusion | `multimodal_sequence_model.keras` | [Google Drive](https://drive.google.com/file/d/1dNZoqwNJYnBTb5M9x5xFGNW65CG4cYDD/view?usp=sharing) |

The `.keras` files are external to Git. The prediction CSV is already included, so these downloads are needed only for inference.

The [fusion model setup](../5_3_multimodal/README.md#model-setup) describes how to reuse the ordered checkpoints. Sequence-order collectors have separate model locations documented in their READMEs.
