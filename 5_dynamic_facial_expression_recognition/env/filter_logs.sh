#!/usr/bin/env bash
# Reads STDERR from TensorFlow/Jupyter and removes logging spam.

set -o pipefail

# read from stdin line by line
while IFS= read -r line; do
  case "$line" in
    *"ptx85' is not a recognized feature for this target"*)
      continue
      ;;
    *"ptx85"*)
      continue
      ;;
    *"successful NUMA node read from SysFS had negative value (-1)"*)
      continue
      ;;
    *"Skipping the delay kernel, measurement accuracy will be reduced"*)
      continue
      ;;
  esac

  # if we didn't continue: print the line
  printf '%s\n' "$line"
done
