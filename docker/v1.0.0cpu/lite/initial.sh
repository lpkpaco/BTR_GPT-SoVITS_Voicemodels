#!/bin/bash
set -e
gptsovits="/demo/gpt-sovits/GPT_SoVITS/pretrained_models"
btr="/demo/active"
echo "=== GPT-SoVITS Docker Startup ==="
if [ ! -d "$gptsovits" ] || \
   [ "$(ls -A "$gptsovits" 2>/dev/null | grep -v '^\.gitignore$' | grep -v '^fast_langdetect$' | wc -l)" -eq 0 ]; then
    echo "  Downloading pt from HF"
    mkdir -p "$gptsovits"
    huggingface-cli download lj1995/GPT-SoVITS --local-dir "$gptsovits"
    mkdir -p /demo/gpt-sovits/GPT_SoVITS/pretrained_models/fast_langdetect
fi
if [ ! -d "$btr" ] || [ -z "$(ls -A "$btr" 2>/dev/null)" ]; then
    echo "BTR models not found. Downloading from HF."
    mkdir -p "$btr"
    huggingface-cli download lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models --include "lite/*" --local-dir /demo/temp
    shopt -s dotglob
    mv /demo/temp/lite/* "$btr/"
    rm -rf /demo/temp
fi
echo "Starting..."
exec python -u web_ui_spaces.py --host 0.0.0.0 --port 7860