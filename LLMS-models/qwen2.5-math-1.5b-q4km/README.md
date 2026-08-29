# Qwen2.5 Math 1.5B (qwen2.5-math-1.5b-q4km)

**Description:** Specialized AI for mathematical reasoning and problem solving.

## Model Overview
- **Parameters:** 1.5B
- **Context Length:** 8192 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `qwen2.5-math-1.5b-instruct-q4_k_m.gguf`
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
- **Hugging Face Repo:** [sheldonrobinson/Qwen2.5-Math-1.5B-Instruct-Q4_K_M-GGUF](https://huggingface.co/sheldonrobinson/Qwen2.5-Math-1.5B-Instruct-Q4_K_M-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/sheldonrobinson/Qwen2.5-Math-1.5B-Instruct-Q4_K_M-GGUF/resolve/main/qwen2.5-math-1.5b-instruct-q4_k_m.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m qwen2.5-math-1.5b-instruct-q4_k_m.gguf -c 8192
```
