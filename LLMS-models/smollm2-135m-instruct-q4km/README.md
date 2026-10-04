# SmolLM2 135M Instruct (`smollm2-135m-instruct-q4km`)

**Description:** Ultra-lightweight AI for basic on-device tasks.

## Model Overview
- **Parameters:** 135M
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `SmolLM2-135M-Instruct-Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** Apache-2.0
- **Categories:** Ultra-Lightweight-2-GB

## Hardware Requirements
- **RAM:** 2 GB
- **Storage:** 0.5 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Writing, Summarization

## Source & Upstream
- **Hugging Face Repo:** [bartowski/SmolLM2-135M-Instruct-GGUF](https://huggingface.co/bartowski/SmolLM2-135M-Instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/bartowski/SmolLM2-135M-Instruct-GGUF/resolve/main/SmolLM2-135M-Instruct-Q4_K_M.gguf)
- **SHA-256 Hash:** `2e8040ceae7815abe0dcb3540b9995eaa1fa0d2ca9e797d0a635ae4433c68c2d`

## Running Locally with LLaMA.cpp
```bash
llama-server -m SmolLM2-135M-Instruct-Q4_K_M.gguf -c 8192
```
