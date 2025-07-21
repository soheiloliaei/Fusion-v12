#!/usr/bin/env python3
import argparse
import json
import sys
import os
from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

from memory_registry import memory
from agent_chain import AgentChain

class ExecutionMode(Enum):
    SIMULATE = "simulate"  # For exploration and testing
    SHIP = "ship"         # For production-ready output
    CRITIQUE = "critique" # For analysis and improvement

@dataclass
class ChainTemplate:
    """Predefined chain configurations"""
    name: str
    description: str
    agents: List[Dict]
    mode: ExecutionMode
    
    @classmethod
    def get_templates(cls) -> Dict[str, 'ChainTemplate']:
        return {
            "strategy": ChainTemplate(
                name="strategy",
                description="Strategic analysis and planning",
                agents=[
                    {"agent": "StrategyPilot", "pattern": "StepwiseInsightSynthesis"},
                    {"agent": "NarrativeArchitect", "pattern": "RoleDirective"},
                    {"agent": "EvaluatorAgent", "pattern": "PatternCritiqueThenRewrite"}
                ],
                mode=ExecutionMode.SIMULATE
            ),
            "critique": ChainTemplate(
                name="critique",
                description="Deep analysis and improvement",
                agents=[
                    {"agent": "EvaluatorAgent", "pattern": "PatternCritiqueThenRewrite"},
                    {"agent": "StrategyPilot", "pattern": "StepwiseInsightSynthesis"}
                ],
                mode=ExecutionMode.CRITIQUE
            ),
            "ship": ChainTemplate(
                name="ship",
                description="Production-ready output generation",
                agents=[
                    {"agent": "StrategyPilot", "pattern": "StepwiseInsightSynthesis"},
                    {"agent": "NarrativeArchitect", "pattern": "RoleDirective"},
                    {"agent": "EvaluatorAgent", "pattern": "PatternCritiqueThenRewrite"}
                ],
                mode=ExecutionMode.SHIP
            )
        }

class FusionCLI:
    def __init__(self):
        self.templates = ChainTemplate.get_templates()
        self._ensure_workspace()
        
    def _ensure_workspace(self):
        """Ensure workspace directories exist"""
        os.makedirs("_fusion_todo", exist_ok=True)
        os.makedirs("_fusion_todo/chains", exist_ok=True)
        os.makedirs("_fusion_todo/outputs", exist_ok=True)
        
    def _save_chain_config(self, template: ChainTemplate, input_text: str) -> str:
        """Save chain configuration for execution"""
        config = {
            "timestamp": datetime.now().isoformat(),
            "mode": template.mode.value,
            "agents": template.agents,
            "input": input_text
        }
        
        filename = f"_fusion_todo/chains/chain_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(config, f, indent=2)
            
        return filename
        
    def _save_output(self, output: Dict, template: ChainTemplate) -> str:
        """Save execution output"""
        filename = f"_fusion_todo/outputs/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump({
                "template": template.name,
                "mode": template.mode.value,
                "timestamp": datetime.now().isoformat(),
                **output
            }, f, indent=2)
            
        return filename
        
    def execute(self, template_name: str, input_text: str, adaptive: bool = True) -> Dict:
        """Execute a chain template"""
        if template_name not in self.templates:
            raise ValueError(f"Unknown template: {template_name}")
            
        template = self.templates[template_name]
        
        # Save chain configuration
        config_file = self._save_chain_config(template, input_text)
        
        # Create and execute chain
        chain = AgentChain(config_file)
        result = chain.execute(input_text, adaptive=adaptive)
        
        # Save output
        output_file = self._save_output(result, template)
        
        # Generate report
        self._generate_execution_report(template, result, config_file, output_file)
        
        return result
        
    def _generate_execution_report(
        self, 
        template: ChainTemplate,
        result: Dict,
        config_file: str,
        output_file: str
    ):
        """Generate markdown execution report"""
        report = [
            f"# Fusion Execution Report\n",
            f"## Template: {template.name}",
            f"Mode: {template.mode.value}",
            f"Time: {datetime.now().isoformat()}\n",
            "## Configuration",
            f"- Config file: `{config_file}`",
            f"- Output file: `{output_file}`\n",
            "## Execution Summary",
            "### Metrics",
        ]
        
        for metric, value in result["metrics"].items():
            report.append(f"- {metric}: {value:.2f}")
            
        report.append("\n### Reasoning Trail\n")
        for step in result["reasoning_trail"]:
            report.append(f"#### Step {step['step']}: {step['agent']}")
            report.append(f"Pattern: {step['pattern']}\n")
            report.append("Metrics:")
            for metric, value in step["metrics"].items():
                report.append(f"- {metric}: {value:.2f}")
            report.append("\n")
            
        # Save report
        report_file = f"_fusion_todo/outputs/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(report_file, "w") as f:
            f.write("\n".join(report))

def main():
    parser = argparse.ArgumentParser(description="Fusion v11.2 CLI")
    parser.add_argument(
        "mode",
        choices=["simulate", "ship", "critique"],
        help="Execution mode"
    )
    parser.add_argument(
        "input",
        help="Input text or task description"
    )
    parser.add_argument(
        "--template", "-t",
        default=None,
        help="Chain template to use (default: based on mode)"
    )
    parser.add_argument(
        "--no-adaptive", "-na",
        action="store_true",
        help="Disable adaptive pattern switching"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file (default: auto-generated)"
    )
    
    args = parser.parse_args()
    
    try:
        cli = FusionCLI()
        
        # Use mode-specific template if none specified
        template = args.template or args.mode
        
        result = cli.execute(
            template_name=template,
            input_text=args.input,
            adaptive=not args.no_adaptive
        )
        
        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
        else:
            print(json.dumps(result, indent=2))
            
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 