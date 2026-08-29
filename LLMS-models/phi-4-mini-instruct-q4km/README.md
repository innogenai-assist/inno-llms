# Phi-4 Mini Instruct (phi-4-mini-instruct-q4km)

**Description:** Compact high-performance model for advanced reasoning and coding.

## Model Overview
- **Parameters:** 3.8B
- **Context Length:** 128K tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Phi-4-mini-instruct-Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** MIT
- **Categories:** High-Performance-8-GB

## Hardware Requirements
- **RAM:** 8 GB
- **Storage:** 4 GB
- **Supported OS / Platforms:** Android 11+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics

## Source & Upstream
- **Hugging Face Repo:** [unsloth/Phi-4-mini-instruct-GGUF](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF/resolve/main/Phi-4-mini-instruct-Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Phi-4-mini-instruct-Q4_K_M.gguf -c 128K
```
