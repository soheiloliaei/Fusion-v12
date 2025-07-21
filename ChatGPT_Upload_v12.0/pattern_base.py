from typing import Optional
from dataclasses import dataclass

@dataclass
class PatternConfig:
    """Pattern configuration"""
    name: str
    description: str
    example: str
    safety_mode: bool = True
    
class BasePattern:
    """Base class for prompt patterns"""
    def __init__(self, config: Optional[PatternConfig] = None):
        self.config = config or PatternConfig(
            name="base",
            description="Base pattern",
            example="Example usage",
            safety_mode=True
        )
        
    def apply(self, text: str) -> str:
        """Apply pattern to text"""
        # Apply pattern
        output = self._apply_pattern(text)
        
        # Apply safety rules if enabled
        if self.config.safety_mode:
            from pattern_safety import PatternSafety
            output = PatternSafety.apply_safety_rules(output, self.config.name)
            
        return output
        
    def _apply_pattern(self, text: str) -> str:
        """Pattern-specific implementation"""
        raise NotImplementedError() 