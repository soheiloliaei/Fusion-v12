#!/bin/bash

# Fusion v12.0 Launcher
# This script sets up and runs the Fusion system with all dependencies

# Configuration
REPO_URL="https://github.com/soheiloliaei/fusion-v11.git"
VENV_DIR=".venv"
FUSION_DIR="fusion-v11"
CHAIN_TEMPLATES_DIR="chain_templates"

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Print with color
print_color() {
    color=$1
    message=$2
    printf "${color}${message}${NC}\n"
}

# Check if Python 3.8+ is installed
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_color $RED "Python 3 is not installed. Please install Python 3.8 or higher."
        exit 1
    fi
    
    version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    if (( $(echo "$version < 3.8" | bc -l) )); then
        print_color $RED "Python $version is not supported. Please install Python 3.8 or higher."
        exit 1
    fi
}

# Create and activate virtual environment
setup_venv() {
    print_color $BLUE "Setting up virtual environment..."
    python3 -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    python3 -m pip install --upgrade pip
}

# Clone or update repository
setup_repo() {
    if [ ! -d "$FUSION_DIR" ]; then
        print_color $BLUE "Cloning Fusion repository..."
        git clone $REPO_URL $FUSION_DIR
    else
        print_color $BLUE "Updating Fusion repository..."
        cd $FUSION_DIR
        git pull
        cd ..
    fi
}

# Install dependencies
install_deps() {
    print_color $BLUE "Installing dependencies..."
    cd $FUSION_DIR
    python3 -m pip install -r requirements.txt
    cd ..
}

# Create chain templates
setup_templates() {
    print_color $BLUE "Setting up chain templates..."
    mkdir -p $FUSION_DIR/$CHAIN_TEMPLATES_DIR
    
    # Create simulate template
    cat > $FUSION_DIR/$CHAIN_TEMPLATES_DIR/simulate.json << EOL
{
    "name": "simulate",
    "description": "Exploration and testing chain",
    "execution_mode": "simulate",
    "chain": [
        {
            "agent": "StrategyPilot",
            "pattern": "StepwiseInsightSynthesis"
        },
        {
            "agent": "NarrativeArchitect",
            "pattern": "RoleDirective"
        },
        {
            "agent": "EvaluatorAgent",
            "pattern": "PatternCritiqueThenRewrite"
        }
    ],
    "success_criteria": {
        "innovation_score": 0.8,
        "clarity_score": 0.8
    }
}
EOL

    # Create ship template
    cat > $FUSION_DIR/$CHAIN_TEMPLATES_DIR/ship.json << EOL
{
    "name": "ship",
    "description": "Production-ready output chain",
    "execution_mode": "ship",
    "chain": [
        {
            "agent": "StrategyPilot",
            "pattern": "StepwiseInsightSynthesis"
        },
        {
            "agent": "NarrativeArchitect",
            "pattern": "RoleDirective"
        },
        {
            "agent": "EvaluatorAgent",
            "pattern": "RiskLens"
        }
    ],
    "success_criteria": {
        "clarity_score": 0.9,
        "pattern_effectiveness": 0.9
    }
}
EOL

    # Create critique template
    cat > $FUSION_DIR/$CHAIN_TEMPLATES_DIR/critique.json << EOL
{
    "name": "critique",
    "description": "Analysis and improvement chain",
    "execution_mode": "critique",
    "chain": [
        {
            "agent": "EvaluatorAgent",
            "pattern": "PatternCritiqueThenRewrite"
        },
        {
            "agent": "StrategyPilot",
            "pattern": "StepwiseInsightSynthesis"
        }
    ],
    "success_criteria": {
        "clarity_score": 0.85,
        "innovation_score": 0.85
    }
}
EOL
}

# Run Fusion CLI
run_fusion() {
    clear
    while true; do
        print_color $GREEN "\nFusion v12.0 CLI"
        print_color $BLUE "\nSelect mode:"
        echo "1) Simulate (exploration and testing)"
        echo "2) Ship (production-ready output)"
        echo "3) Critique (analysis and improvement)"
        echo "4) Debug (detailed logging)"
        echo "5) Pattern Test (interactive pattern testing)"
        echo "6) View Stats (pattern performance)"
        echo "7) Exit"
        
        read -p "Enter choice [1-7]: " choice
        
        case $choice in
            1)
                read -p "Enter input file path: " input_file
                python3 fusion_cli.py simulate -i "$input_file" -t simulate
                ;;
            2)
                read -p "Enter input file path: " input_file
                python3 fusion_cli.py ship -i "$input_file" -t ship
                ;;
            3)
                read -p "Enter input file path: " input_file
                python3 fusion_cli.py critique -i "$input_file" -t critique
                ;;
            4)
                read -p "Enter input file path: " input_file
                read -p "Enter chain config file: " config_file
                python3 fusion.py --input "$input_file" --config "$config_file"
                ;;
            5)
                read -p "Enter input file path: " input_file
                read -p "Enter pattern name: " pattern
                python3 pattern_dev.py "$pattern" -i "$input_file"
                ;;
            6)
                python3 -c "from pattern_stats import stats; stats.update_stats(); print(stats.generate_report())"
                ;;
            7)
                print_color $GREEN "Goodbye!"
                exit 0
                ;;
            *)
                print_color $RED "Invalid choice"
                ;;
        esac
        
        echo
        read -p "Press Enter to continue..."
    done
}

# Main execution
main() {
    print_color $GREEN "Welcome to Fusion v12.0!"
    
    # Setup steps
    check_python
    setup_venv
    setup_repo
    install_deps
    setup_templates
    
    # Change to Fusion directory
    cd $FUSION_DIR
    
    # Run CLI
    run_fusion
}

# Run main function
main 