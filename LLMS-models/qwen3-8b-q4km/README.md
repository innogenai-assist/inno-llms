# Qwen3 8B (`qwen3-8b-q4km`)

**Description:** High-end on-device AI for demanding reasoning and coding workloads.

## Model Overview
- **Parameters:** 8.2B
- **Context Length:** 40960 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Qwen3-8B-Q4_K_M.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** High-End-12-GB-Plus

## Hardware Requirements
- **RAM:** 12 GB+
- **Storage:** 6 GB
- **Supported OS / Platforms:** Android 12+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing, Translation

## Source & Upstream
- **Hugging Face Repo:** [Qwen/Qwen3-8B-GGUF](https://huggingface.co/Qwen/Qwen3-8B-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/Qwen/Qwen3-8B-GGUF/resolve/main/Qwen3-8B-Q4_K_M.gguf)
- **SHA-256 Hash:** `d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785`

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-8B-Q4_K_M.gguf -c 40960
```
