#!/usr/bin/env python3
from typing import Dict, List, Optional
import json
from datetime import datetime
import os

from prompt_pattern_registry import get_pattern_by_name, get_available_patterns
from evaluator_metrics import evaluate_output
from execution_mode_map import get_mode_config, apply_mode_to_pattern

class PatternTester:
    def __init__(self, results_dir: str = "_fusion_todo/pattern_tests"):
        self.results_dir = results_dir
        os.makedirs(results_dir, exist_ok=True)
        
    def test_pattern(
        self,
        pattern_name: str,
        input_text: str,
        mode: Optional[str] = None,
        save_results: bool = True
    ) -> Dict:
        """Test a pattern with input text"""
        
        # Get pattern
        pattern = get_pattern_by_name(pattern_name)
        if not pattern:
            raise ValueError(f"Pattern not found: {pattern_name}")
            
        # Get base config
        base_config = pattern.get_config() if hasattr(pattern, 'get_config') else {}
        
        # Apply mode if specified
        if mode:
            config = apply_mode_to_pattern(pattern_name, mode, base_config)
        else:
            config = base_config
            
        # Apply pattern
        output = pattern.apply(input_text)
        
        # Evaluate output
        metrics = evaluate_output(
            text=output,
            pattern_name=pattern_name
        )
        
        # Prepare results
        results = {
            "timestamp": datetime.now().isoformat(),
            "pattern": pattern_name,
            "mode": mode,
            "config": config,
            "input_preview": input_text[:200] + "..." if len(input_text) > 200 else input_text,
            "output_preview": output[:200] + "..." if len(output) > 200 else output,
            "metrics": metrics,
            "full_output": output
        }
        
        # Save results if requested
        if save_results:
            self._save_test_results(results)
            
        return results
        
    def benchmark_patterns(
        self,
        input_text: str,
        patterns: Optional[List[str]] = None,
        mode: Optional[str] = None
    ) -> Dict:
        """Benchmark multiple patterns against input"""
        
        # Use all patterns if none specified
        if not patterns:
            patterns = get_available_patterns()
            
        results = {}
        for pattern_name in patterns:
            try:
                result = self.test_pattern(
                    pattern_name=pattern_name,
                    input_text=input_text,
                    mode=mode,
                    save_results=True
                )
                results[pattern_name] = result
            except Exception as e:
                results[pattern_name] = {
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
                
        # Calculate comparative metrics
        comparison = self._compare_results(results)
        
        # Save benchmark results
        self._save_benchmark_results(results, comparison)
        
        return {
            "results": results,
            "comparison": comparison
        }
        
    def _save_test_results(self, results: Dict):
        """Save individual test results"""
        filename = f"test_{results['pattern']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2)
            
    def _save_benchmark_results(self, results: Dict, comparison: Dict):
        """Save benchmark results"""
        filename = f"benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump({
                "results": results,
                "comparison": comparison
            }, f, indent=2)
            
    def _compare_results(self, results: Dict) -> Dict:
        """Compare results across patterns"""
        comparison = {
            "best_overall": None,
            "best_clarity": None,
            "best_innovation": None,
            "metrics_summary": {}
        }
        
        # Calculate averages and find best performers
        best_overall_score = 0
        best_clarity_score = 0
        best_innovation_score = 0
        
        for pattern, result in results.items():
            if "error" in result:
                continue
                
            metrics = result["metrics"]
            
            # Track averages
            if pattern not in comparison["metrics_summary"]:
                comparison["metrics_summary"][pattern] = {
                    "overall": metrics.get("overall", 0),
                    "clarity": metrics.get("clarity", 0),
                    "innovation": metrics.get("innovation", 0)
                }
                
            # Track best performers
            overall = metrics.get("overall", 0)
            clarity = metrics.get("clarity", 0)
            innovation = metrics.get("innovation", 0)
            
            if overall > best_overall_score:
                best_overall_score = overall
                comparison["best_overall"] = pattern
                
            if clarity > best_clarity_score:
                best_clarity_score = clarity
                comparison["best_clarity"] = pattern
                
            if innovation > best_innovation_score:
                best_innovation_score = innovation
                comparison["best_innovation"] = pattern
                
        return comparison

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Pattern Development and Testing Tool")
    
    parser.add_argument(
        "action",
        choices=["test", "benchmark"],
        help="Action to perform"
    )
    
    parser.add_argument(
        "--pattern",
        help="Pattern to test"
    )
    
    parser.add_argument(
        "--input",
        required=True,
        help="Input text file"
    )
    
    parser.add_argument(
        "--mode",
        choices=["simulate", "ship", "critique"],
        help="Execution mode"
    )
    
    parser.add_argument(
        "--output",
        help="Output file for results"
    )
    
    args = parser.parse_args()
    
    # Read input text
    with open(args.input, 'r') as f:
        input_text = f.read()
        
    tester = PatternTester()
    
    try:
        if args.action == "test":
            if not args.pattern:
                parser.error("--pattern is required for test action")
                
            results = tester.test_pattern(
                pattern_name=args.pattern,
                input_text=input_text,
                mode=args.mode
            )
        else:  # benchmark
            results = tester.benchmark_patterns(
                input_text=input_text,
                patterns=[args.pattern] if args.pattern else None,
                mode=args.mode
            )
            
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
        else:
            print(json.dumps(results, indent=2))
            
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main() 