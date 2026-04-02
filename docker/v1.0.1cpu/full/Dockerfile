FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
RUN apt-get update && apt-get install -y ffmpeg libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev git curl ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://hf.co/cli/install.sh | bash

RUN useradd -m -u 1000 user

RUN pip install --no-cache-dir torch==2.4.1+cpu torchvision==0.19.1+cpu torchaudio==2.4.1+cpu torchcodec --index-url https://download.pytorch.org/whl/cpu

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
    rm -rf /demo/gpt-sovits/.git && \
    pip install --no-cache-dir --force-reinstall onnxruntime && \
    pip install --no-cache-dir torch==2.4.1+cpu torchvision==0.19.1+cpu torchaudio==2.4.1+cpu torchcodec --index-url https://download.pytorch.org/whl/cpu


#RUN git clone https://github.com/RVC-Boss/GPT-SoVITS.git /demo/gpt-sovits
#WORKDIR /demo/gpt-sovits
#RUN pip install --no-cache-dir --upgrade -r requirements.txt
#RUN pip install --no-cache-dir pyopenjtalk
#RUN python -c "import pyopenjtalk; pyopenjtalk._extract_dic()"
#RUN pip install --no-cache-dir nltk
#RUN python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger_eng punkt_tab cmudict
#RUN hf download lj1995/GPT-SoVITS --local-dir /demo/gpt-sovits/GPT_SoVITS/pretrained_models
#RUN mkdir -p /demo/gpt-sovits/GPT_SoVITS/pretrained_models/fast_langdetect
#this is for triggering rebuild
    

USER root
RUN mkdir -p /demo && chmod -R 777 /demo && \
chown -R 1000:1000 /demo && \
chmod -R 777 /usr/local/lib/python3.11/site-packages/pyopenjtalk
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /demo
#COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    pip install --upgrade gradio
COPY --chown=user . /demo

EXPOSE 7860

CMD ["python", "-u", "ui.py", "--host", "0.0.0.0", "--port", "7860"]