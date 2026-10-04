# SmolLM2 1.7B Instruct (`smollm2-1.7b-instruct-q4km`)

**Description:** Small instruction model optimized for local inference.

## Model Overview
- **Parameters:** 1.7B
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `smollm2-1.7b-instruct-q4_k_m.gguf`
- **Thinking Mode:** No
- **License:** Apache-2.0
- **Categories:** Lightweight-3-GB

## Hardware Requirements
- **RAM:** 3 GB
- **Storage:** 2 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Coding, Writing, Summarization

## Source & Upstream
- **Hugging Face Repo:** [HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF/resolve/main/smollm2-1.7b-instruct-q4_k_m.gguf)
- **SHA-256 Hash:** `decd2598bc2c8ed08c19adc3c8fdd461ee19ed5708679d1c54ef54a5a30d4f33`

## Running Locally with LLaMA.cpp
```bash
llama-server -m smollm2-1.7b-instruct-q4_k_m.gguf -c 8192
```
