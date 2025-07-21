from typing import Dict, List, Optional
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

FUSION_TODO_DIR = Path("_fusion_todo")
MEMORY_FILE = FUSION_TODO_DIR / "memory.json"

class MemoryRegistry:
    """Registry for pattern usage and chain execution memory"""
    def __init__(self):
        self.pattern_uses = []
        self.chain_executions = []
        self._load_memory()
        
    def _load_memory(self):
        """Load memory from file"""
        if MEMORY_FILE.exists():
            with open(MEMORY_FILE, 'r') as f:
                data = json.load(f)
                self.pattern_uses = data.get("pattern_uses", [])
                self.chain_executions = data.get("chain_executions", [])
                
    def _save_memory(self):
        """Save memory to file"""
        os.makedirs(FUSION_TODO_DIR, exist_ok=True)
        with open(MEMORY_FILE, 'w') as f:
            json.dump({
                "pattern_uses": self.pattern_uses,
                "chain_executions": self.chain_executions
            }, f, indent=2)
            
    def record_pattern_use(
        self,
        agent: str,
        pattern: str,
        metrics: Dict[str, float]
    ):
        """Record pattern usage"""
        self.pattern_uses.append({
            "timestamp": datetime.now().isoformat(),
            "agent": agent,
            "pattern": pattern,
            "metrics": metrics
        })
        self._save_memory()
        
    def record_chain_execution(
        self,
        chain_config: Dict,
        metrics: Dict[str, float],
        output: str
    ):
        """Record chain execution"""
        self.chain_executions.append({
            "timestamp": datetime.now().isoformat(),
            "config": chain_config,
            "metrics": metrics,
            "output_preview": output[:200] + "..." if len(output) > 200 else output
        })
        self._save_memory()
        
    def get_pattern_uses(self, minutes: int = 60) -> List[Dict]:
        """Get recent pattern uses"""
        cutoff = (datetime.now() - timedelta(minutes=minutes)).isoformat()
        return [u for u in self.pattern_uses if u["timestamp"] > cutoff]
        
    def get_chain_executions(self, minutes: int = 60) -> List[Dict]:
        """Get recent chain executions"""
        cutoff = (datetime.now() - timedelta(minutes=minutes)).isoformat()
        return [e for e in self.chain_executions if e["timestamp"] > cutoff]
        
    def get_best_pattern(self, agent: str) -> Optional[str]:
        """Get best performing pattern for agent"""
        recent_uses = self.get_pattern_uses()
        
        # Filter uses by agent
        agent_uses = [u for u in recent_uses if u["agent"] == agent]
        if not agent_uses:
            return None
            
        # Calculate average metrics per pattern
        pattern_scores = {}
        for use in agent_uses:
            pattern = use["pattern"]
            metrics = use["metrics"]
            
            if pattern not in pattern_scores:
                pattern_scores[pattern] = {
                    "total": sum(metrics.values()),
                    "count": 1
                }
            else:
                pattern_scores[pattern]["total"] += sum(metrics.values())
                pattern_scores[pattern]["count"] += 1
                
        # Find pattern with highest average score
        best_pattern = None
        best_score = 0
        
        for pattern, scores in pattern_scores.items():
            avg_score = scores["total"] / scores["count"]
            if avg_score > best_score:
                best_score = avg_score
                best_pattern = pattern
                
        return best_pattern

# Global instance
memory = MemoryRegistry() 