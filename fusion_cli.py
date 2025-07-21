#!/usr/bin/env python3
import argparse
import json
import sys
import os
from typing import Dict, Optional
from agent_chain import AgentChain
from execution_mode_map import ExecutionMode

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
    os.makedirs("_fusion_todo/chains", exist_ok=True)
    path = f"_fusion_todo/chains/chain_config.json"
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    return path

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
        
        # Load chain config
        if args.chain:
            chain_config = load_chain_config(args.chain)
            chain_config["execution_mode"] = args.mode
        else:
            # Use template or default config
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
        
        # Save output
        save_output(result, args.output)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 