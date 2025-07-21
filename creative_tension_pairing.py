"""
Creative Tension Pairing - Strategic Agent Collaboration
Implements creative tension between agents for breakthrough design thinking and innovation.
"""

import json
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from enum import Enum

from fusion_agents import BaseAgent


class TensionType(Enum):
    """Types of creative tension that drive breakthrough thinking."""
    VISION_VS_EXECUTION = "vision_vs_execution"
    INNOVATION_VS_FEASIBILITY = "innovation_vs_feasibility" 
    USER_VS_BUSINESS = "user_vs_business"
    CREATIVE_VS_STRATEGIC = "creative_vs_strategic"
    EXPLORATION_VS_OPTIMIZATION = "exploration_vs_optimization"
    DEPTH_VS_BREADTH = "depth_vs_breadth"
    SPEED_VS_QUALITY = "speed_vs_quality"


class CreativeTensionPairing(BaseAgent):
    """
    Manages creative tension between agents to generate breakthrough insights.
    Focuses on productive conflict that drives design innovation and strategic thinking.
    """
    
    def __init__(self):
        super().__init__(
            agent_id="CreativeTensionPairing",
            name="Creative Tension Pairing",
            role="Orchestrates creative tension between agents for breakthrough thinking",
            capabilities=[
                "tension_orchestration",
                "creative_conflict_facilitation",
                "breakthrough_synthesis",
                "innovation_catalyst"
            ],
            quality_metrics={
                "creative_breakthrough_rate": {"target": 0.80, "measured_by": "innovation_scoring"},
                "tension_productivity": {"target": 0.85, "measured_by": "synthesis_quality"},
                "strategic_alignment": {"target": 0.90, "measured_by": "outcome_coherence"}
            },
            agent_contract={
                "inputs": ["pairing_context", "tension_type", "agent_pool"],
                "guarantees": {"breakthrough_potential": 0.75, "synthesis_quality": 0.80},
                "fallback_on": ["insufficient_tension", "unproductive_conflict"]
            }
        )
        
        self.tension_frameworks = {
            TensionType.VISION_VS_EXECUTION: {
                "description": "Visionary thinking vs. practical implementation",
                "optimal_pairs": [
                    ("StrategyPilot", "DesignTechnologist"),
                    ("CreativeDirector", "CriticalDesignAdvisor")
                ],
                "synthesis_approach": "staged_realization",
                "breakthrough_potential": "paradigm_shifts",
                "conflict_value": "prevents_premature_optimization_and_under_ambition"
            },
            TensionType.INNOVATION_VS_FEASIBILITY: {
                "description": "Breakthrough innovation vs. realistic constraints",
                "optimal_pairs": [
                    ("CreativeDirector", "DesignTechnologist"),
                    ("StrategyPilot", "CriticalDesignAdvisor")
                ],
                "synthesis_approach": "constraint_innovation",
                "breakthrough_potential": "feasible_breakthroughs",
                "conflict_value": "ensures_implementable_innovation"
            },
            TensionType.USER_VS_BUSINESS: {
                "description": "User experience excellence vs. business objectives",
                "optimal_pairs": [
                    ("DesignMaestro", "StrategyPilot"),
                    ("CreativeDirector", "StrategyPilot")
                ],
                "synthesis_approach": "value_alignment",
                "breakthrough_potential": "win_win_solutions",
                "conflict_value": "prevents_user_neglect_and_business_blindness"
            },
            TensionType.CREATIVE_VS_STRATEGIC: {
                "description": "Creative expression vs. strategic alignment",
                "optimal_pairs": [
                    ("CreativeDirector", "StrategyPilot"),
                    ("DesignMaestro", "StrategyPilot")
                ],
                "synthesis_approach": "strategic_creativity",
                "breakthrough_potential": "brand_differentiation",
                "conflict_value": "balances_expression_with_purpose"
            },
            TensionType.EXPLORATION_VS_OPTIMIZATION: {
                "description": "Broad exploration vs. focused optimization",
                "optimal_pairs": [
                    ("CreativeDirector", "CriticalDesignAdvisor"),
                    ("DesignMaestro", "CriticalDesignAdvisor")
                ],
                "synthesis_approach": "staged_focusing",
                "breakthrough_potential": "optimized_innovations",
                "conflict_value": "prevents_tunnel_vision_and_endless_exploration"
            },
            TensionType.DEPTH_VS_BREADTH: {
                "description": "Deep specialization vs. comprehensive coverage",
                "optimal_pairs": [
                    ("CriticalDesignAdvisor", "DesignMaestro"),
                    ("DesignTechnologist", "StrategyPilot")
                ],
                "synthesis_approach": "layered_analysis",
                "breakthrough_potential": "comprehensive_excellence",
                "conflict_value": "ensures_both_depth_and_completeness"
            },
            TensionType.SPEED_VS_QUALITY: {
                "description": "Rapid iteration vs. quality excellence",
                "optimal_pairs": [
                    ("DesignTechnologist", "CriticalDesignAdvisor"),
                    ("CreativeDirector", "CriticalDesignAdvisor")
                ],
                "synthesis_approach": "quality_velocity",
                "breakthrough_potential": "efficient_excellence",
                "conflict_value": "optimizes_both_speed_and_quality"
            }
        }
        
        self.agent_characteristics = {
            "StrategyPilot": {
                "natural_tendencies": ["strategic_thinking", "business_focus", "long_term_vision"],
                "tension_strengths": ["market_reality", "strategic_alignment", "viability_assessment"],
                "complementary_weaknesses": ["creative_exploration", "user_empathy", "tactical_execution"]
            },
            "CreativeDirector": {
                "natural_tendencies": ["creative_innovation", "brand_expression", "user_inspiration"],
                "tension_strengths": ["breakthrough_thinking", "emotional_resonance", "narrative_power"],
                "complementary_weaknesses": ["strategic_alignment", "technical_constraints", "business_metrics"]
            },
            "DesignMaestro": {
                "natural_tendencies": ["user_experience", "journey_optimization", "interaction_excellence"],
                "tension_strengths": ["user_advocacy", "experience_quality", "friction_detection"],
                "complementary_weaknesses": ["business_strategy", "technical_implementation", "brand_expression"]
            },
            "DesignTechnologist": {
                "natural_tendencies": ["technical_feasibility", "implementation_excellence", "systematic_thinking"],
                "tension_strengths": ["practical_constraints", "technical_innovation", "scalability_awareness"],
                "complementary_weaknesses": ["creative_vision", "user_empathy", "strategic_perspective"]
            },
            "CriticalDesignAdvisor": {
                "natural_tendencies": ["analytical_thinking", "quality_assessment", "systematic_evaluation"],
                "tension_strengths": ["objective_analysis", "risk_identification", "quality_standards"],
                "complementary_weaknesses": ["creative_generation", "visionary_thinking", "rapid_iteration"]
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Orchestrate creative tension between agent pairs:
        1. Analyze context to identify optimal tension type
        2. Select complementary agent pairs
        3. Configure productive conflict parameters
        4. Facilitate breakthrough synthesis
        """
        pairing_context = inputs.get('pairing_context', {})
        requested_tension = inputs.get('tension_type', None)
        available_agents = inputs.get('agent_pool', list(self.agent_characteristics.keys()))
        execution_mode = inputs.get('execution_mode', 'ship')
        
        # Self-check for productive tension
        self.self_check("What creative tension will generate the most breakthrough value?")
        
        # Analyze context to determine optimal tension
        tension_analysis = self._analyze_tension_needs(pairing_context, execution_mode)
        
        # Select tension type
        optimal_tension = self._select_tension_type(tension_analysis, requested_tension)
        
        # Select agent pairs
        agent_pairs = self._select_agent_pairs(optimal_tension, available_agents, tension_analysis)
        
        # Configure tension parameters
        tension_configuration = self._configure_tension_parameters(optimal_tension, agent_pairs, execution_mode)
        
        # Plan synthesis approach
        synthesis_plan = self._plan_synthesis_approach(optimal_tension, agent_pairs, pairing_context)
        
        # Generate facilitation strategy
        facilitation_strategy = self._generate_facilitation_strategy(optimal_tension, tension_configuration)
        
        return {
            "tension_type": optimal_tension.value,
            "agent_pairs": agent_pairs,
            "tension_configuration": tension_configuration,
            "synthesis_plan": synthesis_plan,
            "facilitation_strategy": facilitation_strategy,
            "tension_analysis": tension_analysis,
            "breakthrough_indicators": self._identify_breakthrough_indicators(optimal_tension),
            "conflict_resolution_approach": self._define_conflict_resolution(optimal_tension),
            "reasoning_trail": self.reasoning_trail,
            "confidence_score": self._calculate_pairing_confidence(tension_analysis, agent_pairs)
        }
    
    def _analyze_tension_needs(self, pairing_context: Dict[str, Any], execution_mode: str) -> Dict[str, Any]:
        """Analyze context to understand what type of creative tension is needed."""
        
        # Identify design challenges
        design_challenges = self._identify_design_challenges(pairing_context)
        
        # Assess innovation requirements
        innovation_needs = self._assess_innovation_needs(pairing_context)
        
        # Evaluate strategic complexity
        strategic_complexity = self._evaluate_strategic_complexity(pairing_context)
        
        # Analyze creative ambition
        creative_ambition = self._analyze_creative_ambition(pairing_context)
        
        # Assess execution constraints
        execution_constraints = self._assess_execution_constraints(pairing_context, execution_mode)
        
        return {
            "design_challenges": design_challenges,
            "innovation_needs": innovation_needs,
            "strategic_complexity": strategic_complexity,
            "creative_ambition": creative_ambition,
            "execution_constraints": execution_constraints,
            "primary_tension_driver": self._identify_primary_tension_driver(
                design_challenges, innovation_needs, strategic_complexity
            )
        }
    
    def _select_tension_type(
        self, 
        tension_analysis: Dict[str, Any], 
        requested_tension: Optional[str]
    ) -> TensionType:
        """Select the optimal tension type based on analysis."""
        
        # If tension explicitly requested, validate and use
        if requested_tension:
            try:
                return TensionType(requested_tension)
            except ValueError:
                pass  # Fall through to analytical selection
        
        # Tension scoring based on context analysis
        tension_scores = {}
        
        # Score each tension type
        for tension_type in TensionType:
            score = self._score_tension_relevance(tension_type, tension_analysis)
            tension_scores[tension_type] = score
        
        # Select highest scoring tension
        return max(tension_scores.items(), key=lambda x: x[1])[0]
    
    def _score_tension_relevance(self, tension_type: TensionType, analysis: Dict[str, Any]) -> float:
        """Score how relevant a tension type is for the current context."""
        
        score = 0.0
        challenges = analysis["design_challenges"]
        innovation_needs = analysis["innovation_needs"]
        strategic_complexity = analysis["strategic_complexity"]
        creative_ambition = analysis["creative_ambition"]
        
        # Scoring logic for each tension type
        if tension_type == TensionType.VISION_VS_EXECUTION:
            score += challenges.get("implementation_clarity", 0) * 0.3
            score += creative_ambition.get("visionary_scope", 0) * 0.4
            score += innovation_needs.get("paradigm_shift_potential", 0) * 0.3
        
        elif tension_type == TensionType.INNOVATION_VS_FEASIBILITY:
            score += innovation_needs.get("breakthrough_requirement", 0) * 0.4
            score += challenges.get("technical_constraints", 0) * 0.3
            score += creative_ambition.get("innovation_risk", 0) * 0.3
        
        elif tension_type == TensionType.USER_VS_BUSINESS:
            score += challenges.get("stakeholder_alignment", 0) * 0.4
            score += strategic_complexity.get("business_pressure", 0) * 0.3
            score += challenges.get("user_business_conflict", 0) * 0.3
        
        elif tension_type == TensionType.CREATIVE_VS_STRATEGIC:
            score += creative_ambition.get("expression_importance", 0) * 0.4
            score += strategic_complexity.get("strategic_alignment_need", 0) * 0.3
            score += challenges.get("brand_strategy_tension", 0) * 0.3
        
        elif tension_type == TensionType.EXPLORATION_VS_OPTIMIZATION:
            score += innovation_needs.get("exploration_requirement", 0) * 0.4
            score += challenges.get("optimization_opportunity", 0) * 0.3
            score += analysis["execution_constraints"].get("time_pressure", 0) * 0.3
        
        elif tension_type == TensionType.DEPTH_VS_BREADTH:
            score += challenges.get("complexity_scope", 0) * 0.4
            score += strategic_complexity.get("comprehensive_analysis_need", 0) * 0.3
            score += innovation_needs.get("thorough_exploration", 0) * 0.3
        
        elif tension_type == TensionType.SPEED_VS_QUALITY:
            score += analysis["execution_constraints"].get("speed_pressure", 0) * 0.4
            score += challenges.get("quality_requirements", 0) * 0.3
            score += strategic_complexity.get("delivery_pressure", 0) * 0.3
        
        return min(score, 1.0)
    
    def _select_agent_pairs(
        self, 
        tension_type: TensionType, 
        available_agents: List[str], 
        tension_analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Select optimal agent pairs for the tension type."""
        
        framework = self.tension_frameworks[tension_type]
        optimal_pairs = framework["optimal_pairs"]
        
        selected_pairs = []
        
        for agent1, agent2 in optimal_pairs:
            if agent1 in available_agents and agent2 in available_agents:
                pair_analysis = self._analyze_pair_dynamics(agent1, agent2, tension_type, tension_analysis)
                
                selected_pairs.append({
                    "agent_1": agent1,
                    "agent_2": agent2,
                    "tension_dynamic": self._describe_tension_dynamic(agent1, agent2, tension_type),
                    "expected_breakthrough": pair_analysis["breakthrough_potential"],
                    "synthesis_approach": pair_analysis["synthesis_approach"],
                    "conflict_areas": pair_analysis["conflict_areas"],
                    "complementary_strengths": pair_analysis["complementary_strengths"],
                    "productive_tension_score": pair_analysis["tension_score"]
                })
        
        # Sort by productive tension score
        selected_pairs.sort(key=lambda p: p["productive_tension_score"], reverse=True)
        
        return selected_pairs[:2]  # Return top 2 pairs
    
    def _analyze_pair_dynamics(
        self, 
        agent1: str, 
        agent2: str, 
        tension_type: TensionType, 
        tension_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze the dynamics between a specific agent pair."""
        
        char1 = self.agent_characteristics[agent1]
        char2 = self.agent_characteristics[agent2]
        
        # Identify conflict areas (productive tension points)
        conflict_areas = []
        for strength1 in char1["tension_strengths"]:
            if strength1 in char2["complementary_weaknesses"]:
                conflict_areas.append(f"{agent1}_{strength1}_vs_{agent2}_weakness")
        
        for strength2 in char2["tension_strengths"]:
            if strength2 in char1["complementary_weaknesses"]:
                conflict_areas.append(f"{agent2}_{strength2}_vs_{agent1}_weakness")
        
        # Identify complementary strengths
        complementary_strengths = []
        for weakness1 in char1["complementary_weaknesses"]:
            if any(strength for strength in char2["tension_strengths"] if self._strengths_complement(weakness1, strength)):
                complementary_strengths.append(f"{weakness1}_complemented_by_{agent2}")
        
        # Calculate tension score
        tension_score = len(conflict_areas) * 0.3 + len(complementary_strengths) * 0.4 + 0.3
        
        return {
            "conflict_areas": conflict_areas,
            "complementary_strengths": complementary_strengths,
            "tension_score": min(tension_score, 1.0),
            "breakthrough_potential": self._assess_breakthrough_potential(agent1, agent2, tension_type),
            "synthesis_approach": self._determine_synthesis_approach(agent1, agent2, tension_type)
        }
    
    def _configure_tension_parameters(
        self, 
        tension_type: TensionType, 
        agent_pairs: List[Dict[str, Any]], 
        execution_mode: str
    ) -> Dict[str, Any]:
        """Configure parameters for productive tension management."""
        
        framework = self.tension_frameworks[tension_type]
        
        return {
            "tension_intensity": self._calculate_tension_intensity(tension_type, execution_mode),
            "conflict_tolerance": self._set_conflict_tolerance(tension_type, execution_mode),
            "synthesis_timing": self._determine_synthesis_timing(tension_type, execution_mode),
            "breakthrough_thresholds": self._set_breakthrough_thresholds(tension_type),
            "facilitation_intervention_triggers": self._set_intervention_triggers(tension_type),
            "productive_conflict_indicators": self._define_productive_indicators(tension_type),
            "unproductive_conflict_warnings": self._define_warning_signs(tension_type),
            "synthesis_success_criteria": framework["breakthrough_potential"]
        }
    
    def _plan_synthesis_approach(
        self, 
        tension_type: TensionType, 
        agent_pairs: List[Dict[str, Any]], 
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Plan how to synthesize insights from creative tension."""
        
        framework = self.tension_frameworks[tension_type]
        approach = framework["synthesis_approach"]
        
        synthesis_plans = {
            "staged_realization": {
                "approach": "vision_then_implementation",
                "stages": ["envision", "reality_check", "bridge_building", "staged_execution"],
                "synthesis_method": "iterative_refinement"
            },
            "constraint_innovation": {
                "approach": "constraint_driven_creativity",
                "stages": ["constraint_mapping", "creative_exploration", "feasibility_testing", "innovative_solution"],
                "synthesis_method": "constraint_as_catalyst"
            },
            "value_alignment": {
                "approach": "shared_value_discovery",
                "stages": ["stakeholder_mapping", "value_intersection", "win_win_ideation", "aligned_solution"],
                "synthesis_method": "value_optimization"
            },
            "strategic_creativity": {
                "approach": "purpose_driven_expression",
                "stages": ["strategic_foundation", "creative_exploration", "brand_alignment", "strategic_expression"],
                "synthesis_method": "purpose_creativity_fusion"
            },
            "staged_focusing": {
                "approach": "explore_then_optimize",
                "stages": ["broad_exploration", "pattern_identification", "focus_selection", "optimization"],
                "synthesis_method": "funnel_approach"
            },
            "layered_analysis": {
                "approach": "depth_and_breadth_integration",
                "stages": ["comprehensive_mapping", "deep_dive_selection", "integration", "complete_solution"],
                "synthesis_method": "multi_dimensional_synthesis"
            },
            "quality_velocity": {
                "approach": "iterative_quality_acceleration",
                "stages": ["rapid_iteration", "quality_gates", "velocity_optimization", "quality_velocity_balance"],
                "synthesis_method": "spiral_improvement"
            }
        }
        
        return synthesis_plans.get(approach, synthesis_plans["staged_realization"])
    
    def _generate_facilitation_strategy(
        self, 
        tension_type: TensionType, 
        tension_configuration: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate strategy for facilitating productive creative tension."""
        
        return {
            "facilitation_style": self._determine_facilitation_style(tension_type),
            "intervention_techniques": self._define_intervention_techniques(tension_type),
            "breakthrough_acceleration": self._define_breakthrough_acceleration(tension_type),
            "conflict_navigation": self._define_conflict_navigation(tension_type),
            "synthesis_facilitation": self._define_synthesis_facilitation(tension_type),
            "success_amplification": self._define_success_amplification(tension_type)
        }
    
    def _identify_design_challenges(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Identify design challenges from context."""
        
        # Simplified challenge identification - in practice would be more sophisticated
        return {
            "implementation_clarity": context.get('implementation_uncertainty', 0.5),
            "technical_constraints": context.get('technical_complexity', 0.5),
            "stakeholder_alignment": context.get('stakeholder_conflicts', 0.3),
            "user_business_conflict": context.get('user_business_tension', 0.4),
            "brand_strategy_tension": context.get('brand_alignment_issues', 0.3),
            "complexity_scope": context.get('project_complexity', 0.5),
            "quality_requirements": context.get('quality_standards', 0.7),
            "optimization_opportunity": context.get('optimization_potential', 0.6)
        }
    
    def _assess_innovation_needs(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Assess innovation requirements from context."""
        
        return {
            "breakthrough_requirement": context.get('innovation_ambition', 0.5),
            "paradigm_shift_potential": context.get('disruption_opportunity', 0.3),
            "exploration_requirement": context.get('exploration_needed', 0.6),
            "thorough_exploration": context.get('comprehensive_analysis', 0.5)
        }
    
    def _evaluate_strategic_complexity(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Evaluate strategic complexity from context."""
        
        return {
            "business_pressure": context.get('business_constraints', 0.5),
            "strategic_alignment_need": context.get('strategic_importance', 0.6),
            "comprehensive_analysis_need": context.get('analysis_depth_required', 0.5),
            "delivery_pressure": context.get('time_pressure', 0.4)
        }
    
    def _analyze_creative_ambition(self, context: Dict[str, Any]) -> Dict[str, float]:
        """Analyze creative ambition from context."""
        
        return {
            "visionary_scope": context.get('vision_ambition', 0.5),
            "innovation_risk": context.get('innovation_risk_tolerance', 0.5),
            "expression_importance": context.get('creative_expression_value', 0.6)
        }
    
    def _assess_execution_constraints(self, context: Dict[str, Any], execution_mode: str) -> Dict[str, float]:
        """Assess execution constraints."""
        
        mode_pressures = {
            "simulate": {"time_pressure": 0.2, "speed_pressure": 0.3},
            "ship": {"time_pressure": 0.8, "speed_pressure": 0.9},
            "critique": {"time_pressure": 0.4, "speed_pressure": 0.3},
            "advisory_board": {"time_pressure": 0.5, "speed_pressure": 0.4}
        }
        
        return mode_pressures.get(execution_mode, {"time_pressure": 0.5, "speed_pressure": 0.5})
    
    def _identify_primary_tension_driver(
        self, 
        design_challenges: Dict[str, float], 
        innovation_needs: Dict[str, float], 
        strategic_complexity: Dict[str, float]
    ) -> str:
        """Identify the primary driver for creative tension."""
        
        drivers = {
            "design_challenges": max(design_challenges.values()),
            "innovation_needs": max(innovation_needs.values()),
            "strategic_complexity": max(strategic_complexity.values())
        }
        
        return max(drivers.items(), key=lambda x: x[1])[0]
    
    def _describe_tension_dynamic(self, agent1: str, agent2: str, tension_type: TensionType) -> str:
        """Describe the tension dynamic between two agents."""
        
        char1 = self.agent_characteristics[agent1]
        char2 = self.agent_characteristics[agent2]
        
        return f"{agent1} ({', '.join(char1['natural_tendencies'])}) vs {agent2} ({', '.join(char2['natural_tendencies'])})"
    
    def _strengths_complement(self, weakness: str, strength: str) -> bool:
        """Check if a strength complements a weakness."""
        
        complements = {
            "creative_exploration": ["breakthrough_thinking", "creative_innovation"],
            "user_empathy": ["user_advocacy", "experience_quality"],
            "tactical_execution": ["technical_innovation", "implementation_excellence"],
            "strategic_alignment": ["strategic_thinking", "market_reality"],
            "technical_constraints": ["technical_innovation", "practical_constraints"],
            "business_metrics": ["strategic_thinking", "viability_assessment"]
        }
        
        return strength in complements.get(weakness, [])
    
    def _assess_breakthrough_potential(self, agent1: str, agent2: str, tension_type: TensionType) -> str:
        """Assess breakthrough potential for agent pair."""
        
        framework = self.tension_frameworks[tension_type]
        return framework["breakthrough_potential"]
    
    def _determine_synthesis_approach(self, agent1: str, agent2: str, tension_type: TensionType) -> str:
        """Determine synthesis approach for agent pair."""
        
        framework = self.tension_frameworks[tension_type]
        return framework["synthesis_approach"]
    
    def _calculate_tension_intensity(self, tension_type: TensionType, execution_mode: str) -> float:
        """Calculate appropriate tension intensity."""
        
        base_intensities = {
            TensionType.VISION_VS_EXECUTION: 0.8,
            TensionType.INNOVATION_VS_FEASIBILITY: 0.7,
            TensionType.USER_VS_BUSINESS: 0.6,
            TensionType.CREATIVE_VS_STRATEGIC: 0.7,
            TensionType.EXPLORATION_VS_OPTIMIZATION: 0.6,
            TensionType.DEPTH_VS_BREADTH: 0.5,
            TensionType.SPEED_VS_QUALITY: 0.7
        }
        
        mode_modifiers = {
            "simulate": 0.9,  # High tension for exploration
            "ship": 0.6,      # Moderate tension for delivery
            "critique": 0.8,  # High tension for analysis
            "advisory_board": 1.0  # Maximum tension for strategic decisions
        }
        
        base = base_intensities[tension_type]
        modifier = mode_modifiers.get(execution_mode, 0.7)
        
        return base * modifier
    
    def _set_conflict_tolerance(self, tension_type: TensionType, execution_mode: str) -> float:
        """Set tolerance for productive conflict."""
        
        if execution_mode == "ship":
            return 0.6  # Lower tolerance when shipping
        elif execution_mode == "advisory_board":
            return 0.9  # High tolerance for strategic discussions
        else:
            return 0.7  # Moderate tolerance
    
    def _determine_synthesis_timing(self, tension_type: TensionType, execution_mode: str) -> str:
        """Determine when to synthesize tension outputs."""
        
        timing_strategies = {
            TensionType.VISION_VS_EXECUTION: "after_exploration_phase",
            TensionType.INNOVATION_VS_FEASIBILITY: "iterative_checkpoint",
            TensionType.USER_VS_BUSINESS: "value_alignment_reached",
            TensionType.CREATIVE_VS_STRATEGIC: "creative_options_generated",
            TensionType.EXPLORATION_VS_OPTIMIZATION: "exploration_saturation",
            TensionType.DEPTH_VS_BREADTH: "comprehensive_coverage_achieved",
            TensionType.SPEED_VS_QUALITY: "quality_velocity_balance_found"
        }
        
        return timing_strategies[tension_type]
    
    def _set_breakthrough_thresholds(self, tension_type: TensionType) -> Dict[str, float]:
        """Set thresholds for identifying breakthroughs."""
        
        return {
            "innovation_score": 0.8,
            "synthesis_quality": 0.7,
            "strategic_alignment": 0.8,
            "creative_excellence": 0.7,
            "feasibility_confidence": 0.6
        }
    
    def _set_intervention_triggers(self, tension_type: TensionType) -> List[str]:
        """Set triggers for facilitation intervention."""
        
        return [
            "unproductive_conflict_detected",
            "synthesis_stagnation",
            "breakthrough_opportunity_identified",
            "tension_intensity_too_low",
            "conflict_resolution_needed"
        ]
    
    def _define_productive_indicators(self, tension_type: TensionType) -> List[str]:
        """Define indicators of productive tension."""
        
        return [
            "new_insights_generated",
            "creative_solutions_emerging",
            "quality_improvements_identified",
            "strategic_clarity_increasing",
            "breakthrough_patterns_visible"
        ]
    
    def _define_warning_signs(self, tension_type: TensionType) -> List[str]:
        """Define warning signs of unproductive conflict."""
        
        return [
            "personal_conflict_emerging",
            "circular_arguments",
            "quality_degradation",
            "stakeholder_confusion",
            "synthesis_avoidance"
        ]
    
    def _identify_breakthrough_indicators(self, tension_type: TensionType) -> List[str]:
        """Identify specific breakthrough indicators for tension type."""
        
        indicators = {
            TensionType.VISION_VS_EXECUTION: [
                "visionary_concepts_with_clear_implementation_path",
                "practical_solutions_with_inspiring_vision",
                "staged_realization_roadmap_clarity"
            ],
            TensionType.INNOVATION_VS_FEASIBILITY: [
                "innovative_solutions_within_constraints",
                "constraint_driven_creative_breakthroughs",
                "feasible_paradigm_shifts"
            ],
            TensionType.USER_VS_BUSINESS: [
                "win_win_value_propositions",
                "user_delight_driving_business_success",
                "business_model_innovation_benefiting_users"
            ]
        }
        
        return indicators.get(tension_type, ["creative_breakthrough_achieved", "strategic_innovation_identified"])
    
    def _define_conflict_resolution(self, tension_type: TensionType) -> Dict[str, str]:
        """Define conflict resolution approaches."""
        
        return {
            "resolution_philosophy": "synthesis_over_compromise",
            "intervention_style": "facilitative_guidance",
            "breakthrough_catalyst": "reframe_tension_as_opportunity",
            "synthesis_method": "creative_integration"
        }
    
    def _determine_facilitation_style(self, tension_type: TensionType) -> str:
        """Determine facilitation style for tension type."""
        
        styles = {
            TensionType.VISION_VS_EXECUTION: "visionary_pragmatist",
            TensionType.INNOVATION_VS_FEASIBILITY: "constraint_catalyst",
            TensionType.USER_VS_BUSINESS: "value_alignment_facilitator",
            TensionType.CREATIVE_VS_STRATEGIC: "purpose_driven_creativity",
            TensionType.EXPLORATION_VS_OPTIMIZATION: "progressive_focusing",
            TensionType.DEPTH_VS_BREADTH: "comprehensive_synthesis",
            TensionType.SPEED_VS_QUALITY: "velocity_quality_optimizer"
        }
        
        return styles[tension_type]
    
    def _define_intervention_techniques(self, tension_type: TensionType) -> List[str]:
        """Define intervention techniques for managing tension."""
        
        return [
            "reframe_conflict_as_creative_opportunity",
            "identify_shared_values_and_goals",
            "facilitate_perspective_taking_exercises",
            "guide_synthesis_thinking",
            "catalyze_breakthrough_moments"
        ]
    
    def _define_breakthrough_acceleration(self, tension_type: TensionType) -> List[str]:
        """Define techniques for accelerating breakthroughs."""
        
        return [
            "amplify_productive_tension_patterns",
            "introduce_synthesis_catalysts",
            "facilitate_creative_leaps",
            "connect_disparate_insights",
            "enable_innovative_integration"
        ]
    
    def _define_conflict_navigation(self, tension_type: TensionType) -> List[str]:
        """Define conflict navigation techniques."""
        
        return [
            "acknowledge_valid_perspectives",
            "identify_underlying_needs_and_values",
            "explore_creative_alternatives",
            "facilitate_collaborative_problem_solving",
            "guide_toward_synthesis_solutions"
        ]
    
    def _define_synthesis_facilitation(self, tension_type: TensionType) -> List[str]:
        """Define synthesis facilitation techniques."""
        
        return [
            "pattern_recognition_and_integration",
            "creative_combination_of_perspectives",
            "strategic_alignment_of_solutions",
            "innovative_resolution_development",
            "breakthrough_insight_crystallization"
        ]
    
    def _define_success_amplification(self, tension_type: TensionType) -> List[str]:
        """Define success amplification techniques."""
        
        return [
            "recognize_and_celebrate_breakthroughs",
            "document_successful_tension_patterns",
            "share_insights_across_agent_network",
            "refine_synthesis_approaches",
            "build_creative_momentum"
        ]
    
    def _calculate_pairing_confidence(
        self, 
        tension_analysis: Dict[str, Any], 
        agent_pairs: List[Dict[str, Any]]
    ) -> float:
        """Calculate confidence in pairing selection."""
        
        if not agent_pairs:
            return 0.3
        
        avg_tension_score = sum(pair["productive_tension_score"] for pair in agent_pairs) / len(agent_pairs)
        context_clarity = 1.0 - tension_analysis.get("uncertainty", 0.2)
        
        return (avg_tension_score * 0.6) + (context_clarity * 0.4)
    
    def _identify_assumptions(self) -> List[str]:
        """Identify assumptions in creative tension pairing."""
        return [
            "Productive conflict leads to better outcomes",
            "Agents can engage in constructive tension",
            "Synthesis is achievable from opposing perspectives",
            "Creative breakthroughs emerge from managed conflict",
            "Agent characteristics accurately predict behavior"
        ]
    
    def _assess_uncertainty(self) -> float:
        """Assess uncertainty in tension management."""
        return 0.25  # Moderate uncertainty in creative processes 