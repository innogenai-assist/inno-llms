# Qwen2.5 Math 1.5B (`qwen2.5-math-1.5b-q4km`)

**Description:** Specialized AI for mathematical reasoning and problem solving.

## Model Overview
- **Parameters:** 1.5B
- **Context Length:** 4096 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Qwen2.5-Math-1.5B-Instruct-Q4_K_M.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** Balanced-4-GB

## Hardware Requirements
- **RAM:** 4 GB
- **Storage:** 2 GB
- **Supported OS / Platforms:** Android 10+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Mathematics, Coding

## Source & Upstream
- **Hugging Face Repo:** [bartowski/Qwen2.5-Math-1.5B-Instruct-GGUF](https://huggingface.co/bartowski/Qwen2.5-Math-1.5B-Instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/bartowski/Qwen2.5-Math-1.5B-Instruct-GGUF/resolve/main/Qwen2.5-Math-1.5B-Instruct-Q4_K_M.gguf)
- **SHA-256 Hash:** `9614a50f03c897028920ca0dc4365da570bf587f9ee7768261216fe370b37e8e`

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen2.5-Math-1.5B-Instruct-Q4_K_M.gguf -c 4096
```
