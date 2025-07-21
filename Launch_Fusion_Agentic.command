#!/bin/bash
# Fusion v12.0 Self-Contained Launcher
# Downloads and sets up all required components

# Create working directory
cd "$(dirname "$0")"
FUSION_DIR="$(pwd)"

echo "🚀 Fusion v12.0 Auto-Play System"
echo "================================"

# Configuration
REPO_OWNER="soheiloliaei"
REPO_NAME="fusion-v11"
BRANCH="main"
BASE_URL="https://raw.githubusercontent.com/$REPO_OWNER/$REPO_NAME/$BRANCH"

# Required files
declare -a FILES=(
    "prompt_patterns.py"
    "prompt_pattern_registry.py"
    "fusion_v11_agents_complete.py"
    "evaluator_metrics.py"
    "agent_chain.py"
    "fusion_v11_knowledge_base.json"
    "fusion_cli.py"
    "memory_registry.py"
    "input_transformer.py"
    "execution_mode_map.py"
    "fusion_v12_config.json"
    "requirements.txt"
)

# Create workspace structure
mkdir -p _fusion_todo/{chains,outputs,memory}
mkdir -p chain_templates

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Download files
echo "📥 Downloading required files..."
for file in "${FILES[@]}"; do
    echo "Downloading $file..."
    curl -s -o "$file" "$BASE_URL/$file"
    if [ $? -ne 0 ]; then
        echo "❌ Failed to download $file"
        exit 1
    fi
done

# Download chain templates
echo "📥 Downloading chain templates..."
declare -a TEMPLATES=(
    "provocation_loop.json"
    "critique_strategy.json"
    "rewrite_evolution.json"
)

for template in "${TEMPLATES[@]}"; do
    echo "Downloading $template..."
    curl -s -o "chain_templates/$template" "$BASE_URL/chain_templates/$template"
done

# Make CLI executable
chmod +x fusion_cli.py

# Install dependencies
echo "📚 Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Initialize fallback log
if [ ! -f "_fusion_todo/fallback_log.json" ]; then
    cat > "_fusion_todo/fallback_log.json" << EOL
{
  "version": "1.0",
  "fallback_history": [],
  "pattern_stats": {},
  "last_updated": null
}
EOL
fi

# Show welcome message
clear
echo "🎯 Welcome to Fusion v12.0!"
echo "============================"
echo ""
echo "This system helps design and analyze Block's internal tooling solutions."
echo ""
echo "Available Modes:"
echo "---------------"
echo "SIMULATE: For exploring ideas and testing concepts"
echo "SHIP: For creating production-ready specifications"
echo "CRITIQUE: For analyzing and improving existing designs"
echo ""
echo "New Features in v12.0:"
echo "--------------------"
echo "• 7 New Patterns (RiskLens, PersonaFramer, etc.)"
echo "• Execution Mode System"
echo "• Chain Templates"
echo "• Pattern Safety & Fallback"
echo "• Enhanced Metrics"
echo ""

# Show menu
echo "Choose an action:"
echo "1. 🧪 Run example chain (Payment Verification Flow)"
echo "2. 🚀 Create new design (with mode selection)"
echo "3. 🔍 Analyze existing design"
echo "4. 📊 Run pattern benchmark"
echo "5. 📚 View documentation"
echo "6. ❌ Exit"

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo "🧪 Running example chain..."
        echo "Choose execution mode:"
        echo "1. SIMULATE (exploratory)"
        echo "2. SHIP (production)"
        echo "3. CRITIQUE (analysis)"
        read -p "Enter mode (1-3): " mode_choice
        
        case $mode_choice in
            1) mode="simulate";;
            2) mode="ship";;
            3) mode="critique";;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        ./fusion_cli.py chain chain_templates/provocation_loop.json --mode $mode
        ;;
    2)
        echo "🚀 Creating new design..."
        echo "Choose domain:"
        echo "1. Payment Systems"
        echo "2. User Authentication"
        echo "3. Analytics Dashboard"
        echo "4. Custom Domain"
        read -p "Choose domain (1-4): " domain_choice
        
        case $domain_choice in
            1) domain="payment_systems";;
            2) domain="user_authentication";;
            3) domain="analytics_dashboard";;
            4) 
                read -p "Enter custom domain: " domain
                ;;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        echo "Choose execution mode:"
        echo "1. SIMULATE (exploratory)"
        echo "2. SHIP (production)"
        echo "3. CRITIQUE (analysis)"
        read -p "Enter mode (1-3): " mode_choice
        
        case $mode_choice in
            1) mode="simulate";;
            2) mode="ship";;
            3) mode="critique";;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        echo "Choose chain template:"
        echo "1. Provocation Loop (breakthrough thinking)"
        echo "2. Critique Strategy (deep analysis)"
        echo "3. Rewrite Evolution (iterative improvement)"
        read -p "Choose template (1-3): " template_choice
        
        case $template_choice in
            1) template="provocation_loop.json";;
            2) template="critique_strategy.json";;
            3) template="rewrite_evolution.json";;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        read -p "Enter design requirements: " requirements
        
        ./fusion_cli.py chain "chain_templates/$template" --mode $mode --domain "$domain" --text "$requirements"
        ;;
    3)
        echo "🔍 Analyzing existing design..."
        echo "Paste your design text (press Ctrl+D when done):"
        design=$(cat)
        
        if [ -z "$design" ]; then
            echo "❌ No input provided"
            exit 1
        fi
        
        ./fusion_cli.py chain chain_templates/critique_strategy.json --mode critique --text "$design"
        ;;
    4)
        echo "📊 Running pattern benchmark..."
        echo "Choose pattern to benchmark:"
        echo "1. StepwiseInsightSynthesis"
        echo "2. RoleDirective"
        echo "3. PatternCritiqueThenRewrite"
        echo "4. RiskLens"
        echo "5. PersonaFramer"
        echo "6. All Patterns"
        read -p "Choose pattern (1-6): " pattern_choice
        
        case $pattern_choice in
            1) pattern="StepwiseInsightSynthesis";;
            2) pattern="RoleDirective";;
            3) pattern="PatternCritiqueThenRewrite";;
            4) pattern="RiskLens";;
            5) pattern="PersonaFramer";;
            6) pattern="all";;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        if [ "$pattern" = "all" ]; then
            ./fusion_cli.py benchmark --input examples/test_input.txt
        else
            ./fusion_cli.py benchmark --pattern "$pattern" --input examples/test_input.txt
        fi
        ;;
    5)
        echo "📚 Opening documentation..."
        if [ -f "README.md" ]; then
            cat README.md
        else
            curl -s "$BASE_URL/README.md"
        fi
        ;;
    6)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

# Show results location
echo ""
echo "📂 Results are saved in:"
echo "- Chain configuration: _fusion_todo/chains/"
echo "- Generated output: _fusion_todo/outputs/"
echo "- Reasoning trail: _fusion_todo/reasoning_trail.md"
echo "- Pattern metrics: _fusion_todo/memory/"

# Deactivate virtual environment
deactivate 