# Gemma 3 1B (gemma-3-1b-it-q4km)

**Description:** Compact general-purpose AI for mobile devices.

## Model Overview
- **Parameters:** 1B
- **Context Length:** verify model release
- **Quantization:** Q4_K_M
- **Format:** GGUF
- **Target File:** `gemma-3-1b-it-Q4_K_M.gguf`
- **Thinking Mode:** No
- **License:** Gemma Terms of Use
- **Categories:** Lightweight-3-GB

## Hardware Requirements
- **RAM:** 3 GB
- **Storage:** 1.5 GB
- **Supported OS / Platforms:** Android 8+, Windows, Linux, macOS

## Capabilities
Chat, Reasoning, Coding, Writing, Summarization

## Source & Upstream
- **Hugging Face Repo:** [ggml-org/gemma-3-1b-it-GGUF](https://huggingface.co/ggml-org/gemma-3-1b-it-GGUF)
- **Download URL:** [Download GGUF](https://huggingface.co/ggml-org/gemma-3-1b-it-GGUF/resolve/main/gemma-3-1b-it-Q4_K_M.gguf)

## Running Locally with LLaMA.cpp
```bash
llama-server -m gemma-3-1b-it-Q4_K_M.gguf -c verify
```
