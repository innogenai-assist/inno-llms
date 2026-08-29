# Qwen3 4B (qwen3-4b-q4km)

**Description:** High-performance local AI for demanding mobile workloads.

## Model Overview
- **Parameters:** 4B
- **Context Length:** 32768 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Qwen3-4B-Q4_K_M.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** High-Performance-8-GB, High-End-12-GB-Plus

## Hardware Requirements
- **RAM:** 8 GB
- **Storage:** 4 GB
- **Supported OS / Platforms:** Android 11+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing, Translation

## Source & Upstream
- **Hugging Face Repo:** [Qwen/Qwen3-4B-GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-4B-Q4_K_M.gguf -c 32768
```
