#!/usr/bin/env python3
"""
Fusion v11.2 CLI Entrypoint
Enables command-line access to agents, chains, and evaluation.
"""

import argparse
import json
import sys
from pathlib import Path

from agent_chain import AgentChain

def main():
    parser = argparse.ArgumentParser(description="Fusion Debug Mode")
    parser.add_argument("--input", required=True,
                      help="Input text file")
    parser.add_argument("--config", required=True,
                      help="Chain configuration file")
    parser.add_argument("--output",
                      help="Output JSON file")
    parser.add_argument("--no-adaptive", action="store_true",
                      help="Disable adaptive pattern switching")
    args = parser.parse_args()
    
    try:
        # Load input
        with open(args.input, 'r') as f:
            input_text = f.read()
            
        # Load config
        with open(args.config, 'r') as f:
            chain_config = json.load(f)
            
        # Create and run chain
        chain = AgentChain(args.config)
        result = chain.execute(
            input_text=input_text,
            adaptive=not args.no_adaptive
        )
        
        # Save or print output
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
        else:
            print("\nOutput:")
            print(result["output"])
            print("\nMetrics:")
            for k, v in result["metrics"].items():
                if isinstance(v, (int, float)):
                    print(f"{k}: {v:.2f}")
                else:
                    print(f"{k}: {v}")
            if result.get("fallbacks"):
                print("\nFallbacks:")
                for f in result["fallbacks"]:
                    print(f"- {f['agent']} -> {f['fallback_pattern']} ({f['reason']})")
                    
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 