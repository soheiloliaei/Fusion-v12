"""
Enhanced evaluator metrics for Fusion v11.2 pattern system.
Provides quantitative assessment of pattern outputs with Block-specific metrics.
"""

from typing import Dict, Any, List, Optional, Union
import re

def evaluate_output(text: str, pattern_name: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Evaluate pattern output quality with enhanced metrics."""
    context = context or {}

    # Core metrics from original
    clarity_score = calculate_clarity_score(text)
    structure_adherence = calculate_structure_adherence(text, pattern_name)
    alignment_score = calculate_alignment_score(context)
    completion_score = calculate_completion_score(text)

    # Enhanced metrics for Block context
    block_relevance = calculate_block_relevance(text, context)
    pattern_effectiveness = calculate_pattern_effectiveness(text, pattern_name)
    innovation_score = calculate_innovation_score(text, context)

    # Calculate weighted overall score
    weights = {
        "clarity": 0.15,
        "structure": 0.15,
        "alignment": 0.15,
        "completion": 0.15,
        "block_relevance": 0.15,
        "pattern_effectiveness": 0.15,
        "innovation": 0.10
    }

    overall = round(
        (clarity_score * weights["clarity"] +
         structure_adherence * weights["structure"] +
         alignment_score * weights["alignment"] +
         completion_score * weights["completion"] +
         block_relevance * weights["block_relevance"] +
         pattern_effectiveness * weights["pattern_effectiveness"] +
         innovation_score * weights["innovation"]), 2
    )

    return {
        "clarity_score": clarity_score,
        "structure_adherence": structure_adherence,
        "alignment_score": alignment_score,
        "completion_score": completion_score,
        "block_relevance": block_relevance,
        "pattern_effectiveness": pattern_effectiveness,
        "innovation_score": innovation_score,
        "overall": overall,
        "breakdown": get_score_breakdown(locals(), weights)
    }

def calculate_clarity_score(text: str) -> float:
    """Calculate clarity score with enhanced metrics."""
    base_score = 1.0 if len(text.strip()) > 20 else 0.2
    
    # Additional clarity checks
    has_clear_sections = bool(re.search(r'\n\n|\n[-*•]', text))
    has_proper_capitalization = text[0].isupper() if text else False
    has_proper_formatting = bool(re.search(r'[.!?][\s]*$', text))
    
    modifiers = [
        1.0 if has_clear_sections else 0.8,
        1.0 if has_proper_capitalization else 0.9,
        1.0 if has_proper_formatting else 0.9
    ]
    
    return round(base_score * sum(modifiers) / len(modifiers), 2)

def calculate_structure_adherence(text: str, pattern_name: str) -> float:
    """Calculate how well the output adheres to the pattern structure."""
    base_score = 1.0 if pattern_name in text else 0.5

    pattern_indicators = {
        "StepwiseInsightSynthesis": [
            r'\b\d+[\)\.]\s',  # Numbered steps
            r'insight|analysis|finding'
        ],
        "RoleDirective": [
            r'as\s+[aA]\s+[A-Z][a-z]+',  # Role identification
            r'perspective|viewpoint|stance'
        ],
        "PatternCritiqueThenRewrite": [
            r'critique|analysis|review',
            r'improved|enhanced|rewritten'
        ]
    }

    if pattern_name in pattern_indicators:
        indicators = pattern_indicators[pattern_name]
        matches = sum(1 for indicator in indicators if re.search(indicator, text, re.I))
        indicator_score = matches / len(indicators)
        return round((base_score + indicator_score) / 2, 2)

    return base_score

def calculate_alignment_score(context: dict) -> float:
    """Calculate alignment with context and goals."""
    base_score = 0.9 if 'goal' in context.get('tags', []) else 0.6
    
    # Check for Block-specific alignment
    if context.get('domain') == 'block':
        base_score *= 1.1  # Boost for Block-specific context
    
    # Check for industry alignment
    if 'industry' in context:
        base_score *= 1.05  # Boost for industry context
        
    return round(min(base_score, 1.0), 2)

def calculate_completion_score(text: str) -> float:
    """Calculate completion and coherence score."""
    base_score = 1.0 if text.strip().endswith('.') else 0.7
    
    # Check for complete thoughts
    has_complete_sentences = bool(re.search(r'[.!?]\s+[A-Z]', text))
    has_proper_structure = bool(re.search(r'^[A-Z].*[.!?]$', text.strip()))
    
    modifiers = [
        1.0 if has_complete_sentences else 0.8,
        1.0 if has_proper_structure else 0.9
    ]
    
    return round(base_score * sum(modifiers) / len(modifiers), 2)

def calculate_block_relevance(text: str, context: dict) -> float:
    """Calculate relevance to Block's domain and needs."""
    block_terms = [
        'cash app', 'support', 'customer', 'payment', 'transaction',
        'security', 'compliance', 'user experience', 'workflow'
    ]
    
    term_matches = sum(1 for term in block_terms if term.lower() in text.lower())
    base_score = min(term_matches / len(block_terms) + 0.3, 1.0)
    
    # Context boosts
    if context.get('domain') == 'block':
        base_score = min(base_score + 0.2, 1.0)
    
    return round(base_score, 2)

def calculate_pattern_effectiveness(text: str, pattern_name: str) -> float:
    """Calculate how effectively the pattern achieves its purpose."""
    pattern_purposes = {
        "StepwiseInsightSynthesis": [
            r'step[s]?\s+\d',
            r'insight|finding|analysis',
            r'therefore|thus|conclusion'
        ],
        "RoleDirective": [
            r'as\s+[aA]\s+[A-Z][a-z]+',
            r'recommend|suggest|advise',
            r'expertise|experience|knowledge'
        ],
        "PatternCritiqueThenRewrite": [
            r'issue|problem|concern',
            r'improve|enhance|optimize',
            r'solution|resolution|approach'
        ]
    }
    
    if pattern_name in pattern_purposes:
        indicators = pattern_purposes[pattern_name]
        matches = sum(1 for indicator in indicators if re.search(indicator, text, re.I))
        return round(matches / len(indicators), 2)
    
    return 0.7  # Default score for unknown patterns

def calculate_innovation_score(text: str, context: dict) -> float:
    """Calculate innovation and creativity score."""
    innovation_indicators = [
        r'new|novel|innovative',
        r'unique|creative|original',
        r'breakthrough|revolutionary|transformative'
    ]
    
    matches = sum(1 for indicator in innovation_indicators if re.search(indicator, text, re.I))
    base_score = matches / len(innovation_indicators)
    
    # Context boosts
    if context.get('innovation_required', False):
        base_score = min(base_score + 0.2, 1.0)
    
    return round(base_score, 2)

def get_score_breakdown(scores: dict, weights: dict) -> Dict[str, Any]:
    """Generate detailed breakdown of scores."""
    return {
        "metrics": {
            "clarity": {
                "score": scores["clarity_score"],
                "weight": weights["clarity"],
                "contribution": round(scores["clarity_score"] * weights["clarity"], 3)
            },
            "structure": {
                "score": scores["structure_adherence"],
                "weight": weights["structure"],
                "contribution": round(scores["structure_adherence"] * weights["structure"], 3)
            },
            "alignment": {
                "score": scores["alignment_score"],
                "weight": weights["alignment"],
                "contribution": round(scores["alignment_score"] * weights["alignment"], 3)
            },
            "completion": {
                "score": scores["completion_score"],
                "weight": weights["completion"],
                "contribution": round(scores["completion_score"] * weights["completion"], 3)
            },
            "block_relevance": {
                "score": scores["block_relevance"],
                "weight": weights["block_relevance"],
                "contribution": round(scores["block_relevance"] * weights["block_relevance"], 3)
            },
            "pattern_effectiveness": {
                "score": scores["pattern_effectiveness"],
                "weight": weights["pattern_effectiveness"],
                "contribution": round(scores["pattern_effectiveness"] * weights["pattern_effectiveness"], 3)
            },
            "innovation": {
                "score": scores["innovation_score"],
                "weight": weights["innovation"],
                "contribution": round(scores["innovation_score"] * weights["innovation"], 3)
            }
        },
        "insights": generate_score_insights(scores)
    }

def generate_score_insights(scores: dict) -> List[str]:
    """Generate insights about the evaluation scores."""
    insights = []
    
    if scores["clarity_score"] < 0.7:
        insights.append("Clarity could be improved with better structure and formatting")
    
    if scores["block_relevance"] < 0.7:
        insights.append("Could be more relevant to Block's specific context")
    
    if scores["innovation_score"] < 0.6:
        insights.append("Consider adding more innovative or novel elements")
    
    if scores["pattern_effectiveness"] < 0.7:
        insights.append("Pattern could be applied more effectively")
    
    return insights if insights else ["All metrics are within acceptable ranges"] 