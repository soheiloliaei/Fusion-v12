from typing import Dict, List, Optional
import re
from dataclasses import dataclass
from enum import Enum

class TransformMode(Enum):
    SUMMARY_ONLY = "summary_only"
    KEY_TAKEAWAYS = "key_takeaways"
    STRATEGY_DECISIONS = "strategy_decisions"

@dataclass
class TransformationRules:
    """Rules for transforming output based on agent role"""
    extract_patterns: List[str]
    format_template: str
    required_sections: List[str]

AGENT_TRANSFORM_RULES: Dict[str, TransformationRules] = {
    "StrategyPilot": TransformationRules(
        extract_patterns=[
            r"(?:^|\n)(?:Strategy|Approach|Plan):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:Key Points|Main Ideas):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:Decisions|Choices):\s*(.*?)(?:\n\n|$)"
        ],
        format_template="""Strategic Context:
{summary}

Key Decisions:
{decisions}

Next Steps:
{next_steps}""",
        required_sections=["summary", "decisions"]
    ),
    "NarrativeArchitect": TransformationRules(
        extract_patterns=[
            r"(?:^|\n)(?:Story|Narrative|Flow):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:User Journey|Experience):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:Key Moments|Touchpoints):\s*(.*?)(?:\n\n|$)"
        ],
        format_template="""Narrative Overview:
{story}

User Experience Flow:
{journey}

Key Moments:
{moments}""",
        required_sections=["story", "journey"]
    ),
    "EvaluatorAgent": TransformationRules(
        extract_patterns=[
            r"(?:^|\n)(?:Analysis|Evaluation):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:Strengths|Positives):\s*(.*?)(?:\n\n|$)",
            r"(?:^|\n)(?:Areas for Improvement|Gaps):\s*(.*?)(?:\n\n|$)"
        ],
        format_template="""Evaluation Summary:
{analysis}

Strengths:
{strengths}

Improvement Areas:
{improvements}""",
        required_sections=["analysis", "improvements"]
    )
}

def extract_section(text: str, patterns: List[str]) -> str:
    """Extract content using patterns"""
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE | re.DOTALL)
        if match:
            return match.group(1).strip()
    return ""

def summarize_text(text: str, max_length: int = 500) -> str:
    """Create a brief summary of text"""
    # Simple summarization for v1 - take first paragraph and truncate
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    if not paragraphs:
        return text[:max_length] + "..." if len(text) > max_length else text
        
    summary = paragraphs[0]
    return summary[:max_length] + "..." if len(summary) > max_length else summary

def extract_key_takeaways(text: str) -> List[str]:
    """Extract key points or takeaways"""
    takeaways = []
    
    # Look for bullet points or numbered lists
    bullet_pattern = r"(?:^|\n)[•\-\*]\s*(.*?)(?:\n|$)"
    numbered_pattern = r"(?:^|\n)\d+\.\s*(.*?)(?:\n|$)"
    
    bullets = re.findall(bullet_pattern, text, re.MULTILINE)
    numbers = re.findall(numbered_pattern, text, re.MULTILINE)
    
    takeaways.extend(bullets)
    takeaways.extend(numbers)
    
    # If no structured points found, split by sentences and take first few
    if not takeaways:
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        takeaways = sentences[:5]  # Take first 5 sentences as takeaways
        
    return takeaways

def extract_strategy_decisions(text: str) -> Dict[str, str]:
    """Extract strategic decisions and rationale"""
    decisions = {}
    
    # Look for decision-rationale patterns
    decision_pattern = r"(?:^|\n)(?:Decision|Choice|Strategy):\s*(.*?)\n(?:Rationale|Reason|Why):\s*(.*?)(?:\n\n|$)"
    matches = re.finditer(decision_pattern, text, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    
    for match in matches:
        decision = match.group(1).strip()
        rationale = match.group(2).strip()
        decisions[decision] = rationale
        
    return decisions

def transform_output_to_input(
    output_text: str,
    agent_role: str,
    mode: str = 'summary_only',
    max_length: Optional[int] = None
) -> str:
    """Transform agent output into structured input for next agent"""
    
    # Get transformation rules for agent
    rules = AGENT_TRANSFORM_RULES.get(agent_role)
    if not rules:
        # Default transformation if no specific rules
        if mode == TransformMode.SUMMARY_ONLY.value:
            return summarize_text(output_text, max_length or 500)
        elif mode == TransformMode.KEY_TAKEAWAYS.value:
            takeaways = extract_key_takeaways(output_text)
            return "\n".join(f"• {point}" for point in takeaways)
        elif mode == TransformMode.STRATEGY_DECISIONS.value:
            decisions = extract_strategy_decisions(output_text)
            return "\n\n".join(f"Decision: {k}\nRationale: {v}" for k, v in decisions.items())
        return output_text
        
    # Extract sections using rules
    sections = {}
    for pattern in rules.extract_patterns:
        content = extract_section(output_text, [pattern])
        if content:
            # Use first word of pattern as section key
            key = re.search(r'\w+', pattern).group(0).lower()
            sections[key] = content
            
    # Ensure required sections exist
    for required in rules.required_sections:
        if required not in sections:
            sections[required] = "No content found for this section."
            
    # Apply length limit if specified
    if max_length:
        for key in sections:
            if len(sections[key]) > max_length:
                sections[key] = sections[key][:max_length] + "..."
                
    # Format using template
    try:
        transformed = rules.format_template.format(**sections)
    except KeyError:
        # Fallback if template keys don't match sections
        transformed = "\n\n".join(f"{k.title()}:\n{v}" for k, v in sections.items())
        
    return transformed

def get_available_modes() -> List[str]:
    """Get list of available transformation modes"""
    return [mode.value for mode in TransformMode] 