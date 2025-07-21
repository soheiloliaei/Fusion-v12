"""
Perspective Overlay System - Strategic Innovation Lenses
Applies multiple strategic perspectives for breakthrough design thinking and innovation.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum

from fusion_agents import BaseAgent


class StrategicPerspective(Enum):
    """Strategic innovation perspectives for design breakthrough."""
    JOBS_TO_BE_DONE = "jobs_to_be_done"        # What job is being hired to do?
    FIRST_PRINCIPLES = "first_principles"      # Fundamental truths and constraints
    CONSTRAINT_REMOVAL = "constraint_removal"  # What if limitations didn't exist?
    FUTURE_BACK = "future_back"               # Working backwards from future vision
    CROSS_POLLINATION = "cross_pollination"   # Learning from other domains
    SYSTEMS_THINKING = "systems_thinking"     # Holistic ecosystem perspective
    PARADOX_RESOLUTION = "paradox_resolution" # Resolving seemingly opposing forces


class PerspectiveOverlaySystem(BaseAgent):
    """
    Applies strategic innovation perspectives to design challenges for breakthrough thinking.
    Overlays multiple lenses to reveal hidden opportunities and innovative solutions.
    """
    
    def __init__(self):
        super().__init__(
            agent_id="PerspectiveOverlaySystem",
            name="Perspective Overlay System",
            role="Applies strategic innovation lenses for breakthrough design thinking",
            capabilities=[
                "multi_perspective_analysis",
                "breakthrough_opportunity_identification",
                "strategic_innovation_facilitation",
                "paradigm_shift_catalyst"
            ],
            quality_metrics={
                "perspective_coverage": {"target": 0.90, "measured_by": "viewpoint_comprehensiveness"},
                "breakthrough_insight_rate": {"target": 0.75, "measured_by": "innovation_scoring"},
                "strategic_alignment": {"target": 0.85, "measured_by": "coherence_assessment"}
            },
            agent_contract={
                "inputs": ["design_challenge", "strategic_context", "innovation_ambition"],
                "guarantees": {"perspective_comprehensiveness": 0.80, "breakthrough_potential": 0.70},
                "fallback_on": ["insufficient_context", "perspective_conflicts"]
            }
        )
        
        self.perspective_frameworks = {
            StrategicPerspective.JOBS_TO_BE_DONE: {
                "description": "Understanding the fundamental job users hire the design to accomplish",
                "key_questions": [
                    "What job is the user truly hiring this design to do?",
                    "What's the deeper functional, emotional, and social need?",
                    "How do users currently get this job done?",
                    "What makes users 'fire' current solutions?",
                    "What would make users love this job-to-be-done experience?"
                ],
                "innovation_lens": "user_motivation_driven",
                "breakthrough_potential": "reframe_entire_value_proposition",
                "application_method": "job_story_mapping",
                "strategic_value": "ensures_user_centered_innovation"
            },
            StrategicPerspective.FIRST_PRINCIPLES: {
                "description": "Breaking down to fundamental truths and building up innovative solutions",
                "key_questions": [
                    "What are the fundamental truths we're building from?",
                    "Which assumptions can we challenge or eliminate?",
                    "What's physically/logically possible vs. conventionally done?",
                    "If we started fresh with no preconceptions, how would we approach this?",
                    "What would we design if we ignored industry conventions?"
                ],
                "innovation_lens": "assumption_challenging",
                "breakthrough_potential": "paradigm_breaking_solutions",
                "application_method": "assumption_deconstruction",
                "strategic_value": "enables_radical_innovation"
            },
            StrategicPerspective.CONSTRAINT_REMOVAL: {
                "description": "Exploring possibilities if current limitations didn't exist",
                "key_questions": [
                    "What would we design if budget/time/tech limitations didn't exist?",
                    "How would this look with unlimited resources?",
                    "What if physics/biology/economics worked differently?",
                    "Which constraints are real vs. assumed?",
                    "How can constraints become creative catalysts?"
                ],
                "innovation_lens": "possibility_expansion",
                "breakthrough_potential": "constraint_transcendent_solutions",
                "application_method": "constraint_liberation_ideation",
                "strategic_value": "reveals_hidden_solution_space"
            },
            StrategicPerspective.FUTURE_BACK: {
                "description": "Working backwards from an ideal future state",
                "key_questions": [
                    "What would this look like in 10 years?",
                    "How will users interact with this in the future?",
                    "What would feel magical then that seems impossible now?",
                    "What future trends will transform this space?",
                    "How do we design for tomorrow's context?"
                ],
                "innovation_lens": "future_vision_driven",
                "breakthrough_potential": "anticipatory_innovation",
                "application_method": "future_scenario_planning",
                "strategic_value": "creates_competitive_advantage"
            },
            StrategicPerspective.CROSS_POLLINATION: {
                "description": "Learning from how other domains solve similar challenges",
                "key_questions": [
                    "How do completely different industries handle similar problems?",
                    "What can we learn from nature/biology/physics?",
                    "How do other cultures approach this challenge?",
                    "What patterns exist across successful solutions?",
                    "Which metaphors or analogies inspire new approaches?"
                ],
                "innovation_lens": "pattern_transfer",
                "breakthrough_potential": "cross_domain_innovation",
                "application_method": "analogical_thinking",
                "strategic_value": "leverages_external_innovation"
            },
            StrategicPerspective.SYSTEMS_THINKING: {
                "description": "Understanding the broader ecosystem and interconnections",
                "key_questions": [
                    "How does this fit into the larger ecosystem?",
                    "What are the feedback loops and system dynamics?",
                    "How might this impact other parts of the system?",
                    "What systemic changes would amplify this solution?",
                    "How do we design for system-wide transformation?"
                ],
                "innovation_lens": "holistic_ecosystem",
                "breakthrough_potential": "system_level_innovation",
                "application_method": "systems_mapping",
                "strategic_value": "ensures_sustainable_innovation"
            },
            StrategicPerspective.PARADOX_RESOLUTION: {
                "description": "Finding innovative solutions to seemingly opposing forces",
                "key_questions": [
                    "How can we achieve both X and Y simultaneously?",
                    "What would make this paradox irrelevant?",
                    "How do we transcend either/or thinking?",
                    "What higher-order solution resolves this tension?",
                    "How can opposing forces become complementary?"
                ],
                "innovation_lens": "paradox_transcendence",
                "breakthrough_potential": "both_and_solutions",
                "application_method": "paradox_integration",
                "strategic_value": "resolves_fundamental_tensions"
            }
        }
        
        self.perspective_application_strategies = {
            "sequential_analysis": "Apply perspectives one by one for depth",
            "parallel_overlay": "Apply multiple perspectives simultaneously",
            "synthesis_integration": "Combine insights from all perspectives",
            "tension_exploration": "Use conflicting perspectives for breakthrough",
            "iterative_refinement": "Progressively apply perspectives to refine solutions"
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply strategic innovation perspectives to design challenges:
        1. Analyze design challenge for perspective relevance
        2. Select optimal perspective combination
        3. Apply each perspective systematically
        4. Synthesize breakthrough insights
        5. Generate strategic recommendations
        """
        design_challenge = inputs.get('design_challenge', '')
        strategic_context = inputs.get('strategic_context', {})
        innovation_ambition = inputs.get('innovation_ambition', 'medium')
        requested_perspectives = inputs.get('perspectives', None)
        execution_mode = inputs.get('execution_mode', 'ship')
        
        # Self-check for perspective application
        self.self_check("Which perspectives will unlock the most breakthrough potential?")
        
        # Analyze challenge for perspective relevance
        challenge_analysis = self._analyze_challenge_for_perspectives(
            design_challenge, strategic_context, innovation_ambition
        )
        
        # Select optimal perspectives
        selected_perspectives = self._select_perspectives(
            challenge_analysis, requested_perspectives, execution_mode
        )
        
        # Apply each perspective
        perspective_insights = self._apply_perspectives(
            design_challenge, strategic_context, selected_perspectives
        )
        
        # Synthesize breakthrough insights
        breakthrough_synthesis = self._synthesize_breakthrough_insights(
            perspective_insights, challenge_analysis
        )
        
        # Generate strategic recommendations
        strategic_recommendations = self._generate_strategic_recommendations(
            breakthrough_synthesis, innovation_ambition
        )
        
        return {
            "selected_perspectives": [p.value for p in selected_perspectives],
            "perspective_insights": perspective_insights,
            "breakthrough_synthesis": breakthrough_synthesis,
            "strategic_recommendations": strategic_recommendations,
            "challenge_analysis": challenge_analysis,
            "innovation_opportunities": self._identify_innovation_opportunities(breakthrough_synthesis),
            "paradigm_shift_potential": self._assess_paradigm_shift_potential(breakthrough_synthesis),
            "implementation_pathway": self._design_implementation_pathway(strategic_recommendations),
            "reasoning_trail": self.reasoning_trail,
            "confidence_score": self._calculate_perspective_confidence(perspective_insights)
        }
    
    def _analyze_challenge_for_perspectives(
        self, 
        design_challenge: str, 
        strategic_context: Dict[str, Any], 
        innovation_ambition: str
    ) -> Dict[str, Any]:
        """Analyze the design challenge to determine optimal perspective application."""
        
        # Analyze challenge characteristics
        challenge_characteristics = self._analyze_challenge_characteristics(design_challenge)
        
        # Assess innovation requirements
        innovation_requirements = self._assess_innovation_requirements(innovation_ambition, strategic_context)
        
        # Identify strategic complexity
        strategic_complexity = self._identify_strategic_complexity(strategic_context)
        
        # Evaluate breakthrough potential
        breakthrough_potential = self._evaluate_breakthrough_potential(
            challenge_characteristics, innovation_requirements
        )
        
        return {
            "challenge_characteristics": challenge_characteristics,
            "innovation_requirements": innovation_requirements,
            "strategic_complexity": strategic_complexity,
            "breakthrough_potential": breakthrough_potential,
            "perspective_readiness": self._assess_perspective_readiness(challenge_characteristics)
        }
    
    def _select_perspectives(
        self, 
        challenge_analysis: Dict[str, Any], 
        requested_perspectives: Optional[List[str]], 
        execution_mode: str
    ) -> List[StrategicPerspective]:
        """Select optimal perspectives based on challenge analysis."""
        
        # If perspectives explicitly requested, validate and use
        if requested_perspectives:
            validated_perspectives = []
            for perspective_name in requested_perspectives:
                try:
                    perspective = StrategicPerspective(perspective_name)
                    validated_perspectives.append(perspective)
                except ValueError:
                    continue
            if validated_perspectives:
                return validated_perspectives
        
        # Score each perspective for relevance
        perspective_scores = {}
        for perspective in StrategicPerspective:
            score = self._score_perspective_relevance(perspective, challenge_analysis, execution_mode)
            perspective_scores[perspective] = score
        
        # Select top perspectives based on execution mode
        selection_counts = {
            "simulate": 5,      # Comprehensive exploration
            "ship": 3,          # Focused application
            "critique": 4,      # Thorough analysis
            "advisory_board": 6 # Maximum perspectives
        }
        
        selection_count = selection_counts.get(execution_mode, 3)
        
        # Sort by score and select top perspectives
        sorted_perspectives = sorted(perspective_scores.items(), key=lambda x: x[1], reverse=True)
        selected = [perspective for perspective, score in sorted_perspectives[:selection_count]]
        
        return selected
    
    def _apply_perspectives(
        self, 
        design_challenge: str, 
        strategic_context: Dict[str, Any], 
        perspectives: List[StrategicPerspective]
    ) -> Dict[str, Dict[str, Any]]:
        """Apply each selected perspective to the design challenge."""
        
        perspective_insights = {}
        
        for perspective in perspectives:
            framework = self.perspective_frameworks[perspective]
            
            # Apply perspective systematically
            insight = self._apply_single_perspective(
                perspective, framework, design_challenge, strategic_context
            )
            
            perspective_insights[perspective.value] = insight
        
        return perspective_insights
    
    def _apply_single_perspective(
        self, 
        perspective: StrategicPerspective, 
        framework: Dict[str, Any], 
        design_challenge: str, 
        strategic_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Apply a single perspective to generate insights."""
        
        # Generate perspective-specific insights
        insights = []
        breakthrough_opportunities = []
        reframe_opportunities = []
        
        # Process each key question
        for question in framework["key_questions"]:
            insight = self._process_perspective_question(
                question, design_challenge, strategic_context, perspective
            )
            insights.append(insight)
            
            # Identify breakthrough opportunities
            if insight.get("breakthrough_potential", 0) > 0.7:
                breakthrough_opportunities.append(insight["insight"])
            
            # Identify reframe opportunities
            if insight.get("reframe_potential", 0) > 0.6:
                reframe_opportunities.append(insight["reframe"])
        
        # Generate perspective summary
        perspective_summary = self._generate_perspective_summary(
            perspective, insights, design_challenge
        )
        
        return {
            "perspective": perspective.value,
            "framework": framework,
            "insights": insights,
            "breakthrough_opportunities": breakthrough_opportunities,
            "reframe_opportunities": reframe_opportunities,
            "perspective_summary": perspective_summary,
            "innovation_potential": self._assess_innovation_potential(insights),
            "strategic_implications": self._identify_strategic_implications(insights, strategic_context)
        }
    
    def _synthesize_breakthrough_insights(
        self, 
        perspective_insights: Dict[str, Dict[str, Any]], 
        challenge_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Synthesize insights from all perspectives to identify breakthrough opportunities."""
        
        # Collect all breakthrough opportunities
        all_breakthroughs = []
        for perspective_data in perspective_insights.values():
            all_breakthroughs.extend(perspective_data["breakthrough_opportunities"])
        
        # Identify patterns across perspectives
        insight_patterns = self._identify_insight_patterns(perspective_insights)
        
        # Find convergent insights
        convergent_insights = self._find_convergent_insights(perspective_insights)
        
        # Identify tension points for creative resolution
        tension_points = self._identify_tension_points(perspective_insights)
        
        # Generate synthesis insights
        synthesis_insights = self._generate_synthesis_insights(
            insight_patterns, convergent_insights, tension_points
        )
        
        # Assess breakthrough potential
        breakthrough_assessment = self._assess_breakthrough_synthesis(
            synthesis_insights, challenge_analysis
        )
        
        return {
            "breakthrough_opportunities": all_breakthroughs,
            "insight_patterns": insight_patterns,
            "convergent_insights": convergent_insights,
            "tension_points": tension_points,
            "synthesis_insights": synthesis_insights,
            "breakthrough_assessment": breakthrough_assessment,
            "paradigm_shift_indicators": self._identify_paradigm_shift_indicators(synthesis_insights)
        }
    
    def _generate_strategic_recommendations(
        self, 
        breakthrough_synthesis: Dict[str, Any], 
        innovation_ambition: str
    ) -> List[Dict[str, Any]]:
        """Generate strategic recommendations based on breakthrough synthesis."""
        
        recommendations = []
        
        # Recommendations from breakthrough opportunities
        for breakthrough in breakthrough_synthesis["breakthrough_opportunities"]:
            recommendation = self._create_breakthrough_recommendation(breakthrough, innovation_ambition)
            recommendations.append(recommendation)
        
        # Recommendations from synthesis insights
        for insight in breakthrough_synthesis["synthesis_insights"]:
            recommendation = self._create_synthesis_recommendation(insight, innovation_ambition)
            recommendations.append(recommendation)
        
        # Recommendations from tension resolution
        for tension in breakthrough_synthesis["tension_points"]:
            recommendation = self._create_tension_resolution_recommendation(tension, innovation_ambition)
            recommendations.append(recommendation)
        
        # Prioritize recommendations
        prioritized_recommendations = self._prioritize_recommendations(recommendations, innovation_ambition)
        
        return prioritized_recommendations[:5]  # Return top 5 recommendations
    
    def _analyze_challenge_characteristics(self, design_challenge: str) -> Dict[str, Any]:
        """Analyze characteristics of the design challenge."""
        
        challenge_lower = design_challenge.lower()
        
        # Analyze challenge type indicators
        user_focus = any(word in challenge_lower for word in ["user", "customer", "experience", "journey"])
        system_focus = any(word in challenge_lower for word in ["system", "ecosystem", "platform", "infrastructure"])
        innovation_focus = any(word in challenge_lower for word in ["innovation", "breakthrough", "disrupt", "transform"])
        constraint_focus = any(word in challenge_lower for word in ["constraint", "limitation", "within", "budget"])
        future_focus = any(word in challenge_lower for word in ["future", "tomorrow", "next", "evolving"])
        
        return {
            "user_centered": user_focus,
            "system_oriented": system_focus,
            "innovation_driven": innovation_focus,
            "constraint_bounded": constraint_focus,
            "future_oriented": future_focus,
            "complexity_level": self._assess_complexity_level(design_challenge),
            "ambiguity_level": self._assess_ambiguity_level(design_challenge)
        }
    
    def _assess_innovation_requirements(self, innovation_ambition: str, strategic_context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess innovation requirements based on ambition and context."""
        
        ambition_levels = {
            "low": {"breakthrough_need": 0.3, "risk_tolerance": 0.2, "timeline_pressure": 0.8},
            "medium": {"breakthrough_need": 0.6, "risk_tolerance": 0.5, "timeline_pressure": 0.5},
            "high": {"breakthrough_need": 0.8, "risk_tolerance": 0.7, "timeline_pressure": 0.3},
            "breakthrough": {"breakthrough_need": 0.9, "risk_tolerance": 0.8, "timeline_pressure": 0.2}
        }
        
        return ambition_levels.get(innovation_ambition, ambition_levels["medium"])
    
    def _identify_strategic_complexity(self, strategic_context: Dict[str, Any]) -> Dict[str, Any]:
        """Identify strategic complexity factors."""
        
        return {
            "stakeholder_complexity": strategic_context.get('stakeholder_count', 3) / 10.0,
            "market_complexity": strategic_context.get('market_dynamics', 'stable') == 'complex',
            "technical_complexity": strategic_context.get('technical_challenges', 'medium') == 'high',
            "regulatory_complexity": strategic_context.get('regulatory_constraints', False),
            "competitive_complexity": strategic_context.get('competitive_pressure', 'medium') == 'high'
        }
    
    def _evaluate_breakthrough_potential(
        self, 
        challenge_characteristics: Dict[str, Any], 
        innovation_requirements: Dict[str, Any]
    ) -> float:
        """Evaluate overall breakthrough potential."""
        
        # Factors that increase breakthrough potential
        potential_factors = [
            challenge_characteristics.get("innovation_driven", False) * 0.3,
            challenge_characteristics.get("future_oriented", False) * 0.2,
            innovation_requirements.get("breakthrough_need", 0.5) * 0.3,
            innovation_requirements.get("risk_tolerance", 0.5) * 0.2
        ]
        
        return sum(potential_factors)
    
    def _assess_perspective_readiness(self, challenge_characteristics: Dict[str, Any]) -> float:
        """Assess readiness for perspective application."""
        
        readiness_factors = [
            challenge_characteristics.get("complexity_level", 0.5),
            1.0 - challenge_characteristics.get("ambiguity_level", 0.5),  # Less ambiguity = more ready
            challenge_characteristics.get("innovation_driven", False) * 0.5 + 0.5
        ]
        
        return sum(readiness_factors) / len(readiness_factors)
    
    def _score_perspective_relevance(
        self, 
        perspective: StrategicPerspective, 
        challenge_analysis: Dict[str, Any], 
        execution_mode: str
    ) -> float:
        """Score how relevant a perspective is for the current challenge."""
        
        characteristics = challenge_analysis["challenge_characteristics"]
        innovation_req = challenge_analysis["innovation_requirements"]
        breakthrough_potential = challenge_analysis["breakthrough_potential"]
        
        # Base scoring for each perspective
        relevance_scores = {
            StrategicPerspective.JOBS_TO_BE_DONE: (
                characteristics.get("user_centered", False) * 0.4 +
                innovation_req.get("breakthrough_need", 0.5) * 0.3 +
                0.3  # Always somewhat relevant
            ),
            StrategicPerspective.FIRST_PRINCIPLES: (
                characteristics.get("innovation_driven", False) * 0.4 +
                innovation_req.get("breakthrough_need", 0.5) * 0.4 +
                breakthrough_potential * 0.2
            ),
            StrategicPerspective.CONSTRAINT_REMOVAL: (
                characteristics.get("constraint_bounded", False) * 0.4 +
                innovation_req.get("risk_tolerance", 0.5) * 0.3 +
                breakthrough_potential * 0.3
            ),
            StrategicPerspective.FUTURE_BACK: (
                characteristics.get("future_oriented", False) * 0.4 +
                innovation_req.get("breakthrough_need", 0.5) * 0.3 +
                breakthrough_potential * 0.3
            ),
            StrategicPerspective.CROSS_POLLINATION: (
                characteristics.get("innovation_driven", False) * 0.3 +
                breakthrough_potential * 0.4 +
                innovation_req.get("risk_tolerance", 0.5) * 0.3
            ),
            StrategicPerspective.SYSTEMS_THINKING: (
                characteristics.get("system_oriented", False) * 0.4 +
                characteristics.get("complexity_level", 0.5) * 0.3 +
                breakthrough_potential * 0.3
            ),
            StrategicPerspective.PARADOX_RESOLUTION: (
                characteristics.get("complexity_level", 0.5) * 0.3 +
                breakthrough_potential * 0.4 +
                innovation_req.get("breakthrough_need", 0.5) * 0.3
            )
        }
        
        base_score = relevance_scores[perspective]
        
        # Execution mode modifiers
        mode_modifiers = {
            "simulate": 1.0,       # All perspectives valuable
            "ship": 0.8,           # Slightly prefer practical perspectives
            "critique": 0.9,       # Most perspectives valuable for analysis
            "advisory_board": 1.1  # Boost all perspectives for strategic decisions
        }
        
        modifier = mode_modifiers.get(execution_mode, 1.0)
        
        return min(base_score * modifier, 1.0)
    
    def _process_perspective_question(
        self, 
        question: str, 
        design_challenge: str, 
        strategic_context: Dict[str, Any], 
        perspective: StrategicPerspective
    ) -> Dict[str, Any]:
        """Process a perspective-specific question to generate insights."""
        
        # Simplified insight generation - in practice would be more sophisticated
        insight_strength = 0.6 + (hash(question + design_challenge) % 30) / 100.0
        breakthrough_potential = 0.5 + (hash(perspective.value + question) % 40) / 100.0
        reframe_potential = 0.4 + (hash(design_challenge + question) % 50) / 100.0
        
        return {
            "question": question,
            "insight": f"Perspective-driven insight addressing: {question[:50]}...",
            "insight_strength": insight_strength,
            "breakthrough_potential": breakthrough_potential,
            "reframe_potential": reframe_potential,
            "reframe": f"Reframed through {perspective.value} lens",
            "strategic_implications": ["implication_1", "implication_2"]
        }
    
    def _generate_perspective_summary(
        self, 
        perspective: StrategicPerspective, 
        insights: List[Dict[str, Any]], 
        design_challenge: str
    ) -> str:
        """Generate a summary of insights from a perspective."""
        
        framework = self.perspective_frameworks[perspective]
        avg_strength = sum(insight["insight_strength"] for insight in insights) / len(insights)
        
        return f"{framework['description']} reveals {len(insights)} insights with {avg_strength:.1f} average strength for {design_challenge[:30]}..."
    
    def _assess_innovation_potential(self, insights: List[Dict[str, Any]]) -> float:
        """Assess innovation potential from perspective insights."""
        
        if not insights:
            return 0.0
        
        breakthrough_scores = [insight["breakthrough_potential"] for insight in insights]
        return sum(breakthrough_scores) / len(breakthrough_scores)
    
    def _identify_strategic_implications(
        self, 
        insights: List[Dict[str, Any]], 
        strategic_context: Dict[str, Any]
    ) -> List[str]:
        """Identify strategic implications from perspective insights."""
        
        implications = []
        for insight in insights:
            implications.extend(insight.get("strategic_implications", []))
        
        return list(set(implications))  # Remove duplicates
    
    def _identify_insight_patterns(self, perspective_insights: Dict[str, Dict[str, Any]]) -> List[str]:
        """Identify patterns across perspective insights."""
        
        patterns = []
        
        # Check for common themes
        all_insights = []
        for perspective_data in perspective_insights.values():
            all_insights.extend([insight["insight"] for insight in perspective_data["insights"]])
        
        # Simplified pattern detection
        if len(all_insights) > 5:
            patterns.append("High insight generation across perspectives")
        
        if any("user" in insight.lower() for insight in all_insights):
            patterns.append("Strong user-centric theme across perspectives")
        
        if any("system" in insight.lower() for insight in all_insights):
            patterns.append("Systems-level thinking emerging")
        
        return patterns
    
    def _find_convergent_insights(self, perspective_insights: Dict[str, Dict[str, Any]]) -> List[str]:
        """Find insights that converge across multiple perspectives."""
        
        convergent = []
        
        # Simplified convergence detection
        perspective_summaries = [data["perspective_summary"] for data in perspective_insights.values()]
        
        # Look for common themes
        if len(perspective_summaries) > 2:
            convergent.append("Multiple perspectives align on core innovation opportunity")
        
        return convergent
    
    def _identify_tension_points(self, perspective_insights: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify tension points between perspectives for creative resolution."""
        
        tensions = []
        
        # Simplified tension detection
        perspectives = list(perspective_insights.keys())
        
        if "first_principles" in perspectives and "constraint_removal" in perspectives:
            tensions.append({
                "tension": "fundamental_truths_vs_unlimited_possibilities",
                "perspectives": ["first_principles", "constraint_removal"],
                "creative_opportunity": "Constraint-driven innovation from first principles"
            })
        
        if "jobs_to_be_done" in perspectives and "systems_thinking" in perspectives:
            tensions.append({
                "tension": "user_focus_vs_system_optimization",
                "perspectives": ["jobs_to_be_done", "systems_thinking"],
                "creative_opportunity": "User-centric system design"
            })
        
        return tensions
    
    def _generate_synthesis_insights(
        self, 
        patterns: List[str], 
        convergent: List[str], 
        tensions: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Generate synthesis insights from pattern analysis."""
        
        synthesis = []
        
        # From patterns
        for pattern in patterns:
            synthesis.append({
                "type": "pattern_insight",
                "insight": f"Pattern-based insight: {pattern}",
                "strategic_value": "high",
                "implementation_priority": "medium"
            })
        
        # From convergence
        for convergent_insight in convergent:
            synthesis.append({
                "type": "convergent_insight",
                "insight": f"Convergent insight: {convergent_insight}",
                "strategic_value": "high",
                "implementation_priority": "high"
            })
        
        # From tensions
        for tension in tensions:
            synthesis.append({
                "type": "tension_resolution",
                "insight": f"Creative resolution: {tension['creative_opportunity']}",
                "strategic_value": "breakthrough",
                "implementation_priority": "high"
            })
        
        return synthesis
    
    def _assess_breakthrough_synthesis(
        self, 
        synthesis_insights: List[Dict[str, Any]], 
        challenge_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assess the breakthrough potential of the synthesis."""
        
        breakthrough_count = sum(1 for insight in synthesis_insights 
                                if insight.get("strategic_value") == "breakthrough")
        
        high_value_count = sum(1 for insight in synthesis_insights 
                              if insight.get("strategic_value") == "high")
        
        total_insights = len(synthesis_insights)
        
        if total_insights == 0:
            breakthrough_score = 0.0
        else:
            breakthrough_score = (breakthrough_count * 0.6 + high_value_count * 0.4) / total_insights
        
        return {
            "breakthrough_score": breakthrough_score,
            "total_insights": total_insights,
            "breakthrough_insights": breakthrough_count,
            "high_value_insights": high_value_count,
            "readiness_for_innovation": breakthrough_score > 0.6
        }
    
    def _identify_paradigm_shift_indicators(self, synthesis_insights: List[Dict[str, Any]]) -> List[str]:
        """Identify indicators of potential paradigm shifts."""
        
        indicators = []
        
        breakthrough_insights = [insight for insight in synthesis_insights 
                               if insight.get("strategic_value") == "breakthrough"]
        
        if len(breakthrough_insights) > 1:
            indicators.append("Multiple breakthrough insights suggest paradigm shift potential")
        
        tension_resolutions = [insight for insight in synthesis_insights 
                             if insight.get("type") == "tension_resolution"]
        
        if tension_resolutions:
            indicators.append("Creative tension resolution indicates paradigm transcendence")
        
        return indicators
    
    def _identify_innovation_opportunities(self, breakthrough_synthesis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify specific innovation opportunities from synthesis."""
        
        opportunities = []
        
        # From breakthrough assessment
        if breakthrough_synthesis["breakthrough_assessment"]["readiness_for_innovation"]:
            opportunities.append({
                "opportunity": "High-impact innovation implementation",
                "confidence": "high",
                "strategic_value": "breakthrough"
            })
        
        # From synthesis insights
        for insight in breakthrough_synthesis["synthesis_insights"]:
            if insight.get("strategic_value") in ["high", "breakthrough"]:
                opportunities.append({
                    "opportunity": insight["insight"],
                    "confidence": "medium",
                    "strategic_value": insight["strategic_value"]
                })
        
        return opportunities
    
    def _assess_paradigm_shift_potential(self, breakthrough_synthesis: Dict[str, Any]) -> Dict[str, Any]:
        """Assess potential for paradigm shift."""
        
        indicators = breakthrough_synthesis.get("paradigm_shift_indicators", [])
        breakthrough_score = breakthrough_synthesis["breakthrough_assessment"]["breakthrough_score"]
        
        shift_potential = len(indicators) * 0.3 + breakthrough_score * 0.7
        
        return {
            "shift_potential_score": min(shift_potential, 1.0),
            "indicators": indicators,
            "readiness": shift_potential > 0.7,
            "confidence": breakthrough_score
        }
    
    def _design_implementation_pathway(self, recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Design implementation pathway for strategic recommendations."""
        
        high_priority = [rec for rec in recommendations if rec.get("priority") == "high"]
        medium_priority = [rec for rec in recommendations if rec.get("priority") == "medium"]
        
        return {
            "immediate_actions": high_priority[:2],
            "near_term_initiatives": high_priority[2:] + medium_priority[:2],
            "long_term_strategic": medium_priority[2:],
            "implementation_sequence": "parallel_execution_with_strategic_coordination"
        }
    
    def _create_breakthrough_recommendation(self, breakthrough: str, innovation_ambition: str) -> Dict[str, Any]:
        """Create recommendation from breakthrough opportunity."""
        
        priority_map = {
            "low": "medium",
            "medium": "high", 
            "high": "high",
            "breakthrough": "high"
        }
        
        return {
            "recommendation": f"Pursue breakthrough opportunity: {breakthrough[:60]}...",
            "type": "breakthrough_pursuit",
            "priority": priority_map.get(innovation_ambition, "medium"),
            "strategic_value": "high",
            "implementation_complexity": "high"
        }
    
    def _create_synthesis_recommendation(self, insight: Dict[str, Any], innovation_ambition: str) -> Dict[str, Any]:
        """Create recommendation from synthesis insight."""
        
        return {
            "recommendation": f"Implement synthesis insight: {insight['insight'][:60]}...",
            "type": "synthesis_implementation",
            "priority": insight.get("implementation_priority", "medium"),
            "strategic_value": insight.get("strategic_value", "medium"),
            "implementation_complexity": "medium"
        }
    
    def _create_tension_resolution_recommendation(self, tension: Dict[str, Any], innovation_ambition: str) -> Dict[str, Any]:
        """Create recommendation from tension resolution."""
        
        return {
            "recommendation": f"Resolve creative tension: {tension['creative_opportunity']}",
            "type": "tension_resolution",
            "priority": "high",
            "strategic_value": "breakthrough",
            "implementation_complexity": "high"
        }
    
    def _prioritize_recommendations(self, recommendations: List[Dict[str, Any]], innovation_ambition: str) -> List[Dict[str, Any]]:
        """Prioritize recommendations based on strategic value and ambition."""
        
        # Priority scoring
        priority_scores = {"high": 3, "medium": 2, "low": 1}
        value_scores = {"breakthrough": 4, "high": 3, "medium": 2, "low": 1}
        
        for rec in recommendations:
            priority_score = priority_scores.get(rec.get("priority", "medium"), 2)
            value_score = value_scores.get(rec.get("strategic_value", "medium"), 2)
            
            # Boost scores based on innovation ambition
            ambition_boost = {"breakthrough": 1.5, "high": 1.3, "medium": 1.0, "low": 0.8}
            boost = ambition_boost.get(innovation_ambition, 1.0)
            
            rec["total_score"] = (priority_score + value_score) * boost
        
        # Sort by total score
        return sorted(recommendations, key=lambda r: r["total_score"], reverse=True)
    
    def _assess_complexity_level(self, design_challenge: str) -> float:
        """Assess complexity level of the design challenge."""
        
        complexity_indicators = ["complex", "multiple", "integrate", "system", "ecosystem", "stakeholder"]
        challenge_lower = design_challenge.lower()
        
        complexity_count = sum(1 for indicator in complexity_indicators if indicator in challenge_lower)
        return min(complexity_count / len(complexity_indicators), 1.0)
    
    def _assess_ambiguity_level(self, design_challenge: str) -> float:
        """Assess ambiguity level of the design challenge."""
        
        clarity_indicators = ["specific", "clear", "defined", "exactly", "precisely"]
        challenge_lower = design_challenge.lower()
        
        clarity_count = sum(1 for indicator in clarity_indicators if indicator in challenge_lower)
        return max(1.0 - (clarity_count / len(clarity_indicators)), 0.0)
    
    def _calculate_perspective_confidence(self, perspective_insights: Dict[str, Dict[str, Any]]) -> float:
        """Calculate confidence in perspective application."""
        
        if not perspective_insights:
            return 0.3
        
        # Average insight strength across all perspectives
        all_strengths = []
        for perspective_data in perspective_insights.values():
            for insight in perspective_data["insights"]:
                all_strengths.append(insight["insight_strength"])
        
        if not all_strengths:
            return 0.5
        
        avg_strength = sum(all_strengths) / len(all_strengths)
        perspective_coverage = len(perspective_insights) / 7.0  # Max 7 perspectives
        
        return (avg_strength * 0.7) + (perspective_coverage * 0.3)
    
    def _identify_assumptions(self) -> List[str]:
        """Identify assumptions in perspective overlay application."""
        return [
            "Multiple perspectives provide better insights than single viewpoint",
            "Strategic innovation frameworks are universally applicable",
            "Breakthrough insights emerge from perspective synthesis",
            "Creative tension between perspectives drives innovation",
            "Design challenges benefit from strategic perspective analysis"
        ]
    
    def _assess_uncertainty(self) -> float:
        """Assess uncertainty in perspective application."""
        return 0.2  # Moderate confidence in perspective frameworks 