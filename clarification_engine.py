"""
ClarificationEngine - Design-Focused Clarity and Strategic Innovation
Forces clarity through strategic questioning before complex creative processing.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
import re

from fusion_agents import BaseAgent


class ClarificationEngine(BaseAgent):
    """
    Forces clarity through strategic questioning focused on design craft and innovation.
    Optimized for creative work, strategic thinking, and breakthrough ideas.
    """
    
    def __init__(self):
        super().__init__(
            agent_id="ClarificationEngine",
            name="Clarification Engine",
            role="Forces clarity through strategic questioning for design excellence and innovation",
            capabilities=[
                "design_requirement_clarification",
                "creative_ambiguity_resolution", 
                "strategic_innovation_questioning",
                "breakthrough_thinking_facilitation"
            ],
            quality_metrics={
                "clarification_completeness": {"target": 0.90, "measured_by": "requirement_coverage"},
                "creative_clarity_score": {"target": 0.85, "measured_by": "design_brief_quality"},
                "innovation_potential_unlock": {"target": 0.80, "measured_by": "breakthrough_idea_generation"}
            },
            agent_contract={
                "inputs": ["ambiguous_task", "context", "design_domain"],
                "guarantees": {"clarification_completeness": 0.85, "innovation_readiness": 0.80},
                "fallback_on": ["user_unavailable", "insufficient_domain_context"]
            }
        )
        
        self.design_domains = {
            "ui_ux": "User interface and user experience design",
            "product_strategy": "Product vision and strategic direction",
            "brand_identity": "Brand expression and visual identity",
            "service_design": "Service experience and touchpoint design",
            "innovation_strategy": "Breakthrough thinking and strategic innovation",
            "design_systems": "Systematic design approach and scalability"
        }
        
        self.innovation_frameworks = {
            "jobs_to_be_done": "What job is the user hiring this design to do?",
            "first_principles": "What are the fundamental truths we're building from?",
            "constraint_removal": "What if this limitation didn't exist?",
            "future_back_thinking": "What would this look like in 10 years?",
            "cross_pollination": "How do other industries solve similar problems?"
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute clarification workflow focused on design excellence and innovation:
        1. Analyze ambiguity patterns in creative/strategic context
        2. Generate targeted clarification questions
        3. Apply innovation frameworks for breakthrough thinking
        4. Prepare enhanced brief for creative agents
        """
        task_text = inputs.get('task_text', '')
        context = inputs.get('context', {})
        design_domain = inputs.get('design_domain', 'ui_ux')
        execution_mode = inputs.get('execution_mode', 'ship')
        
        # Self-check for creative clarity
        self.self_check("What creative assumptions might limit breakthrough thinking?")
        
        # Analyze ambiguity with design focus
        ambiguity_analysis = self._analyze_design_ambiguity(task_text, design_domain)
        
        # Generate clarification questions
        clarification_questions = self._generate_design_clarification_questions(
            task_text, ambiguity_analysis, design_domain, execution_mode
        )
        
        # Apply innovation frameworks
        innovation_questions = self._apply_innovation_frameworks(task_text, context)
        
        # Create enhanced design brief
        enhanced_brief = self._create_enhanced_design_brief(
            task_text, context, clarification_questions, innovation_questions
        )
        
        # Calculate innovation readiness
        innovation_readiness = self._assess_innovation_readiness(enhanced_brief)
        
        return {
            "clarification_required": len(clarification_questions) > 0,
            "clarification_questions": clarification_questions,
            "innovation_questions": innovation_questions,
            "enhanced_brief": enhanced_brief,
            "ambiguity_analysis": ambiguity_analysis,
            "innovation_readiness": innovation_readiness,
            "design_domain": design_domain,
            "execution_mode": execution_mode,
            "reasoning_trail": self.reasoning_trail,
            "confidence_score": self._calculate_confidence_score(ambiguity_analysis)
        }
    
    def _analyze_design_ambiguity(self, task_text: str, design_domain: str) -> Dict[str, Any]:
        """Analyze ambiguity patterns specific to design and creative work."""
        
        # Design-specific ambiguity indicators
        design_ambiguity_indicators = {
            "outcome_clarity": self._assess_outcome_clarity(task_text),
            "audience_definition": self._assess_audience_clarity(task_text),
            "constraint_definition": self._assess_constraint_clarity(task_text),
            "success_criteria": self._assess_success_criteria_clarity(task_text),
            "innovation_scope": self._assess_innovation_scope_clarity(task_text),
            "design_context": self._assess_design_context_clarity(task_text, design_domain)
        }
        
        # Calculate overall ambiguity score
        overall_ambiguity = sum(design_ambiguity_indicators.values()) / len(design_ambiguity_indicators)
        
        return {
            "indicators": design_ambiguity_indicators,
            "overall_score": overall_ambiguity,
            "high_ambiguity_areas": [
                area for area, score in design_ambiguity_indicators.items() 
                if score > 0.6
            ],
            "domain": design_domain
        }
    
    def _generate_design_clarification_questions(
        self, 
        task_text: str, 
        ambiguity_analysis: Dict[str, Any], 
        design_domain: str,
        execution_mode: str
    ) -> List[Dict[str, Any]]:
        """Generate targeted clarification questions for design excellence."""
        
        questions = []
        indicators = ambiguity_analysis["indicators"]
        
        # Outcome clarity questions
        if indicators["outcome_clarity"] > 0.5:
            questions.append({
                "category": "outcome_definition",
                "question": "What specific outcome should this design achieve? How will users' lives be different?",
                "priority": "high",
                "design_focus": "impact_definition"
            })
        
        # Audience definition questions
        if indicators["audience_definition"] > 0.5:
            questions.append({
                "category": "audience_clarity",
                "question": "Who exactly is this for? What's their context, mindset, and current behavior?",
                "priority": "high",
                "design_focus": "user_understanding"
            })
        
        # Innovation scope questions
        if indicators["innovation_scope"] > 0.4:
            questions.append({
                "category": "innovation_ambition",
                "question": "How innovative should this be? Incremental improvement or breakthrough reimagining?",
                "priority": "medium",
                "design_focus": "innovation_level"
            })
        
        # Constraint definition questions
        if indicators["constraint_definition"] > 0.6:
            questions.append({
                "category": "design_constraints",
                "question": "What are the real constraints vs. assumed limitations? What's truly non-negotiable?",
                "priority": "medium",
                "design_focus": "constraint_reality"
            })
        
        # Success criteria questions
        if indicators["success_criteria"] > 0.5:
            questions.append({
                "category": "success_definition",
                "question": "How will we know this design is successful? What behavior change indicates success?",
                "priority": "high",
                "design_focus": "success_metrics"
            })
        
        # Domain-specific questions
        domain_questions = self._get_domain_specific_questions(design_domain, task_text)
        questions.extend(domain_questions)
        
        # Execution mode specific questions
        mode_questions = self._get_execution_mode_questions(execution_mode, task_text)
        questions.extend(mode_questions)
        
        return questions
    
    def _apply_innovation_frameworks(self, task_text: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply innovation frameworks for breakthrough thinking."""
        
        innovation_questions = []
        
        # Jobs-to-be-Done framework
        innovation_questions.append({
            "framework": "jobs_to_be_done",
            "question": "What job is the user truly hiring this design to accomplish? What's the deeper need?",
            "thinking_mode": "user_motivation",
            "breakthrough_potential": "high"
        })
        
        # First principles thinking
        innovation_questions.append({
            "framework": "first_principles",
            "question": "If we started from scratch with no assumptions, how would we solve this?",
            "thinking_mode": "fundamental_truths",
            "breakthrough_potential": "high"
        })
        
        # Constraint removal
        innovation_questions.append({
            "framework": "constraint_removal",
            "question": "What would we design if technical limitations, budget, or time didn't exist?",
            "thinking_mode": "possibility_expansion",
            "breakthrough_potential": "medium"
        })
        
        # Future-back thinking
        innovation_questions.append({
            "framework": "future_back_thinking",
            "question": "How will users interact with this in 10 years? What would feel magical then?",
            "thinking_mode": "future_vision",
            "breakthrough_potential": "high"
        })
        
        # Cross-pollination
        innovation_questions.append({
            "framework": "cross_pollination",
            "question": "How do completely different industries handle similar challenges?",
            "thinking_mode": "pattern_transfer",
            "breakthrough_potential": "medium"
        })
        
        return innovation_questions
    
    def _create_enhanced_design_brief(
        self,
        task_text: str,
        context: Dict[str, Any],
        clarification_questions: List[Dict[str, Any]],
        innovation_questions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Create an enhanced design brief with clarity and innovation focus."""
        
        return {
            "original_task": task_text,
            "enhanced_context": context,
            "clarity_requirements": {
                "questions_to_resolve": clarification_questions,
                "ambiguity_areas": [q["category"] for q in clarification_questions],
                "priority_clarifications": [
                    q for q in clarification_questions if q["priority"] == "high"
                ]
            },
            "innovation_opportunities": {
                "breakthrough_questions": innovation_questions,
                "thinking_frameworks": [q["framework"] for q in innovation_questions],
                "high_potential_areas": [
                    q for q in innovation_questions if q["breakthrough_potential"] == "high"
                ]
            },
            "design_readiness": {
                "clarity_score": self._calculate_clarity_score(clarification_questions),
                "innovation_priming": self._calculate_innovation_priming(innovation_questions),
                "ready_for_execution": len(clarification_questions) < 3
            },
            "next_steps": self._generate_next_steps(clarification_questions, innovation_questions)
        }
    
    def _assess_outcome_clarity(self, task_text: str) -> float:
        """Assess clarity of desired outcome."""
        clarity_indicators = [
            "will result in", "so that", "in order to", "the goal is",
            "users will be able to", "success looks like", "the outcome"
        ]
        
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in clarity_indicators if indicator in text_lower)
        
        # Higher score = more ambiguous (less clear)
        return max(0.0, 1.0 - (found_indicators * 0.3))
    
    def _assess_audience_clarity(self, task_text: str) -> float:
        """Assess clarity of target audience."""
        audience_indicators = [
            "users", "customers", "for people who", "target audience",
            "persona", "user type", "demographic", "segment"
        ]
        
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in audience_indicators if indicator in text_lower)
        
        return max(0.0, 1.0 - (found_indicators * 0.25))
    
    def _assess_constraint_clarity(self, task_text: str) -> float:
        """Assess clarity of constraints and limitations."""
        constraint_indicators = [
            "constraint", "limitation", "requirement", "must", "cannot",
            "within", "budget", "timeline", "technical", "platform"
        ]
        
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in constraint_indicators if indicator in text_lower)
        
        return max(0.0, 1.0 - (found_indicators * 0.2))
    
    def _assess_success_criteria_clarity(self, task_text: str) -> float:
        """Assess clarity of success criteria."""
        success_indicators = [
            "success", "measure", "metric", "kpi", "goal", "target",
            "achieve", "improve", "increase", "reduce", "optimize"
        ]
        
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in success_indicators if indicator in text_lower)
        
        return max(0.0, 1.0 - (found_indicators * 0.25))
    
    def _assess_innovation_scope_clarity(self, task_text: str) -> float:
        """Assess clarity of innovation ambition."""
        innovation_indicators = [
            "innovative", "breakthrough", "revolutionary", "reimagine",
            "disrupt", "transform", "novel", "creative", "original"
        ]
        
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in innovation_indicators if indicator in text_lower)
        
        return max(0.0, 1.0 - (found_indicators * 0.3))
    
    def _assess_design_context_clarity(self, task_text: str, design_domain: str) -> float:
        """Assess clarity of design context."""
        domain_indicators = {
            "ui_ux": ["interface", "experience", "usability", "interaction"],
            "product_strategy": ["strategy", "vision", "roadmap", "market"],
            "brand_identity": ["brand", "identity", "voice", "personality"],
            "service_design": ["service", "touchpoint", "journey", "experience"],
            "innovation_strategy": ["innovation", "disruption", "opportunity", "future"],
            "design_systems": ["system", "scalable", "consistent", "components"]
        }
        
        relevant_indicators = domain_indicators.get(design_domain, [])
        text_lower = task_text.lower()
        found_indicators = sum(1 for indicator in relevant_indicators if indicator in text_lower)
        
        return max(0.0, 1.0 - (found_indicators * 0.3))
    
    def _get_domain_specific_questions(self, design_domain: str, task_text: str) -> List[Dict[str, Any]]:
        """Generate domain-specific clarification questions."""
        
        domain_questions = {
            "ui_ux": [
                {
                    "category": "interaction_model",
                    "question": "What's the core interaction model? How should users feel during the experience?",
                    "priority": "medium",
                    "design_focus": "interaction_design"
                }
            ],
            "product_strategy": [
                {
                    "category": "strategic_positioning",
                    "question": "How does this fit into the bigger strategic vision? What advantage are we building?",
                    "priority": "high",
                    "design_focus": "strategic_alignment"
                }
            ],
            "innovation_strategy": [
                {
                    "category": "breakthrough_ambition",
                    "question": "Are we optimizing existing patterns or creating new paradigms?",
                    "priority": "high",
                    "design_focus": "innovation_scope"
                }
            ]
        }
        
        return domain_questions.get(design_domain, [])
    
    def _get_execution_mode_questions(self, execution_mode: str, task_text: str) -> List[Dict[str, Any]]:
        """Generate execution mode specific questions."""
        
        mode_questions = {
            "simulate": [
                {
                    "category": "exploration_scope",
                    "question": "What scenarios should we explore? What assumptions should we test?",
                    "priority": "medium",
                    "design_focus": "exploration_planning"
                }
            ],
            "ship": [
                {
                    "category": "delivery_readiness",
                    "question": "What's the minimum viable solution that still delivers the core value?",
                    "priority": "high",
                    "design_focus": "delivery_optimization"
                }
            ],
            "critique": [
                {
                    "category": "evaluation_criteria",
                    "question": "What specific aspects should we evaluate? What would make this fail?",
                    "priority": "medium",
                    "design_focus": "critical_evaluation"
                }
            ],
            "advisory_board": [
                {
                    "category": "perspective_requirements",
                    "question": "What different viewpoints would add the most value to this decision?",
                    "priority": "medium",
                    "design_focus": "multi_perspective_planning"
                }
            ]
        }
        
        return mode_questions.get(execution_mode, [])
    
    def _assess_innovation_readiness(self, enhanced_brief: Dict[str, Any]) -> float:
        """Assess readiness for breakthrough innovation work."""
        
        clarity_score = enhanced_brief["design_readiness"]["clarity_score"]
        innovation_priming = enhanced_brief["design_readiness"]["innovation_priming"]
        
        # Innovation readiness combines clarity and breakthrough preparation
        innovation_readiness = (clarity_score * 0.4) + (innovation_priming * 0.6)
        
        return min(innovation_readiness, 1.0)
    
    def _calculate_clarity_score(self, clarification_questions: List[Dict[str, Any]]) -> float:
        """Calculate how clear the requirements are."""
        if not clarification_questions:
            return 1.0
        
        high_priority_questions = sum(1 for q in clarification_questions if q["priority"] == "high")
        total_questions = len(clarification_questions)
        
        # More high-priority questions = lower clarity
        clarity_penalty = (high_priority_questions * 0.3) + (total_questions * 0.1)
        
        return max(0.0, 1.0 - clarity_penalty)
    
    def _calculate_innovation_priming(self, innovation_questions: List[Dict[str, Any]]) -> float:
        """Calculate how well primed for innovation thinking."""
        high_potential_count = sum(1 for q in innovation_questions if q["breakthrough_potential"] == "high")
        
        # More high-potential frameworks = better innovation priming
        return min(1.0, high_potential_count * 0.25 + 0.5)
    
    def _calculate_confidence_score(self, ambiguity_analysis: Dict[str, Any]) -> float:
        """Calculate confidence in the clarification process."""
        overall_ambiguity = ambiguity_analysis["overall_score"]
        
        # Lower ambiguity = higher confidence
        return 1.0 - overall_ambiguity
    
    def _generate_next_steps(
        self, 
        clarification_questions: List[Dict[str, Any]], 
        innovation_questions: List[Dict[str, Any]]
    ) -> List[str]:
        """Generate recommended next steps."""
        
        next_steps = []
        
        if clarification_questions:
            high_priority = [q for q in clarification_questions if q["priority"] == "high"]
            if high_priority:
                next_steps.append(f"Resolve {len(high_priority)} high-priority clarifications before proceeding")
            else:
                next_steps.append("Address remaining clarifications for optimal results")
        
        if innovation_questions:
            high_potential = [q for q in innovation_questions if q["breakthrough_potential"] == "high"]
            if high_potential:
                next_steps.append(f"Explore {len(high_potential)} high-potential innovation frameworks")
        
        if not clarification_questions:
            next_steps.append("Ready for creative agent execution")
        
        return next_steps
    
    def _identify_assumptions(self) -> List[str]:
        """Identify assumptions specific to design clarification."""
        return [
            "User requirements are clearly understood",
            "Design domain context is sufficient",
            "Innovation scope is appropriately defined",
            "Success criteria are measurable",
            "Constraints are accurately identified"
        ]
    
    def _assess_uncertainty(self) -> float:
        """Assess uncertainty in clarification process."""
        # For ClarificationEngine, uncertainty comes from incomplete information
        return 0.2  # Generally confident in clarification process 