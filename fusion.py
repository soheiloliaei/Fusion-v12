#!/usr/bin/env python3
"""
Fusion v11.2 CLI Entrypoint
Enables command-line access to agents, chains, and evaluation.
"""

import argparse
import json
import sys
from typing import Dict, List, Optional
from memory_registry import memory
from agent_chain import AgentChain

def load_input(input_path: str) -> str:
    """Load input text from file"""
    with open(input_path, 'r') as f:
        return f.read()

def save_output(output: Dict, output_path: Optional[str] = None):
    """Save output to file or print to stdout"""
    if output_path:
        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)
    else:
        print(json.dumps(output, indent=2))

def run_chain(args):
    """Run an agent chain"""
    chain = AgentChain(args.config)
    input_text = load_input(args.input)
    
    result = chain.execute(
        input_text=input_text,
        adaptive=args.adaptive
    )
    
    save_output(result, args.output)
    
    # Print insights report
    if args.insights:
        print("\nSystem Insights:")
        print(memory.generate_insights_report())

def run_single(args):
    """Run a single agent with pattern"""
    # Create temporary config file
    config = [{
        "agent": args.agent,
        "pattern": args.pattern,
        "metrics_threshold": args.threshold
    }]
    
    with open("_fusion_todo/temp_config.json", "w") as f:
        json.dump(config, f)
    
    chain = AgentChain("_fusion_todo/temp_config.json")
    
    input_text = load_input(args.input) if args.input else args.text
    
    result = chain.execute(
        input_text=input_text,
        adaptive=args.adaptive
    )
    
    save_output(result, args.output)
    
    # Clean up temp file
    import os
    os.remove("_fusion_todo/temp_config.json")

def evaluate_output(args):
    """Evaluate output using metrics"""
    from evaluator_metrics import evaluate_output
    
    with open(args.input, 'r') as f:
        text = f.read()
    
    metrics = evaluate_output(
        text=text,
        pattern_name=args.pattern
    )
    
    save_output({"metrics": metrics}, args.output)

def main():
    parser = argparse.ArgumentParser(description="Fusion v11.2 CLI Runner")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Chain command
    chain_parser = subparsers.add_parser("chain", help="Run agent chain")
    chain_parser.add_argument("config", help="Chain configuration JSON file")
    chain_parser.add_argument("--input", "-i", required=True, help="Input text file")
    chain_parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    chain_parser.add_argument("--adaptive", "-a", action="store_true", help="Enable adaptive pattern switching")
    chain_parser.add_argument("--insights", "-s", action="store_true", help="Show system insights")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run single agent")
    run_parser.add_argument("agent", help="Agent name")
    run_parser.add_argument("--pattern", "-p", required=True, help="Pattern name")
    run_parser.add_argument("--input", "-i", help="Input text file")
    run_parser.add_argument("--text", "-t", help="Direct input text")
    run_parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    run_parser.add_argument("--threshold", type=float, default=0.7, help="Metrics threshold")
    run_parser.add_argument("--adaptive", "-a", action="store_true", help="Enable adaptive pattern switching")
    
    # Evaluate command
    eval_parser = subparsers.add_parser("evaluate", help="Evaluate output")
    eval_parser.add_argument("input", help="Input text file to evaluate")
    eval_parser.add_argument("--pattern", "-p", required=True, help="Pattern name")
    eval_parser.add_argument("--output", "-o", help="Output JSON file (default: stdout)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == "chain":
            run_chain(args)
        elif args.command == "run":
            run_single(args)
        elif args.command == "evaluate":
            evaluate_output(args)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 