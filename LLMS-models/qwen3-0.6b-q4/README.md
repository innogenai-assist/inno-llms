# Qwen3 0.6B (`qwen3-0.6b-q4`)

**Description:** Fast, lightweight AI for private on-device use.

## Model Overview
- **Parameters:** 0.6B
- **Context Length:** 40960 tokens
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
- **SHA-256 Hash:** `da2572f16c06133561ce56accaa822216f2391ef4d37fba427801cd6736417d4`

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-0.6B-Q4_0.gguf -c 40960
```
