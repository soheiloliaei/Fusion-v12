# Fusion v12.0 ChatGPT Upload Package

This package contains the essential files for running Fusion v12.0 in ChatGPT. The system features pattern-driven processing with real-time memory, adaptive capabilities, execution modes, and chain templates.

## Files to Upload (in this order)

1. **MASTER_PROMPT.md**
   - Core system prompt under 8000 tokens
   - Defines system capabilities and behavior
   - Includes patterns, modes, and templates

2. **fusion_v12_config.json**
   - System configuration
   - Pattern settings
   - Mode configurations
   - Chain templates

3. **Core System Files:**
   - `prompt_patterns.py`: Pattern definitions and safety
   - `prompt_pattern_registry.py`: Pattern management
   - `input_transformer.py`: Input/output transformation
   - `execution_mode_map.py`: Mode behavior mapping
   - `agent_chain.py`: Chain execution with modes
   - `evaluator_metrics.py`: Enhanced metrics

## Key Features

1. **Pattern System**
   - 10 production patterns
   - Pattern safety layer
   - Fallback system
   - Performance tracking

2. **Execution Modes**
   - SIMULATE: For exploration
   - SHIP: For production
   - CRITIQUE: For analysis
   - Mode-specific behaviors

3. **Chain Templates**
   - Strategy chains
   - Critique chains
   - Ship chains
   - Custom configurations

4. **Quality Metrics**
   - Mode-aware scoring
   - Pattern effectiveness
   - Chain success criteria
   - Fallback triggers

## Usage Examples

1. **Simulate Mode**
   ```
   Task: Design new payment flow
   Mode: SIMULATE
   Template: provocation_loop
   Result: Innovative solution with balanced practicality
   ```

2. **Ship Mode**
   ```
   Task: Implement security feature
   Mode: SHIP
   Template: ship_chain
   Result: Production-ready specification
   ```

3. **Critique Mode**
   ```
   Task: Review design proposal
   Mode: CRITIQUE
   Template: critique_strategy
   Result: Deep analysis with improvements
   ```

## Best Practices

1. **Mode Selection**
   - Use SIMULATE for exploration
   - Use SHIP for deliverables
   - Use CRITIQUE for analysis

2. **Pattern Usage**
   - Let system choose patterns
   - Trust fallback system
   - Monitor performance

3. **Chain Selection**
   - Match template to goal
   - Consider mode requirements
   - Follow success criteria

4. **Quality Control**
   - Check mode-specific metrics
   - Verify pattern effectiveness
   - Ensure clear outputs

## Support

For issues or questions:
1. Check execution mode
2. Review pattern selection
3. Verify chain template
4. Adjust metrics thresholds

Remember: This system is specialized for Block's internal tooling. Focus on practical, implementable solutions while maintaining innovation and technical excellence. 