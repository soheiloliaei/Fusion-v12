#!/usr/bin/env python3
"""
Fusion v11 Monitoring System
Integrates v10 monitoring capabilities with v11 enhancements
"""

import os
import sys
import time
import json
import psutil
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import threading
from dataclasses import dataclass, asdict

@dataclass
class SystemHealth:
    """System health metrics."""
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    agent_performance: Dict[str, float]
    trust_calibration_quality: float
    bias_detection_accuracy: float
    overall_health_score: float
    timestamp: float

@dataclass
class AgentMetrics:
    """Individual agent performance metrics."""
    agent_id: str
    response_time_ms: float
    success_rate: float
    confidence_accuracy: float
    quality_score: float
    trust_score: float
    bias_score: float
    last_updated: float

class FusionV11Monitor:
    """Comprehensive monitoring system for Fusion v11."""
    
    def __init__(self, workspace_path: Optional[str] = None):
        self.workspace_path = workspace_path or os.getcwd()
        self.data_file = os.path.join(self.workspace_path, "fusion_v11_monitor_data.json")
        self.config_file = os.path.join(self.workspace_path, "fusion_v11_monitor_config.json")
        
        # Load or create monitoring data
        self.monitoring_data = self._load_monitoring_data()
        self.config = self._load_config()
        
        # Agent performance tracking
        self.agent_metrics = {}
        self.system_health_history = []
        
        # V11 specific monitoring
        self.execution_mode_metrics = {}
        self.personality_overlay_metrics = {}
        self.creative_tension_metrics = {}
        self.design_craft_metrics = {}
        
        # Monitoring thread
        self.monitoring_active = False
        self.monitoring_thread = None
    
    def _load_monitoring_data(self) -> Dict[str, Any]:
        """Load existing monitoring data or create new."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "version": "11.0",
            "created": time.time(),
            "last_update": time.time(),
            "sessions": [],
            "metrics_history": [],
            "alerts": [],
            "improvements_suggested": [],
            "system_health_snapshots": [],
            "agent_performance_history": {},
            "v11_enhancement_metrics": {
                "execution_modes": {},
                "personality_overlays": {},
                "creative_tensions": {},
                "design_craft_scores": []
            }
        }
    
    def _load_config(self) -> Dict[str, Any]:
        """Load monitoring configuration."""
        default_config = {
            "monitoring_enabled": True,
            "check_interval_seconds": 300,  # 5 minutes
            "alert_thresholds": {
                "cpu_usage": 80,
                "memory_usage": 85,
                "disk_usage": 90,
                "agent_response_time": 1000,  # ms
                "trust_calibration_quality": 0.8,
                "bias_detection_accuracy": 0.9
            },
            "track_files": ["*.py", "*.json", "*.md", "*.yaml"],
            "git_monitoring": True,
            "auto_suggestions": True,
            "v11_features": {
                "execution_mode_tracking": True,
                "personality_overlay_monitoring": True,
                "creative_tension_analysis": True,
                "design_craft_metrics": True
            }
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
            except:
                pass
        
        return default_config
    
    def start_monitoring(self):
        """Start continuous monitoring."""
        if not self.monitoring_active:
            self.monitoring_active = True
            self.monitoring_thread = threading.Thread(target=self._monitoring_loop)
            self.monitoring_thread.daemon = True
            self.monitoring_thread.start()
            print("🔍 Fusion v11 monitoring started")
    
    def stop_monitoring(self):
        """Stop continuous monitoring."""
        self.monitoring_active = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        print("⏹️  Fusion v11 monitoring stopped")
    
    def _monitoring_loop(self):
        """Main monitoring loop."""
        while self.monitoring_active:
            try:
                # Collect comprehensive metrics
                system_health = self.collect_system_health()
                agent_metrics = self.collect_agent_metrics()
                v11_metrics = self.collect_v11_enhancement_metrics()
                
                # Store metrics
                self.system_health_history.append(system_health)
                self.monitoring_data["system_health_snapshots"].append(asdict(system_health))
                
                # Check for alerts
                alerts = self.check_for_alerts(system_health, agent_metrics)
                if alerts:
                    self.monitoring_data["alerts"].extend(alerts)
                
                # Generate suggestions
                suggestions = self.generate_optimization_suggestions(system_health, agent_metrics, v11_metrics)
                if suggestions:
                    self.monitoring_data["improvements_suggested"].extend(suggestions)
                
                # Save data
                self._save_data()
                
                # Wait for next check
                time.sleep(self.config["check_interval_seconds"])
                
            except Exception as e:
                print(f"⚠️  Monitoring error: {e}")
                time.sleep(60)  # Wait 1 minute before retrying
    
    def collect_system_health(self) -> SystemHealth:
        """Collect comprehensive system health metrics."""
        # Basic system metrics
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        # Agent performance summary
        agent_performance = {}
        for agent_id, metrics in self.agent_metrics.items():
            agent_performance[agent_id] = metrics.quality_score
        
        # V11 specific metrics
        trust_calibration_quality = self._calculate_average_trust_quality()
        bias_detection_accuracy = self._calculate_average_bias_accuracy()
        
        # Overall health score
        health_components = [
            (100 - cpu_usage) / 100,  # CPU health
            (100 - memory_usage) / 100,  # Memory health
            (100 - disk_usage) / 100,  # Disk health
            trust_calibration_quality,
            bias_detection_accuracy
        ]
        overall_health_score = sum(health_components) / len(health_components)
        
        return SystemHealth(
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            disk_usage=disk_usage,
            agent_performance=agent_performance,
            trust_calibration_quality=trust_calibration_quality,
            bias_detection_accuracy=bias_detection_accuracy,
            overall_health_score=overall_health_score,
            timestamp=time.time()
        )
    
    def collect_agent_metrics(self) -> Dict[str, AgentMetrics]:
        """Collect individual agent performance metrics."""
        # This would be populated by actual agent executions
        # For now, return current tracked metrics
        return self.agent_metrics.copy()
    
    def collect_v11_enhancement_metrics(self) -> Dict[str, Any]:
        """Collect v11 enhancement-specific metrics."""
        return {
            "execution_modes": self.execution_mode_metrics.copy(),
            "personality_overlays": self.personality_overlay_metrics.copy(),
            "creative_tensions": self.creative_tension_metrics.copy(),
            "design_craft_metrics": self.design_craft_metrics.copy()
        }
    
    def update_agent_metrics(self, agent_id: str, response_time_ms: float, 
                           success_rate: float, confidence_accuracy: float,
                           quality_score: float, trust_score: float = 0.85,
                           bias_score: float = 0.05):
        """Update metrics for a specific agent."""
        self.agent_metrics[agent_id] = AgentMetrics(
            agent_id=agent_id,
            response_time_ms=response_time_ms,
            success_rate=success_rate,
            confidence_accuracy=confidence_accuracy,
            quality_score=quality_score,
            trust_score=trust_score,
            bias_score=bias_score,
            last_updated=time.time()
        )
    
    def update_v11_metrics(self, execution_mode: str, personality_overlay: Optional[str] = None,
                          creative_tension: Optional[str] = None, design_craft_scores: Optional[Dict[str, float]] = None):
        """Update v11 enhancement metrics."""
        # Track execution mode usage
        if execution_mode not in self.execution_mode_metrics:
            self.execution_mode_metrics[execution_mode] = {"count": 0, "avg_performance": 0.0}
        self.execution_mode_metrics[execution_mode]["count"] += 1
        
        # Track personality overlay usage
        if personality_overlay:
            if personality_overlay not in self.personality_overlay_metrics:
                self.personality_overlay_metrics[personality_overlay] = {"count": 0, "avg_effectiveness": 0.0}
            self.personality_overlay_metrics[personality_overlay]["count"] += 1
        
        # Track creative tension usage
        if creative_tension:
            if creative_tension not in self.creative_tension_metrics:
                self.creative_tension_metrics[creative_tension] = {"count": 0, "avg_balance": 0.0}
            self.creative_tension_metrics[creative_tension]["count"] += 1
        
        # Track design craft scores
        if design_craft_scores:
            self.design_craft_metrics[time.time()] = design_craft_scores
    
    def check_for_alerts(self, system_health: SystemHealth, agent_metrics: Dict[str, AgentMetrics]) -> List[Dict[str, Any]]:
        """Check for system alerts based on thresholds."""
        alerts = []
        thresholds = self.config["alert_thresholds"]
        
        # System resource alerts
        if system_health.cpu_usage > thresholds["cpu_usage"]:
            alerts.append({
                "type": "high_cpu_usage",
                "severity": "warning",
                "message": f"CPU usage at {system_health.cpu_usage:.1f}%",
                "timestamp": time.time()
            })
        
        if system_health.memory_usage > thresholds["memory_usage"]:
            alerts.append({
                "type": "high_memory_usage",
                "severity": "warning",
                "message": f"Memory usage at {system_health.memory_usage:.1f}%",
                "timestamp": time.time()
            })
        
        # Agent performance alerts
        for agent_id, metrics in agent_metrics.items():
            if metrics.response_time_ms > thresholds["agent_response_time"]:
                alerts.append({
                    "type": "slow_agent_response",
                    "severity": "warning",
                    "message": f"Agent {agent_id} response time: {metrics.response_time_ms:.0f}ms",
                    "timestamp": time.time()
                })
        
        # V11 specific alerts
        if system_health.trust_calibration_quality < thresholds["trust_calibration_quality"]:
            alerts.append({
                "type": "low_trust_calibration",
                "severity": "critical",
                "message": f"Trust calibration quality at {system_health.trust_calibration_quality:.2f}",
                "timestamp": time.time()
            })
        
        if system_health.bias_detection_accuracy < thresholds["bias_detection_accuracy"]:
            alerts.append({
                "type": "low_bias_detection",
                "severity": "critical",
                "message": f"Bias detection accuracy at {system_health.bias_detection_accuracy:.2f}",
                "timestamp": time.time()
            })
        
        return alerts
    
    def generate_optimization_suggestions(self, system_health: SystemHealth, 
                                        agent_metrics: Dict[str, AgentMetrics],
                                        v11_metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate optimization suggestions based on metrics."""
        suggestions = []
        
        # System optimization suggestions
        if system_health.cpu_usage > 70:
            suggestions.append({
                "type": "performance_optimization",
                "priority": "medium",
                "suggestion": "Consider optimizing agent execution for better CPU utilization",
                "details": f"Current CPU usage: {system_health.cpu_usage:.1f}%",
                "timestamp": time.time()
            })
        
        # Agent-specific suggestions
        slow_agents = [agent_id for agent_id, metrics in agent_metrics.items() 
                      if metrics.response_time_ms > 800]
        if slow_agents:
            suggestions.append({
                "type": "agent_optimization",
                "priority": "high",
                "suggestion": f"Optimize response time for agents: {', '.join(slow_agents)}",
                "details": "Consider caching or algorithm improvements",
                "timestamp": time.time()
            })
        
        # V11 enhancement suggestions
        if len(self.execution_mode_metrics) < 3:
            suggestions.append({
                "type": "v11_enhancement",
                "priority": "low",
                "suggestion": "Explore more execution modes for better task handling",
                "details": "Currently using limited execution modes",
                "timestamp": time.time()
            })
        
        return suggestions
    
    def _calculate_average_trust_quality(self) -> float:
        """Calculate average trust calibration quality."""
        if not self.agent_metrics:
            return 0.85  # Default value
        
        trust_scores = [metrics.trust_score for metrics in self.agent_metrics.values()]
        return sum(trust_scores) / len(trust_scores) if trust_scores else 0.85
    
    def _calculate_average_bias_accuracy(self) -> float:
        """Calculate average bias detection accuracy."""
        if not self.agent_metrics:
            return 0.95  # Default value
        
        # Bias score is inverted (lower is better), so accuracy is 1 - bias_score
        bias_scores = [1 - metrics.bias_score for metrics in self.agent_metrics.values()]
        return sum(bias_scores) / len(bias_scores) if bias_scores else 0.95
    
    def _save_data(self):
        """Save monitoring data to file."""
        self.monitoring_data["last_update"] = time.time()
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.monitoring_data, f, indent=2)
        except Exception as e:
            print(f"⚠️  Could not save monitoring data: {e}")
    
    def generate_dashboard_report(self) -> Dict[str, Any]:
        """Generate comprehensive dashboard report."""
        if not self.system_health_history:
            return {"error": "No monitoring data available"}
        
        latest_health = self.system_health_history[-1]
        
        # Calculate trends
        if len(self.system_health_history) >= 2:
            previous_health = self.system_health_history[-2]
            health_trend = latest_health.overall_health_score - previous_health.overall_health_score
        else:
            health_trend = 0.0
        
        return {
            "system_overview": {
                "overall_health_score": latest_health.overall_health_score,
                "health_trend": health_trend,
                "cpu_usage": latest_health.cpu_usage,
                "memory_usage": latest_health.memory_usage,
                "disk_usage": latest_health.disk_usage,
                "timestamp": latest_health.timestamp
            },
            "agent_performance": {
                "total_agents": len(self.agent_metrics),
                "average_response_time": self._calculate_average_response_time(),
                "average_quality_score": self._calculate_average_quality_score(),
                "top_performing_agents": self._get_top_performing_agents(3)
            },
            "v11_enhancements": {
                "execution_modes_used": len(self.execution_mode_metrics),
                "personality_overlays_used": len(self.personality_overlay_metrics),
                "creative_tensions_analyzed": len(self.creative_tension_metrics),
                "design_craft_average": self._calculate_average_design_craft()
            },
            "trust_and_bias": {
                "trust_calibration_quality": latest_health.trust_calibration_quality,
                "bias_detection_accuracy": latest_health.bias_detection_accuracy
            },
            "recent_alerts": self.monitoring_data["alerts"][-5:],  # Last 5 alerts
            "optimization_suggestions": self.monitoring_data["improvements_suggested"][-3:]  # Last 3 suggestions
        }
    
    def _calculate_average_response_time(self) -> float:
        """Calculate average response time across all agents."""
        if not self.agent_metrics:
            return 0.0
        
        response_times = [metrics.response_time_ms for metrics in self.agent_metrics.values()]
        return sum(response_times) / len(response_times)
    
    def _calculate_average_quality_score(self) -> float:
        """Calculate average quality score across all agents."""
        if not self.agent_metrics:
            return 0.0
        
        quality_scores = [metrics.quality_score for metrics in self.agent_metrics.values()]
        return sum(quality_scores) / len(quality_scores)
    
    def _get_top_performing_agents(self, count: int) -> List[Dict[str, Any]]:
        """Get top performing agents."""
        if not self.agent_metrics:
            return []
        
        sorted_agents = sorted(self.agent_metrics.items(), 
                             key=lambda x: x[1].quality_score, reverse=True)
        
        return [
            {
                "agent_id": agent_id,
                "quality_score": metrics.quality_score,
                "response_time_ms": metrics.response_time_ms
            }
            for agent_id, metrics in sorted_agents[:count]
        ]
    
    def _calculate_average_design_craft(self) -> float:
        """Calculate average design craft score."""
        if not self.design_craft_metrics:
            return 0.0
        
        all_scores = []
        for timestamp, scores in self.design_craft_metrics.items():
            all_scores.extend(scores.values())
        
        return sum(all_scores) / len(all_scores) if all_scores else 0.0
    
    def display_dashboard(self):
        """Display monitoring dashboard."""
        report = self.generate_dashboard_report()
        
        if "error" in report:
            print(f"❌ {report['error']}")
            return
        
        print("\n" + "="*70)
        print("🚀 FUSION V11 MONITORING DASHBOARD")
        print("="*70)
        
        # System overview
        system = report["system_overview"]
        print(f"\n📊 SYSTEM HEALTH: {system['overall_health_score']:.1%}")
        print(f"   📈 Trend: {'+' if system['health_trend'] >= 0 else ''}{system['health_trend']:.2%}")
        print(f"   🖥️  CPU: {system['cpu_usage']:.1f}%")
        print(f"   🧠 Memory: {system['memory_usage']:.1f}%")
        print(f"   💾 Disk: {system['disk_usage']:.1f}%")
        
        # Agent performance
        agents = report["agent_performance"]
        print(f"\n🤖 AGENT PERFORMANCE")
        print(f"   🎯 Total Agents: {agents['total_agents']}")
        print(f"   ⚡ Avg Response: {agents['average_response_time']:.0f}ms")
        print(f"   📊 Avg Quality: {agents['average_quality_score']:.1%}")
        
        if agents["top_performing_agents"]:
            print(f"   🏆 Top Performers:")
            for agent in agents["top_performing_agents"]:
                print(f"      • {agent['agent_id']}: {agent['quality_score']:.1%} ({agent['response_time_ms']:.0f}ms)")
        
        # V11 enhancements
        v11 = report["v11_enhancements"]
        print(f"\n✨ V11 ENHANCEMENTS")
        print(f"   🎭 Execution Modes: {v11['execution_modes_used']}")
        print(f"   👤 Personality Overlays: {v11['personality_overlays_used']}")
        print(f"   ⚖️  Creative Tensions: {v11['creative_tensions_analyzed']}")
        print(f"   🎨 Design Craft Avg: {v11['design_craft_average']:.1%}")
        
        # Trust and bias
        trust = report["trust_and_bias"]
        print(f"\n🛡️  TRUST & BIAS")
        print(f"   🤝 Trust Calibration: {trust['trust_calibration_quality']:.1%}")
        print(f"   🔍 Bias Detection: {trust['bias_detection_accuracy']:.1%}")
        
        # Recent alerts
        if report["recent_alerts"]:
            print(f"\n🚨 RECENT ALERTS")
            for alert in report["recent_alerts"]:
                severity_icon = "🔴" if alert["severity"] == "critical" else "🟡"
                print(f"   {severity_icon} {alert['message']}")
        
        # Optimization suggestions
        if report["optimization_suggestions"]:
            print(f"\n💡 OPTIMIZATION SUGGESTIONS")
            for suggestion in report["optimization_suggestions"]:
                priority_icon = "🔴" if suggestion["priority"] == "high" else "🟡" if suggestion["priority"] == "medium" else "🟢"
                print(f"   {priority_icon} {suggestion['suggestion']}")
        
        print(f"\n⏰ Last updated: {datetime.fromtimestamp(system['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main function for standalone monitoring."""
    monitor = FusionV11Monitor()
    
    # Start monitoring
    monitor.start_monitoring()
    
    try:
        # Display dashboard every 30 seconds
        while True:
            monitor.display_dashboard()
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n🛑 Stopping monitoring...")
        monitor.stop_monitoring()

if __name__ == "__main__":
    main() 