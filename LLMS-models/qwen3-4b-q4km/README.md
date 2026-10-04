# Qwen3 4B (`qwen3-4b-q4km`)

**Description:** High-performance local AI for demanding mobile workloads.

## Model Overview
- **Parameters:** 4B
- **Context Length:** 40960 tokens
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
- **SHA-256 Hash:** `7485fe6f11af29433bc51cab58009521f205840f5b4ae3a32fa7f92e8534fdf5`

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-4B-Q4_K_M.gguf -c 40960
```
