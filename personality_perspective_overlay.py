"""
Personality Perspective Overlay - Relatable Design Thinking
Combines strategic frameworks with personality-driven design perspectives for breakthrough thinking.
"""

import json
from typing import Dict, Any, List
from enum import Enum

from fusion_agents import BaseAgent
from perspective_overlay_system import PerspectiveOverlaySystem, StrategicPerspective


class DesignPersonality(Enum):
    """Design personality perspectives for relatable breakthrough thinking."""
    JOBS_VISIONARY = "jobs_visionary"           # Steve Jobs: Magical simplicity & user delight
    STRATEGIC_OPTIMIZER = "strategic_optimizer"  # Strategic efficiency & scalable impact  
    BRAND_STORYTELLER = "brand_storyteller"     # Seth Godin: Brand narrative & tribe building
    TRUST_BUILDER = "trust_builder"             # Brené Brown: Vulnerability & authentic connection
    PURPOSE_LEADER = "purpose_leader"           # Simon Sinek: Why-driven design & mission clarity


class PersonalityPerspectiveOverlay(BaseAgent):
    """
    Applies personality-driven perspectives to design challenges.
    Makes strategic thinking relatable through design personality lenses.
    """
    
    def __init__(self):
        super().__init__(
            agent_id="PersonalityPerspectiveOverlay",
            name="Personality Perspective Overlay",
            role="Applies relatable design personality perspectives for breakthrough thinking"
        )
        
        # Initialize the strategic system
        self.strategic_overlay = PerspectiveOverlaySystem()
        
        self.personality_frameworks = {
            DesignPersonality.JOBS_VISIONARY: {
                "description": "Magical simplicity and transcendent user experience",
                "design_philosophy": "Technology should disappear, experience should delight",
                "key_questions": [
                    "How do we make this feel magical rather than mechanical?",
                    "What would make users say 'wow, this just works'?",
                    "How do we hide complexity while amplifying capability?",
                    "What would this look like if we started from pure user delight?",
                    "How do we create an experience that sells itself?"
                ],
                "strategic_focus": "user_transcendence",
                "design_principles": ["radical_simplicity", "invisible_complexity", "emotional_resonance"],
                "breakthrough_lens": "How can we make the impossible feel inevitable?"
            },
            DesignPersonality.STRATEGIC_OPTIMIZER: {
                "description": "Scalable systems and efficient value creation", 
                "design_philosophy": "Design should multiply value through intelligent systems",
                "key_questions": [
                    "How do we automate 80% of this while improving the experience?",
                    "What would this look like if we had to scale to 10x users tomorrow?",
                    "Where are we spending human effort on what machines could do better?",
                    "How do we turn every friction point into a competitive advantage?",
                    "What data would tell us this design is actually working?"
                ],
                "strategic_focus": "systematic_efficiency",
                "design_principles": ["intelligent_automation", "scalable_architecture", "measurable_impact"],
                "breakthrough_lens": "How can we build systems that get better as they grow?"
            },
            DesignPersonality.BRAND_STORYTELLER: {
                "description": "Narrative-driven design and tribal connection",
                "design_philosophy": "Design should tell a story that creates belonging",
                "key_questions": [
                    "What story does someone tell after using this?",
                    "How does this design express our unique point of view?",
                    "Who is this NOT for, and how does that make it better for our tribe?",
                    "How do we turn users into evangelists through design?",
                    "What would our biggest competitor never dare to build?"
                ],
                "strategic_focus": "narrative_differentiation", 
                "design_principles": ["story_driven_experience", "tribal_belonging", "bold_differentiation"],
                "breakthrough_lens": "How can we create a design that builds a movement?"
            },
            DesignPersonality.TRUST_BUILDER: {
                "description": "Vulnerable authenticity and deep human connection",
                "design_philosophy": "Design should honor human vulnerability and build trust",
                "key_questions": [
                    "How do we acknowledge what users are really afraid of here?",
                    "Where are we hiding behind jargon instead of being human?",
                    "How do we show our work instead of just showing results?",
                    "What would radical transparency look like in this interface?",
                    "How do we design for the emotional truth, not just the functional need?"
                ],
                "strategic_focus": "authentic_connection",
                "design_principles": ["vulnerable_transparency", "emotional_honesty", "trust_through_truth"],
                "breakthrough_lens": "How can we build unshakeable trust through courageous design?"
            },
            DesignPersonality.PURPOSE_LEADER: {
                "description": "Mission-driven design and inspirational clarity",
                "design_philosophy": "Design should inspire people toward their highest purpose",
                "key_questions": [
                    "Why does this design need to exist in the world?",
                    "How does this connect to something bigger than the immediate task?",
                    "What would this look like if we optimized for human flourishing?",
                    "How do we help people become who they want to become?",
                    "What legacy does this design leave in people's lives?"
                ],
                "strategic_focus": "purpose_alignment",
                "design_principles": ["mission_clarity", "inspirational_direction", "human_elevation"],
                "breakthrough_lens": "How can we design experiences that elevate human potential?"
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply personality perspectives to design challenges:
        1. Apply strategic frameworks first (foundation)
        2. Overlay personality perspectives (relatability)
        3. Synthesize breakthrough insights
        4. Generate personality-driven recommendations
        """
        design_challenge = inputs.get('design_challenge', '')
        strategic_context = inputs.get('strategic_context', {})
        innovation_ambition = inputs.get('innovation_ambition', 'medium')
        requested_personalities = inputs.get('personalities', None)
        
        # First get strategic foundation
        strategic_result = self.strategic_overlay.execute(inputs)
        
        # Select personality perspectives
        selected_personalities = self._select_personalities(
            design_challenge, strategic_context, requested_personalities
        )
        
        # Apply personality perspectives
        personality_insights = self._apply_personality_perspectives(
            design_challenge, strategic_context, selected_personalities, strategic_result
        )
        
        # Create personality-strategic synthesis
        breakthrough_synthesis = self._synthesize_personality_strategic_insights(
            strategic_result, personality_insights
        )
        
        # Generate relatable recommendations
        personality_recommendations = self._generate_personality_recommendations(
            breakthrough_synthesis, innovation_ambition
        )
        
        return {
            "strategic_foundation": strategic_result,
            "selected_personalities": [p.value for p in selected_personalities],
            "personality_insights": personality_insights,
            "breakthrough_synthesis": breakthrough_synthesis,
            "personality_recommendations": personality_recommendations,
            "design_philosophy_alignment": self._assess_philosophy_alignment(personality_insights),
            "relatable_value_proposition": self._generate_relatable_value_prop(breakthrough_synthesis)
        }
    
    def _select_personalities(
        self, 
        design_challenge: str, 
        strategic_context: Dict[str, Any], 
        requested_personalities: List[str] = None
    ) -> List[DesignPersonality]:
        """Select optimal personality perspectives based on challenge context."""
        
        if requested_personalities:
            validated = []
            for personality_name in requested_personalities:
                try:
                    personality = DesignPersonality(personality_name)
                    validated.append(personality)
                except ValueError:
                    continue
            if validated:
                return validated
        
        # Auto-select based on challenge characteristics
        challenge_lower = design_challenge.lower()
        
        selected = []
        
        # Always include Jobs for user experience excellence
        selected.append(DesignPersonality.JOBS_VISIONARY)
        
        # Add based on context
        if any(word in challenge_lower for word in ["complex", "scale", "system", "efficiency"]):
            selected.append(DesignPersonality.STRATEGIC_OPTIMIZER)
        
        if any(word in challenge_lower for word in ["brand", "story", "unique", "different"]):
            selected.append(DesignPersonality.BRAND_STORYTELLER)
        
        if any(word in challenge_lower for word in ["trust", "security", "privacy", "transparency"]):
            selected.append(DesignPersonality.TRUST_BUILDER)
        
        if any(word in challenge_lower for word in ["purpose", "mission", "impact", "meaningful"]):
            selected.append(DesignPersonality.PURPOSE_LEADER)
        
        # Ensure we have at least 3 perspectives for good tension
        if len(selected) < 3:
            remaining = [p for p in DesignPersonality if p not in selected]
            selected.extend(remaining[:3-len(selected)])
        
        return selected[:4]  # Max 4 for focused tension
    
    def _apply_personality_perspectives(
        self, 
        design_challenge: str, 
        strategic_context: Dict[str, Any], 
        personalities: List[DesignPersonality],
        strategic_result: Dict[str, Any]
    ) -> Dict[str, Dict[str, Any]]:
        """Apply each personality perspective to the design challenge."""
        
        personality_insights = {}
        
        for personality in personalities:
            framework = self.personality_frameworks[personality]
            
            # Generate personality-specific insights
            insights = []
            design_principles = []
            breakthrough_questions = []
            
            for question in framework["key_questions"]:
                insight = self._process_personality_question(
                    question, design_challenge, personality, framework
                )
                insights.append(insight)
                
                if insight.get("breakthrough_potential", 0) > 0.7:
                    breakthrough_questions.append(question)
            
            # Generate personality-driven design principles
            design_principles = self._derive_design_principles(
                framework, insights, design_challenge
            )
            
            personality_insights[personality.value] = {
                "personality": personality.value,
                "design_philosophy": framework["design_philosophy"],
                "insights": insights,
                "design_principles": design_principles,
                "breakthrough_questions": breakthrough_questions,
                "breakthrough_lens": framework["breakthrough_lens"],
                "strategic_focus": framework["strategic_focus"]
            }
        
        return personality_insights
    
    def _synthesize_personality_strategic_insights(
        self, 
        strategic_result: Dict[str, Any], 
        personality_insights: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Synthesize personality and strategic insights for breakthrough thinking."""
        
        # Extract strategic breakthrough opportunities
        strategic_breakthroughs = strategic_result.get("breakthrough_synthesis", {}).get("breakthrough_opportunities", [])
        
        # Extract personality breakthrough questions
        personality_breakthroughs = []
        for personality_data in personality_insights.values():
            personality_breakthroughs.extend(personality_data.get("breakthrough_questions", []))
        
        # Find convergent themes
        convergent_themes = self._identify_convergent_themes(strategic_result, personality_insights)
        
        # Identify creative tensions between personalities
        personality_tensions = self._identify_personality_tensions(personality_insights)
        
        # Generate synthesis breakthroughs
        synthesis_breakthroughs = self._generate_synthesis_breakthroughs(
            convergent_themes, personality_tensions, strategic_breakthroughs
        )
        
        return {
            "strategic_breakthroughs": strategic_breakthroughs,
            "personality_breakthroughs": personality_breakthroughs,
            "convergent_themes": convergent_themes,
            "personality_tensions": personality_tensions,
            "synthesis_breakthroughs": synthesis_breakthroughs,
            "breakthrough_score": self._calculate_synthesis_breakthrough_score(synthesis_breakthroughs)
        }
    
    def _generate_personality_recommendations(
        self, 
        breakthrough_synthesis: Dict[str, Any], 
        innovation_ambition: str
    ) -> List[Dict[str, Any]]:
        """Generate personality-driven design recommendations."""
        
        recommendations = []
        
        # From synthesis breakthroughs
        for breakthrough in breakthrough_synthesis.get("synthesis_breakthroughs", []):
            recommendations.append({
                "type": "synthesis_breakthrough",
                "recommendation": breakthrough["recommendation"],
                "personality_influence": breakthrough["personality_influence"],
                "strategic_foundation": breakthrough["strategic_foundation"],
                "impact": "breakthrough",
                "relatability": "high"
            })
        
        # From personality tensions
        for tension in breakthrough_synthesis.get("personality_tensions", []):
            recommendations.append({
                "type": "creative_tension_resolution",
                "recommendation": f"Resolve tension between {tension['personalities']} through {tension['resolution_approach']}",
                "creative_opportunity": tension["creative_opportunity"],
                "impact": "high",
                "relatability": "medium"
            })
        
        # From convergent themes
        for theme in breakthrough_synthesis.get("convergent_themes", []):
            recommendations.append({
                "type": "convergent_amplification",
                "recommendation": f"Amplify convergent theme: {theme['theme']}",
                "supporting_perspectives": theme["supporting_perspectives"],
                "impact": "medium",
                "relatability": "high"
            })
        
        return recommendations[:6]  # Top 6 recommendations
    
    def _process_personality_question(
        self, 
        question: str, 
        design_challenge: str, 
        personality: DesignPersonality, 
        framework: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Process a personality-specific question to generate insights."""
        
        # Simulate personality-driven insight generation
        insight_strength = 0.65 + (hash(question + personality.value) % 30) / 100.0
        breakthrough_potential = 0.5 + (hash(framework["strategic_focus"] + question) % 40) / 100.0
        
        return {
            "question": question,
            "personality_lens": personality.value,
            "insight": f"From {personality.value} perspective: {question[:60]}...",
            "insight_strength": insight_strength,
            "breakthrough_potential": breakthrough_potential,
            "design_implication": f"This suggests {framework['strategic_focus']} approach"
        }
    
    def _derive_design_principles(
        self, 
        framework: Dict[str, Any], 
        insights: List[Dict[str, Any]], 
        design_challenge: str
    ) -> List[str]:
        """Derive design principles from personality framework and insights."""
        
        base_principles = framework["design_principles"]
        
        # Add insight-derived principles
        derived_principles = []
        high_insight_count = sum(1 for insight in insights if insight["insight_strength"] > 0.8)
        
        if high_insight_count > 2:
            derived_principles.append(f"{framework['strategic_focus']}_optimization")
        
        return base_principles + derived_principles
    
    def _identify_convergent_themes(
        self, 
        strategic_result: Dict[str, Any], 
        personality_insights: Dict[str, Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Identify themes that converge across strategic and personality perspectives."""
        
        themes = []
        
        # Check for user-centricity convergence
        strategic_user_focus = any("user" in str(insight).lower() 
                                 for insight in strategic_result.get("breakthrough_synthesis", {}).get("breakthrough_opportunities", []))
        
        personality_user_focus = "jobs_visionary" in personality_insights
        
        if strategic_user_focus and personality_user_focus:
            themes.append({
                "theme": "user_centric_excellence",
                "supporting_perspectives": ["strategic_frameworks", "jobs_visionary"],
                "convergence_strength": "high"
            })
        
        # Check for innovation convergence
        if len(personality_insights) > 2:
            themes.append({
                "theme": "multi_perspective_innovation",
                "supporting_perspectives": list(personality_insights.keys()),
                "convergence_strength": "medium"
            })
        
        return themes
    
    def _identify_personality_tensions(self, personality_insights: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify creative tensions between personality perspectives."""
        
        tensions = []
        personalities = list(personality_insights.keys())
        
        # Jobs vs Strategic Optimizer tension
        if "jobs_visionary" in personalities and "strategic_optimizer" in personalities:
            tensions.append({
                "personalities": ["jobs_visionary", "strategic_optimizer"],
                "tension": "magical_simplicity_vs_systematic_efficiency",
                "creative_opportunity": "Efficient systems that feel magical",
                "resolution_approach": "invisible_optimization"
            })
        
        # Brand Storyteller vs Trust Builder tension  
        if "brand_storyteller" in personalities and "trust_builder" in personalities:
            tensions.append({
                "personalities": ["brand_storyteller", "trust_builder"],
                "tension": "bold_differentiation_vs_vulnerable_authenticity",
                "creative_opportunity": "Authentic brand stories that build trust",
                "resolution_approach": "vulnerable_differentiation"
            })
        
        return tensions
    
    def _generate_synthesis_breakthroughs(
        self, 
        convergent_themes: List[Dict[str, Any]], 
        personality_tensions: List[Dict[str, Any]], 
        strategic_breakthroughs: List[str]
    ) -> List[Dict[str, Any]]:
        """Generate breakthrough insights from synthesis."""
        
        breakthroughs = []
        
        # From convergent themes
        for theme in convergent_themes:
            breakthroughs.append({
                "type": "convergent_breakthrough",
                "recommendation": f"Leverage {theme['theme']} convergence for breakthrough design",
                "personality_influence": theme["supporting_perspectives"],
                "strategic_foundation": "multi_perspective_alignment",
                "breakthrough_score": 0.8 if theme["convergence_strength"] == "high" else 0.6
            })
        
        # From personality tensions
        for tension in personality_tensions:
            breakthroughs.append({
                "type": "tension_resolution_breakthrough", 
                "recommendation": f"Resolve {tension['tension']} through {tension['creative_opportunity']}",
                "personality_influence": tension["personalities"],
                "strategic_foundation": "creative_tension_synthesis",
                "breakthrough_score": 0.75
            })
        
        return breakthroughs
    
    def _calculate_synthesis_breakthrough_score(self, synthesis_breakthroughs: List[Dict[str, Any]]) -> float:
        """Calculate overall breakthrough score from synthesis."""
        
        if not synthesis_breakthroughs:
            return 0.5
        
        scores = [breakthrough.get("breakthrough_score", 0.6) for breakthrough in synthesis_breakthroughs]
        return sum(scores) / len(scores)
    
    def _assess_philosophy_alignment(self, personality_insights: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Assess alignment between personality philosophies."""
        
        philosophies = [data["design_philosophy"] for data in personality_insights.values()]
        
        return {
            "philosophy_count": len(philosophies),
            "diversity_score": len(set(philosophies)) / len(philosophies) if philosophies else 0,
            "alignment_strength": "high_diversity" if len(set(philosophies)) > 3 else "moderate_diversity"
        }
    
    def _generate_relatable_value_prop(self, breakthrough_synthesis: Dict[str, Any]) -> str:
        """Generate relatable value proposition from synthesis."""
        
        breakthrough_count = len(breakthrough_synthesis.get("synthesis_breakthroughs", []))
        tension_count = len(breakthrough_synthesis.get("personality_tensions", []))
        
        if breakthrough_count > 2 and tension_count > 1:
            return "Multi-personality breakthrough design with creative tension resolution"
        elif breakthrough_count > 1:
            return "Personality-driven design excellence with strategic foundation"
        else:
            return "Enhanced design thinking through personality perspectives"


# Integration with existing Fusion v11
def enhance_fusion_v11_with_personalities():
    """Enhance Fusion v11 with personality-driven perspectives."""
    
    # This would integrate with the main system
    personality_overlay = PersonalityPerspectiveOverlay()
    
    # Example usage
    design_inputs = {
        'design_challenge': 'Create a breakthrough Bitcoin support experience that builds trust while handling Lightning network complexity',
        'strategic_context': {'crypto_complexity': 'high', 'trust_requirements': 'critical'},
        'innovation_ambition': 'breakthrough',
        'personalities': ['jobs_visionary', 'trust_builder', 'strategic_optimizer']
    }
    
    result = personality_overlay.execute(design_inputs)
    
    return result 