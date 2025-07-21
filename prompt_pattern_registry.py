from typing import Dict, Optional, Type
from prompt_patterns import (
    BasePattern,
    StepwiseInsightSynthesis,
    RoleDirective,
    PatternCritiqueThenRewrite,
    RiskLens,
    PersonaFramer,
    SignalExtractor,
    InversePattern,
    ReductionistPrompt,
    StyleTransformer,
    PatternAmplifier,
    PatternConfig
)

class PatternRegistry:
    """Registry for prompt patterns"""
    _patterns: Dict[str, Type[BasePattern]] = {
        "StepwiseInsightSynthesis": StepwiseInsightSynthesis,
        "RoleDirective": RoleDirective,
        "PatternCritiqueThenRewrite": PatternCritiqueThenRewrite,
        "RiskLens": RiskLens,
        "PersonaFramer": PersonaFramer,
        "SignalExtractor": SignalExtractor,
        "InversePattern": InversePattern,
        "ReductionistPrompt": ReductionistPrompt,
        "StyleTransformer": StyleTransformer,
        "PatternAmplifier": PatternAmplifier
    }
    
    _fallback_preferences: Dict[str, str] = {
        "StepwiseInsightSynthesis": "RoleDirective",
        "RoleDirective": "PatternCritiqueThenRewrite",
        "PatternCritiqueThenRewrite": "StepwiseInsightSynthesis",
        "RiskLens": "PatternCritiqueThenRewrite",
        "PersonaFramer": "RoleDirective",
        "SignalExtractor": "StepwiseInsightSynthesis",
        "InversePattern": "RiskLens",
        "ReductionistPrompt": "StepwiseInsightSynthesis",
        "StyleTransformer": "RoleDirective",
        "PatternAmplifier": "PatternCritiqueThenRewrite"
    }
    
    @classmethod
    def get_pattern(
        cls,
        pattern_name: str,
        config: Optional[PatternConfig] = None
    ) -> Optional[BasePattern]:
        """Get pattern instance by name"""
        pattern_class = cls._patterns.get(pattern_name)
        if pattern_class:
            return pattern_class(config)
        return None
        
    @classmethod
    def get_fallback_pattern(
        cls,
        pattern_name: str,
        config: Optional[PatternConfig] = None
    ) -> Optional[BasePattern]:
        """Get fallback pattern for given pattern"""
        fallback_name = cls._fallback_preferences.get(pattern_name)
        if fallback_name:
            return cls.get_pattern(fallback_name, config)
        return None
        
    @classmethod
    def get_available_patterns(cls) -> Dict[str, str]:
        """Get dictionary of available patterns and descriptions"""
        return {
            name: pattern.__doc__ or ""
            for name, pattern in cls._patterns.items()
        }
        
    @classmethod
    def register_pattern(
        cls,
        name: str,
        pattern_class: Type[BasePattern],
        fallback: Optional[str] = None
    ):
        """Register a new pattern"""
        cls._patterns[name] = pattern_class
        if fallback:
            cls._fallback_preferences[name] = fallback

# Global functions for easy access
def get_pattern_by_name(
    pattern_name: str,
    config: Optional[PatternConfig] = None
) -> Optional[BasePattern]:
    """Get pattern instance by name"""
    return PatternRegistry.get_pattern(pattern_name, config)

def get_fallback_pattern(
    pattern_name: str,
    config: Optional[PatternConfig] = None
) -> Optional[BasePattern]:
    """Get fallback pattern for given pattern"""
    return PatternRegistry.get_fallback_pattern(pattern_name, config)

def get_available_patterns() -> Dict[str, str]:
    """Get dictionary of available patterns and descriptions"""
    return PatternRegistry.get_available_patterns()

def register_pattern(
    name: str,
    pattern_class: Type[BasePattern],
    fallback: Optional[str] = None
):
    """Register a new pattern"""
    PatternRegistry.register_pattern(name, pattern_class, fallback) 