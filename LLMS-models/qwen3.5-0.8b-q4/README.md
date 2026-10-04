# Qwen3.5 0.8B (`qwen3.5-0.8b-q4`)

**Description:** Compact AI for fast everyday conversations and tasks.

## Model Overview
- **Parameters:** 0.8B
- **Context Length:** 262144 tokens
- **Quantization:** Q4_0
- **Format:** GGUF
- **Target File:** `Qwen3.5-0.8B-Q4_0.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** Ultra-Lightweight-2-GB

## Hardware Requirements
- **RAM:** 2 GB
- **Storage:** 1.5 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing, Translation

## Source & Upstream
- **Hugging Face Repo:** [ggml-org/Qwen3.5-0.8B-GGUF](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_0.gguf)
- **SHA-256 Hash:** `57d1997790d1744fba5b40a7317df71ea5e2acee28c47e78f0cce39c0703f8cf`

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3.5-0.8B-Q4_0.gguf -c 262144
```
