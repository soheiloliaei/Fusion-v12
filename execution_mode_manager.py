"""
ExecutionModeManager - Design-Focused Execution Modes
Manages different processing paradigms for design craft and strategic innovation.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum

from fusion_agents import BaseAgent


class ExecutionMode(Enum):
    """Design-focused execution modes for different creative scenarios."""
    SIMULATE = "simulate"      # Explore possibilities, test ideas
    SHIP = "ship"              # Production-ready execution
    CRITIQUE = "critique"      # Challenge and improve existing work
    ADVISORY_BOARD = "advisory_board"  # Multi-perspective strategic analysis


class ExecutionModeManager(BaseAgent):
    """
    Manages execution modes optimized for design craft and strategic innovation.
    Routes tasks through different processing paradigms based on creative intent.
    """
    
    def __init__(self):
        super().__init__(
            agent_id="ExecutionModeManager",
            name="Execution Mode Manager",
            role="Manages design-focused execution modes for optimal creative outcomes",
            capabilities=[
                "mode_selection",
                "design_iteration_optimization",
                "creative_process_management",
                "strategic_routing"
            ],
            quality_metrics={
                "mode_accuracy": {"target": 0.90, "measured_by": "outcome_satisfaction"},
                "design_iteration_efficiency": {"target": 0.85, "measured_by": "iteration_quality"},
                "creative_breakthrough_rate": {"target": 0.75, "measured_by": "innovation_scoring"}
            },
            agent_contract={
                "inputs": ["task_context", "creative_intent", "design_domain"],
                "guarantees": {"mode_accuracy": 0.85, "execution_optimization": 0.80},
                "fallback_on": ["ambiguous_intent", "mode_conflict"]
            }
        )
        
        self.mode_configurations = {
            ExecutionMode.SIMULATE: {
                "description": "Explore design possibilities and test creative ideas",
                "agent_behavior": "exploratory_creative",
                "output_type": "scenarios_prototypes",
                "iteration_style": "rapid_divergent",
                "risk_tolerance": "high",
                "innovation_emphasis": "breakthrough_exploration",
                "time_investment": "flexible",
                "quality_bar": "conceptual_clarity"
            },
            ExecutionMode.SHIP: {
                "description": "Production-ready design execution",
                "agent_behavior": "decisive_practical",
                "output_type": "deliverable_assets",
                "iteration_style": "focused_convergent",
                "risk_tolerance": "low",
                "innovation_emphasis": "proven_excellence",
                "time_investment": "optimized",
                "quality_bar": "production_ready"
            },
            ExecutionMode.CRITIQUE: {
                "description": "Challenge and improve existing design work",
                "agent_behavior": "analytical_constructive",
                "output_type": "improvement_recommendations",
                "iteration_style": "systematic_evaluation",
                "risk_tolerance": "medium",
                "innovation_emphasis": "optimization_refinement",
                "time_investment": "thorough",
                "quality_bar": "comprehensive_analysis"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "description": "Multi-perspective strategic design analysis",
                "agent_behavior": "collaborative_strategic",
                "output_type": "strategic_consensus",
                "iteration_style": "deliberative_synthesis",
                "risk_tolerance": "calculated",
                "innovation_emphasis": "strategic_breakthrough",
                "time_investment": "intensive",
                "quality_bar": "strategic_excellence"
            }
        }
        
        self.design_contexts = {
            "early_exploration": {
                "preferred_mode": ExecutionMode.SIMULATE,
                "alternative_modes": [ExecutionMode.ADVISORY_BOARD],
                "focus": "possibility_space_exploration"
            },
            "concept_development": {
                "preferred_mode": ExecutionMode.SIMULATE,
                "alternative_modes": [ExecutionMode.CRITIQUE],
                "focus": "idea_refinement_and_testing"
            },
            "design_refinement": {
                "preferred_mode": ExecutionMode.CRITIQUE,
                "alternative_modes": [ExecutionMode.SHIP],
                "focus": "quality_optimization"
            },
            "strategic_decision": {
                "preferred_mode": ExecutionMode.ADVISORY_BOARD,
                "alternative_modes": [ExecutionMode.CRITIQUE],
                "focus": "multi_perspective_analysis"
            },
            "production_delivery": {
                "preferred_mode": ExecutionMode.SHIP,
                "alternative_modes": [ExecutionMode.CRITIQUE],
                "focus": "execution_excellence"
            },
            "innovation_breakthrough": {
                "preferred_mode": ExecutionMode.ADVISORY_BOARD,
                "alternative_modes": [ExecutionMode.SIMULATE],
                "focus": "paradigm_shifting_thinking"
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determine optimal execution mode and configure agent behavior:
        1. Analyze task context and creative intent
        2. Select optimal execution mode
        3. Configure agent behaviors and expectations
        4. Set up success criteria and iteration approach
        """
        task_context = inputs.get('task_context', {})
        creative_intent = inputs.get('creative_intent', '')
        design_domain = inputs.get('design_domain', 'ui_ux')
        current_mode = inputs.get('execution_mode', None)
        
        # Self-check for mode selection
        self.self_check("What execution approach will yield the best creative outcome?")
        
        # Analyze context to determine optimal mode
        context_analysis = self._analyze_creative_context(task_context, creative_intent, design_domain)
        
        # Select execution mode
        recommended_mode = self._select_execution_mode(context_analysis, current_mode)
        
        # Configure agent behavior for selected mode
        agent_configuration = self._configure_agents_for_mode(recommended_mode, context_analysis)
        
        # Set up success criteria
        success_criteria = self._define_success_criteria(recommended_mode, context_analysis)
        
        # Plan iteration approach
        iteration_plan = self._plan_iterations(recommended_mode, context_analysis)
        
        return {
            "execution_mode": recommended_mode.value,
            "mode_rationale": self._generate_mode_rationale(recommended_mode, context_analysis),
            "agent_configuration": agent_configuration,
            "success_criteria": success_criteria,
            "iteration_plan": iteration_plan,
            "context_analysis": context_analysis,
            "alternative_modes": self._suggest_alternative_modes(recommended_mode, context_analysis),
            "mode_switching_triggers": self._define_mode_switching_triggers(recommended_mode),
            "reasoning_trail": self.reasoning_trail,
            "confidence_score": self._calculate_mode_confidence(context_analysis)
        }
    
    def _analyze_creative_context(
        self, 
        task_context: Dict[str, Any], 
        creative_intent: str, 
        design_domain: str
    ) -> Dict[str, Any]:
        """Analyze context to understand optimal creative approach."""
        
        # Analyze creative intent
        intent_analysis = self._analyze_creative_intent(creative_intent)
        
        # Assess project phase
        project_phase = self._assess_project_phase(task_context)
        
        # Evaluate innovation requirements
        innovation_requirements = self._evaluate_innovation_requirements(creative_intent, task_context)
        
        # Assess complexity and stakes
        complexity_assessment = self._assess_task_complexity(task_context)
        
        # Determine time constraints
        time_constraints = self._assess_time_constraints(task_context)
        
        return {
            "intent_analysis": intent_analysis,
            "project_phase": project_phase,
            "innovation_requirements": innovation_requirements,
            "complexity_assessment": complexity_assessment,
            "time_constraints": time_constraints,
            "design_domain": design_domain,
            "creative_ambition_level": self._assess_creative_ambition(creative_intent)
        }
    
    def _select_execution_mode(
        self, 
        context_analysis: Dict[str, Any], 
        current_mode: Optional[str]
    ) -> ExecutionMode:
        """Select optimal execution mode based on context analysis."""
        
        project_phase = context_analysis["project_phase"]
        innovation_requirements = context_analysis["innovation_requirements"]
        complexity_assessment = context_analysis["complexity_assessment"]
        creative_ambition = context_analysis["creative_ambition_level"]
        
        # Mode selection logic
        mode_scores = {}
        
        # SIMULATE mode scoring
        mode_scores[ExecutionMode.SIMULATE] = 0
        if project_phase in ["early_exploration", "concept_development"]:
            mode_scores[ExecutionMode.SIMULATE] += 30
        if innovation_requirements["breakthrough_potential"] == "high":
            mode_scores[ExecutionMode.SIMULATE] += 25
        if creative_ambition == "high":
            mode_scores[ExecutionMode.SIMULATE] += 20
        if complexity_assessment["ambiguity_level"] == "high":
            mode_scores[ExecutionMode.SIMULATE] += 15
        
        # SHIP mode scoring
        mode_scores[ExecutionMode.SHIP] = 0
        if project_phase == "production_delivery":
            mode_scores[ExecutionMode.SHIP] += 40
        if context_analysis["time_constraints"] == "tight":
            mode_scores[ExecutionMode.SHIP] += 25
        if complexity_assessment["clarity_level"] == "high":
            mode_scores[ExecutionMode.SHIP] += 20
        if creative_ambition == "low":
            mode_scores[ExecutionMode.SHIP] += 15
        
        # CRITIQUE mode scoring
        mode_scores[ExecutionMode.CRITIQUE] = 0
        if project_phase in ["design_refinement", "optimization"]:
            mode_scores[ExecutionMode.CRITIQUE] += 35
        if innovation_requirements["improvement_focus"] == "high":
            mode_scores[ExecutionMode.CRITIQUE] += 25
        if complexity_assessment["existing_solution_quality"] == "medium":
            mode_scores[ExecutionMode.CRITIQUE] += 20
        
        # ADVISORY_BOARD mode scoring
        mode_scores[ExecutionMode.ADVISORY_BOARD] = 0
        if project_phase in ["strategic_decision", "innovation_breakthrough"]:
            mode_scores[ExecutionMode.ADVISORY_BOARD] += 40
        if complexity_assessment["strategic_impact"] == "high":
            mode_scores[ExecutionMode.ADVISORY_BOARD] += 30
        if innovation_requirements["perspective_diversity_needed"] == "high":
            mode_scores[ExecutionMode.ADVISORY_BOARD] += 25
        if creative_ambition == "breakthrough":
            mode_scores[ExecutionMode.ADVISORY_BOARD] += 20
        
        # Select highest scoring mode
        selected_mode = max(mode_scores.items(), key=lambda x: x[1])[0]
        
        # Override with current mode if explicitly set and reasonable
        if current_mode:
            try:
                current_mode_enum = ExecutionMode(current_mode)
                if mode_scores[current_mode_enum] >= mode_scores[selected_mode] * 0.8:
                    selected_mode = current_mode_enum
            except ValueError:
                pass  # Invalid mode, stick with selected
        
        return selected_mode
    
    def _configure_agents_for_mode(
        self, 
        mode: ExecutionMode, 
        context_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Configure agent behaviors for selected execution mode."""
        
        base_config = self.mode_configurations[mode]
        
        return {
            "agent_behavior_style": base_config["agent_behavior"],
            "output_expectations": base_config["output_type"],
            "iteration_approach": base_config["iteration_style"],
            "risk_tolerance": base_config["risk_tolerance"],
            "innovation_emphasis": base_config["innovation_emphasis"],
            "quality_expectations": base_config["quality_bar"],
            "collaboration_mode": self._determine_collaboration_mode(mode),
            "confidence_thresholds": self._set_confidence_thresholds(mode),
            "debate_triggers": self._configure_debate_triggers(mode, context_analysis),
            "agent_pairing_strategy": self._configure_agent_pairing(mode, context_analysis)
        }
    
    def _define_success_criteria(
        self, 
        mode: ExecutionMode, 
        context_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Define success criteria for the selected execution mode."""
        
        success_criteria = {
            ExecutionMode.SIMULATE: {
                "primary_metrics": ["creative_exploration_breadth", "concept_viability", "innovation_potential"],
                "quality_indicators": ["idea_diversity", "feasibility_assessment", "user_value_potential"],
                "completion_criteria": "multiple_viable_concepts_explored"
            },
            ExecutionMode.SHIP: {
                "primary_metrics": ["deliverable_completeness", "production_readiness", "quality_excellence"],
                "quality_indicators": ["specification_compliance", "design_consistency", "user_experience_quality"],
                "completion_criteria": "production_ready_deliverables"
            },
            ExecutionMode.CRITIQUE: {
                "primary_metrics": ["improvement_identification", "analysis_depth", "recommendation_quality"],
                "quality_indicators": ["issue_coverage", "solution_viability", "strategic_alignment"],
                "completion_criteria": "comprehensive_improvement_roadmap"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "primary_metrics": ["perspective_diversity", "strategic_consensus", "breakthrough_potential"],
                "quality_indicators": ["viewpoint_comprehensiveness", "decision_quality", "innovation_ambition"],
                "completion_criteria": "multi_perspective_strategic_alignment"
            }
        }
        
        return success_criteria[mode]
    
    def _plan_iterations(
        self, 
        mode: ExecutionMode, 
        context_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Plan iteration approach for the selected mode."""
        
        iteration_plans = {
            ExecutionMode.SIMULATE: {
                "iteration_style": "rapid_prototyping",
                "cycles": "multiple_short_cycles",
                "feedback_loops": "frequent_validation",
                "pivot_readiness": "high",
                "exploration_depth": "broad_then_deep"
            },
            ExecutionMode.SHIP: {
                "iteration_style": "focused_refinement",
                "cycles": "fewer_deep_cycles",
                "feedback_loops": "milestone_validation",
                "pivot_readiness": "low",
                "exploration_depth": "deep_optimization"
            },
            ExecutionMode.CRITIQUE: {
                "iteration_style": "systematic_analysis",
                "cycles": "analysis_then_solution",
                "feedback_loops": "validation_heavy",
                "pivot_readiness": "medium",
                "exploration_depth": "comprehensive_coverage"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "iteration_style": "deliberative_consensus",
                "cycles": "perspective_then_synthesis",
                "feedback_loops": "continuous_alignment",
                "pivot_readiness": "medium",
                "exploration_depth": "strategic_depth"
            }
        }
        
        return iteration_plans[mode]
    
    def _analyze_creative_intent(self, creative_intent: str) -> Dict[str, Any]:
        """Analyze the creative intent to understand approach needs."""
        
        intent_lower = creative_intent.lower()
        
        # Innovation indicators
        innovation_keywords = ["innovative", "breakthrough", "revolutionary", "disruptive", "novel"]
        innovation_score = sum(1 for keyword in innovation_keywords if keyword in intent_lower)
        
        # Exploration indicators
        exploration_keywords = ["explore", "discover", "investigate", "experiment", "prototype"]
        exploration_score = sum(1 for keyword in exploration_keywords if keyword in intent_lower)
        
        # Delivery indicators
        delivery_keywords = ["deliver", "ship", "complete", "finalize", "production"]
        delivery_score = sum(1 for keyword in delivery_keywords if keyword in intent_lower)
        
        # Improvement indicators
        improvement_keywords = ["improve", "optimize", "enhance", "refine", "better"]
        improvement_score = sum(1 for keyword in improvement_keywords if keyword in intent_lower)
        
        return {
            "innovation_emphasis": innovation_score,
            "exploration_emphasis": exploration_score,
            "delivery_emphasis": delivery_score,
            "improvement_emphasis": improvement_score,
            "primary_intent": self._determine_primary_intent(
                innovation_score, exploration_score, delivery_score, improvement_score
            )
        }
    
    def _assess_project_phase(self, task_context: Dict[str, Any]) -> str:
        """Assess what phase of the design process this task represents."""
        
        context_indicators = task_context.get('indicators', {})
        
        # Phase indicators
        if context_indicators.get('has_existing_solution', False):
            if context_indicators.get('needs_improvement', False):
                return "design_refinement"
            else:
                return "optimization"
        
        if context_indicators.get('strategic_importance', 'medium') == 'high':
            return "strategic_decision"
        
        if context_indicators.get('exploration_needed', False):
            return "early_exploration"
        
        if context_indicators.get('ready_for_delivery', False):
            return "production_delivery"
        
        # Default based on context clues
        return "concept_development"
    
    def _evaluate_innovation_requirements(
        self, 
        creative_intent: str, 
        task_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Evaluate innovation requirements for the task."""
        
        intent_lower = creative_intent.lower()
        
        breakthrough_indicators = ["breakthrough", "revolutionary", "paradigm", "transform"]
        breakthrough_potential = "high" if any(ind in intent_lower for ind in breakthrough_indicators) else "medium"
        
        improvement_indicators = ["improve", "optimize", "enhance", "better"]
        improvement_focus = "high" if any(ind in intent_lower for ind in improvement_indicators) else "medium"
        
        perspective_indicators = ["perspective", "viewpoint", "angle", "stakeholder"]
        perspective_diversity_needed = "high" if any(ind in intent_lower for ind in perspective_indicators) else "medium"
        
        return {
            "breakthrough_potential": breakthrough_potential,
            "improvement_focus": improvement_focus,
            "perspective_diversity_needed": perspective_diversity_needed,
            "innovation_risk_tolerance": task_context.get('innovation_risk_tolerance', 'medium')
        }
    
    def _assess_task_complexity(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess the complexity of the design task."""
        
        return {
            "ambiguity_level": task_context.get('ambiguity_level', 'medium'),
            "clarity_level": task_context.get('clarity_level', 'medium'),
            "strategic_impact": task_context.get('strategic_impact', 'medium'),
            "stakeholder_complexity": task_context.get('stakeholder_complexity', 'medium'),
            "technical_complexity": task_context.get('technical_complexity', 'medium'),
            "existing_solution_quality": task_context.get('existing_solution_quality', 'none')
        }
    
    def _assess_time_constraints(self, task_context: Dict[str, Any]) -> str:
        """Assess time constraints for the task."""
        
        deadline = task_context.get('deadline', 'flexible')
        urgency = task_context.get('urgency', 'medium')
        
        if deadline == 'tight' or urgency == 'high':
            return 'tight'
        elif deadline == 'flexible' and urgency == 'low':
            return 'flexible'
        else:
            return 'moderate'
    
    def _assess_creative_ambition(self, creative_intent: str) -> str:
        """Assess the level of creative ambition."""
        
        intent_lower = creative_intent.lower()
        
        high_ambition = ["breakthrough", "revolutionary", "innovative", "disruptive", "transform"]
        medium_ambition = ["creative", "novel", "original", "unique"]
        
        if any(word in intent_lower for word in high_ambition):
            return "breakthrough" if "breakthrough" in intent_lower else "high"
        elif any(word in intent_lower for word in medium_ambition):
            return "medium"
        else:
            return "low"
    
    def _determine_primary_intent(
        self, 
        innovation_score: int, 
        exploration_score: int, 
        delivery_score: int, 
        improvement_score: int
    ) -> str:
        """Determine the primary creative intent."""
        
        scores = {
            "innovation": innovation_score,
            "exploration": exploration_score,
            "delivery": delivery_score,
            "improvement": improvement_score
        }
        
        return max(scores.items(), key=lambda x: x[1])[0]
    
    def _determine_collaboration_mode(self, mode: ExecutionMode) -> str:
        """Determine collaboration approach for the mode."""
        
        collaboration_modes = {
            ExecutionMode.SIMULATE: "parallel_exploration",
            ExecutionMode.SHIP: "coordinated_execution",
            ExecutionMode.CRITIQUE: "structured_analysis",
            ExecutionMode.ADVISORY_BOARD: "collaborative_synthesis"
        }
        
        return collaboration_modes[mode]
    
    def _set_confidence_thresholds(self, mode: ExecutionMode) -> Dict[str, float]:
        """Set confidence thresholds for the mode."""
        
        thresholds = {
            ExecutionMode.SIMULATE: {"proceed": 0.5, "debate": 0.3, "clarify": 0.7},
            ExecutionMode.SHIP: {"proceed": 0.8, "debate": 0.6, "clarify": 0.9},
            ExecutionMode.CRITIQUE: {"proceed": 0.7, "debate": 0.5, "clarify": 0.8},
            ExecutionMode.ADVISORY_BOARD: {"proceed": 0.6, "debate": 0.4, "clarify": 0.8}
        }
        
        return thresholds[mode]
    
    def _configure_debate_triggers(self, mode: ExecutionMode, context_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Configure when debates should be triggered for this mode."""
        
        debate_configs = {
            ExecutionMode.SIMULATE: {
                "trigger_on": ["creative_conflict", "feasibility_questions", "direction_uncertainty"],
                "debate_style": "generative_exploration",
                "resolution_approach": "synthesize_multiple_directions"
            },
            ExecutionMode.SHIP: {
                "trigger_on": ["quality_concerns", "specification_conflicts", "delivery_risks"],
                "debate_style": "solution_focused",
                "resolution_approach": "decisive_convergence"
            },
            ExecutionMode.CRITIQUE: {
                "trigger_on": ["analysis_disagreement", "improvement_priorities", "evaluation_criteria"],
                "debate_style": "analytical_structured",
                "resolution_approach": "evidence_based_consensus"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "trigger_on": ["strategic_disagreement", "perspective_conflicts", "priority_tensions"],
                "debate_style": "strategic_deliberation",
                "resolution_approach": "multi_perspective_synthesis"
            }
        }
        
        return debate_configs[mode]
    
    def _configure_agent_pairing(self, mode: ExecutionMode, context_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Configure agent pairing strategy for this mode."""
        
        pairing_strategies = {
            ExecutionMode.SIMULATE: {
                "pairing_focus": "creative_tension",
                "preferred_pairs": ["StrategyPilot + CreativeDirector", "DesignMaestro + DesignTechnologist"],
                "tension_type": "vision_vs_feasibility"
            },
            ExecutionMode.SHIP: {
                "pairing_focus": "execution_excellence",
                "preferred_pairs": ["DesignTechnologist + CriticalDesignAdvisor"],
                "tension_type": "innovation_vs_reliability"
            },
            ExecutionMode.CRITIQUE: {
                "pairing_focus": "comprehensive_analysis",
                "preferred_pairs": ["CriticalDesignAdvisor + DesignMaestro"],
                "tension_type": "depth_vs_breadth"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "pairing_focus": "strategic_perspectives",
                "preferred_pairs": ["StrategyPilot + DesignMaestro", "CreativeDirector + CriticalDesignAdvisor"],
                "tension_type": "multiple_strategic_viewpoints"
            }
        }
        
        return pairing_strategies[mode]
    
    def _generate_mode_rationale(self, mode: ExecutionMode, context_analysis: Dict[str, Any]) -> str:
        """Generate explanation for mode selection."""
        
        project_phase = context_analysis["project_phase"]
        creative_ambition = context_analysis["creative_ambition_level"]
        primary_intent = context_analysis["intent_analysis"]["primary_intent"]
        
        rationale_templates = {
            ExecutionMode.SIMULATE: f"Selected SIMULATE mode due to {project_phase} phase and {creative_ambition} creative ambition. Focus on {primary_intent} through exploratory iteration.",
            ExecutionMode.SHIP: f"Selected SHIP mode for {project_phase} phase with {primary_intent} focus. Optimized for production-ready delivery.",
            ExecutionMode.CRITIQUE: f"Selected CRITIQUE mode to address {primary_intent} in {project_phase} phase. Systematic analysis and improvement focus.",
            ExecutionMode.ADVISORY_BOARD: f"Selected ADVISORY_BOARD mode for {project_phase} with {creative_ambition} ambition. Multi-perspective strategic analysis needed."
        }
        
        return rationale_templates[mode]
    
    def _suggest_alternative_modes(self, selected_mode: ExecutionMode, context_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Suggest alternative modes and when to switch."""
        
        alternatives = []
        
        for mode in ExecutionMode:
            if mode != selected_mode:
                alternatives.append({
                    "mode": mode.value,
                    "when_to_switch": self._define_switch_conditions(selected_mode, mode),
                    "benefit": self._explain_mode_benefit(mode, context_analysis)
                })
        
        return alternatives
    
    def _define_mode_switching_triggers(self, current_mode: ExecutionMode) -> Dict[str, Any]:
        """Define when to consider switching modes."""
        
        switching_triggers = {
            ExecutionMode.SIMULATE: {
                "switch_to_ship": "concepts_validated_and_direction_clear",
                "switch_to_critique": "initial_solutions_need_evaluation",
                "switch_to_advisory_board": "strategic_alignment_needed"
            },
            ExecutionMode.SHIP: {
                "switch_to_critique": "quality_concerns_or_optimization_needed",
                "switch_to_simulate": "requirements_change_significantly",
                "switch_to_advisory_board": "strategic_decisions_required"
            },
            ExecutionMode.CRITIQUE: {
                "switch_to_ship": "improvements_identified_and_ready_to_implement",
                "switch_to_simulate": "fundamental_rethinking_needed",
                "switch_to_advisory_board": "evaluation_requires_multiple_perspectives"
            },
            ExecutionMode.ADVISORY_BOARD: {
                "switch_to_simulate": "consensus_reached_exploration_needed",
                "switch_to_ship": "strategic_direction_clear_execution_needed",
                "switch_to_critique": "specific_analysis_required"
            }
        }
        
        return switching_triggers[current_mode]
    
    def _define_switch_conditions(self, from_mode: ExecutionMode, to_mode: ExecutionMode) -> str:
        """Define specific conditions for mode switching."""
        
        switch_map = {
            (ExecutionMode.SIMULATE, ExecutionMode.SHIP): "when concepts are validated and ready for production",
            (ExecutionMode.SIMULATE, ExecutionMode.CRITIQUE): "when initial solutions need systematic evaluation",
            (ExecutionMode.SHIP, ExecutionMode.CRITIQUE): "when quality optimization is needed",
            (ExecutionMode.CRITIQUE, ExecutionMode.ADVISORY_BOARD): "when evaluation requires diverse perspectives"
        }
        
        return switch_map.get((from_mode, to_mode), f"when {to_mode.value} approach would be more effective")
    
    def _explain_mode_benefit(self, mode: ExecutionMode, context_analysis: Dict[str, Any]) -> str:
        """Explain the benefit of switching to this mode."""
        
        benefits = {
            ExecutionMode.SIMULATE: "enables creative exploration and breakthrough thinking",
            ExecutionMode.SHIP: "ensures production-ready delivery and execution excellence",
            ExecutionMode.CRITIQUE: "provides systematic analysis and improvement identification",
            ExecutionMode.ADVISORY_BOARD: "brings diverse perspectives and strategic alignment"
        }
        
        return benefits[mode]
    
    def _calculate_mode_confidence(self, context_analysis: Dict[str, Any]) -> float:
        """Calculate confidence in mode selection."""
        
        clarity_indicators = [
            context_analysis.get("intent_analysis", {}).get("primary_intent") is not None,
            context_analysis.get("project_phase") is not None,
            context_analysis.get("creative_ambition_level") != "unknown"
        ]
        
        confidence = sum(clarity_indicators) / len(clarity_indicators)
        return min(confidence + 0.2, 1.0)  # Boost slightly for base confidence
    
    def _identify_assumptions(self) -> List[str]:
        """Identify assumptions in execution mode selection."""
        return [
            "Task context accurately reflects actual requirements",
            "Creative intent is clearly expressed",
            "Project phase assessment is accurate",
            "Mode switching flexibility is available",
            "Agent capabilities match mode requirements"
        ]
    
    def _assess_uncertainty(self) -> float:
        """Assess uncertainty in mode management."""
        return 0.15  # Generally confident in mode selection logic 