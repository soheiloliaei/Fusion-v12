# Fusion v11.2 ChatGPT Upload Package

## 📦 Files to Upload (in this order)

1. **`MASTER_PROMPT.txt`** (FIRST!)
   - System prompt under 8000 tokens
   - Sets up Block-specialized, industry-led approach
   - Configures pattern system and creative tension

2. **Core System Files:**
   - `prompt_patterns.py` - Pattern definitions
   - `prompt_pattern_registry.py` - Pattern management
   - `fusion_v11_agents_complete.py` - Agent system
   - `evaluator_metrics.py` - Quality assessment
   - `agent_chain.py` - Sequential execution

3. **Knowledge Base:**
   - `fusion_v11_knowledge_base.json` - Context data

## 🚀 Quick Start

After uploading files, test with:

```
Analyze this support workflow and extract key process insights, using creative tension between user needs and business goals.

Context:
{
  "domain": "block",
  "industry": "fintech",
  "tags": ["goal:optimization"]
}
```

## ✨ New in v11.2

- Pattern-driven agent outputs
- Quality metrics and evaluation
- Creative tension integration
- Block-specialized, industry-led approach
- Automatic pattern selection
- Quality scoring and insights

## 🎯 Example Chain

```json
[
  {
    "agent": "StrategyPilot",
    "pattern": "StepwiseInsightSynthesis",
    "tension_type": "vision_vs_execution"
  },
  {
    "agent": "NarrativeArchitect",
    "pattern": "RoleDirective"
  },
  {
    "agent": "EvaluatorAgent",
    "pattern": "PatternCritiqueThenRewrite"
  }
]
```

## 📊 Quality Metrics

The system now tracks:
- Clarity score
- Structure adherence
- Block relevance
- Pattern effectiveness
- Innovation score
- Overall quality

## ⚠️ Important Notes

1. Always upload files in the specified order
2. MASTER_PROMPT.txt must be set as system prompt
3. Other files provide context and code examples
4. System is Block-specialized by default
5. No UI/Figma integration needed 