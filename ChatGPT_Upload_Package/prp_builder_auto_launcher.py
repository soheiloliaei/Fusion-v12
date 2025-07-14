#!/usr/bin/env python3
"""
🚀 PRP Builder Auto Launcher - Simple Trigger System
Responds to simple phrases like "write a PRP" or "let's start a PRP for cursor"
Automatically handles all setup, installation, and dependencies
"""

import os
import sys
import json
import subprocess
import importlib.util
from datetime import datetime
from pathlib import Path

# Auto-install required packages
def auto_install_dependencies():
    """Automatically install required dependencies"""
    required_packages = [
        'requests',
        'aiohttp',
        'asyncio',
        'json',
        'datetime',
        'pathlib'
    ]
    
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"📦 Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    
    print("✅ All dependencies installed!")

# Auto-install on import
auto_install_dependencies()

import requests
import aiohttp
import asyncio

class PRPAutoLauncher:
    """
    Automatic PRP Builder with Simple Trigger System
    
    Responds to simple phrases:
    - "write a PRP"
    - "I am starting a new prototype"
    - "let's start a PRP for cursor"
    - "create product requirements"
    - "new project planning"
    """
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.setup_directories()
        self.load_or_create_config()
        self.prp_data = {}
        self.context_layers = {}
        
    def setup_directories(self):
        """Create necessary directories"""
        directories = [
            'prp_outputs',
            'api_keys',
            'design_inspiration',
            'prp_templates'
        ]
        
        for dir_name in directories:
            dir_path = self.project_root / dir_name
            dir_path.mkdir(exist_ok=True)
            
    def load_or_create_config(self):
        """Load or create configuration file"""
        config_path = self.project_root / 'prp_config.json'
        
        if config_path.exists():
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "version": "1.0",
                "auto_setup": True,
                "design_inspiration_enabled": True,
                "fusion_v11_integration": True,
                "output_formats": ["json", "markdown"],
                "created": datetime.now().isoformat()
            }
            
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
    
    def detect_trigger_phrase(self, user_input):
        """Detect simple trigger phrases"""
        trigger_phrases = [
            "write a prp",
            "create a prp",
            "start a prp",
            "new prp",
            "prp for",
            "starting a new prototype",
            "new prototype",
            "create product requirements",
            "new project planning",
            "project requirements",
            "requirements planning",
            "let's start a prp",
            "i need a prp",
            "help me create a prp"
        ]
        
        user_input_lower = user_input.lower()
        
        for phrase in trigger_phrases:
            if phrase in user_input_lower:
                return True
                
        return False
    
    def extract_project_context(self, user_input):
        """Extract project context from user input"""
        context = {}
        
        # Extract project name/type
        if "for cursor" in user_input.lower():
            context["project_type"] = "cursor_extension"
            context["platform"] = "cursor_ide"
        elif "mobile" in user_input.lower():
            context["project_type"] = "mobile_app"
        elif "web" in user_input.lower():
            context["project_type"] = "web_application"
        elif "desktop" in user_input.lower():
            context["project_type"] = "desktop_application"
        else:
            context["project_type"] = "general"
            
        # Extract industry/domain
        industries = ["fintech", "healthcare", "education", "ecommerce", "gaming", "social", "productivity"]
        for industry in industries:
            if industry in user_input.lower():
                context["industry"] = industry
                break
                
        return context
    
    def auto_launch_prp_builder(self, user_input, context=None):
        """Automatically launch PRP builder with smart defaults"""
        print("\n🚀 **PRP AUTO-LAUNCHER ACTIVATED**")
        print("=" * 50)
        
        # Extract context from user input
        if context is None:
            context = self.extract_project_context(user_input)
        
        # Auto-detect project type and set smart defaults
        if context.get("project_type") == "cursor_extension":
            return self.launch_cursor_prp_builder(user_input)
        else:
            return self.launch_general_prp_builder(user_input, context)
    
    def launch_cursor_prp_builder(self, user_input):
        """Specialized PRP builder for Cursor IDE projects"""
        print("\n🎯 **CURSOR IDE PROJECT DETECTED**")
        print("Launching specialized Cursor PRP builder...")
        
        # Pre-populate with Cursor-specific context
        cursor_context = {
            "platform": "cursor_ide",
            "project_type": "cursor_extension",
            "technical_stack": "typescript_javascript",
            "deployment_target": "cursor_marketplace",
            "user_base": "developers",
            "integration_requirements": ["cursor_api", "vscode_compatibility"],
            "design_system": "cursor_native_ui"
        }
        
        questions = [
            {
                "question": "What specific Cursor IDE functionality do you want to enhance or add?",
                "context_layer": "strategic_vision",
                "examples": ["AI-powered code analysis", "Custom sidebar panel", "Enhanced debugging tools", "Productivity shortcuts"]
            },
            {
                "question": "Who is your target user within the Cursor IDE ecosystem?",
                "context_layer": "user_context",
                "examples": ["Frontend developers", "Full-stack developers", "Data scientists", "DevOps engineers"]
            },
            {
                "question": "What problem does this solve for Cursor IDE users?",
                "context_layer": "problem_context",
                "examples": ["Faster code review", "Better debugging experience", "Improved collaboration", "Enhanced productivity"]
            },
            {
                "question": "What makes this different from existing Cursor extensions?",
                "context_layer": "competitive_context",
                "examples": ["Unique AI integration", "Better performance", "Novel UI approach", "Specialized domain focus"]
            }
        ]
        
        return self.run_interactive_questions(questions, cursor_context)
    
    def launch_general_prp_builder(self, user_input, context):
        """General PRP builder for any project type"""
        print("\n🎯 **GENERAL PROJECT BUILDER**")
        print(f"Project type: {context.get('project_type', 'general')}")
        
        # Smart question selection based on context
        questions = self.get_smart_questions(context)
        
        return self.run_interactive_questions(questions, context)
    
    def get_smart_questions(self, context):
        """Get smart questions based on project context"""
        base_questions = [
            {
                "question": "What is the core purpose of this project?",
                "context_layer": "strategic_vision",
                "examples": ["User productivity tool", "Entertainment platform", "Business automation", "Educational resource"]
            },
            {
                "question": "Who is your primary target user?",
                "context_layer": "user_context",
                "examples": ["Business professionals", "Students", "Creative professionals", "General consumers"]
            },
            {
                "question": "What key problem does this solve?",
                "context_layer": "problem_context",
                "examples": ["Time management", "Communication barriers", "Learning difficulties", "Process inefficiencies"]
            }
        ]
        
        # Add context-specific questions
        project_type = context.get("project_type", "general")
        
        if project_type == "mobile_app":
            base_questions.extend([
                {
                    "question": "What mobile platforms will you target?",
                    "context_layer": "technical_context",
                    "examples": ["iOS only", "Android only", "Cross-platform", "Progressive web app"]
                },
                {
                    "question": "What key mobile features will you use?",
                    "context_layer": "feature_context",
                    "examples": ["Push notifications", "Camera integration", "GPS/location", "Offline functionality"]
                }
            ])
        elif project_type == "web_application":
            base_questions.extend([
                {
                    "question": "What type of web application is this?",
                    "context_layer": "technical_context",
                    "examples": ["Single-page app", "Multi-page app", "Progressive web app", "Dashboard/admin panel"]
                },
                {
                    "question": "What browsers/devices need to be supported?",
                    "context_layer": "technical_context",
                    "examples": ["Modern browsers only", "IE11 compatibility", "Mobile-first", "Desktop-focused"]
                }
            ])
        
        return base_questions
    
    def run_interactive_questions(self, questions, base_context):
        """Run interactive question flow"""
        print("\n💬 **INTERACTIVE PRP BUILDER**")
        print("Answer these questions to build your Product Requirements Planning document")
        print("=" * 70)
        
        responses = {}
        context_layers = {}
        
        for i, q in enumerate(questions, 1):
            print(f"\n📋 **Question {i}/{len(questions)}**")
            print(f"🎯 {q['question']}")
            
            if q.get('examples'):
                print(f"💡 Examples: {', '.join(q['examples'])}")
            
            print("=" * 50)
            
            # Get user response
            response = input("Your answer: ").strip()
            
            if response:
                responses[f"question_{i}"] = {
                    "question": q['question'],
                    "answer": response,
                    "context_layer": q.get('context_layer', 'general')
                }
                
                # Map to context layer
                context_layers[q.get('context_layer', 'general')] = response
        
        # Auto-generate additional context
        self.generate_additional_context(responses, context_layers, base_context)
        
        # Generate PRP document
        prp_document = self.generate_prp_document(responses, context_layers, base_context)
        
        # Auto-fetch design inspiration if enabled
        if self.config.get('design_inspiration_enabled', True):
            self.auto_fetch_design_inspiration(context_layers, base_context)
        
        # Save and display results
        self.save_prp_document(prp_document)
        self.display_prp_summary(prp_document)
        
        return prp_document
    
    def generate_additional_context(self, responses, context_layers, base_context):
        """Generate additional context based on responses"""
        
        # Auto-generate timeline
        project_complexity = "medium"  # Default
        if any("complex" in str(r.get('answer', '')).lower() for r in responses.values()):
            project_complexity = "high"
        elif any("simple" in str(r.get('answer', '')).lower() for r in responses.values()):
            project_complexity = "low"
        
        timeline_suggestions = {
            "low": {"phases": 2, "duration": "4-6 weeks"},
            "medium": {"phases": 3, "duration": "8-12 weeks"},
            "high": {"phases": 4, "duration": "16-24 weeks"}
        }
        
        context_layers["timeline_context"] = timeline_suggestions[project_complexity]
        
        # Auto-generate success metrics
        context_layers["success_metrics"] = self.generate_success_metrics(responses, base_context)
        
        # Auto-generate risk assessment
        context_layers["risk_assessment"] = self.generate_risk_assessment(responses, base_context)
    
    def generate_success_metrics(self, responses, base_context):
        """Generate success metrics based on project type"""
        project_type = base_context.get("project_type", "general")
        
        metrics = {
            "cursor_extension": [
                "Downloads from Cursor marketplace",
                "User rating (4.0+ stars)",
                "Active daily users",
                "Code completion accuracy"
            ],
            "mobile_app": [
                "App store downloads",
                "User retention rate",
                "Session duration",
                "User rating (4.0+ stars)"
            ],
            "web_application": [
                "Monthly active users",
                "Page load time (<3 seconds)",
                "Conversion rate",
                "User engagement metrics"
            ],
            "general": [
                "User adoption rate",
                "Task completion rate",
                "User satisfaction score",
                "Performance benchmarks"
            ]
        }
        
        return metrics.get(project_type, metrics["general"])
    
    def generate_risk_assessment(self, responses, base_context):
        """Generate risk assessment based on project context"""
        risks = []
        
        # Technical risks
        if base_context.get("project_type") == "cursor_extension":
            risks.append({
                "risk": "Cursor API changes",
                "impact": "High",
                "mitigation": "Regular API monitoring and quick updates"
            })
        
        # General risks
        risks.extend([
            {
                "risk": "User adoption challenges",
                "impact": "Medium",
                "mitigation": "User research and iterative testing"
            },
            {
                "risk": "Technical complexity",
                "impact": "Medium",
                "mitigation": "Phased development approach"
            },
            {
                "risk": "Timeline delays",
                "impact": "Low",
                "mitigation": "Regular milestone reviews"
            }
        ])
        
        return risks
    
    def auto_fetch_design_inspiration(self, context_layers, base_context):
        """Auto-fetch design inspiration based on project context"""
        print("\n🎨 **AUTO-FETCHING DESIGN INSPIRATION**")
        
        # Determine search terms based on project
        search_terms = []
        
        if base_context.get("project_type") == "cursor_extension":
            search_terms = ["code editor ui", "developer tools", "ide interface", "coding productivity"]
        elif base_context.get("project_type") == "mobile_app":
            search_terms = ["mobile app design", "app interface", "mobile ux"]
        elif base_context.get("project_type") == "web_application":
            search_terms = ["web app design", "dashboard ui", "web interface"]
        else:
            search_terms = ["product design", "user interface", "app design"]
        
        # Add industry-specific terms
        if base_context.get("industry"):
            search_terms.append(f"{base_context['industry']} design")
        
        print(f"🔍 Searching for: {', '.join(search_terms)}")
        
        # Try to fetch inspiration (graceful failure if no API keys)
        try:
            inspiration_data = self.fetch_design_inspiration_safe(search_terms)
            if inspiration_data:
                print(f"✅ Found {len(inspiration_data)} design inspirations")
                
                # Save inspiration data
                inspiration_path = self.project_root / 'design_inspiration' / f"inspiration_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(inspiration_path, 'w') as f:
                    json.dump(inspiration_data, f, indent=2)
                    
                print(f"💾 Saved inspiration to: {inspiration_path}")
            else:
                print("⚠️ No design inspiration fetched (API keys not configured)")
        except Exception as e:
            print(f"⚠️ Design inspiration fetch failed: {e}")
    
    def fetch_design_inspiration_safe(self, search_terms):
        """Safely fetch design inspiration without failing if no API keys"""
        try:
            # Check if design inspiration API exists
            design_api_path = self.project_root / 'design_inspiration_api.py'
            if not design_api_path.exists():
                return None
                
            # Try to import and use
            import importlib.util
            spec = importlib.util.spec_from_file_location("design_inspiration_api", design_api_path)
            design_api = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(design_api)
            
            # Create design fetcher
            fetcher = design_api.DesignInspirationAPI()
            
            # Fetch with first search term
            if search_terms:
                return fetcher.fetch_curated_inspiration(search_terms[0])
            
        except Exception as e:
            print(f"Design inspiration not available: {e}")
            return None
    
    def generate_prp_document(self, responses, context_layers, base_context):
        """Generate comprehensive PRP document"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        document = {
            "meta": {
                "title": f"Product Requirements Planning - {base_context.get('project_type', 'General Project')}",
                "generated": timestamp,
                "version": "1.0",
                "auto_generated": True
            },
            
            "executive_summary": {
                "project_type": base_context.get("project_type", "general"),
                "industry": base_context.get("industry", "general"),
                "platform": base_context.get("platform", "multi-platform"),
                "target_users": context_layers.get("user_context", "General users"),
                "key_problem": context_layers.get("problem_context", "User needs analysis required"),
                "solution_approach": context_layers.get("strategic_vision", "Comprehensive solution development")
            },
            
            "detailed_requirements": {
                "user_responses": responses,
                "context_mapping": context_layers,
                "success_metrics": context_layers.get("success_metrics", []),
                "timeline": context_layers.get("timeline_context", {}),
                "risk_assessment": context_layers.get("risk_assessment", [])
            },
            
            "technical_specifications": {
                "project_type": base_context.get("project_type"),
                "platform_requirements": base_context.get("platform", "multi-platform"),
                "integration_requirements": base_context.get("integration_requirements", []),
                "technical_stack": base_context.get("technical_stack", "to_be_determined")
            },
            
            "next_steps": self.generate_next_steps(base_context, context_layers),
            
            "fusion_v11_integration": {
                "context_layers_mapped": len(context_layers),
                "ready_for_fusion_processing": True,
                "recommended_agents": self.get_recommended_fusion_agents(base_context)
            }
        }
        
        return document
    
    def generate_next_steps(self, base_context, context_layers):
        """Generate recommended next steps"""
        project_type = base_context.get("project_type", "general")
        
        base_steps = [
            "Review and validate PRP document",
            "Conduct user research and validation",
            "Create detailed wireframes and prototypes",
            "Develop technical architecture plan",
            "Set up development environment",
            "Begin iterative development process"
        ]
        
        if project_type == "cursor_extension":
            base_steps.extend([
                "Set up Cursor extension development environment",
                "Study Cursor API documentation",
                "Create extension manifest and basic structure",
                "Test in Cursor IDE development mode"
            ])
        elif project_type == "mobile_app":
            base_steps.extend([
                "Choose mobile development framework",
                "Set up app store developer accounts",
                "Create app mockups and user flows",
                "Plan app store optimization strategy"
            ])
        
        return base_steps
    
    def get_recommended_fusion_agents(self, base_context):
        """Get recommended Fusion v11 agents based on project type"""
        project_type = base_context.get("project_type", "general")
        
        agent_recommendations = {
            "cursor_extension": [
                "DesignTechnologist",
                "VPDesign",
                "CriticalDesignAdvisor",
                "PromptEngineer"
            ],
            "mobile_app": [
                "DesignMaestro",
                "CreativeDirector",
                "InsightsSynthesizer",
                "VPDesign"
            ],
            "web_application": [
                "DesignTechnologist",
                "DesignMaestro",
                "VPDesign",
                "StrategyPilot"
            ],
            "general": [
                "VPDesign",
                "StrategyPilot",
                "InsightsSynthesizer",
                "CriticalDesignAdvisor"
            ]
        }
        
        return agent_recommendations.get(project_type, agent_recommendations["general"])
    
    def save_prp_document(self, document):
        """Save PRP document in multiple formats"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"prp_document_{timestamp}"
        
        # Save as JSON
        json_path = self.project_root / 'prp_outputs' / f"{base_filename}.json"
        with open(json_path, 'w') as f:
            json.dump(document, f, indent=2)
        
        # Save as Markdown
        md_path = self.project_root / 'prp_outputs' / f"{base_filename}.md"
        with open(md_path, 'w') as f:
            f.write(self.convert_to_markdown(document))
        
        print(f"\n💾 **PRP DOCUMENT SAVED**")
        print(f"📄 JSON: {json_path}")
        print(f"📝 Markdown: {md_path}")
    
    def convert_to_markdown(self, document):
        """Convert PRP document to Markdown format"""
        md_content = f"""# {document['meta']['title']}

**Generated:** {document['meta']['generated']}
**Version:** {document['meta']['version']}

## Executive Summary

- **Project Type:** {document['executive_summary']['project_type']}
- **Industry:** {document['executive_summary']['industry']}
- **Platform:** {document['executive_summary']['platform']}
- **Target Users:** {document['executive_summary']['target_users']}
- **Key Problem:** {document['executive_summary']['key_problem']}
- **Solution Approach:** {document['executive_summary']['solution_approach']}

## Detailed Requirements

### User Responses
"""
        
        for key, response in document['detailed_requirements']['user_responses'].items():
            md_content += f"\n**{response['question']}**\n"
            md_content += f"Answer: {response['answer']}\n"
            md_content += f"Context Layer: {response['context_layer']}\n"
        
        md_content += "\n## Success Metrics\n"
        for metric in document['detailed_requirements']['success_metrics']:
            md_content += f"- {metric}\n"
        
        md_content += "\n## Timeline\n"
        timeline = document['detailed_requirements']['timeline']
        md_content += f"- **Phases:** {timeline.get('phases', 'TBD')}\n"
        md_content += f"- **Duration:** {timeline.get('duration', 'TBD')}\n"
        
        md_content += "\n## Risk Assessment\n"
        for risk in document['detailed_requirements']['risk_assessment']:
            md_content += f"- **Risk:** {risk['risk']}\n"
            md_content += f"  - **Impact:** {risk['impact']}\n"
            md_content += f"  - **Mitigation:** {risk['mitigation']}\n"
        
        md_content += "\n## Next Steps\n"
        for step in document['next_steps']:
            md_content += f"- {step}\n"
        
        md_content += "\n## Fusion v11 Integration\n"
        fusion_info = document['fusion_v11_integration']
        md_content += f"- **Context Layers Mapped:** {fusion_info['context_layers_mapped']}\n"
        md_content += f"- **Ready for Fusion Processing:** {fusion_info['ready_for_fusion_processing']}\n"
        md_content += f"- **Recommended Agents:** {', '.join(fusion_info['recommended_agents'])}\n"
        
        return md_content
    
    def display_prp_summary(self, document):
        """Display PRP summary"""
        print("\n" + "="*70)
        print("🎯 **PRP DOCUMENT GENERATED SUCCESSFULLY**")
        print("="*70)
        
        print(f"\n📋 **Project:** {document['executive_summary']['project_type']}")
        print(f"🎯 **Purpose:** {document['executive_summary']['solution_approach']}")
        print(f"👥 **Users:** {document['executive_summary']['target_users']}")
        print(f"🏢 **Industry:** {document['executive_summary']['industry']}")
        
        print(f"\n📊 **Success Metrics:** {len(document['detailed_requirements']['success_metrics'])} defined")
        print(f"⏰ **Timeline:** {document['detailed_requirements']['timeline'].get('duration', 'TBD')}")
        print(f"⚠️ **Risks:** {len(document['detailed_requirements']['risk_assessment'])} identified")
        
        print(f"\n🤖 **Fusion v11 Ready:** {document['fusion_v11_integration']['ready_for_fusion_processing']}")
        print(f"🎯 **Recommended Agents:** {', '.join(document['fusion_v11_integration']['recommended_agents'])}")
        
        print("\n" + "="*70)
        print("✅ **READY FOR DEVELOPMENT**")
        print("="*70)

# Simple trigger function
def prp_trigger(user_input):
    """Simple trigger function for PRP creation"""
    launcher = PRPAutoLauncher()
    
    if launcher.detect_trigger_phrase(user_input):
        return launcher.auto_launch_prp_builder(user_input)
    else:
        print("❌ No PRP trigger phrase detected.")
        print("Try phrases like: 'write a PRP', 'start a PRP for cursor', 'new prototype'")
        return None

# Main execution
if __name__ == "__main__":
    # Check if run with command line argument
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        prp_trigger(user_input)
    else:
        # Interactive mode
        print("🚀 **PRP AUTO-LAUNCHER**")
        print("Type a simple phrase to start creating a PRP...")
        print("Examples: 'write a PRP', 'start a PRP for cursor', 'new prototype'")
        print("=" * 50)
        
        while True:
            user_input = input("\nWhat do you want to create? (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if user_input:
                result = prp_trigger(user_input)
                if result:
                    break
            else:
                print("Please enter a command or 'quit' to exit.") 