# Qwen3 0.6B (qwen3-0.6b-q4)

**Description:** Fast, lightweight AI for private on-device use.

## Model Overview
- **Parameters:** 0.6B
- **Context Length:** 32768 tokens
- **Quantization:** Q4_0
- **Format:** GGUF
- **Target File:** `Qwen3-0.6B-Q4_0.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** Ultra-Lightweight-2-GB, Lightweight-3-GB

## Hardware Requirements
- **RAM:** 2 GB
- **Storage:** 1 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing, Translation

## Source & Upstream
- **Hugging Face Repo:** [ggml-org/Qwen3-0.6B-GGUF](https://huggingface.co/ggml-org/Qwen3-0.6B-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/ggml-org/Qwen3-0.6B-GGUF/resolve/main/Qwen3-0.6B-Q4_0.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-0.6B-Q4_0.gguf -c 32768
```
