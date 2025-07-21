#!/bin/bash
# Fusion v11.2 Self-Contained Launcher
# Downloads and sets up all required components

cd "$(dirname "$0")"

echo "🚀 Fusion v11.2 Auto-Play System"
echo "================================"

# GitHub repository information
REPO_OWNER="soheiloliaei"
REPO_NAME="fusion-v11"
BRANCH="main"
BASE_URL="https://raw.githubusercontent.com/$REPO_OWNER/$REPO_NAME/$BRANCH"

# Required files to download
declare -a FILES=(
    "prompt_patterns.py"
    "prompt_pattern_registry.py"
    "fusion_v11_agents_complete.py"
    "evaluator_metrics.py"
    "agent_chain.py"
    "fusion_v11_knowledge_base.json"
    "fusion_cli.py"
    "memory_registry.py"
    "requirements.txt"
)

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Download required files
echo "📥 Downloading required files..."
for file in "${FILES[@]}"; do
    echo "Downloading $file..."
    curl -s -o "$file" "$BASE_URL/$file"
    if [ $? -ne 0 ]; then
        echo "❌ Failed to download $file"
        exit 1
    fi
done

# Make CLI executable
chmod +x fusion_cli.py

# Install dependencies
echo "📚 Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Create workspace structure
mkdir -p examples _fusion_todo/{chains,outputs}

# Create example input if it doesn't exist
if [ ! -f "examples/test_input.txt" ]; then
    cat > examples/test_input.txt << EOL
Design a new payment verification flow for Cash App that balances security with user experience. The flow should handle:

1. First-time large transactions
2. Cross-border payments
3. Business account verifications

Key requirements:
- Maintain Block's security standards
- Minimize user friction
- Support real-time verification where possible
- Comply with financial regulations

Consider both customer support implications and technical implementation requirements.
EOL
fi

# Show welcome message
clear
echo "🎯 Welcome to Fusion v11.2!"
echo "============================"
echo ""
echo "This system helps design and analyze Block's internal tooling solutions."
echo ""
echo "Available modes:"
echo "---------------"
echo "SIMULATE: For exploring ideas and testing concepts"
echo "SHIP: For creating production-ready specifications"
echo "CRITIQUE: For analyzing and improving existing designs"
echo ""
echo "Example tasks:"
echo "-------------"
echo "1. Design a new payment verification flow"
echo "2. Analyze Cash App's onboarding experience"
echo "3. Improve merchant dashboard analytics"
echo ""

# Show menu
echo "Choose an action:"
echo "1. 🧪 Run example (Payment Verification Flow)"
echo "2. 🚀 Create new design specification"
echo "3. 🔍 Analyze existing design"
echo "4. 📚 View documentation"
echo "5. ❌ Exit"

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🧪 Running example analysis..."
        echo "Using example: Payment Verification Flow"
        echo ""
        ./fusion_cli.py simulate "$(cat examples/test_input.txt)"
        ;;
    2)
        echo "🚀 Creating new design specification..."
        echo "Available areas:"
        echo "1. Payment Systems"
        echo "2. User Authentication"
        echo "3. Analytics Dashboard"
        echo "4. Custom Area"
        read -p "Choose area (1-4): " area
        
        case $area in
            1) domain="payment systems";;
            2) domain="user authentication";;
            3) domain="analytics dashboard";;
            4) 
                read -p "Enter custom area: " domain
                ;;
            *) 
                echo "❌ Invalid choice"
                exit 1
                ;;
        esac
        
        echo ""
        echo "Creating design specification for: $domain"
        read -p "Enter specific requirements (or press Enter for guided prompts): " requirements
        
        if [ -z "$requirements" ]; then
            requirements="Design a new solution for $domain that focuses on:
1. User experience and accessibility
2. Security and compliance
3. Performance and scalability
4. Integration with existing systems"
        fi
        
        ./fusion_cli.py ship "$requirements"
        ;;
    3)
        echo "🔍 Analyzing existing design..."
        echo "Enter the design to analyze (paste text and press Ctrl+D when done):"
        design=$(cat)
        
        if [ -z "$design" ]; then
            echo "❌ No input provided"
            exit 1
        fi
        
        ./fusion_cli.py critique "$design"
        ;;
    4)
        echo "📚 Opening documentation..."
        if [ -f "README.md" ]; then
            cat README.md
        else
            curl -s "$BASE_URL/README.md"
        fi
        ;;
    5)
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

# Deactivate virtual environment
deactivate 