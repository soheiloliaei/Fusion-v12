"""
Enhanced evaluator metrics for Fusion v11.2 pattern system.
Provides quantitative assessment of pattern outputs with Block-specific metrics.
"""

from typing import Dict, Any, List, Optional, Union, Tuple
import re
from dataclasses import dataclass

@dataclass
class MetricResult:
    """Result of a metric evaluation"""
    score: float
    reason: Optional[str] = None
    confidence: Optional[float] = None

def evaluate_clarity(text: str) -> MetricResult:
    """Evaluate text clarity"""
    # Count sentences
    sentences = len(re.split(r'[.!?]+', text))
    
    # Count words per sentence
    words = len(text.split())
    avg_words = words / max(sentences, 1)
    
    # Check for complex words (>3 syllables)
    complex_words = len([w for w in text.split() if len(re.findall(r'[aeiou]', w.lower())) > 3])
    complex_ratio = complex_words / max(words, 1)
    
    # Calculate base score
    base_score = max(0.0, min(1.0, 1.0 - (avg_words - 15) / 30 - complex_ratio))
    
    # Calculate confidence
    confidence = min(1.0, sentences / 10)
    
    # Generate reason
    reasons = []
    if avg_words > 25:
        reasons.append("Sentences are too long")
    if complex_ratio > 0.2:
        reasons.append("Too many complex words")
        
    return MetricResult(
        score=base_score,
        reason="; ".join(reasons) if reasons else None,
        confidence=confidence
    )

def evaluate_innovation(text: str) -> MetricResult:
    """Evaluate innovation level"""
    # Count unique words
    words = text.lower().split()
    unique_ratio = len(set(words)) / len(words)
    
    # Check for innovation markers
    innovation_markers = [
        "novel", "innovative", "unique", "creative",
        "breakthrough", "original", "revolutionary"
    ]
    marker_count = sum(1 for w in words if w in innovation_markers)
    
    # Calculate base score
    base_score = max(0.0, min(1.0, unique_ratio + marker_count * 0.1))
    
    # Calculate confidence
    confidence = min(1.0, len(words) / 200)
    
    # Generate reason
    reasons = []
    if unique_ratio < 0.4:
        reasons.append("Low vocabulary diversity")
    if marker_count == 0:
        reasons.append("No innovation markers found")
        
    return MetricResult(
        score=base_score,
        reason="; ".join(reasons) if reasons else None,
        confidence=confidence
    )

def evaluate_pattern_effectiveness(text: str, pattern_name: str) -> MetricResult:
    """Evaluate how well the text follows the pattern"""
    # Pattern-specific checks
    pattern_markers = {
        "StepwiseInsightSynthesis": [
            r"Step \d+",
            r"First,|Next,|Finally,",
            r"This leads to|Therefore,"
        ],
        "RoleDirective": [
            r"As a|From the perspective",
            r"would|should|must",
            r"recommend|suggest|advise"
        ],
        "PatternCritiqueThenRewrite": [
            r"Issues?:|Problems?:",
            r"Instead,|Better approach",
            r"Improved version"
        ]
    }
    
    if pattern_name not in pattern_markers:
        return MetricResult(
            score=0.5,
            reason="Unknown pattern",
            confidence=0.0
        )
        
    # Check for pattern markers
    markers = pattern_markers[pattern_name]
    matches = sum(1 for m in markers if re.search(m, text))
    marker_score = matches / len(markers)
    
    # Calculate confidence
    confidence = min(1.0, matches / len(markers))
    
    # Generate reason
    reasons = []
    if marker_score < 0.5:
        reasons.append(f"Missing key {pattern_name} elements")
    if matches == 0:
        reasons.append("No pattern markers found")
        
    return MetricResult(
        score=marker_score,
        reason="; ".join(reasons) if reasons else None,
        confidence=confidence
    )

def evaluate_output(text: str, pattern_name: str) -> Dict[str, Union[float, Optional[str]]]:
    """Evaluate output text and return metrics"""
    # Get individual metrics
    clarity = evaluate_clarity(text)
    innovation = evaluate_innovation(text)
    effectiveness = evaluate_pattern_effectiveness(text, pattern_name)
    
    # Calculate overall confidence
    confidence = min(
        clarity.confidence or 0.0,
        innovation.confidence or 0.0,
        effectiveness.confidence or 0.0
    )
    
    # Collect reasons for potential fallback
    fallback_reasons = []
    if clarity.reason:
        fallback_reasons.append(f"Clarity: {clarity.reason}")
    if innovation.reason:
        fallback_reasons.append(f"Innovation: {innovation.reason}")
    if effectiveness.reason:
        fallback_reasons.append(f"Pattern: {effectiveness.reason}")
        
    return {
        "clarity_score": clarity.score,
        "innovation_score": innovation.score,
        "pattern_effectiveness": effectiveness.score,
        "confidence_score": confidence,
        "fallback_reason": "; ".join(fallback_reasons) if fallback_reasons else None
    } 