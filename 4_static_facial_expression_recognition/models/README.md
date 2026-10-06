# Static model checkpoints

[Section 4](../README.md) · [Repository home](../../README.md)

Download the three linked static checkpoints and save them in this directory with the following filenames. These are the links previously supplied in `put_static_models_here`.

| Model | Required local filename | Download |
|---|---|---|
| Image — EfficientNet-B0 | `image_model.keras` | [Google Drive](https://drive.google.com/file/d/1dWeQEf4VkhsVXUWwITMN09Ya-cBVsuNY/view?usp=sharing) |
| FEA — MLP | `fea_model.keras` | [Google Drive](https://drive.google.com/file/d/1Pbd3CRPjY2B_jn9ilHyEGZ10RkNgzV4L/view?usp=sharing) |
| Multimodal — intermediate cross-attention fusion | `multimodal_model.keras` | [Google Drive](https://drive.google.com/file/d/1qqxmZ4NNWb1bqEZ73BL4SSt-I0v-M1R0/view?usp=sharing) |

The prediction collector loads these models with `compile=False` in the static TensorFlow/Keras 2.15 environment and supplies the custom `CrossAttention` layer for the multimodal checkpoint. Model outputs use the legacy class order and are remapped by the collector before export.

Expected test results are 528/756 Image, 271/378 FEA, and 608/756 Multimodal correct predictions. Validate these counts before replacing `static_test_predictions.csv`. Checkpoint files are excluded from Git by the repository's `*.keras` rule.
