# EmoHeVRDB-SFER TensorFlow 2.15 environment

[Up one level](../README.md) · [Repository home](../../../../README.md)

This folder provides a Windows/Docker setup for reproducing the original
TensorFlow 2.15 environment used by the static EmoHeVRDB-SFER experiments.
It follows the container/Jupyter workflow used in `emohevrdb-dfer`, while
keeping the static experiments on their original TensorFlow/Keras generation.

## Base image

The image is based on:

```text
tensorflow/tensorflow:2.15.0.post1-gpu-jupyter
```

This gives a Linux GPU environment with TensorFlow 2.15.0.post1 and Python
3.11, matching the original SFER `tf215` environment much more closely than
the newer DFER/NVIDIA container.

The directly specified package versions from the original SFER
`environment.yml` are installed on top:

- TensorFlow 2.15.0.post1
- JupyterLab 4.0.12
- NumPy 1.26.4
- Matplotlib 3.7.5
- scikit-learn 1.3.2
- seaborn 0.13.2

## Host directory layout

The Compose file deliberately does not encode machine-specific CPU or memory
limits. It mounts three configurable Windows directories:

```text
<repo>      -> /workspace/emohevrdb-sfer
<datasets>  -> /workspace/datasets
<models>    -> /workspace/models
```

This lets the new static prediction notebook use the same style as the DFER
notebooks, e.g. `Path('/workspace/datasets')`, regardless of the Windows drive
letters or local directory names.

`DATASETS_PATH` can point to the parent directory containing the current
published EmoHeVRDB subsets. The prediction notebook can therefore align the
same static samples from the current `EmoHeVRDB-SI` / `EmoHeVRDB-SFEA`
representation rather than relying on the older `emoji-hero-multimodal`
layout. The expected published model results should be used as the validation
check after adapting the paths/sample identifiers.

## Setup on Windows

Prerequisites:

- Docker Desktop using the WSL2 backend
- a working NVIDIA driver
- NVIDIA GPU access from Docker

First verify GPU access from Docker in PowerShell:

```powershell
docker run --rm --gpus all nvidia/cuda:12.3.2-base-ubuntu22.04 nvidia-smi
```

Then place this `env` folder where you want to keep the environment definition,
copy `.env.example` to `.env`, and edit the three paths. Use forward slashes,
for example:

```text
SFER_REPO_PATH=D:/workspace/repos/emohevrdb-sfer
DATASETS_PATH=D:/workspace/datasets
MODELS_PATH=D:/workspace/models
```

Build the image:

```powershell
docker compose build
```

Start JupyterLab:

```powershell
docker compose up
```

The console prints a Jupyter URL containing the access token. Open the URL on
Windows. The complete `/workspace` tree is available from JupyterLab.

To stop the environment:

```powershell
docker compose down
```

## Verify the environment

With the container running, execute:

```powershell
docker compose exec tf215 python /workspace/emohevrdb-sfer/env/verify_environment.py
```

and/or

```powershell
docker compose exec tf215 pip show tensorflow
```

 A successful check should report TensorFlow
`2.15.0.post1`, the pinned package versions, and at least one visible GPU.

You can also verify directly from a notebook:

```python
import tensorflow as tf
print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))
```

## Suggested use for the static prediction extraction

1. Use the current published static subset files under `/workspace/datasets`.
2. Adapt the sample/path parsing analogously to the DFER complementarity
   notebook so that static image views and FEAs are aligned by their common
   sample identifiers.
3. Load the frozen image, FEA, and static multimodal models from
   `/workspace/models` (or adjust that path once in the notebook).
4. Before exporting any per-sample predictions, reproduce the expected static
   test results. This validates both the environment and the new path/sample
   mapping.
5. Only then add identifiers, predictions, probabilities, and CSV export.

## Notes

- The container is intentionally separate from the DFER environment. DFER uses
  a newer TensorFlow/Keras stack, whereas these saved static models were created
  with TensorFlow/Keras 2.15.
- No training is required for the planned prediction extraction. The GPU is
  mainly useful for quickly reproducing inference results and loading the image
  and multimodal models.
- Do not change model serialization formats before first confirming the original
  expected test results.
