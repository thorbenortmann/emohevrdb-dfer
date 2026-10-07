FROM tensorflow/tensorflow:2.15.0.post1-gpu-jupyter

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt

# Keep the TensorFlow 2.15.0.post1 stack from the original 
# - https://github.com/thorbenortmann/emoji-hero-vr-database
# - https://github.com/thorbenortmann/emohevrdb-sfer
# repositories.
# Exact environments:
# https://github.com/thorbenortmann/emoji-hero-vr-database/blob/main/vii_baseline/b_training_c_results/environment.yml
# https://github.com/thorbenortmann/emohevrdb-sfer/blob/main/iii_unimodal_facial_expression_recognition/b_c_training_results/tensorflow/environment.yml
# https://github.com/thorbenortmann/emohevrdb-sfer/blob/main/iv_multimodal_facial_expression_recognition/b_training_and_results/environment.yml

RUN python -m pip install --no-cache-dir \
    --upgrade-strategy only-if-needed \
    -r /tmp/requirements.txt

EXPOSE 8888

CMD ["bash"]
