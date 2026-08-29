# Local LLMs Hub & Model Manager

An open, organized catalog and download manager for 19 popular open-source Large Language Models (GGUF format) optimized for local inference across various hardware tiers (2 GB to 12+ GB RAM).

Each model is housed in its own dedicated directory with complete metadata, hardware requirements, upstream repository references, and official legal licenses.

---

## Repository Structure

```
llms/
├── llms.json                 # Catalog of all models with specifications & requirements
├── download_manager.py       # Resumable downloader and verification engine
├── licenses.py               # Official license templates
├── .gitignore                # Ignores large binary model weights (*.gguf)
│
├── smollm2-135m-instruct-q4km/
│   ├── LICENSE.txt           # Apache-2.0
│   ├── model_info.json       # Specifications and metadata
│   └── README.md             # Model card & run instructions
│
├── llama-3.2-1b-instruct-q4km/
│   ├── LICENSE.txt           # Llama 3.2 Community License
│   ├── model_info.json
│   └── README.md
│
├── gemma-3-1b-it-q4km/
│   ├── LICENSE.txt           # Gemma Terms of Use
│   ├── model_info.json
│   └── README.md
│
... (19 model directories)
```

---

## Model Catalog Overview

| Model ID | Model Name | Parameters | Quantization | Context | Memory Tier | License |
|---|---|---|---|---|---|---|
| `smollm2-135m-instruct-q4km` | SmolLM2 135M Instruct | 135M | Q4_K_M | 8K | 2 GB | Apache-2.0 |
| `smollm2-360m-instruct-q4km` | SmolLM2 360M Instruct | 360M | Q4_K_M | 8K | 2 GB | Apache-2.0 |
| `qwen3-0.6b-q4` | Qwen3 0.6B | 0.6B | Q4_0 | 32K | 2 GB | Apache-2.0 |
| `qwen3.5-0.8b-q4` | Qwen3.5 0.8B | 0.8B | Q4_0 | 32K | 2 GB | Apache-2.0 |
| `llama-3.2-1b-instruct-q4km` | Llama 3.2 1B Instruct | 1B | Q4_K_M | 8K | 2 GB / 3 GB | Llama 3.2 Community License |
| `gemma-3-1b-it-q4km` | Gemma 3 1B | 1B | Q4_K_M | 32K | 3 GB | Gemma Terms of Use |
| `smollm2-1.7b-instruct-q4km` | SmolLM2 1.7B Instruct | 1.7B | Q4_K_M | 8K | 3 GB | Apache-2.0 |
| `qwen3-1.7b-q4km` | Qwen3 1.7B | 1.7B | Q4_K_M | 32K | 4 GB | Apache-2.0 |
| `deepseek-r1-distill-qwen-1.5b` | DeepSeek R1 Distill Qwen 1.5B | 1.5B | Q4_K_M | 32K | 4 GB | MIT |
| `qwen2.5-math-1.5b-q4km` | Qwen2.5 Math 1.5B | 1.5B | Q4_K_M | 8K | 4 GB | Apache-2.0 |
| `llama-3.2-3b-instruct-q4km` | Llama 3.2 3B Instruct | 3B | Q4_K_M | 8K | 4 GB | Llama 3.2 Community License |
| `qwen3.5-2b-q4km` | Qwen3.5 2B | 2B | Q4_K_M | 32K | 6 GB | Apache-2.0 |
| `granite-3.3-2b-instruct-q4km` | Granite 3.3 2B Instruct | 2B | Q4_K_M | 32K | 6 GB | Apache-2.0 |
| `phi-3.5-mini-instruct-q4km` | Phi-3.5 Mini Instruct | 3.8B | Q4_K_M | 128K | 6 GB | MIT |
| `qwen3-4b-q4km` | Qwen3 4B | 4B | Q4_K_M | 32K | 8 GB / 12+ GB | Apache-2.0 |
| `qwen3-4b-thinking-2507-q4` | Qwen3 4B Thinking 2507 | 4B | Q4_0 | 256K | 8 GB | Apache-2.0 |
| `phi-4-mini-instruct-q4km` | Phi-4 Mini Instruct | 3.8B | Q4_K_M | 128K | 8 GB | MIT |
| `ministral-3b-instruct-q4km` | Ministral 3B Instruct | 3B | Q4_K_M | 32K | 8 GB | Mistral Research License |
| `qwen3-8b-q4km` | Qwen3 8B | 8.2B | Q4_K_M | 32K | 12+ GB | Apache-2.0 |

---

## Quick Start & Usage

### 1. Requirements
- Python 3.8+
- `requests` library:
  ```bash
  pip install requests
  ```

### 2. Check Download Status
```bash
python download_manager.py --status
```

### 3. Download All Models
Downloads all 19 models sequentially into their respective directories with HTTP Range resume support and GGUF header verification:
```bash
python download_manager.py
```

### 4. Download a Specific Model
```bash
python download_manager.py --model llama-3.2-1b-instruct-q4km
```

### 5. Initialize Model Folders and Licenses Without Downloading Weights
```bash
python download_manager.py --setup-dirs
```

---

## Running Models Locally

Once downloaded, you can run any of the GGUF models with `llama.cpp` or compatible engines:

```bash
# Example: Running Llama 3.2 1B
llama-server -m llama-3.2-1b-instruct-q4km/llama-3.2-1b-instruct-q4_k_m.gguf -c 8192
```

---

## Licenses

Each model is distributed under its respective creator's license agreement. Please inspect the `LICENSE.txt` inside each model's folder for exact terms.
- **Apache-2.0**: SmolLM2, Qwen3, Qwen3.5, Qwen2.5-Math, Granite 3.3
- **MIT**: DeepSeek-R1-Distill, Phi-3.5, Phi-4-mini
- **Llama 3.2 Community License**: Llama 3.2 models (Meta Platforms, Inc.)
- **Gemma Terms of Use**: Gemma 3 (Google LLC)
- **Mistral Research License**: Ministral 3B (Mistral AI)
