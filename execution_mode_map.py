from typing import Dict, Any
from enum import Enum
from dataclasses import dataclass

class ExecutionMode(Enum):
    SIMULATE = "simulate"
    SHIP = "ship"
    CRITIQUE = "critique"

@dataclass
class ModeConfig:
    """Configuration for an execution mode"""
    tone: str
    innovation_weight: float
    clarity_weight: float
    critique_threshold: float
    pattern_modifiers: Dict[str, float]
    agent_modifiers: Dict[str, Dict[str, float]]

EXECUTION_MODE_BEHAVIOR: Dict[str, ModeConfig] = {
    "simulate": ModeConfig(
        tone="exploratory",
        innovation_weight=1.2,
        clarity_weight=0.8,
        critique_threshold=0.6,
        pattern_modifiers={
            "StepwiseInsightSynthesis": 1.1,  # Amplify step breakdown
            "RoleDirective": 0.9,             # Reduce role constraints
            "PatternCritiqueThenRewrite": 1.0  # Normal critique level
        },
        agent_modifiers={
            "StrategyPilot": {
                "innovation_bias": 1.2,
                "practicality_bias": 0.8
            },
            "NarrativeArchitect": {
                "creativity_bias": 1.2,
                "structure_bias": 0.8
            },
            "EvaluatorAgent": {
                "exploration_bias": 1.2,
                "strictness_bias": 0.8
            }
        }
    ),
    "ship": ModeConfig(
        tone="precise",
        innovation_weight=0.8,
        clarity_weight=1.2,
        critique_threshold=0.8,
        pattern_modifiers={
            "StepwiseInsightSynthesis": 1.2,  # Emphasize clear steps
            "RoleDirective": 1.1,             # Strengthen role alignment
            "PatternCritiqueThenRewrite": 1.1  # Higher critique bar
        },
        agent_modifiers={
            "StrategyPilot": {
                "innovation_bias": 0.8,
                "practicality_bias": 1.2
            },
            "NarrativeArchitect": {
                "creativity_bias": 0.8,
                "structure_bias": 1.2
            },
            "EvaluatorAgent": {
                "exploration_bias": 0.8,
                "strictness_bias": 1.2
            }
        }
    ),
    "critique": ModeConfig(
        tone="analytical",
        innovation_weight=0.9,
        clarity_weight=1.1,
        critique_threshold=0.9,
        pattern_modifiers={
            "StepwiseInsightSynthesis": 1.0,  # Normal step analysis
            "RoleDirective": 1.2,             # Strong role perspective
            "PatternCritiqueThenRewrite": 1.3  # Maximum critique level
        },
        agent_modifiers={
            "StrategyPilot": {
                "innovation_bias": 0.9,
                "practicality_bias": 1.1
            },
            "NarrativeArchitect": {
                "creativity_bias": 0.9,
                "structure_bias": 1.1
            },
            "EvaluatorAgent": {
                "exploration_bias": 0.7,
                "strictness_bias": 1.3
            }
        }
    )
}

def get_mode_config(mode: str) -> ModeConfig:
    """Get configuration for execution mode"""
    if mode not in EXECUTION_MODE_BEHAVIOR:
        # Return default mode config
        return ModeConfig(
            tone="balanced",
            innovation_weight=1.0,
            clarity_weight=1.0,
            critique_threshold=0.7,
            pattern_modifiers={},
            agent_modifiers={}
        )
    return EXECUTION_MODE_BEHAVIOR[mode]

def apply_mode_to_agent(
    agent_name: str,
    mode: str,
    base_config: Dict[str, Any]
) -> Dict[str, Any]:
    """Apply execution mode modifiers to agent configuration"""
    mode_config = get_mode_config(mode)
    
    # Start with base config
    config = base_config.copy()
    
    # Apply mode-specific modifiers
    if agent_name in mode_config.agent_modifiers:
        modifiers = mode_config.agent_modifiers[agent_name]
        for key, modifier in modifiers.items():
            if key in config and isinstance(config[key], (int, float)):
                config[key] *= modifier
                
    # Add mode metadata
    config["execution_mode"] = mode
    config["tone"] = mode_config.tone
    config["critique_threshold"] = mode_config.critique_threshold
    
    return config

def apply_mode_to_pattern(
    pattern_name: str,
    mode: str,
    base_config: Dict[str, Any]
) -> Dict[str, Any]:
    """Apply execution mode modifiers to pattern configuration"""
    mode_config = get_mode_config(mode)
    
    # Start with base config
    config = base_config.copy()
    
    # Apply pattern-specific modifier
    if pattern_name in mode_config.pattern_modifiers:
        modifier = mode_config.pattern_modifiers[pattern_name]
        if "effectiveness_weight" in config and isinstance(config["effectiveness_weight"], (int, float)):
            config["effectiveness_weight"] *= modifier
            
    # Apply global mode weights
    config["innovation_weight"] = mode_config.innovation_weight
    config["clarity_weight"] = mode_config.clarity_weight
    
    return config

def get_available_modes() -> Dict[str, str]:
    """Get dictionary of available modes and their descriptions"""
    return {
        "simulate": "Exploratory mode for testing and ideation",
        "ship": "Production mode for deliverable output",
        "critique": "Analysis mode for deep evaluation"
    } 