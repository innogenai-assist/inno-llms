# Qwen3 1.7B (qwen3-1.7b-q4km)

**Description:** Balanced on-device AI with strong reasoning and coding.

## Model Overview
- **Parameters:** 1.7B
- **Context Length:** 32768 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Qwen3-1.7B-Q4_K_M.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** Balanced-4-GB

## Hardware Requirements
- **RAM:** 4 GB
- **Storage:** 2 GB
- **Supported OS / Platforms:** Android 10+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing, Translation

## Source & Upstream
- **Hugging Face Repo:** [ggml-org/Qwen3-1.7B-GGUF](https://huggingface.co/ggml-org/Qwen3-1.7B-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/ggml-org/Qwen3-1.7B-GGUF/resolve/main/Qwen3-1.7B-Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-1.7B-Q4_K_M.gguf -c 32768
```
