# Granite 3.3 2B Instruct (granite-3.3-2b-instruct-q4km)

**Description:** Compact instruction model for coding and general tasks.

## Model Overview
- **Parameters:** 2B
- **Context Length:** verify model release
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `granite-3.3-2B-instruct-Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** Apache-2.0
- **Categories:** Advanced-6-GB

## Hardware Requirements
- **RAM:** 6 GB
- **Storage:** 3 GB
- **Supported OS / Platforms:** Android 10+, Windows, Linux, macOS

## Capabilities
Chat, Coding, Reasoning, Summarization

## Source & Upstream
- **Hugging Face Repo:** [lm-kit/granite-3.3-2b-instruct-gguf](https://huggingface.co/lm-kit/granite-3.3-2b-instruct-gguf)
- **Download URL:** [Download GGUF](https://huggingface.co/lm-kit/granite-3.3-2b-instruct-gguf/resolve/main/granite-3.3-2B-instruct-Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m granite-3.3-2B-instruct-Q4_K_M.gguf -c verify
```
