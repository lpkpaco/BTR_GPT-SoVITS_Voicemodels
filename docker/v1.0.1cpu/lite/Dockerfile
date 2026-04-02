FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
RUN apt-get update && apt-get install -y ffmpeg libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev git curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://hf.co/cli/install.sh | bash

RUN useradd -m -u 1000 user

RUN pip install --no-cache-dir torch==2.4.1+cpu torchvision==0.19.1+cpu torchaudio==2.4.1+cpu torchcodec --index-url https://download.pytorch.org/whl/cpu

RUN git clone https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models.git  /demo && rm -rf /demo/active


RUN git clone --depth 1 https://github.com/RVC-Boss/GPT-SoVITS.git /demo/gpt-sovits && \
    pip install --no-cache-dir --upgrade -r /demo/gpt-sovits/requirements.txt && \
    pip install --no-cache-dir pyopenjtalk && \
    python -c "import pyopenjtalk; pyopenjtalk._extract_dic()" && \
    pip install --no-cache-dir nltk && \
    python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger_eng punkt_tab cmudict && \
    rm -rf /demo/gpt-sovits/.git && \
    pip install --no-cache-dir --force-reinstall onnxruntime && \
    pip install --no-cache-dir torch==2.4.1+cpu torchvision==0.19.1+cpu torchaudio==2.4.1+cpu torchcodec --index-url https://download.pytorch.org/whl/cpu

USER root
RUN mkdir -p /demo && chmod -R 777 /demo && \
chown -R 1000:1000 /demo && \
chmod -R 777 /usr/local/lib/python3.11/site-packages/pyopenjtalk
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /demo
RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    pip install --upgrade gradio
COPY --chown=user . /demo

EXPOSE 7860

COPY --chown=user initial.sh /demo/initial.sh
RUN chmod +x /demo/initial.sh

CMD ["/demo/initial.sh"]