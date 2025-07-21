from typing import Dict, Optional, List
from pattern_base import BasePattern, PatternConfig

class PatternRegistry:
    """Registry of available patterns"""
    _patterns: Dict[str, BasePattern] = {}
    _fallback_preferences: Dict[str, str] = {
        "StepwiseInsightSynthesis": "RoleDirective",
        "RoleDirective": "PatternCritiqueThenRewrite",
        "PatternCritiqueThenRewrite": "StepwiseInsightSynthesis"
    }
    
    @classmethod
    def register(cls, name: str, pattern: BasePattern):
        """Register a pattern"""
        cls._patterns[name] = pattern
        
    @classmethod
    def get_pattern(cls, name: str) -> Optional[BasePattern]:
        """Get pattern by name"""
        return cls._patterns.get(name)
        
    @classmethod
    def get_fallback_pattern(
        cls,
        pattern_name: str,
        config: Optional[PatternConfig] = None
    ) -> Optional[str]:
        """Get fallback pattern name for given pattern"""
        return cls._fallback_preferences.get(pattern_name)
        
    @classmethod
    def list_patterns(cls) -> List[str]:
        """List all registered patterns"""
        return sorted(cls._patterns.keys())

def get_pattern_by_name(name: str) -> Optional[BasePattern]:
    """Get pattern by name"""
    return PatternRegistry.get_pattern(name)
    
def get_fallback_pattern(
    pattern_name: str,
    config: Optional[PatternConfig] = None
) -> Optional[str]:
    """Get fallback pattern for given pattern"""
    return PatternRegistry.get_fallback_pattern(pattern_name, config)
    
def list_patterns() -> List[str]:
    """List all registered patterns"""
    return PatternRegistry.list_patterns()

# Register built-in patterns
from prompt_patterns import (
    StepwiseInsightSynthesis,
    RoleDirective,
    PatternCritiqueThenRewrite,
    RiskLens,
    PersonaFramer,
    SignalExtractor,
    InversePattern,
    ReductionistPrompt,
    StyleTransformer,
    PatternAmplifier
)

# Initialize patterns with default configs
PatternRegistry.register("StepwiseInsightSynthesis", StepwiseInsightSynthesis())
PatternRegistry.register("RoleDirective", RoleDirective())
PatternRegistry.register("PatternCritiqueThenRewrite", PatternCritiqueThenRewrite())
PatternRegistry.register("RiskLens", RiskLens())
PatternRegistry.register("PersonaFramer", PersonaFramer())
PatternRegistry.register("SignalExtractor", SignalExtractor())
PatternRegistry.register("InversePattern", InversePattern())
PatternRegistry.register("ReductionistPrompt", ReductionistPrompt())
PatternRegistry.register("StyleTransformer", StyleTransformer())
PatternRegistry.register("PatternAmplifier", PatternAmplifier()) 