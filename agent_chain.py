"""
Enhanced agent chain system for Fusion v11.2.
Provides sequential agent execution with pattern application, creative tension, and metrics tracking.
"""

from typing import Dict, List, Optional
import json
from dataclasses import dataclass
from datetime import datetime
import os

from memory_registry import memory
from evaluator_metrics import evaluate_output
from execution_mode_map import get_mode_config, apply_mode_to_agent, apply_mode_to_pattern
from prompt_pattern_registry import get_pattern_by_name, get_fallback_pattern
from input_transformer import transform_output_to_input

@dataclass
class ChainConfig:
    """Chain configuration"""
    execution_mode: str
    chain: List[Dict]
    success_criteria: Optional[Dict] = None
    max_iterations: int = 3

class AgentChain:
    def __init__(self, config_path: str):
        """Initialize chain from config file"""
        with open(config_path, 'r') as f:
            config_data = json.load(f)
            
        self.config = ChainConfig(
            execution_mode=config_data.get("execution_mode", "simulate"),
            chain=config_data.get("chain", []),
            success_criteria=config_data.get("success_criteria"),
            max_iterations=config_data.get("max_iterations", 3)
        )
        
        self.mode_config = get_mode_config(self.config.execution_mode)
        self.metrics = {}
        self.chain_output = ""
        self.reasoning_trail = []
        
    def execute(self, input_text: str, adaptive: bool = True) -> Dict:
        """Execute the chain"""
        self.chain_output = input_text
        self.reasoning_trail = []
        
        for step in self.config.chain:
            # Get step configuration
            agent = step["agent"]
            pattern = step["pattern"]
            step_config = step.get("config", {})
            
            # Apply mode-specific configuration
            agent_config = apply_mode_to_agent(
                agent_name=agent,
                mode=self.config.execution_mode,
                base_config=step_config
            )
            
            pattern_config = apply_mode_to_pattern(
                pattern_name=pattern,
                mode=self.config.execution_mode,
                base_config=step_config
            )
            
            # Execute step
            step_output = self._execute_step(
                agent=agent,
                pattern=pattern,
                input_text=self.chain_output,
                agent_config=agent_config,
                pattern_config=pattern_config
            )
            
            # Evaluate output
            metrics = evaluate_output(
                text=step_output,
                pattern_name=pattern
            )
            
            # Record execution
            memory.record_pattern_use(agent, pattern, metrics)
            
            # Check if metrics meet threshold
            threshold = self.mode_config.critique_threshold
            if adaptive and any(v < threshold for v in metrics.values()):
                # Try fallback pattern
                fallback_pattern = get_fallback_pattern(pattern)
                if fallback_pattern:
                    fallback_output = self._execute_step(
                        agent=agent,
                        pattern=fallback_pattern,
                        input_text=self.chain_output,
                        agent_config=agent_config,
                        pattern_config=pattern_config
                    )
                    
                    fallback_metrics = evaluate_output(
                        text=fallback_output,
                        pattern_name=fallback_pattern
                    )
                    
                    # Use better result
                    if all(v >= threshold for v in fallback_metrics.values()):
                        step_output = fallback_output
                        metrics = fallback_metrics
                        pattern = fallback_pattern
                        memory.record_pattern_use(agent, pattern, metrics)
            
            # Transform output for next step
            self.chain_output = transform_output_to_input(
                step_output,
                agent,
                mode=self.config.execution_mode
            )
            
            # Update metrics
            self.metrics.update(metrics)
            
            # Record reasoning trail
            self.reasoning_trail.append({
                "step": len(self.reasoning_trail) + 1,
                "agent": agent,
                "pattern": pattern,
                "metrics": metrics,
                "output_preview": step_output[:200] + "..." if len(step_output) > 200 else step_output
            })
            
        # Generate trail markdown
        self._generate_reasoning_trail()
        
        return {
            "output": self.chain_output,
            "metrics": self.metrics,
            "reasoning_trail": self.reasoning_trail
        }
        
    def _execute_step(
        self,
        agent: str,
        pattern: str,
        input_text: str,
        agent_config: Dict,
        pattern_config: Dict
    ) -> str:
        """Execute single chain step"""
        # Get pattern
        pattern_obj = get_pattern_by_name(pattern)
        if not pattern_obj:
            raise ValueError(f"Pattern not found: {pattern}")
            
        # Apply pattern
        return pattern_obj.apply(input_text)
        
    def _generate_reasoning_trail(self):
        """Generate markdown reasoning trail"""
        trail = [
            f"# Chain Execution Report\n",
            f"Mode: {self.config.execution_mode}",
            f"Time: {datetime.now().isoformat()}\n",
            "## Steps\n"
        ]
        
        for step in self.reasoning_trail:
            trail.extend([
                f"### Step {step['step']}: {step['agent']}",
                f"Pattern: {step['pattern']}\n",
                "Metrics:",
                *[f"- {k}: {v:.2f}" for k, v in step['metrics'].items()],
                "\nOutput Preview:",
                step['output_preview'],
                "\n---\n"
            ])
            
        # Save trail
        os.makedirs("_fusion_todo", exist_ok=True)
        with open("_fusion_todo/reasoning_trail.md", "w") as f:
            f.write("\n".join(trail)) 