# SmolLM2 360M Instruct (smollm2-360m-instruct-q4km)

**Description:** Small and fast AI for lightweight on-device tasks.

## Model Overview
- **Parameters:** 360M
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `smollm2-360m-instruct-q4_k_m.gguf`
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
- **Hugging Face Repo:** [mfuntowicz/SmolLM2-360M-Instruct-Q4_K_M-GGUF](https://huggingface.co/mfuntowicz/SmolLM2-360M-Instruct-Q4_K_M-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/mfuntowicz/SmolLM2-360M-Instruct-Q4_K_M-GGUF/resolve/main/smollm2-360m-instruct-q4_k_m.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m smollm2-360m-instruct-q4_k_m.gguf -c 8192
```
