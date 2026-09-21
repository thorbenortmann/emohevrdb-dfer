# Dynamic FER environment

[Up one level](../README.md) · [Repository home](../../README.md)

This directory contains the existing environment definitions used by the dynamic FER workflow.

- [Dockerfile](Dockerfile): NVIDIA TensorFlow base image and dependency installation.
- [requirements.txt](requirements.txt): additional Python dependencies.
- [compose.yml](compose.yml): container, GPU, mounts, resource settings, and Jupyter command.
- [filter_logs.sh](filter_logs.sh): log filter used by the Jupyter launch command.

Before using Compose, adapt its existing host mounts and container paths to your checkout. The supplied configuration still uses the original `emoji_hero_vr_dfer` mount and an absolute path to `filter_logs.sh`; these need to resolve in your environment. Check each notebook's dataset/model paths and launch analyses from their containing directories when they use relative paths.

The [static prediction environment](../../6_discussion/significance-tests/static-significance-tests/env/README.md) is documented separately. Saved CSV analysis and report reading do not require rerunning model inference.
