from typing import Dict, List, Optional
import json
import os
from datetime import datetime

class MemoryRegistry:
    def __init__(self, storage_path: str = "_fusion_todo/memory_registry.json"):
        self.storage_path = storage_path
        self._ensure_storage()
        self.memory = self._load_memory()
        
    def _ensure_storage(self):
        """Ensure storage directory and file exist"""
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, 'w') as f:
                json.dump({
                    "agent_patterns": {},
                    "pattern_performance": {},
                    "chain_history": [],
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2)

    def _load_memory(self) -> Dict:
        """Load memory from storage"""
        with open(self.storage_path, 'r') as f:
            return json.load(f)

    def _save_memory(self):
        """Save current memory state"""
        self.memory["last_updated"] = datetime.now().isoformat()
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def record_pattern_use(self, agent: str, pattern: str, metrics: Dict[str, float]):
        """Record pattern usage and success metrics"""
        if agent not in self.memory["agent_patterns"]:
            self.memory["agent_patterns"][agent] = {}
        
        if pattern not in self.memory["agent_patterns"][agent]:
            self.memory["agent_patterns"][agent][pattern] = {
                "uses": 0,
                "success_rate": 0.0,
                "avg_metrics": {}
            }
        
        entry = self.memory["agent_patterns"][agent][pattern]
        entry["uses"] += 1
        
        # Update running averages for metrics
        for metric, value in metrics.items():
            if metric not in entry["avg_metrics"]:
                entry["avg_metrics"][metric] = value
            else:
                old_avg = entry["avg_metrics"][metric]
                entry["avg_metrics"][metric] = (old_avg * (entry["uses"] - 1) + value) / entry["uses"]
        
        # Update success rate (assuming threshold of 0.7 for success)
        success = all(v >= 0.7 for v in metrics.values())
        old_successes = entry["success_rate"] * (entry["uses"] - 1)
        entry["success_rate"] = (old_successes + (1 if success else 0)) / entry["uses"]
        
        self._save_memory()

    def record_chain_execution(self, chain_config: List[Dict], metrics: Dict[str, float], output: str):
        """Record chain execution history"""
        self.memory["chain_history"].append({
            "timestamp": datetime.now().isoformat(),
            "chain_config": chain_config,
            "metrics": metrics,
            "output_summary": output[:500] + "..." if len(output) > 500 else output
        })
        
        # Keep only last 100 chain executions
        if len(self.memory["chain_history"]) > 100:
            self.memory["chain_history"] = self.memory["chain_history"][-100:]
        
        self._save_memory()

    def get_best_pattern(self, agent: str, task_type: Optional[str] = None) -> Optional[str]:
        """Get best performing pattern for an agent"""
        if agent not in self.memory["agent_patterns"]:
            return None
            
        patterns = self.memory["agent_patterns"][agent]
        if not patterns:
            return None
            
        # Sort by success rate and usage count
        sorted_patterns = sorted(
            patterns.items(),
            key=lambda x: (x[1]["success_rate"], x[1]["uses"]),
            reverse=True
        )
        
        return sorted_patterns[0][0] if sorted_patterns else None

    def get_pattern_metrics(self, pattern: str) -> Dict:
        """Get aggregated metrics for a pattern"""
        metrics = {
            "total_uses": 0,
            "avg_success_rate": 0.0,
            "agent_specific": {}
        }
        
        for agent, patterns in self.memory["agent_patterns"].items():
            if pattern in patterns:
                metrics["total_uses"] += patterns[pattern]["uses"]
                metrics["avg_success_rate"] += patterns[pattern]["success_rate"]
                metrics["agent_specific"][agent] = patterns[pattern]
        
        if metrics["total_uses"] > 0:
            metrics["avg_success_rate"] /= len(metrics["agent_specific"])
            
        return metrics

    def generate_insights_report(self) -> str:
        """Generate a markdown report of system insights"""
        report = ["# Fusion System Insights\n"]
        
        # Pattern Performance
        report.append("## Pattern Performance\n")
        for pattern in set(p for a in self.memory["agent_patterns"].values() for p in a.keys()):
            metrics = self.get_pattern_metrics(pattern)
            report.append(f"### {pattern}\n")
            report.append(f"- Total Uses: {metrics['total_uses']}\n")
            report.append(f"- Average Success Rate: {metrics['avg_success_rate']:.2%}\n")
            report.append("- Agent-Specific Performance:\n")
            for agent, data in metrics["agent_specific"].items():
                report.append(f"  - {agent}: {data['success_rate']:.2%} success ({data['uses']} uses)\n")
            report.append("\n")
        
        # Recent Chains
        report.append("## Recent Chain Executions\n")
        for chain in self.memory["chain_history"][-5:]:
            report.append(f"### {chain['timestamp']}\n")
            report.append("Chain Configuration:\n```json\n")
            report.append(json.dumps(chain["chain_config"], indent=2))
            report.append("\n```\n")
            report.append(f"Overall Metrics: {json.dumps(chain['metrics'], indent=2)}\n\n")
        
        return "\n".join(report)

# Global instance
memory = MemoryRegistry() 