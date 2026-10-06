# Static inference environment

[Section 4](../README.md) · [Repository home](../../README.md)

This Docker environment runs the static prediction collector with the legacy TensorFlow/Keras 2.15 model stack. The dynamic experiments use the repository's root `env/` directory.

The [Dockerfile](Dockerfile) uses `tensorflow/tensorflow:2.15.0.post1-gpu-jupyter`. [requirements.txt](requirements.txt) specifies the additional package versions: JupyterLab 4.0.13, NumPy 1.26.4, pandas 2.3.3, Matplotlib 3.7.5, scikit-learn 1.7.2, SciPy 1.15.3, Seaborn 0.13.2, and statsmodels 0.14.6. These are the supplied inference-environment pins, rather than an exact copy of every original training dependency.

## Repository and dataset locations

The host directories are set directly in the `volumes` entries of [compose.yml](compose.yml):

```yaml
volumes:
  - /home/thorben/workspace/repos:/workspace/repos
  - /home/thorben/workspace/datasets:/workspace/datasets
```

The path before each colon is the directory on the host computer; the path after it is its location inside the container. This mounts the repositories parent directory, so this repository is available as `/workspace/repos/emohevrdb-dfer` when its host folder has that name.

To use different host directories, edit the paths on the left side of these volume entries directly in `compose.yml`. For example, on Windows they could be `D:/workspace/repos` and `D:/workspace/datasets`. Keeping the container paths on the right side preserves the notebook's `/workspace` layout. If you change the container dataset path too, update the notebook's `DATASET_ROOT` accordingly.

The current collector defaults to `DATASET_ROOT = Path('/workspace/datasets/emohevrdb')`. This corresponds to `/home/thorben/workspace/datasets/emohevrdb` with the supplied mounts. That directory should contain:

- `emoji-hero-vr-db-si/test_set/` — the published SI test images;
- `emoji-hero-vr-db-sfea-as-csv/test_set.csv` — the published SFEA test vectors.

Place the static checkpoints in `4_static_facial_expression_recognition/models/` as `image_model.keras`, `fea_model.keras`, and `multimodal_model.keras`. The existing download links are in [models/put_static_models_here](../models/put_static_models_here). The collector uses the relative `./models` path and exports `static_test_predictions.csv` to its working directory, so run it from the Section 4 directory.

## Build and run

Use Docker Compose with NVIDIA GPU support. On Windows, use Docker Desktop's WSL2 backend and an NVIDIA driver. The supplied configuration selects GPU device `0`; edit its device setting if your machine requires another GPU.

From `4_static_facial_expression_recognition/env/`, run:

```bash
docker compose build
docker compose up
```

Open the Jupyter URL printed by the container, navigate to the static prediction collector under `/workspace/repos/emohevrdb-dfer/4_static_facial_expression_recognition/`, and run its cells in order. The Compose configuration exposes port 8888 and starts JupyterLab with `/workspace` as its root directory.

Check TensorFlow and GPU visibility directly in the notebook:

```python
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))
```

Installed TensorFlow metadata can also be inspected with `docker compose exec tf215 pip show tensorflow`. Stop the environment with `docker compose down`.

## Prediction validation

No retraining is required. The collector loads the frozen checkpoints, supplies the custom CrossAttention layer for the multimodal model, remaps the legacy class order, and checks these expected results before export:

| Model | Correct predictions | Accuracy |
|---|---:|---:|
| Image | 528 / 756 views | 69.84% |
| FEA | 542 / 756 duplicated view rows, equivalent to 271 / 378 reenactments | 71.69% |
| Multimodal | 608 / 756 views | 80.42% |

The saved prediction CSV can be used by downstream analyses without building this container. This environment is needed when regenerating predictions from the static checkpoints.
