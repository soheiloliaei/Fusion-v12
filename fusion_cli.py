#!/usr/bin/env python3
import argparse
import json
import sys
import os
from datetime import datetime
from typing import Dict, Optional, List
from pathlib import Path

from agent_chain import AgentChain
from execution_mode_map import ExecutionMode, get_mode_config
from input_transformer import transform_output_to_input
from prompt_pattern_registry import get_pattern_by_name

CHAIN_TEMPLATES_DIR = Path("chain_templates")
FUSION_TODO_DIR = Path("_fusion_todo")
CHAIN_RUN_LOGS_DIR = FUSION_TODO_DIR / "chain_run_logs"

def load_input(path: str) -> str:
    """Load input from file"""
    with open(path, 'r') as f:
        return f.read()

def load_chain_config(path: str) -> Dict:
    """Load chain configuration"""
    with open(path, 'r') as f:
        return json.load(f)

def save_output(output: Dict, path: Optional[str] = None):
    """Save output to file or print to stdout"""
    if path:
        with open(path, 'w') as f:
            json.dump(output, f, indent=2)
    else:
        print(json.dumps(output, indent=2))

def save_chain_config(config: Dict) -> str:
    """Save chain config and return path"""
    os.makedirs(FUSION_TODO_DIR / "chains", exist_ok=True)
    path = FUSION_TODO_DIR / "chains" / "chain_config.json"
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    return str(path)

def run_chain_from_template(
    template_name: str,
    mode: str,
    input_text: str,
    adaptive: bool = True
) -> Dict:
    """Run chain from template"""
    # Load template
    template_path = CHAIN_TEMPLATES_DIR / f"{template_name}.json"
    if not template_path.exists():
        raise ValueError(f"Template not found: {template_name}")
        
    template = load_chain_config(str(template_path))
    
    # Override mode
    template["execution_mode"] = mode
    
    # Save config
    config_path = save_chain_config(template)
    
    # Create and run chain
    chain = AgentChain(config_path)
    result = chain.execute(input_text=input_text, adaptive=adaptive)
    
    # Log execution
    log_chain_execution(template, result)
    
    return result

def log_chain_execution(template: Dict, result: Dict):
    """Log chain execution details"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create log directory
    os.makedirs(CHAIN_RUN_LOGS_DIR, exist_ok=True)
    
    # Generate markdown log
    log = [
        f"# Chain Execution Log - {timestamp}\n",
        f"## Template: {template.get('name', 'unnamed')}\n",
        f"Mode: {template.get('execution_mode', 'unknown')}\n",
        "## Chain Steps\n"
    ]
    
    for step in result.get("reasoning_trail", []):
        log.extend([
            f"### Step {step['step']}: {step['agent']}",
            f"Pattern: {step['pattern']}\n",
            "#### Metrics",
            *[f"- {k}: {v:.2f}" for k, v in step['metrics'].items()],
            "\n#### Output Preview",
            step['output_preview'],
            "\n---\n"
        ])
        
    # Save log
    log_path = CHAIN_RUN_LOGS_DIR / f"chain_run_{timestamp}.md"
    with open(log_path, 'w') as f:
        f.write("\n".join(log))

def main():
    parser = argparse.ArgumentParser(description="Fusion v12.0 CLI")
    
    parser.add_argument(
        "mode",
        choices=["simulate", "ship", "critique"],
        help="Execution mode"
    )
    
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input text file"
    )
    
    parser.add_argument(
        "--chain",
        "-c",
        help="Chain configuration JSON file"
    )
    
    parser.add_argument(
        "--template",
        "-t",
        help="Chain template name"
    )
    
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file (default: stdout)"
    )
    
    parser.add_argument(
        "--no-adaptive",
        "-na",
        action="store_true",
        help="Disable adaptive pattern switching"
    )
    
    args = parser.parse_args()
    
    try:
        # Load input
        input_text = load_input(args.input)
        
        if args.template:
            # Run from template
            result = run_chain_from_template(
                template_name=args.template,
                mode=args.mode,
                input_text=input_text,
                adaptive=not args.no_adaptive
            )
        else:
            # Load chain config
            if args.chain:
                chain_config = load_chain_config(args.chain)
                chain_config["execution_mode"] = args.mode
            else:
                # Use default config
                chain_config = {
                    "execution_mode": args.mode,
                    "chain": [
                        {
                            "agent": "StrategyPilot",
                            "pattern": "StepwiseInsightSynthesis"
                        },
                        {
                            "agent": "NarrativeArchitect",
                            "pattern": "RoleDirective"
                        },
                        {
                            "agent": "EvaluatorAgent",
                            "pattern": "PatternCritiqueThenRewrite"
                        }
                    ]
                }
            
            # Save config and create chain
            config_path = save_chain_config(chain_config)
            chain = AgentChain(config_path)
            
            # Execute chain
            result = chain.execute(
                input_text=input_text,
                adaptive=not args.no_adaptive
            )
            
            # Log execution
            log_chain_execution(chain_config, result)
        
        # Save output
        save_output(result, args.output)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 