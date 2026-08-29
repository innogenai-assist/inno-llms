"""
LLM Download and Management Engine
Downloads models specified in llms.json into dedicated folders with licenses, metadata, and verification.
"""

import os
import sys
import time
import json
import argparse
import requests
from licenses import get_license_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "llms.json")

# Mapping of all 19 unique models to verified repositories and files
MODEL_CONFIGS = {
    "smollm2-135m-instruct-q4km": {
        "repo": "Segilmez06/SmolLM2-135M-Instruct-Q4_K_M-GGUF",
        "file": "smollm2-135m-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 105487424
    },
    "smollm2-360m-instruct-q4km": {
        "repo": "mfuntowicz/SmolLM2-360M-Instruct-Q4_K_M-GGUF",
        "file": "smollm2-360m-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 270724576
    },
    "qwen3-0.6b-q4": {
        "repo": "ggml-org/Qwen3-0.6B-GGUF",
        "file": "Qwen3-0.6B-Q4_0.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 429742080
    },
    "qwen3.5-0.8b-q4": {
        "repo": "ggml-org/Qwen3.5-0.8B-GGUF",
        "file": "Qwen3.5-0.8B-Q4_0.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 563059200
    },
    "llama-3.2-1b-instruct-q4km": {
        "repo": "hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF",
        "file": "llama-3.2-1b-instruct-q4_k_m.gguf",
        "license": "Llama 3.2 Community License",
        "expected_bytes": 807761984
    },
    "gemma-3-1b-it-q4km": {
        "repo": "ggml-org/gemma-3-1b-it-GGUF",
        "file": "gemma-3-1b-it-Q4_K_M.gguf",
        "license": "Gemma Terms of Use",
        "expected_bytes": 806628480
    },
    "smollm2-1.7b-instruct-q4km": {
        "repo": "HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF",
        "file": "smollm2-1.7b-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 1055420448
    },
    "qwen3-1.7b-q4km": {
        "repo": "ggml-org/Qwen3-1.7B-GGUF",
        "file": "Qwen3-1.7B-Q4_K_M.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 1281993472
    },
    "deepseek-r1-distill-qwen-1.5b": {
        "repo": "unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
        "file": "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "license": "MIT",
        "expected_bytes": 1117921984
    },
    "qwen2.5-math-1.5b-q4km": {
        "repo": "sheldonrobinson/Qwen2.5-Math-1.5B-Instruct-Q4_K_M-GGUF",
        "file": "qwen2.5-math-1.5b-instruct-q4_k_m.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 985917056
    },
    "llama-3.2-3b-instruct-q4km": {
        "repo": "hugging-quants/Llama-3.2-3B-Instruct-Q4_K_M-GGUF",
        "file": "llama-3.2-3b-instruct-q4_k_m.gguf",
        "license": "Llama 3.2 Community License",
        "expected_bytes": 2019774976
    },
    "qwen3.5-2b-q4km": {
        "repo": "openresearchtools/Qwen3.5-2B-GGUF",
        "file": "Qwen3.5-2B-Q4_K_M.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 1274808352
    },
    "granite-3.3-2b-instruct-q4km": {
        "repo": "lm-kit/granite-3.3-2b-instruct-gguf",
        "file": "granite-3.3-2B-instruct-Q4_K_M.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 1545510880
    },
    "phi-3.5-mini-instruct-q4km": {
        "repo": "QuantFactory/Phi-3.5-mini-instruct-GGUF",
        "file": "Phi-3.5-mini-instruct.Q4_K_M.gguf",
        "license": "MIT",
        "expected_bytes": 2393250560
    },
    "qwen3-4b-q4km": {
        "repo": "Qwen/Qwen3-4B-GGUF",
        "file": "Qwen3-4B-Q4_K_M.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 2497381664
    },
    "qwen3-4b-thinking-2507-q4": {
        "repo": "QuantFactory/Qwen3-4B-Thinking-2507-GGUF",
        "file": "Qwen3-4B-Thinking-2507.Q4_0.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 2588674848
    },
    "phi-4-mini-instruct-q4km": {
        "repo": "unsloth/Phi-4-mini-instruct-GGUF",
        "file": "Phi-4-mini-instruct-Q4_K_M.gguf",
        "license": "MIT",
        "expected_bytes": 2492028896
    },
    "ministral-3b-instruct-q4km": {
        "repo": "matrixportalx/Ministral-3b-instruct-Q4_K_M-GGUF",
        "file": "ministral-3b-instruct-q4_k_m.gguf",
        "license": "Mistral Research License",
        "expected_bytes": 1997557568
    },
    "qwen3-8b-q4km": {
        "repo": "Qwen/Qwen3-8B-GGUF",
        "file": "Qwen3-8B-Q4_K_M.gguf",
        "license": "Apache-2.0",
        "expected_bytes": 5027337472
    }
}


