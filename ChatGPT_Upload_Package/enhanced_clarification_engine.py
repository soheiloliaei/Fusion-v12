#!/usr/bin/env python3
"""
Enhanced Clarification Engine for Fusion v11
Proactively asks questions when confidence < 99% for precision and perfection
"""

import json
import re
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass

@dataclass
class ConfidenceAssessment:
    """Confidence assessment for response quality"""
    overall_confidence: float
    context_completeness: float
    requirement_clarity: float
    ambiguity_score: float
    missing_information: List[str]
    confidence_gaps: List[str]
    
class EnhancedClarificationEngine:
    """
    Enhanced Clarification Engine that proactively asks questions when confidence < 99%
    
    Features:
    - Confidence assessment (targets 99% precision)
    - Proactive questioning system
    - Context gap identification
    - Strategic questioning frameworks
    - Multi-domain questioning (design, business, technical)
    """
    
    def __init__(self, confidence_threshold: float = 0.99):
        self.confidence_threshold = confidence_threshold
        self.question_frameworks = {
            'design': {
                'user_context': [
                    "Who exactly is this for? What's their context, mindset, and current behavior?",
                    "What's the emotional journey users need to experience?",
                    "How do we design for the spectrum from novice to expert?",
                    "What are the hidden user needs not explicitly stated?"
                ],
                'outcome_clarity': [
                    "What specific outcome should this achieve? How will users' lives be different?",
                    "What would make this feel trustworthy vs overwhelming?",
                    "What story should users tell after this interaction?",
                    "How does this connect to broader user goals?"
                ],
                'design_scope': [
                    "How innovative should this be? Incremental improvement or breakthrough reimagining?",
                    "What would breakthrough design look like here?",
                    "What design patterns should we challenge vs. follow?",
                    "What's the minimum viable design vs. the aspirational version?"
                ],
                'constraints': [
                    "What are the real constraints vs. assumed limitations? What's truly non-negotiable?",
                    "What technical constraints will impact the design?",
                    "What business constraints must we work within?",
                    "What timeline constraints affect design decisions?"
                ]
            },
            'business': {
                'success_metrics': [
                    "How will we measure success? What does 'good enough' look like?",
                    "What are the key performance indicators for this project?",
                    "What business outcomes are we trying to achieve?",
                    "How will we know if users are satisfied?"
                ],
                'stakeholder_context': [
                    "Who are the key stakeholders and what are their priorities?",
                    "What are the political considerations we need to navigate?",
                    "Who has decision-making authority?",
                    "What are the competing priorities we need to balance?"
                ],
                'market_context': [
                    "What's the competitive landscape like?",
                    "What market trends are influencing this decision?",
                    "What's the business case for this project?",
                    "How does this fit into the broader business strategy?"
                ]
            },
            'technical': {
                'implementation': [
                    "What technical platforms or systems need to be integrated?",
                    "What are the performance requirements?",
                    "What are the scalability considerations?",
                    "What are the security requirements?"
                ],
                'resources': [
                    "What's the timeline for implementation?",
                    "What's the budget or resource constraints?",
                    "What team capabilities do we have available?",
                    "What external dependencies exist?"
                ],
                'risk_assessment': [
                    "What are the biggest technical risks?",
                    "What could go wrong with this approach?",
                    "What are the fallback options if the primary approach fails?",
                    "What compliance or regulatory considerations exist?"
                ]
            }
        }
    
    def assess_confidence(self, user_input: str, context: Optional[Dict[str, Any]] = None) -> ConfidenceAssessment:
        """
        Assess confidence level for providing 99% precision response
        
        Args:
            user_input: User's request or challenge
            context: Additional context information
            
        Returns:
            ConfidenceAssessment with detailed confidence metrics
        """
        if context is None:
            context = {}
        
        # Analyze different aspects of confidence
        context_completeness = self._assess_context_completeness(user_input, context)
        requirement_clarity = self._assess_requirement_clarity(user_input)
        ambiguity_score = self._assess_ambiguity(user_input)
        
        # Calculate overall confidence
        overall_confidence = (context_completeness + requirement_clarity + (1 - ambiguity_score)) / 3
        
        # Identify missing information
        missing_information = self._identify_missing_information(user_input, context)
        confidence_gaps = self._identify_confidence_gaps(user_input, overall_confidence)
        
        return ConfidenceAssessment(
            overall_confidence=overall_confidence,
            context_completeness=context_completeness,
            requirement_clarity=requirement_clarity,
            ambiguity_score=ambiguity_score,
            missing_information=missing_information,
            confidence_gaps=confidence_gaps
        )
    
    def should_ask_questions(self, confidence_assessment: ConfidenceAssessment) -> bool:
        """Determine if questions should be asked based on confidence assessment"""
        return confidence_assessment.overall_confidence < self.confidence_threshold
    
    def generate_clarification_questions(
        self, 
        user_input: str, 
        confidence_assessment: ConfidenceAssessment,
        context: Optional[Dict[str, Any]] = None,
        max_questions: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Generate targeted clarification questions to reach 99% confidence
        
        Args:
            user_input: User's request or challenge
            confidence_assessment: Current confidence assessment
            context: Additional context information
            max_questions: Maximum number of questions to generate
            
        Returns:
            List of structured clarification questions
        """
        if context is None:
            context = {}
        
        questions = []
        
        # Determine question domains needed
        question_domains = self._determine_question_domains(user_input, confidence_assessment)
        
        # Generate questions for each domain
        for domain in question_domains:
            domain_questions = self._generate_domain_questions(
                user_input, domain, confidence_assessment, context
            )
            questions.extend(domain_questions)
        
        # Prioritize questions based on confidence gaps
        questions = self._prioritize_questions(questions, confidence_assessment)
        
        # Limit to max_questions
        questions = questions[:max_questions]
        
        return questions
    
    def _assess_context_completeness(self, user_input: str, context: Dict[str, Any]) -> float:
        """Assess how complete the context information is"""
        
        # Key context areas to check
        context_areas = [
            'user_context', 'business_context', 'technical_context',
            'timeline_context', 'resource_context', 'success_metrics',
            'constraints', 'stakeholders', 'competitive_context'
        ]
        
        # Check for explicit context mentions in user input
        input_lower = user_input.lower()
        context_mentions = 0
        
        for area in context_areas:
            area_keywords = {
                'user_context': ['user', 'customer', 'audience', 'persona'],
                'business_context': ['business', 'revenue', 'profit', 'market'],
                'technical_context': ['technical', 'technology', 'platform', 'integration'],
                'timeline_context': ['deadline', 'timeline', 'schedule', 'urgency'],
                'resource_context': ['budget', 'team', 'resources', 'capacity'],
                'success_metrics': ['success', 'metrics', 'kpi', 'measure'],
                'constraints': ['constraint', 'limitation', 'requirement', 'must'],
                'stakeholders': ['stakeholder', 'management', 'team', 'decision'],
                'competitive_context': ['competitor', 'market', 'differentiation', 'advantage']
            }
            
            if any(keyword in input_lower for keyword in area_keywords.get(area, [])):
                context_mentions += 1
        
        # Check provided context
        provided_context_score = len(context) / len(context_areas)
        
        # Combine input mentions and provided context
        input_context_score = context_mentions / len(context_areas)
        
        return min(1.0, (input_context_score + provided_context_score) / 2)
    
    def _assess_requirement_clarity(self, user_input: str) -> float:
        """Assess how clear the requirements are"""
        
        clarity_indicators = [
            # Outcome clarity
            'will result in', 'so that', 'in order to', 'the goal is',
            'users will be able to', 'success looks like', 'the outcome',
            
            # Specificity indicators
            'specifically', 'exactly', 'precisely', 'must have',
            'required', 'needed', 'essential', 'critical',
            
            # Scope clarity
            'scope', 'includes', 'excludes', 'covers', 'focuses on',
            'boundaries', 'limitations', 'constraints'
        ]
        
        # Vague language (reduces clarity)
        vague_indicators = [
            'something', 'somehow', 'maybe', 'possibly', 'might',
            'could', 'would be nice', 'ideally', 'probably'
        ]
        
        input_lower = user_input.lower()
        
        # Count clarity indicators
        clarity_count = sum(1 for indicator in clarity_indicators if indicator in input_lower)
        
        # Count vague language
        vague_count = sum(1 for indicator in vague_indicators if indicator in input_lower)
        
        # Calculate clarity score
        clarity_score = clarity_count / max(1, len(clarity_indicators))
        vague_penalty = vague_count / max(1, len(vague_indicators))
        
        return max(0.0, clarity_score - vague_penalty)
    
    def _assess_ambiguity(self, user_input: str) -> float:
        """Assess ambiguity level in user input"""
        
        # Ambiguous terms
        ambiguous_terms = [
            'good', 'bad', 'better', 'worse', 'best', 'worst',
            'fast', 'slow', 'easy', 'hard', 'simple', 'complex',
            'big', 'small', 'large', 'little', 'many', 'few',
            'modern', 'traditional', 'innovative', 'standard',
            'user-friendly', 'intuitive', 'seamless', 'robust'
        ]
        
        # Ambiguous phrases
        ambiguous_phrases = [
            'as soon as possible', 'when convenient', 'at some point',
            'in the future', 'eventually', 'later on', 'sometime',
            'similar to', 'like', 'kind of', 'sort of'
        ]
        
        input_lower = user_input.lower()
        
        # Count ambiguous terms
        ambiguous_term_count = sum(1 for term in ambiguous_terms if term in input_lower)
        
        # Count ambiguous phrases
        ambiguous_phrase_count = sum(1 for phrase in ambiguous_phrases if phrase in input_lower)
        
        # Calculate ambiguity score
        total_ambiguous = ambiguous_term_count + ambiguous_phrase_count
        input_length = len(user_input.split())
        
        return min(1.0, total_ambiguous / max(1, input_length / 10))
    
    def _identify_missing_information(self, user_input: str, context: Dict[str, Any]) -> List[str]:
        """Identify what information is missing for 99% confidence"""
        
        missing_info = []
        
        # Check for missing user context
        if not self._has_user_context(user_input, context):
            missing_info.append("Clear target user definition")
        
        # Check for missing outcome definition
        if not self._has_outcome_definition(user_input, context):
            missing_info.append("Specific outcome or goal definition")
        
        # Check for missing success metrics
        if not self._has_success_metrics(user_input, context):
            missing_info.append("Success metrics and measurement criteria")
        
        # Check for missing constraints
        if not self._has_constraints(user_input, context):
            missing_info.append("Constraints and limitations")
        
        # Check for missing timeline
        if not self._has_timeline(user_input, context):
            missing_info.append("Timeline and urgency level")
        
        # Check for missing scope
        if not self._has_scope_definition(user_input, context):
            missing_info.append("Project scope and boundaries")
        
        return missing_info
    
    def _identify_confidence_gaps(self, user_input: str, overall_confidence: float) -> List[str]:
        """Identify specific gaps preventing 99% confidence"""
        
        gaps = []
        
        if overall_confidence < 0.99:
            if overall_confidence < 0.7:
                gaps.append("Fundamental requirement clarity needed")
            if overall_confidence < 0.8:
                gaps.append("Missing critical context information")
            if overall_confidence < 0.9:
                gaps.append("Ambiguous terms need clarification")
            if overall_confidence < 0.95:
                gaps.append("Success criteria need definition")
            if overall_confidence < 0.99:
                gaps.append("Minor clarifications needed for precision")
        
        return gaps
    
    def _determine_question_domains(self, user_input: str, confidence_assessment: ConfidenceAssessment) -> List[str]:
        """Determine which question domains are needed"""
        
        domains = []
        
        # Always include design domain for design-related tasks
        if any(keyword in user_input.lower() for keyword in ['design', 'ui', 'ux', 'interface', 'experience']):
            domains.append('design')
        
        # Include business domain for business-related tasks
        if any(keyword in user_input.lower() for keyword in ['business', 'strategy', 'market', 'revenue', 'success']):
            domains.append('business')
        
        # Include technical domain for technical tasks
        if any(keyword in user_input.lower() for keyword in ['technical', 'development', 'implementation', 'system', 'platform']):
            domains.append('technical')
        
        # Default to design if no specific domain detected
        if not domains:
            domains.append('design')
        
        return domains
    
    def _generate_domain_questions(
        self, 
        user_input: str, 
        domain: str, 
        confidence_assessment: ConfidenceAssessment,
        context: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate questions for a specific domain"""
        
        questions = []
        domain_framework = self.question_frameworks.get(domain, {})
        
        for category, category_questions in domain_framework.items():
            # Determine if this category needs questions
            if self._needs_category_questions(user_input, category, confidence_assessment, context):
                # Select most relevant question from category
                selected_question = self._select_most_relevant_question(
                    category_questions, user_input, confidence_assessment
                )
                
                if selected_question:
                    questions.append({
                        'question': selected_question,
                        'domain': domain,
                        'category': category,
                        'priority': self._calculate_question_priority(category, confidence_assessment),
                        'confidence_impact': self._estimate_confidence_impact(category, confidence_assessment)
                    })
        
        return questions
    
    def _needs_category_questions(
        self, 
        user_input: str, 
        category: str, 
        confidence_assessment: ConfidenceAssessment,
        context: Dict[str, Any]
    ) -> bool:
        """Determine if a category needs questions"""
        
        # Category-specific checks
        if category == 'user_context':
            return not self._has_user_context(user_input, context)
        elif category == 'outcome_clarity':
            return not self._has_outcome_definition(user_input, context)
        elif category == 'success_metrics':
            return not self._has_success_metrics(user_input, context)
        elif category == 'constraints':
            return not self._has_constraints(user_input, context)
        elif category == 'design_scope':
            return confidence_assessment.ambiguity_score > 0.3
        else:
            return confidence_assessment.overall_confidence < 0.9
    
    def _select_most_relevant_question(
        self, 
        category_questions: List[str], 
        user_input: str, 
        confidence_assessment: ConfidenceAssessment
    ) -> Optional[str]:
        """Select the most relevant question from a category"""
        
        # For now, select the first question in the category
        # In a more advanced version, this could use NLP to match context
        return category_questions[0] if category_questions else None
    
    def _calculate_question_priority(self, category: str, confidence_assessment: ConfidenceAssessment) -> str:
        """Calculate priority for a question"""
        
        high_priority_categories = ['user_context', 'outcome_clarity', 'success_metrics']
        
        if category in high_priority_categories:
            return 'high'
        elif confidence_assessment.overall_confidence < 0.8:
            return 'high'
        elif confidence_assessment.overall_confidence < 0.9:
            return 'medium'
        else:
            return 'low'
    
    def _estimate_confidence_impact(self, category: str, confidence_assessment: ConfidenceAssessment) -> float:
        """Estimate how much this question would improve confidence"""
        
        # Categories with high impact on confidence
        high_impact_categories = ['user_context', 'outcome_clarity', 'success_metrics']
        
        if category in high_impact_categories:
            return 0.2  # 20% confidence improvement
        else:
            return 0.1  # 10% confidence improvement
    
    def _prioritize_questions(self, questions: List[Dict[str, Any]], confidence_assessment: ConfidenceAssessment) -> List[Dict[str, Any]]:
        """Prioritize questions based on impact and importance"""
        
        # Sort by priority (high first), then by confidence impact
        return sorted(questions, key=lambda q: (
            q['priority'] == 'high',
            q['confidence_impact']
        ), reverse=True)
    
    # Helper methods for context checks
    def _has_user_context(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if user context is provided"""
        user_keywords = ['user', 'customer', 'audience', 'persona', 'target']
        return any(keyword in user_input.lower() for keyword in user_keywords) or 'user_context' in context
    
    def _has_outcome_definition(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if outcome is defined"""
        outcome_keywords = ['goal', 'outcome', 'result', 'achieve', 'accomplish']
        return any(keyword in user_input.lower() for keyword in outcome_keywords) or 'outcome' in context
    
    def _has_success_metrics(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if success metrics are defined"""
        metrics_keywords = ['success', 'measure', 'metric', 'kpi', 'performance']
        return any(keyword in user_input.lower() for keyword in metrics_keywords) or 'success_metrics' in context
    
    def _has_constraints(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if constraints are defined"""
        constraint_keywords = ['constraint', 'limitation', 'requirement', 'must', 'cannot']
        return any(keyword in user_input.lower() for keyword in constraint_keywords) or 'constraints' in context
    
    def _has_timeline(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if timeline is defined"""
        timeline_keywords = ['deadline', 'timeline', 'schedule', 'urgency', 'when']
        return any(keyword in user_input.lower() for keyword in timeline_keywords) or 'timeline' in context
    
    def _has_scope_definition(self, user_input: str, context: Dict[str, Any]) -> bool:
        """Check if scope is defined"""
        scope_keywords = ['scope', 'includes', 'excludes', 'covers', 'boundaries']
        return any(keyword in user_input.lower() for keyword in scope_keywords) or 'scope' in context
    
    def execute(self, user_input: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Main execution method for enhanced clarification
        
        Args:
            user_input: User's request or challenge
            context: Additional context information
            
        Returns:
            Clarification result with questions (if needed) or confidence assessment
        """
        if context is None:
            context = {}
        
        # Assess confidence
        confidence_assessment = self.assess_confidence(user_input, context)
        
        # Determine if questions are needed
        needs_questions = self.should_ask_questions(confidence_assessment)
        
        result = {
            'confidence_assessment': {
                'overall_confidence': confidence_assessment.overall_confidence,
                'context_completeness': confidence_assessment.context_completeness,
                'requirement_clarity': confidence_assessment.requirement_clarity,
                'ambiguity_score': confidence_assessment.ambiguity_score,
                'missing_information': confidence_assessment.missing_information,
                'confidence_gaps': confidence_assessment.confidence_gaps
            },
            'needs_clarification': needs_questions,
            'ready_for_99_percent_precision': confidence_assessment.overall_confidence >= self.confidence_threshold
        }
        
        # Generate questions if needed
        if needs_questions:
            questions = self.generate_clarification_questions(user_input, confidence_assessment, context)
            result['clarification_questions'] = questions
            result['question_count'] = len(questions)
            result['next_steps'] = 'Please answer the clarification questions to proceed with 99% precision.'
        else:
            result['next_steps'] = 'Sufficient information available for 99% precision response.'
        
        return result

# Example usage
if __name__ == "__main__":
    # Create enhanced clarification engine
    clarification_engine = EnhancedClarificationEngine()
    
    # Test with a vague request
    test_input = "Design a better user experience"
    result = clarification_engine.execute(test_input)
    
    print("🔍 Enhanced Clarification Engine Results:")
    print(f"Overall confidence: {result['confidence_assessment']['overall_confidence']:.2f}")
    print(f"Needs clarification: {result['needs_clarification']}")
    print(f"Ready for 99% precision: {result['ready_for_99_percent_precision']}")
    
    if result['needs_clarification']:
        print("\n❓ Clarification Questions:")
        for i, question in enumerate(result['clarification_questions'], 1):
            print(f"{i}. {question['question']} (Priority: {question['priority']})") 