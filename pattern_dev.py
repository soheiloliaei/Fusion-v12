#!/usr/bin/env python3
import argparse
import json
import sys
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any

from prompt_pattern_registry import PatternRegistry
from evaluator_metrics import evaluate_output
from execution_mode_map import get_mode_config

FUSION_TODO_DIR = Path("_fusion_todo")
PATTERN_TESTS_DIR = FUSION_TODO_DIR / "pattern_tests"

def test_pattern(
    pattern_name: str,
    input_text: str,
    mode: str = "simulate",
    save_results: bool = True
) -> Dict[str, Any]:
    """Test a pattern with given input"""
    # Get pattern
    pattern = PatternRegistry.get_pattern(pattern_name)
    if not pattern:
        raise ValueError(f"Pattern not found: {pattern_name}")
        
    # Apply pattern
    output = pattern.apply(input_text)
    
    # Evaluate output
    metrics = evaluate_output(text=output, pattern_name=pattern_name)
    
    # Get mode config
    mode_config = get_mode_config(mode)
    threshold = mode_config.critique_threshold
    
    # Check if fallback would trigger
    failed_metrics = [k for k, v in metrics.items() 
                     if isinstance(v, (int, float)) and v < threshold]
    would_fallback = bool(failed_metrics)
    
    # Prepare results
    results = {
        "timestamp": datetime.now().isoformat(),
        "pattern": pattern_name,
        "mode": mode,
        "input_preview": input_text[:200] + "..." if len(input_text) > 200 else input_text,
        "output": output,
        "metrics": metrics,
        "would_fallback": would_fallback,
        "failed_metrics": failed_metrics if would_fallback else None,
        "threshold": threshold
    }
    
    # Save results if requested
    if save_results:
        save_test_results(results)
        
    return results

def save_test_results(results: Dict[str, Any]):
    """Save test results"""
    os.makedirs(PATTERN_TESTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save JSON results
    json_path = PATTERN_TESTS_DIR / f"test_{timestamp}.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
        
    # Generate markdown report
    report = [
        f"# Pattern Test Report - {timestamp}\n",
        f"Pattern: {results['pattern']}",
        f"Mode: {results['mode']}\n",
        "## Input Preview",
        results["input_preview"],
        "\n## Output",
        results["output"],
        "\n## Metrics",
        *[f"- {k}: {v:.2f}" if isinstance(v, (int, float)) else f"- {k}: {v}"
          for k, v in results["metrics"].items()],
        "\n## Fallback Analysis",
        f"Threshold: {results['threshold']:.2f}"
    ]
    
    if results["would_fallback"]:
        report.extend([
            "Failed metrics:",
            *[f"- {m}" for m in results["failed_metrics"]]
        ])
    else:
        report.append("No fallback needed")
        
    # Save markdown report
    md_path = PATTERN_TESTS_DIR / f"test_{timestamp}.md"
    with open(md_path, 'w') as f:
        f.write("\n".join(report))

def list_patterns():
    """List available patterns"""
    patterns = PatternRegistry.list_patterns()
    print("\nAvailable patterns:")
    for p in patterns:
        print(f"- {p}")

def main():
    parser = argparse.ArgumentParser(description="Pattern Development Tool")
    parser.add_argument("pattern",
                      help="Pattern name to test")
    parser.add_argument("-i", "--input",
                      help="Input text file")
    parser.add_argument("-m", "--mode", default="simulate",
                      choices=["simulate", "ship", "critique"],
                      help="Execution mode")
    parser.add_argument("-l", "--list", action="store_true",
                      help="List available patterns")
    args = parser.parse_args()
    
    try:
        if args.list:
            list_patterns()
            return
            
        if not args.input:
            print("Error: Input file required", file=sys.stderr)
            sys.exit(1)
            
        # Load input
        with open(args.input, 'r') as f:
            input_text = f.read()
            
        # Test pattern
        results = test_pattern(
            pattern_name=args.pattern,
            input_text=input_text,
            mode=args.mode
        )
        
        # Print results
        print("\nTest Results:")
        print(f"Pattern: {results['pattern']}")
        print(f"Mode: {results['mode']}\n")
        print("Metrics:")
        for k, v in results["metrics"].items():
            if isinstance(v, (int, float)):
                print(f"- {k}: {v:.2f}")
            else:
                print(f"- {k}: {v}")
                
        print("\nFallback Analysis:")
        print(f"Threshold: {results['threshold']:.2f}")
        if results["would_fallback"]:
            print("Failed metrics:")
            for m in results["failed_metrics"]:
                print(f"- {m}")
        else:
            print("No fallback needed")
            
        print(f"\nResults saved to: {PATTERN_TESTS_DIR}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 