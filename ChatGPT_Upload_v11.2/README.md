# Fusion v11.2 ChatGPT Upload Package

This package contains the essential files for running Fusion v11.2 in ChatGPT. The system features pattern-driven processing with real-time memory and adaptive capabilities.

## Files Overview

1. **MASTER_PROMPT.md**
   - Core system prompt under 8000 tokens
   - Defines system capabilities and behavior
   - Includes pattern definitions and metrics

2. **fusion_v11_knowledge_base.json**
   - Pattern definitions and templates
   - Metrics and thresholds
   - Agent profiles and memory structure

3. **Python Files**
   - `memory_registry.py`: Pattern and agent performance tracking
   - `agent_chain.py`: Chain execution with adaptive switching
   - `evaluator_metrics.py`: Output quality assessment
   - `fusion.py`: CLI runner for local testing

## Key Features

1. **Pattern System**
   - StepwiseInsightSynthesis
   - RoleDirective
   - PatternCritiqueThenRewrite

2. **Adaptive Intelligence**
   - Real-time pattern switching
   - Performance memory
   - Success rate tracking

3. **Quality Metrics**
   - Block relevance
   - Technical feasibility
   - Innovation balance
   - Pattern effectiveness

## Usage Instructions

1. **Setup**
   ```bash
   # Copy files to your workspace
   cp -r ChatGPT_Upload_v11.2/* /your/workspace/

   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Running Tests**
   ```bash
   # Run a chain
   ./fusion.py chain example_chain.json --input test_input.txt --adaptive

   # Run single agent
   ./fusion.py run StrategyPilot --pattern StepwiseInsightSynthesis --text "Your input"
   ```

3. **Viewing Results**
   - Check `_fusion_todo/reasoning_trail.md` for execution details
   - View `_fusion_todo/memory_registry.json` for performance history

## Best Practices

1. **Pattern Selection**
   - Use StepwiseInsightSynthesis for complex problems
   - Use RoleDirective for specialized perspectives
   - Use PatternCritiqueThenRewrite for refinement

2. **Quality Assurance**
   - Monitor metrics in reasoning trail
   - Review pattern performance history
   - Adjust thresholds as needed

3. **Memory Management**
   - Let system learn from interactions
   - Review insights reports regularly
   - Clean up old records periodically

## Support

For issues or questions:
1. Check the reasoning trail for insights
2. Review metrics and pattern history
3. Adjust thresholds or patterns as needed

Remember: This system is specialized for Block's internal tooling. Focus on practical, implementable solutions while maintaining innovation and technical excellence. 