from prompt_patterns import StepwiseInsightSynthesis, RoleDirective, PatternCritiqueThenRewrite, PromptPattern

# Registry of available patterns
PATTERN_REGISTRY = {
    "StepwiseInsightSynthesis": StepwiseInsightSynthesis(),
    "RoleDirective": RoleDirective(),
    "PatternCritiqueThenRewrite": PatternCritiqueThenRewrite(),
}

def get_pattern_by_name(name: str) -> PromptPattern:
    pattern = PATTERN_REGISTRY.get(name)
    if pattern is None:
        raise ValueError(f"Prompt pattern '{name}' not found.")
    return pattern

def list_patterns() -> list:
    return list(PATTERN_REGISTRY.keys()) 