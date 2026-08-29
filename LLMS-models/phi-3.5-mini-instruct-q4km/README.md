# Phi-3.5 Mini Instruct (phi-3.5-mini-instruct-q4km)

**Description:** Strong compact model for advanced mobile AI tasks.

## Model Overview
- **Parameters:** 3.8B
- **Context Length:** 128K tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `Phi-3.5-mini-instruct.Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** MIT
- **Categories:** Advanced-6-GB

## Hardware Requirements
- **RAM:** 6 GB
- **Storage:** 4 GB
- **Supported OS / Platforms:** Android 10+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Mathematics, Writing

## Source & Upstream
- **Hugging Face Repo:** [QuantFactory/Phi-3.5-mini-instruct-GGUF](https://huggingface.co/QuantFactory/Phi-3.5-mini-instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/QuantFactory/Phi-3.5-mini-instruct-GGUF/resolve/main/Phi-3.5-mini-instruct.Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m Phi-3.5-mini-instruct.Q4_K_M.gguf -c 128K
```
