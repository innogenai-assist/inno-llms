# Llama 3.2 1B Instruct (llama-3.2-1b-instruct-q4km)

**Description:** Efficient instruction-following AI for mobile devices.

## Model Overview
- **Parameters:** 1B
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `llama-3.2-1b-instruct-q4_k_m.gguf`
- **Thinking Mode:** No
- **License:** Llama 3.2 Community License
- **Categories:** Ultra-Lightweight-2-GB, Lightweight-3-GB

## Hardware Requirements
- **RAM:** 2 GB
- **Storage:** 1.5 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Coding, Writing, Summarization

## Source & Upstream
- **Hugging Face Repo:** [hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF](https://huggingface.co/hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.2-1b-instruct-q4_k_m.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m llama-3.2-1b-instruct-q4_k_m.gguf -c 8192
```
