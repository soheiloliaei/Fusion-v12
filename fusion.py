#!/usr/bin/env python3
"""
Fusion v11.2 CLI Entrypoint
Enables command-line access to agents, chains, and evaluation.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any
import os
import traceback

from agent_chain import AgentChain
from pattern_safety import PatternSafety
from memory_registry import memory
from evaluator_metrics import evaluate_output

FUSION_TODO_DIR = Path("_fusion_todo")
DEBUG_LOGS_DIR = FUSION_TODO_DIR / "debug_logs"

def debug_run(
    input_text: str,
    chain_config: Dict[str, Any],
    output_path: Optional[str] = None
) -> Dict[str, Any]:
    """Run chain in debug mode with detailed logging"""
    # Initialize chain
    config_path = save_chain_config(chain_config)
    chain = AgentChain(config_path)
    
    # Initialize debug log
    debug_log = {
        "timestamp": datetime.now().isoformat(),
        "input": input_text,
        "config": chain_config,
        "steps": [],
        "safety_events": [],
        "memory_stats": {}
    }
    
    try:
        # Execute chain
        result = chain.execute(input_text)
        
        # Get safety events
        safety_events = PatternSafety.get_recent_events()
        
        # Get memory stats
        memory_stats = {
            "pattern_uses": memory.get_pattern_uses(),
            "chain_executions": memory.get_chain_executions()
        }
        
        # Update debug log
        debug_log.update({
            "output": result["output"],
            "metrics": result["metrics"],
            "steps": result["reasoning_trail"],
            "safety_events": safety_events,
            "memory_stats": memory_stats
        })
        
        # Generate markdown report
        report = [
            f"# Fusion Debug Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "## Input",
            input_text,
            "\n## Configuration",
            f"```json\n{json.dumps(chain_config, indent=2)}\n```\n",
            "## Execution Steps\n"
        ]
        
        for step in result["reasoning_trail"]:
            report.extend([
                f"### Step {step['step']}: {step['agent']}",
                f"Pattern: {step['pattern']}\n",
                "#### Input Preview",
                step.get("input_preview", "N/A"),
                "\n#### Output Preview",
                step["output_preview"],
                "\n#### Metrics",
                *[f"- {k}: {v:.2f}" if isinstance(v, float) else f"- {k}: {v}"
                  for k, v in step["metrics"].items()],
                "\n---\n"
            ])
            
        if safety_events:
            report.extend([
                "## Safety Events\n",
                *[f"- {e['pattern']}: {e['rule']} ({e['timestamp']})"
                  for e in safety_events],
                "\n"
            ])
            
        report.extend([
            "## Memory Statistics\n",
            *[f"- {k}: {v}" for k, v in memory_stats.items()],
            "\n## Final Output",
            result["output"]
        ])
        
        # Save report
        os.makedirs(DEBUG_LOGS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON debug log
        json_path = DEBUG_LOGS_DIR / f"debug_log_{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump(debug_log, f, indent=2)
            
        # Save markdown report
        md_path = DEBUG_LOGS_DIR / f"debug_report_{timestamp}.md"
        with open(md_path, 'w') as f:
            f.write("\n".join(report))
            
        # Save to output path if specified
        if output_path:
            with open(output_path, 'w') as f:
                json.dump(debug_log, f, indent=2)
                
        return debug_log
        
    except Exception as e:
        error_log = {
            **debug_log,
            "error": str(e),
            "traceback": traceback.format_exc()
        }
        
        # Save error log
        os.makedirs(DEBUG_LOGS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        error_path = DEBUG_LOGS_DIR / f"error_log_{timestamp}.json"
        with open(error_path, 'w') as f:
            json.dump(error_log, f, indent=2)
            
        raise

def save_chain_config(config: Dict[str, Any]) -> str:
    """Save chain config and return path"""
    os.makedirs(FUSION_TODO_DIR / "chains", exist_ok=True)
    path = FUSION_TODO_DIR / "chains" / "chain_config.json"
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    return str(path)

def main():
    parser = argparse.ArgumentParser(description="Fusion v12.0 Debug Runner")
    
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input text file"
    )
    
    parser.add_argument(
        "--config",
        "-c",
        required=True,
        help="Chain configuration JSON file"
    )
    
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file (default: auto-generated)"
    )
    
    args = parser.parse_args()
    
    try:
        # Load input
        with open(args.input, 'r') as f:
            input_text = f.read()
            
        # Load config
        with open(args.config, 'r') as f:
            chain_config = json.load(f)
            
        # Run in debug mode
        debug_run(
            input_text=input_text,
            chain_config=chain_config,
            output_path=args.output
        )
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 