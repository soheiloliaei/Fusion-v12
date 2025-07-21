"""
Enhanced agent chain system for Fusion v11.2.
Provides sequential agent execution with pattern application, creative tension, and metrics tracking.
"""

from typing import Dict, List, Optional
import json
import os
from datetime import datetime
from memory_registry import memory
from evaluator_metrics import evaluate_output

class AgentChain:
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path) if config_path else []
        self.metrics = {}
        self.chain_output = ""
        self.reasoning_trail = []
        
    def _load_config(self, path: str) -> List[Dict]:
        with open(path, 'r') as f:
            return json.load(f)
            
    def _get_fallback_pattern(self, agent: str, current_pattern: str) -> Optional[str]:
        """Get alternative pattern if current one fails"""
        patterns = {
            "StepwiseInsightSynthesis": "RoleDirective",
            "RoleDirective": "PatternCritiqueThenRewrite",
            "PatternCritiqueThenRewrite": "StepwiseInsightSynthesis"
        }
        return patterns.get(current_pattern)
        
    def generate_step_insights(self, step_output: str, metrics: Dict[str, float]) -> Dict:
        """Generate detailed insights for a chain step"""
        insights = {
            "metrics_breakdown": {},
            "improvement_suggestions": [],
            "pattern_effectiveness": metrics.get("pattern_effectiveness", 0.0)
        }
        
        # Analyze individual metrics
        for metric, value in metrics.items():
            insights["metrics_breakdown"][metric] = {
                "score": value,
                "interpretation": "Good" if value >= 0.8 else "Fair" if value >= 0.6 else "Needs Improvement"
            }
            
            if value < 0.7:
                insights["improvement_suggestions"].append(f"Consider improving {metric}")
                
        return insights
        
    def execute(self, input_text: str, adaptive: bool = True) -> Dict:
        """Execute the agent chain with memory and adaptive pattern switching"""
        self.chain_output = input_text
        self.reasoning_trail = []
        
        for step in self.config:
            agent = step["agent"]
            pattern = step["pattern"]
            metrics_threshold = step.get("metrics_threshold", 0.7)
            
            # Check memory for better pattern
            if adaptive:
                best_pattern = memory.get_best_pattern(agent)
                if best_pattern and best_pattern != pattern:
                    pattern = best_pattern
                    
            # Execute step
            step_output = self._execute_step(agent, pattern, self.chain_output)
            metrics = evaluate_output(
                text=step_output,
                pattern_name=pattern
            )
            
            # Generate insights
            insights = self.generate_step_insights(step_output, metrics)
            
            # Record execution
            memory.record_pattern_use(agent, pattern, metrics)
            
            # Check if metrics meet threshold
            if adaptive and any(v < metrics_threshold for v in metrics.values()):
                fallback_pattern = self._get_fallback_pattern(agent, pattern)
                if fallback_pattern:
                    # Try fallback pattern
                    fallback_output = self._execute_step(agent, fallback_pattern, self.chain_output)
                    fallback_metrics = evaluate_output(
                        text=fallback_output,
                        pattern_name=fallback_pattern
                    )
                    
                    # Use better result
                    if all(v >= metrics_threshold for v in fallback_metrics.values()):
                        step_output = fallback_output
                        metrics = fallback_metrics
                        pattern = fallback_pattern
                        memory.record_pattern_use(agent, pattern, metrics)
            
            # Update chain state
            self.chain_output = step_output
            self.metrics = {**self.metrics, **metrics}
            
            # Record reasoning trail
            self.reasoning_trail.append({
                "step": len(self.reasoning_trail) + 1,
                "agent": agent,
                "pattern": pattern,
                "metrics": metrics,
                "insights": insights
            })
            
        # Record chain execution
        memory.record_chain_execution(self.config, self.metrics, self.chain_output)
        
        # Generate trail markdown
        self._generate_reasoning_trail()
        
        return {
            "output": self.chain_output,
            "metrics": self.metrics,
            "reasoning_trail": self.reasoning_trail
        }
        
    def _execute_step(self, agent: str, pattern: str, input_text: str) -> str:
        """Execute single chain step (implement agent-specific logic here)"""
        # TODO: Implement actual agent execution
        return f"Output from {agent} using {pattern} on input: {input_text[:100]}..."
        
    def _generate_reasoning_trail(self):
        """Generate markdown reasoning trail"""
        trail = ["# Chain Execution Reasoning Trail\n"]
        
        for step in self.reasoning_trail:
            trail.append(f"## Step {step['step']}: {step['agent']}\n")
            trail.append(f"Pattern: {step['pattern']}\n\n")
            
            trail.append("### Metrics\n")
            for metric, value in step["metrics"].items():
                trail.append(f"- {metric}: {value:.2f}\n")
            
            trail.append("\n### Insights\n")
            for metric, data in step["insights"]["metrics_breakdown"].items():
                trail.append(f"- {metric}: {data['score']:.2f} ({data['interpretation']})\n")
            
            if step["insights"]["improvement_suggestions"]:
                trail.append("\nImprovement Suggestions:\n")
                for suggestion in step["insights"]["improvement_suggestions"]:
                    trail.append(f"- {suggestion}\n")
            
            trail.append("\n---\n")
        
        # Save trail
        os.makedirs("_fusion_todo", exist_ok=True)
        with open("_fusion_todo/reasoning_trail.md", "w") as f:
            f.write("\n".join(trail)) 