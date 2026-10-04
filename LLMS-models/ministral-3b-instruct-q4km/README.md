# Ministral 3B Instruct (`ministral-3b-instruct-q4km`)

**Description:** Efficient high-quality AI for resource-constrained environments.

## Model Overview
- **Parameters:** 3B
- **Context Length:** 131072 tokens
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `ministral-3b-instruct-q4_k_m.gguf`
- **Thinking Mode:** No
- **License:** Mistral Research License
- **Categories:** High-Performance-8-GB

## Hardware Requirements
- **RAM:** 8 GB
- **Storage:** 4 GB
- **Supported OS / Platforms:** Android 11+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Writing

## Source & Upstream
- **Hugging Face Repo:** [matrixportalx/Ministral-3b-instruct-Q4_K_M-GGUF](https://huggingface.co/matrixportalx/Ministral-3b-instruct-Q4_K_M-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/matrixportalx/Ministral-3b-instruct-Q4_K_M-GGUF/resolve/main/ministral-3b-instruct-q4_k_m.gguf)
- **SHA-256 Hash:** `f6559975dfe5f3cabd43cc059baaf5c4007c670b2d17ee60ee6c40733259f686`

## Running Locally with LLaMA.cpp
```bash
llama-server -m ministral-3b-instruct-q4_k_m.gguf -c 131072
```
