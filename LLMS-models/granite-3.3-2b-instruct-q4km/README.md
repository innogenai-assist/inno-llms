# Granite 3.3 2B Instruct (`granite-3.3-2b-instruct-q4km`)

**Description:** Compact instruction model for coding and general tasks.

## Model Overview
- **Parameters:** 2B
- **Context Length:** 131072 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `granite-3.3-2b-instruct-Q4_K_M.gguf`
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
- **Hugging Face Repo:** [ibm-granite/granite-3.3-2b-instruct-GGUF](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct-GGUF/resolve/main/granite-3.3-2b-instruct-Q4_K_M.gguf)
- **SHA-256 Hash:** `ac71e9e32c0bea919b409c5918f69ca74339854b0319c5065e4e9fb6d95c4852`

## Running Locally with LLaMA.cpp
```bash
llama-server -m granite-3.3-2b-instruct-Q4_K_M.gguf -c 131072
```
