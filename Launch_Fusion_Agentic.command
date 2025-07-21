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
declare -A FILES=(
    ["prompt_patterns.py"]="prompt_patterns.py"
    ["prompt_pattern_registry.py"]="prompt_pattern_registry.py"
    ["fusion_v11_agents_complete.py"]="fusion_v11_agents_complete.py"
    ["evaluator_metrics.py"]="evaluator_metrics.py"
    ["agent_chain.py"]="agent_chain.py"
    ["fusion_v11_knowledge_base.json"]="fusion_v11_knowledge_base.json"
    ["fusion.py"]="fusion.py"
    ["requirements.txt"]="requirements.txt"
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
for local_file in "${!FILES[@]}"; do
    remote_file="${FILES[$local_file]}"
    echo "Downloading $remote_file..."
    curl -s -o "$local_file" "$BASE_URL/$remote_file"
    if [ $? -ne 0 ]; then
        echo "❌ Failed to download $remote_file"
        exit 1
    fi
done

# Make fusion.py executable
chmod +x fusion.py

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create examples directory if it doesn't exist
mkdir -p examples

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

# Create example chain if it doesn't exist
if [ ! -f "examples/example_chain.json" ]; then
    cat > examples/example_chain.json << EOL
[
  {
    "agent": "StrategyPilot",
    "pattern": "StepwiseInsightSynthesis",
    "tension_type": "innovation_vs_feasibility",
    "metrics_threshold": 0.8
  },
  {
    "agent": "NarrativeArchitect",
    "pattern": "RoleDirective",
    "context": {
      "role": "Support Design Lead",
      "domain": "block",
      "industry": "fintech"
    },
    "metrics_threshold": 0.85
  },
  {
    "agent": "EvaluatorAgent",
    "pattern": "PatternCritiqueThenRewrite",
    "tension_type": "user_vs_business",
    "metrics_threshold": 0.9
  }
]
EOL
fi

# Create _fusion_todo directory if it doesn't exist
mkdir -p _fusion_todo

# Run system test
echo "🧪 Running system test..."
./fusion.py chain examples/example_chain.json --input examples/test_input.txt --adaptive

# Show menu
echo ""
echo "🎯 Fusion v11.2 is ready!"
echo "Choose an option:"
echo "1. Run interactive launcher"
echo "2. Run quick test"
echo "3. Run pattern evaluation"
echo "4. View documentation"
echo "5. Exit"

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo "🚀 Launching interactive mode..."
        ./fusion.py run strategy_pilot --pattern StepwiseInsightSynthesis --text "Enter your design challenge" --evaluate
        ;;
    2)
        echo "🧪 Running quick test..."
        ./fusion.py chain examples/example_chain.json --input examples/test_input.txt --adaptive
        ;;
    3)
        echo "📊 Running pattern evaluation..."
        ./fusion.py evaluate examples/test_output.txt --pattern RoleDirective
        ;;
    4)
        echo "📚 Opening documentation..."
        curl -s "$BASE_URL/ChatGPT_Upload_v11.2/README.md"
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

# Deactivate virtual environment
deactivate 