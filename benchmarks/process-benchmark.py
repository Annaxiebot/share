#!/usr/bin/env python3
"""
Process benchmark JSON and add metadata for GitHub repo
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def process_benchmark(benchmark_file, fast_models_file, deep_models_file):
    """Add metadata to benchmark file"""
    
    # Load benchmark results
    with open(benchmark_file) as f:
        results = json.load(f)
    
    # Load model selections
    with open(fast_models_file) as f:
        fast = json.load(f)
    
    with open(deep_models_file) as f:
        deep = json.load(f)
    
    # Calculate statistics
    total = len(results)
    successful = len([r for r in results if r.get('status') == 'success'])
    failed = total - successful
    
    # Check if conversational filtering was applied
    conversational = len([r for r in results if r.get('status') == 'success' and r.get('word_count', 0) >= 10])
    
    # Build enriched benchmark
    enriched = {
        "timestamp": datetime.now().isoformat(),
        "total_models_tested": total,
        "successful_models": successful,
        "failed_models": failed,
        "conversational_models": conversational,
        "success_rate": round(successful / total * 100, 1) if total > 0 else 0,
        "results": results,
        "fast_models_selected": [m['model'] for m in fast.get('fast_models', [])],
        "deep_models_selected": [m['model'] for m in deep.get('deep_models', [])]
    }
    
    return enriched

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: process-benchmark.py <benchmark.json> <fast-models.json> <deep-models.json>")
        sys.exit(1)
    
    benchmark = process_benchmark(sys.argv[1], sys.argv[2], sys.argv[3])
    print(json.dumps(benchmark, indent=2))
