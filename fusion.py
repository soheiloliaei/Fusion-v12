#!/usr/bin/env python3
"""
Fusion v11.2 CLI Entrypoint
Enables command-line access to agents, chains, and evaluation.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List, Union
from datetime import datetime

from fusion_v11_agents_complete import (
    Dispatcher, 
    TensionType,
    apply_creative_tension
)
from prompt_pattern_registry import get_pattern_by_name
from evaluator_metrics import evaluate_output
from agent_chain import run_agent_chain, ChainMode

def load_json(file_path: str) -> Dict[str, Any]:
    """Load and parse JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str):
    """Save data as JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def read_input_file(file_path: str) -> str:
    """Read input text from file."""
    with open(file_path, 'r') as f:
        return f.read()

def log_pattern_usage(pattern: str, score: float, context: Dict[str, Any]):
    """Log pattern usage and score to pattern_log.json."""
    log_file = Path('_fusion_todo/pattern_log.json')
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        if log_file.exists():
            logs = json.loads(log_file.read_text())
        else:
            logs = []
    except:
        logs = []
    
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "pattern": pattern,
        "score": score,
        "context": context
    })
    
    log_file.write_text(json.dumps(logs, indent=2))

def run_agent(args):
    """Run a single agent with optional pattern."""
    dispatcher = Dispatcher()
    input_text = read_input_file(args.input) if args.input else args.text
    
    context = {}
    if args.context:
        context = load_json(args.context)
    
    # Apply pattern if specified
    if args.pattern:
        pattern = get_pattern_by_name(args.pattern)
        input_text = pattern.apply(input_text, context)
    
    # Apply creative tension if specified
    if args.tension:
        tension_type = TensionType(args.tension)
        tension_result = apply_creative_tension(
            {"input": input_text},
            tension_type.value,
            context
        )
        input_text = tension_result["balanced_perspective"]
    
    # Execute agent
    result = dispatcher.execute({
        "agent_name": args.agent,
        "user_input": input_text,
        "context": context
    })
    
    # Evaluate output if requested
    if args.evaluate or args.pattern:
        metrics = evaluate_output(
            text=result["output"],
            pattern_name=args.pattern or "default",
            context=context
        )
        result["metrics"] = metrics
        
        if args.pattern:
            log_pattern_usage(args.pattern, metrics["overall"], context)
    
    # Save output if requested
    if args.output:
        save_json(result, args.output)
    else:
        print(json.dumps(result, indent=2))

def run_chain(args):
    """Run an agent chain from JSON config."""
    input_text = read_input_file(args.input) if args.input else args.text
    chain_config = load_json(args.chain)
    
    # Ensure flow is a list
    flow = chain_config if isinstance(chain_config, list) else [chain_config]
    
    context = {}
    if args.context:
        context = load_json(args.context)
    
    mode = ChainMode.ADAPTIVE if args.adaptive else ChainMode.SEQUENTIAL
    
    result = run_agent_chain(
        flow=flow,
        input_text=input_text,
        context=context,
        mode=mode,
        metrics_threshold=args.threshold
    )
    
    # Save output if requested
    if args.output:
        save_json(result, args.output)
    else:
        print(json.dumps(result, indent=2))

def evaluate_text(args):
    """Evaluate text output against pattern and metrics."""
    input_text = read_input_file(args.input)
    
    context = {}
    if args.context:
        context = load_json(args.context)
    
    metrics = evaluate_output(
        text=input_text,
        pattern_name=args.pattern or "default",
        context=context
    )
    
    if args.pattern:
        log_pattern_usage(args.pattern, metrics["overall"], context)
    
    # Save output if requested
    if args.output:
        save_json(metrics, args.output)
    else:
        print(json.dumps(metrics, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Fusion v11.2 CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Run agent command
    run_parser = subparsers.add_parser("run", help="Run a single agent")
    run_parser.add_argument("agent", help="Agent name to run")
    run_parser.add_argument("--pattern", help="Pattern to apply")
    run_parser.add_argument("--tension", help="Creative tension type to apply")
    run_parser.add_argument("--input", help="Input file path")
    run_parser.add_argument("--text", help="Direct input text")
    run_parser.add_argument("--context", help="Context JSON file")
    run_parser.add_argument("--output", help="Output JSON file")
    run_parser.add_argument("--evaluate", action="store_true", help="Evaluate output")
    
    # Run chain command
    chain_parser = subparsers.add_parser("chain", help="Run an agent chain")
    chain_parser.add_argument("chain", help="Chain JSON config file")
    chain_parser.add_argument("--input", help="Input file path")
    chain_parser.add_argument("--text", help="Direct input text")
    chain_parser.add_argument("--context", help="Context JSON file")
    chain_parser.add_argument("--output", help="Output JSON file")
    chain_parser.add_argument("--adaptive", action="store_true", help="Use adaptive mode")
    chain_parser.add_argument("--threshold", type=float, default=0.7, help="Quality threshold")
    
    # Evaluate command
    eval_parser = subparsers.add_parser("evaluate", help="Evaluate text output")
    eval_parser.add_argument("input", help="Input file to evaluate")
    eval_parser.add_argument("--pattern", help="Pattern to evaluate against")
    eval_parser.add_argument("--context", help="Context JSON file")
    eval_parser.add_argument("--output", help="Output JSON file")
    
    args = parser.parse_args()
    
    if args.command == "run":
        if not (args.input or args.text):
            parser.error("Either --input or --text is required")
        run_agent(args)
    elif args.command == "chain":
        if not (args.input or args.text):
            parser.error("Either --input or --text is required")
        run_chain(args)
    elif args.command == "evaluate":
        evaluate_text(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 