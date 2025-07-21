# Fusion v11.2 ChatGPT Upload Package

This package contains the essential files for running Fusion v11.2 in ChatGPT. The system features pattern-driven processing with real-time memory, adaptive capabilities, and execution modes.

## Files Overview

1. **MASTER_PROMPT.md**
   - Core system prompt under 8000 tokens
   - Defines system capabilities and behavior
   - Includes patterns, modes, and metrics

2. **fusion_v11_knowledge_base.json**
   - Pattern definitions and templates
   - Metrics and thresholds
   - Agent profiles and memory structure

3. **Python Files**
   - `memory_registry.py`: Pattern and agent performance tracking
   - `agent_chain.py`: Chain execution with adaptive switching
   - `evaluator_metrics.py`: Output quality assessment
   - `fusion_cli.py`: Command-line interface with execution modes

## Key Features

1. **Pattern System**
   - StepwiseInsightSynthesis
   - RoleDirective
   - PatternCritiqueThenRewrite

2. **Execution Modes**
   - SIMULATE: For exploration and testing
   - SHIP: For production-ready output
   - CRITIQUE: For analysis and improvement

3. **Chain Templates**
   - Strategy: StrategyPilot → NarrativeArchitect → Evaluator
   - Critique: Evaluator → StrategyPilot
   - Ship: StrategyPilot → NarrativeArchitect → Evaluator

4. **Quality Metrics**
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

   # Make CLI executable
   chmod +x fusion_cli.py
   ```

2. **Running with CLI**
   ```bash
   # Simulate mode (for testing)
   ./fusion_cli.py simulate "Design a new payment flow"

   # Ship mode (for production)
   ./fusion_cli.py ship "Design a new payment flow"

   # Critique mode (for analysis)
   ./fusion_cli.py critique "Design a new payment flow"
   ```

3. **Advanced Usage**
   ```bash
   # Use specific template
   ./fusion_cli.py simulate "Task" --template strategy

   # Disable adaptive switching
   ./fusion_cli.py ship "Task" --no-adaptive

   # Custom output file
   ./fusion_cli.py critique "Task" --output result.json
   ```

4. **Viewing Results**
   - Check `_fusion_todo/reasoning_trail.md` for execution details
   - View `_fusion_todo/memory_registry.json` for performance history
   - See `_fusion_todo/outputs/` for generated files

## Best Practices

1. **Mode Selection**
   - Use SIMULATE for exploration and testing
   - Use SHIP for production deliverables
   - Use CRITIQUE for analysis and improvement

2. **Chain Selection**
   - Strategy chain for planning and vision
   - Critique chain for deep analysis
   - Ship chain for production output

3. **Quality Assurance**
   - Monitor metrics in reasoning trail
   - Review pattern performance history
   - Adjust thresholds as needed

4. **Memory Management**
   - Let system learn from interactions
   - Review insights reports regularly
   - Clean up old records periodically

## Support

For issues or questions:
1. Check the reasoning trail for insights
2. Review metrics and pattern history
3. Adjust modes or patterns as needed

Remember: This system is specialized for Block's internal tooling. Focus on practical, implementable solutions while maintaining innovation and technical excellence. 