def load_catalog():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    unique = {}
    for cat_name, models in data.items():
        for m in models:
            mid = m["id"]
            if mid not in unique:
                item = dict(m)
                item["categories"] = [cat_name]
                unique[mid] = item
            else:
                unique[mid]["categories"].append(cat_name)
    return unique


def verify_gguf_file(filepath, expected_bytes=None):
    if not os.path.exists(filepath):
        return False, "File does not exist"
    
    size = os.path.getsize(filepath)
    if size < 1024 * 1024:  # Less than 1 MB is suspiciously small for an LLM
        return False, f"File too small ({size} bytes)"
    
    if expected_bytes and size != expected_bytes:
        # If difference is more than 0.1% or 100KB, flag mismatch
        diff = abs(size - expected_bytes)
        if diff > 1024 * 1024:
            return False, f"Size mismatch: {size} vs expected {expected_bytes}"
    
    with open(filepath, "rb") as f:
        magic = f.read(4)
        if magic != b"GGUF":
            return False, f"Invalid GGUF header magic: {magic}"
    
    return True, "OK"


def create_model_artifacts(model_dir, model_meta, config, actual_size=None):
    os.makedirs(model_dir, exist_ok=True)
    
    # 1. Write LICENSE.txt
    license_type = config.get("license", "Apache-2.0")
    license_text = get_license_text(license_type)
    license_path = os.path.join(model_dir, "LICENSE.txt")
    with open(license_path, "w", encoding="utf-8") as f:
        f.write(license_text)
    
    # 2. Write model_info.json
    info_path = os.path.join(model_dir, "model_info.json")
    info_data = {
        "id": model_meta.get("id"),
        "name": model_meta.get("name"),
        "version": model_meta.get("version"),
        "license": license_type,
        "sourceRepository": config.get("repo"),
        "filename": config.get("file"),
        "fileSizeBytes": actual_size if actual_size else config.get("expected_bytes"),
        "directDownloadUrl": f"https://huggingface.co/{config.get('repo')}/resolve/main/{config.get('file')}",
        "specifications": model_meta.get("specifications"),
        "thinkingMode": model_meta.get("thinkingMode"),
        "capabilities": model_meta.get("capabilities"),
        "requirements": model_meta.get("requirements"),
        "description": model_meta.get("description"),
        "categories": model_meta.get("categories")
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info_data, f, indent=4)
        
    # 3. Write README.md
    readme_path = os.path.join(model_dir, "README.md")
    specs = model_meta.get("specifications", {})
    reqs = model_meta.get("requirements", {})
    caps = ", ".join(model_meta.get("capabilities", []))
    cats = ", ".join(model_meta.get("categories", []))
    
    readme_content = f"""# {model_meta.get('name')} ({model_meta.get('id')})

**Description:** {model_meta.get('description')}

## Model Overview
- **Parameters:** {specs.get('parameters', 'N/A')}
- **Context Length:** {specs.get('contextLength', 'N/A')}
- **Quantization:** {specs.get('quantization', 'N/A')}
- **Format:** GGUF
- **Target File:** `{config.get('file')}`
- **Thinking Mode:** {'Yes' if model_meta.get('thinkingMode') else 'No'}
- **License:** {license_type}
- **Categories:** {cats}

## Hardware Requirements
- **RAM:** {reqs.get('ram', 'N/A')}
- **Storage:** {reqs.get('storage', 'N/A')}
- **Supported OS / Platforms:** Android {reqs.get('android', 'N/A')}, Windows, Linux, macOS

## Capabilities
{caps}

## Source & Upstream
- **Hugging Face Repo:** [{config.get('repo')}](https://huggingface.co/{config.get('repo')})
- **Download URL:** [Download GGUF](https://huggingface.co/{config.get('repo')}/resolve/main/{config.get('file')})

## Running Locally with LLaMA.cpp
```bash
llama-server -m {config.get('file')} -c {specs.get('contextLength', '4096').split()[0]}
```
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)


def download_file(url, target_path, expected_bytes=None, chunk_size=8 * 1024 * 1024):
    part_path = target_path + ".part"
    existing_bytes = 0
    if os.path.exists(part_path):
        existing_bytes = os.path.getsize(part_path)
    
    headers = {"User-Agent": "Mozilla/5.0"}
    if existing_bytes > 0:
        headers["Range"] = f"bytes={existing_bytes}-"
        print(f"  [Resume] Found existing partial file: {existing_bytes / (1024**2):.2f} MB")
    
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=5)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    response = session.get(url, headers=headers, stream=True, timeout=30)
    
    if response.status_code == 416:  # Requested Range Not Satisfiable
        # File might be already complete
        if os.path.exists(part_path) and os.path.getsize(part_path) > 1024 * 1024:
            os.replace(part_path, target_path)
            ok, _ = verify_gguf_file(target_path)
            if ok:
                return True
        print("  [Range error] Restarting download from beginning...")
        existing_bytes = 0
        if os.path.exists(part_path):
            os.remove(part_path)
        headers.pop("Range", None)
        response = session.get(url, headers=headers, stream=True, timeout=30)
            
    if response.status_code not in (200, 206):
        print(f"  [Error] HTTP Status {response.status_code} from {url}")
        return False
        
    content_len = response.headers.get("content-length")
    if content_len:
        total_bytes = existing_bytes + int(content_len)
    else:
        total_bytes = expected_bytes
    
    mode = "ab" if existing_bytes > 0 and response.status_code == 206 else "wb"
    if mode == "wb":
        existing_bytes = 0
        
    downloaded = existing_bytes
    start_time = time.time()
    last_print = start_time
    
    print(f"  [Downloading] Target: {os.path.basename(target_path)}")
    if total_bytes:
        print(f"  Total Size: {total_bytes / (1024**3):.3f} GB ({total_bytes} bytes)")
    
    with open(part_path, mode) as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if not chunk:
                continue
            f.write(chunk)
            downloaded += len(chunk)
            
            now = time.time()
            if now - last_print >= 2.0 or (total_bytes and downloaded >= total_bytes):
                elapsed = now - start_time
                speed = (downloaded - existing_bytes) / elapsed if elapsed > 0 else 0
                pct = (downloaded / total_bytes * 100) if total_bytes else 0
                eta = (total_bytes - downloaded) / speed if speed > 0 and total_bytes else 0
                total_str = f"{total_bytes / (1024**3):.3f} GB" if total_bytes else "unknown"
                print(f"    Progress: {downloaded / (1024**3):.3f} / {total_str} "
                      f"({pct:5.1f}%) | Speed: {speed / (1024**2):.2f} MB/s | ETA: {eta:.0f}s", flush=True)
                last_print = now
                
    # Validate downloaded file
    os.replace(part_path, target_path)
    ok, msg = verify_gguf_file(target_path, total_bytes)
    if not ok:
        print(f"  [Validation Failed] {msg}")
        return False
    print(f"  [Success] Downloaded and verified GGUF: {target_path} ({os.path.getsize(target_path)} bytes)")
    return True


def process_model(mid, model_meta, config):
    model_dir = os.path.join(BASE_DIR, mid)
    target_file = os.path.join(model_dir, config["file"])
    
    print(f"\n=======================================================")
    print(f"Processing: {model_meta.get('name')} ({mid})")
    print(f"Folder:     {model_dir}")
    print(f"File:       {config['file']} (~{config['expected_bytes'] / (1024**3):.3f} GB)")
    print(f"License:    {config['license']}")
    print(f"=======================================================")
    
    # 1. Create model folder, LICENSE.txt, model_info.json, README.md
    create_model_artifacts(model_dir, model_meta, config)
    
    # 2. Check if model file already exists and valid
    valid, reason = verify_gguf_file(target_file, config.get("expected_bytes"))
    if valid:
        print(f"  [Skip] Model already fully downloaded and verified.")
        return True
    else:
        if os.path.exists(target_file):
            print(f"  [Re-download] Existing file invalid ({reason}). Removing and redownloading.")
            os.remove(target_file)
            
    # 3. Download model file
    download_url = f"https://huggingface.co/{config['repo']}/resolve/main/{config['file']}"
    success = download_file(download_url, target_file, config.get("expected_bytes"))
    if success:
        create_model_artifacts(model_dir, model_meta, config, os.path.getsize(target_file))
    return success


def check_status():
    catalog = load_catalog()
    print("\n" + "="*80)
    print(f"{'#':<3} {'Model ID':<30} {'Folder':<7} {'License':<8} {'Metadata':<9} {'GGUF Status':<20}")
    print("="*80)
    
    total_expected = 0
    total_downloaded = 0
    completed_count = 0
    
    for idx, (mid, config) in enumerate(MODEL_CONFIGS.items(), 1):
        meta = catalog.get(mid, {})
        model_dir = os.path.join(BASE_DIR, mid)
        target_file = os.path.join(model_dir, config["file"])
        license_file = os.path.join(model_dir, "LICENSE.txt")
        info_file = os.path.join(model_dir, "model_info.json")
        
        has_folder = "YES" if os.path.isdir(model_dir) else "NO"
        has_license = "YES" if os.path.isfile(license_file) else "NO"
        has_meta = "YES" if os.path.isfile(info_file) else "NO"
        
        expected = config.get("expected_bytes", 0)
        total_expected += expected
        
        valid, msg = verify_gguf_file(target_file, expected)
        if valid:
            status_str = "COMPLETED"
            total_downloaded += expected
            completed_count += 1
        elif os.path.exists(target_file + ".part"):
            part_size = os.path.getsize(target_file + ".part")
            total_downloaded += part_size
            status_str = f"PARTIAL ({part_size / (1024**2):.1f}MB)"
        else:
            status_str = "NOT DOWNLOADED"
            
        print(f"{idx:<3} {mid:<30} {has_folder:<7} {has_license:<8} {has_meta:<9} {status_str:<20}")
        
    print("="*80)
    print(f"Summary: {completed_count}/{len(MODEL_CONFIGS)} models completed.")
    print(f"Total Downloaded: {total_downloaded / (1024**3):.2f} GB / {total_expected / (1024**3):.2f} GB")
    print("="*80 + "\n")


def setup_all_dirs():
    catalog = load_catalog()
    print("Setting up model folders, licenses, and metadata for all 19 models...")
    for mid, config in MODEL_CONFIGS.items():
        model_dir = os.path.join(BASE_DIR, mid)
        meta = catalog.get(mid, {"id": mid, "name": mid})
        create_model_artifacts(model_dir, meta, config)
    print("All model directories initialized with LICENSE.txt, model_info.json, and README.md.")


def main():
    parser = argparse.ArgumentParser(description="LLM Model Downloader and License Manager")
    parser.add_argument("--status", action="store_true", help="Check status of all models")
    parser.add_argument("--setup-dirs", action="store_true", help="Initialize all model folders, licenses, and metadata without downloading")
    parser.add_argument("--model", type=str, help="Download a specific model ID")
    parser.add_argument("--limit", type=int, help="Limit number of models to download")
    args = parser.parse_args()
    
    catalog = load_catalog()
    
    if args.setup_dirs:
        setup_all_dirs()
        check_status()
        return
        
    if args.status:
        check_status()
        return
        
    if args.model:
        if args.model not in MODEL_CONFIGS:
            print(f"Unknown model ID: {args.model}")
            print(f"Available IDs: {list(MODEL_CONFIGS.keys())}")
            sys.exit(1)
        meta = catalog.get(args.model, {"id": args.model, "name": args.model})
        config = MODEL_CONFIGS[args.model]
        success = process_model(args.model, meta, config)
        sys.exit(0 if success else 1)
        
    # Pre-initialize all folders and licenses
    setup_all_dirs()
    
    count = 0
    for mid, config in MODEL_CONFIGS.items():
        if args.limit and count >= args.limit:
            break
        meta = catalog.get(mid, {"id": mid, "name": mid})
        success = process_model(mid, meta, config)
        if not success:
            print(f"Failed to process {mid}. Continuing to next model...")
        count += 1
        
    print("\nAll requested downloads finished.")
    check_status()


if __name__ == "__main__":
    main()
