# Qwen3 4B Thinking 2507 (qwen3-4b-thinking-2507-q4)

**Description:** Reasoning-focused Qwen model optimized for complex thinking tasks.

## Model Overview
- **Parameters:** 4B
- **Context Length:** 262144 tokens
- **Quantization:** Q4_K_S
- **Format:** GGUF
- **Target File:** `Qwen3-4B-Thinking-2507.Q4_0.gguf`
- **Thinking Mode:** Yes
- **License:** Apache-2.0
- **Categories:** High-Performance-8-GB

## Hardware Requirements
- **RAM:** 8 GB
- **Storage:** 4 GB
- **Supported OS / Platforms:** Android 11+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Science

## Source & Upstream
- **Hugging Face Repo:** [QuantFactory/Qwen3-4B-Thinking-2507-GGUF](https://huggingface.co/QuantFactory/Qwen3-4B-Thinking-2507-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/QuantFactory/Qwen3-4B-Thinking-2507-GGUF/resolve/main/Qwen3-4B-Thinking-2507.Q4_0.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Qwen3-4B-Thinking-2507.Q4_0.gguf -c 262144
```
