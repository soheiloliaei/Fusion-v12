# Fusion v12.0 ChatGPT Upload Checklist

## Core Files
- [ ] `MASTER_PROMPT.md` - System prompt and configuration
- [ ] `README.md` - Package documentation
- [ ] `prompt_patterns.py` - Pattern implementations
- [ ] `prompt_pattern_registry.py` - Pattern management
- [ ] `pattern_base.py` - Base pattern classes
- [ ] `pattern_safety.py` - Safety features
- [ ] `pattern_stats.py` - Statistics tracking
- [ ] `agent_chain.py` - Chain execution
- [ ] `evaluator_metrics.py` - Quality metrics
- [ ] `memory_registry.py` - Pattern memory
- [ ] `fusion_cli.py` - CLI interface

## Configuration
- [ ] `fusion_v12_config.json` - System settings
- [ ] `requirements.txt` - Dependencies

## Chain Templates
- [ ] `chain_templates/provocation_loop.json` - Breakthrough thinking
- [ ] `chain_templates/critique_strategy.json` - Deep analysis
- [ ] `chain_templates/rewrite_evolution.json` - Iterative improvement

## Directory Structure
- [ ] `_fusion_todo/` - Working directory
- [ ] `chain_templates/` - Template directory

## Upload Order
1. `MASTER_PROMPT.md`
2. `pattern_base.py`
3. `pattern_safety.py`
4. `prompt_patterns.py`
5. `prompt_pattern_registry.py`
6. `evaluator_metrics.py`
7. `memory_registry.py`
8. `pattern_stats.py`
9. `agent_chain.py`
10. `fusion_cli.py`
11. Chain templates
12. Configuration files

## Verification Steps
1. Check file contents match latest v12.0 code
2. Verify all imports resolve correctly
3. Ensure no missing dependencies
4. Test each pattern implementation
5. Verify chain templates
6. Check configuration settings

## Post-Upload Tasks
1. Test SIMULATE mode
2. Test SHIP mode
3. Test CRITIQUE mode
4. Verify pattern safety
5. Check metrics tracking
6. Review chain execution 