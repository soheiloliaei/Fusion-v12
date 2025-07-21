from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json
from pathlib import Path
import os

from memory_registry import memory

FUSION_TODO_DIR = Path("_fusion_todo")
STATS_FILE = FUSION_TODO_DIR / "pattern_stats.json"

class PatternStats:
    """Pattern statistics tracker"""
    def __init__(self):
        self.stats = self._load_stats()
        
    def _load_stats(self) -> Dict:
        """Load or initialize stats"""
        if STATS_FILE.exists():
            with open(STATS_FILE, 'r') as f:
                return json.load(f)
        return {
            "patterns": {},
            "agents": {},
            "modes": {},
            "last_updated": datetime.now().isoformat()
        }
        
    def _save_stats(self):
        """Save current stats"""
        os.makedirs(FUSION_TODO_DIR, exist_ok=True)
        with open(STATS_FILE, 'w') as f:
            json.dump(self.stats, f, indent=2)
            
    def update_stats(self, minutes: int = 60):
        """Update stats from recent memory"""
        # Get recent data
        pattern_uses = memory.get_pattern_uses(minutes)
        chain_executions = memory.get_chain_executions(minutes)
        
        # Reset stats
        self.stats = {
            "patterns": {},
            "agents": {},
            "modes": {},
            "last_updated": datetime.now().isoformat()
        }
        
        # Process pattern uses
        for use in pattern_uses:
            pattern = use["pattern"]
            agent = use["agent"]
            metrics = use["metrics"]
            
            # Update pattern stats
            if pattern not in self.stats["patterns"]:
                self.stats["patterns"][pattern] = {
                    "uses": 0,
                    "avg_metrics": {},
                    "success_rate": 0.0,
                    "fallback_rate": 0.0
                }
                
            pattern_stats = self.stats["patterns"][pattern]
            pattern_stats["uses"] += 1
            
            # Update metrics
            for metric, value in metrics.items():
                if isinstance(value, (int, float)):
                    if metric not in pattern_stats["avg_metrics"]:
                        pattern_stats["avg_metrics"][metric] = value
                    else:
                        old_avg = pattern_stats["avg_metrics"][metric]
                        pattern_stats["avg_metrics"][metric] = (old_avg * (pattern_stats["uses"] - 1) + value) / pattern_stats["uses"]
                        
            # Update success rate
            success = all(isinstance(v, (int, float)) and v >= 0.7 for v in metrics.values())
            old_successes = pattern_stats["success_rate"] * (pattern_stats["uses"] - 1)
            pattern_stats["success_rate"] = (old_successes + (1 if success else 0)) / pattern_stats["uses"]
            
            # Update agent stats
            if agent not in self.stats["agents"]:
                self.stats["agents"][agent] = {
                    "patterns": {},
                    "total_uses": 0,
                    "success_rate": 0.0
                }
                
            agent_stats = self.stats["agents"][agent]
            agent_stats["total_uses"] += 1
            
            if pattern not in agent_stats["patterns"]:
                agent_stats["patterns"][pattern] = {
                    "uses": 0,
                    "success_rate": 0.0
                }
                
            pattern_stats = agent_stats["patterns"][pattern]
            pattern_stats["uses"] += 1
            old_successes = pattern_stats["success_rate"] * (pattern_stats["uses"] - 1)
            pattern_stats["success_rate"] = (old_successes + (1 if success else 0)) / pattern_stats["uses"]
            
        # Process chain executions
        for execution in chain_executions:
            mode = execution["config"].get("execution_mode", "simulate")
            metrics = execution["metrics"]
            
            if mode not in self.stats["modes"]:
                self.stats["modes"][mode] = {
                    "executions": 0,
                    "avg_metrics": {},
                    "success_rate": 0.0
                }
                
            mode_stats = self.stats["modes"][mode]
            mode_stats["executions"] += 1
            
            # Update metrics
            for metric, value in metrics.items():
                if isinstance(value, (int, float)):
                    if metric not in mode_stats["avg_metrics"]:
                        mode_stats["avg_metrics"][metric] = value
                    else:
                        old_avg = mode_stats["avg_metrics"][metric]
                        mode_stats["avg_metrics"][metric] = (old_avg * (mode_stats["executions"] - 1) + value) / mode_stats["executions"]
                        
            # Update success rate
            success = all(isinstance(v, (int, float)) and v >= 0.7 for v in metrics.values())
            old_successes = mode_stats["success_rate"] * (mode_stats["executions"] - 1)
            mode_stats["success_rate"] = (old_successes + (1 if success else 0)) / mode_stats["executions"]
            
        self._save_stats()
        
    def generate_report(self) -> str:
        """Generate markdown report of current stats"""
        report = [
            f"# Pattern Statistics Report\n",
            f"Last Updated: {self.stats['last_updated']}\n",
            "## Pattern Performance\n"
        ]
        
        # Pattern stats
        for pattern, stats in sorted(self.stats["patterns"].items()):
            report.extend([
                f"### {pattern}\n",
                f"- Uses: {stats['uses']}",
                f"- Success Rate: {stats['success_rate']:.2%}",
                f"- Fallback Rate: {stats['fallback_rate']:.2%}",
                "\nAverage Metrics:"
            ])
            
            for metric, value in stats["avg_metrics"].items():
                report.append(f"- {metric}: {value:.2f}")
                
            report.append("\n")
            
        # Agent stats
        report.append("## Agent Performance\n")
        for agent, stats in sorted(self.stats["agents"].items()):
            report.extend([
                f"### {agent}\n",
                f"- Total Uses: {stats['total_uses']}",
                f"- Success Rate: {stats['success_rate']:.2%}",
                "\nPattern Usage:"
            ])
            
            for pattern, pattern_stats in stats["patterns"].items():
                report.append(f"- {pattern}: {pattern_stats['uses']} uses, {pattern_stats['success_rate']:.2%} success")
                
            report.append("\n")
            
        # Mode stats
        report.append("## Execution Mode Performance\n")
        for mode, stats in sorted(self.stats["modes"].items()):
            report.extend([
                f"### {mode}\n",
                f"- Executions: {stats['executions']}",
                f"- Success Rate: {stats['success_rate']:.2%}",
                "\nAverage Metrics:"
            ])
            
            for metric, value in stats["avg_metrics"].items():
                report.append(f"- {metric}: {value:.2f}")
                
            report.append("\n")
            
        return "\n".join(report)

# Global instance
stats = PatternStats() 