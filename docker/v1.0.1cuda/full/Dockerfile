FROM nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update && apt-get install -y --no-install-recommends \
        python3.11-full \
        python3.11-dev \
        python3-pip \
        git curl ca-certificates ffmpeg \
        libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev \
        build-essential \
        cmake \
        ninja-build \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/bin/python3.11 /usr/bin/python \
    && ln -sf /usr/bin/python3.11 /usr/bin/python3 \
    && ln -sf /usr/bin/pip3 /usr/bin/pip \
    && python -m ensurepip --upgrade --default-pip \
    && python -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN curl -LsSf https://hf.co/cli/install.sh | bash
RUN useradd -m -u 1000 user
RUN git clone https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models.git  /demo && \
    rm -rf /demo/active && \
    pip install -U huggingface_hub && \
    hf download lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models --include "active/" --local-dir /demo
RUN git clone --depth 1 https://github.com/RVC-Boss/GPT-SoVITS.git /demo/gpt-sovits && \
    pip install --no-cache-dir --upgrade -r /demo/gpt-sovits/requirements.txt && \
    pip install --no-cache-dir pyopenjtalk && \
    python -c "import pyopenjtalk; pyopenjtalk._extract_dic()" && \
    pip install --no-cache-dir nltk && \
    python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger_eng punkt_tab cmudict && \
    hf download lj1995/GPT-SoVITS --local-dir /demo/gpt-sovits/GPT_SoVITS/pretrained_models && \
    mkdir -p /demo/gpt-sovits/GPT_SoVITS/pretrained_models/fast_langdetect && \
    rm -rf /demo/gpt-sovits/.git
RUN mkdir -p /demo && \
    chown -R 1000:1000 /demo && \
    chmod -R 777 /demo && \
    PY_PATH=$(python3 -c "import pyopenjtalk, os; print(os.path.dirname(pyopenjtalk.__file__))") && \
    chmod -R 777 "$PY_PATH"
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /demo
RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    pip install --upgrade gradio
RUN pip install --no-cache-dir --force-reinstall torch torchvision torchaudio torchcodec --index-url https://download.pytorch.org/whl/cu128
COPY --chown=user . /demo
EXPOSE 7860
CMD ["python", "-u", "web_ui_spaces_cuda.py", "--host", "0.0.0.0", "--port", "7860"]