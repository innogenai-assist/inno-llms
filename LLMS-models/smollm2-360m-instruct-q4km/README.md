# SmolLM2 360M Instruct (`smollm2-360m-instruct-q4km`)

**Description:** Small and fast AI for lightweight on-device tasks.

## Model Overview
- **Parameters:** 360M
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `SmolLM2-360M-Instruct-Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** Apache-2.0
- **Categories:** Ultra-Lightweight-2-GB

## Hardware Requirements
- **RAM:** 2 GB
- **Storage:** 0.7 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Writing, Summarization

## Source & Upstream
- **Hugging Face Repo:** [bartowski/SmolLM2-360M-Instruct-GGUF](https://huggingface.co/bartowski/SmolLM2-360M-Instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/bartowski/SmolLM2-360M-Instruct-GGUF/resolve/main/SmolLM2-360M-Instruct-Q4_K_M.gguf)
- **SHA-256 Hash:** `2fa3f013dcdd7b99f9b237717fa0b12d75bbb89984cc1274be1471a465bac9c2`

## Running Locally with LLaMA.cpp
```bash
llama-server -m SmolLM2-360M-Instruct-Q4_K_M.gguf -c 8192
```
