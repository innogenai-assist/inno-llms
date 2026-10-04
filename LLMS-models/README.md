# ZAYEN Local LLMs Hub & Model Catalog

An open, organized catalog and download manager for 19 verified open-source Large Language Models (GGUF format) optimized for on-device and local inference across various hardware tiers (2 GB to 12+ GB RAM).

Each model is housed with complete metadata, hardware requirements, upstream repository references, SHA-256 integrity verification, and official legal licenses.

---

## Model Catalog Overview (19 Verified Models)

| Model Name | Parameters | Quantization | Size | RAM Required | Direct Download Link |
|:---|:---:|:---:|:---:|:---:|:---|
| **SmolLM2 135M Instruct** (`smollm2-135m-instruct-q4km`) | 135M | `Q4_K_M` | 105 MB | 2 GB | [`SmolLM2-135M-Instruct-Q4_K_M.gguf`](https://huggingface.co/bartowski/SmolLM2-135M-Instruct-GGUF/resolve/main/SmolLM2-135M-Instruct-Q4_K_M.gguf) |
| **SmolLM2 360M Instruct** (`smollm2-360m-instruct-q4km`) | 360M | `Q4_K_M` | 271 MB | 2 GB | [`SmolLM2-360M-Instruct-Q4_K_M.gguf`](https://huggingface.co/bartowski/SmolLM2-360M-Instruct-GGUF/resolve/main/SmolLM2-360M-Instruct-Q4_K_M.gguf) |
| **Qwen3 0.6B** (`qwen3-0.6b-q4`) | 0.6B | `Q4_0` | 429 MB | 2 GB | [`Qwen3-0.6B-Q4_0.gguf`](https://huggingface.co/ggml-org/Qwen3-0.6B-GGUF/resolve/main/Qwen3-0.6B-Q4_0.gguf) |
| **Qwen3.5 0.8B** (`qwen3.5-0.8b-q4`) | 0.8B | `Q4_0` | 563 MB | 2 GB | [`Qwen3.5-0.8B-Q4_0.gguf`](https://huggingface.co/ggml-org/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_0.gguf) |
| **Llama 3.2 1B Instruct** (`llama-3.2-1b-instruct-q4km`) | 1B | `Q4_K_M` | 808 MB | 2 GB | [`llama-3.2-1b-instruct-q4_k_m.gguf`](https://huggingface.co/hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.2-1b-instruct-q4_k_m.gguf) |
| **Gemma 3 1B** (`gemma-3-1b-it-q4km`) | 1B | `Q4_K_M` | 806 MB | 3 GB | [`gemma-3-1b-it-Q4_K_M.gguf`](https://huggingface.co/ggml-org/gemma-3-1b-it-GGUF/resolve/main/gemma-3-1b-it-Q4_K_M.gguf) |
| **SmolLM2 1.7B Instruct** (`smollm2-1.7b-instruct-q4km`) | 1.7B | `Q4_K_M` | 1.06 GB | 3 GB | [`smollm2-1.7b-instruct-q4_k_m.gguf`](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF/resolve/main/smollm2-1.7b-instruct-q4_k_m.gguf) |
| **Qwen3 1.7B** (`qwen3-1.7b-q4km`) | 1.7B | `Q4_K_M` | 1.28 GB | 4 GB | [`Qwen3-1.7B-Q4_K_M.gguf`](https://huggingface.co/ggml-org/Qwen3-1.7B-GGUF/resolve/main/Qwen3-1.7B-Q4_K_M.gguf) |
| **DeepSeek R1 Distill Qwen 1.5B** (`deepseek-r1-distill-qwen-1.5b`) | 1.5B | `Q4_K_M` | 1.12 GB | 4 GB | [`DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf`](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf) |
| **Qwen2.5 Math 1.5B** (`qwen2.5-math-1.5b-q4km`) | 1.5B | `Q4_K_M` | 0.986 GB | 4 GB | [`Qwen2.5-Math-1.5B-Instruct-Q4_K_M.gguf`](https://huggingface.co/bartowski/Qwen2.5-Math-1.5B-Instruct-GGUF/resolve/main/Qwen2.5-Math-1.5B-Instruct-Q4_K_M.gguf) |
| **Llama 3.2 3B Instruct** (`llama-3.2-3b-instruct-q4km`) | 3B | `Q4_K_M` | 2.02 GB | 4 GB | [`llama-3.2-3b-instruct-q4_k_m.gguf`](https://huggingface.co/hugging-quants/Llama-3.2-3B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.2-3b-instruct-q4_k_m.gguf) |
| **Qwen3.5 2B** (`qwen3.5-2b-q4km`) | 2B | `Q4_K_M` | 1.27 GB | 6 GB | [`Qwen3.5-2B-Q4_K_M.gguf`](https://huggingface.co/openresearchtools/Qwen3.5-2B-GGUF/resolve/main/Qwen3.5-2B-Q4_K_M.gguf) |
| **Granite 3.3 2B Instruct** (`granite-3.3-2b-instruct-q4km`) | 2B | `Q4_K_M` | 1.55 GB | 6 GB | [`granite-3.3-2b-instruct-Q4_K_M.gguf`](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct-GGUF/resolve/main/granite-3.3-2b-instruct-Q4_K_M.gguf) |
| **Phi-3.5 Mini Instruct** (`phi-3.5-mini-instruct-q4km`) | 3.8B | `Q4_K_M` | 2.39 GB | 6 GB | [`Phi-3.5-mini-instruct.Q4_K_M.gguf`](https://huggingface.co/QuantFactory/Phi-3.5-mini-instruct-GGUF/resolve/main/Phi-3.5-mini-instruct.Q4_K_M.gguf) |
| **Qwen3 4B** (`qwen3-4b-q4km`) | 4B | `Q4_K_M` | 2.50 GB | 8 GB | [`Qwen3-4B-Q4_K_M.gguf`](https://huggingface.co/Qwen/Qwen3-4B-GGUF/resolve/main/Qwen3-4B-Q4_K_M.gguf) |
| **Qwen3 4B Thinking 2507** (`qwen3-4b-thinking-2507-q4`) | 4B | `Q4_K_S` | 2.60 GB | 8 GB | [`Qwen3-4B-Thinking-2507.Q4_K_S.gguf`](https://huggingface.co/QuantFactory/Qwen3-4B-Thinking-2507-GGUF/resolve/main/Qwen3-4B-Thinking-2507.Q4_K_S.gguf) |
| **Phi-4 Mini Instruct** (`phi-4-mini-instruct-q4km`) | 3.8B | `Q4_K_M` | 2.49 GB | 8 GB | [`Phi-4-mini-instruct-Q4_K_M.gguf`](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF/resolve/main/Phi-4-mini-instruct-Q4_K_M.gguf) |
| **Ministral 3B Instruct** (`ministral-3b-instruct-q4km`) | 3B | `Q4_K_M` | 2.00 GB | 8 GB | [`ministral-3b-instruct-q4_k_m.gguf`](https://huggingface.co/matrixportalx/Ministral-3b-instruct-Q4_K_M-GGUF/resolve/main/ministral-3b-instruct-q4_k_m.gguf) |
| **Qwen3 8B** (`qwen3-8b-q4km`) | 8.2B | `Q4_K_M` | 5.03 GB | 12 GB+ | [`Qwen3-8B-Q4_K_M.gguf`](https://huggingface.co/Qwen/Qwen3-8B-GGUF/resolve/main/Qwen3-8B-Q4_K_M.gguf) |

---

## Hardware Tiers & Categories

### 1. Ultra-Lightweight (2 GB RAM)
Ultra-compact models for low-end mobile devices and fast responses.
- **SmolLM2 135M Instruct** (`smollm2-135m-instruct-q4km`)
- **SmolLM2 360M Instruct** (`smollm2-360m-instruct-q4km`)
- **Qwen3 0.6B** (`qwen3-0.6b-q4`)
- **Qwen3.5 0.8B** (`qwen3.5-0.8b-q4`)

### 2. Lightweight (3 GB RAM)
Balanced compact models providing quality chat and reasoning.
- **Llama 3.2 1B Instruct** (`llama-3.2-1b-instruct-q4km`)
- **Gemma 3 1B** (`gemma-3-1b-it-q4km`)
- **SmolLM2 1.7B Instruct** (`smollm2-1.7b-instruct-q4km`)

### 3. Balanced (4 GB RAM)
Solid performance for coding, mathematics, and reasoning.
- **Qwen3 1.7B** (`qwen3-1.7b-q4km`)
- **DeepSeek R1 Distill Qwen 1.5B** (`deepseek-r1-distill-qwen-1.5b`)
- **Qwen2.5 Math 1.5B** (`qwen2.5-math-1.5b-q4km`)
- **Llama 3.2 3B Instruct** (`llama-3.2-3b-instruct-q4km`)

### 4. Advanced (6 GB RAM)
Higher capacity models for complex multi-turn coding and knowledge tasks.
- **Qwen3.5 2B** (`qwen3.5-2b-q4km`)
- **Granite 3.3 2B Instruct** (`granite-3.3-2b-instruct-q4km`)
- **Phi-3.5 Mini Instruct** (`phi-3.5-mini-instruct-q4km`)
- **Ministral 3B Instruct** (`ministral-3b-instruct-q4km`)

### 5. High-Performance (8 GB RAM)
Top-tier on-device reasoning and reasoning/thinking models.
- **Qwen3 4B** (`qwen3-4b-q4km`)
- **Qwen3 4B Thinking 2507** (`qwen3-4b-thinking-2507-q4`)
- **Phi-4 Mini Instruct** (`phi-4-mini-instruct-q4km`)

### 6. High-End (12+ GB RAM)
Full-capability flagship models for workstation and flagship device inference.
- **Qwen3 8B** (`qwen3-8b-q4km`)

---

## Direct Raw Catalog Endpoint
To fetch this catalog in JSON format directly:
```
https://raw.githubusercontent.com/innogenai-assist/inno-llms/main/llms.json
```

---

## License
All models are distributed under their respective upstream open-source licenses (Apache 2.0, MIT, Gemma Terms of Use, Llama 3.2 Community License, Mistral Research License). See `LLMS-models/<model-id>/LICENSE.txt` for details.
