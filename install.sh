#!/bin/bash

# 🚀 Fusion v11 - One-Command Installer
# Transform any project into a strategic design powerhouse

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Configuration
FUSION_V11_REPO="https://github.com/[username]/fusion-v11.git"
FUSION_V11_DIR="fusion-v11"
INSTALL_DIR="$HOME/.fusion-v11"
TEMP_DIR="/tmp/fusion-v11-install"

# Functions
print_header() {
    echo -e "${PURPLE}"
    echo "╔══════════════════════════════════════════════════════════════════════════╗"
    echo "║                       🚀 Fusion v11 Installer                           ║"
    echo "║                                                                          ║"
    echo "║         Transform your project into a strategic design powerhouse       ║"
    echo "╚══════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_step() {
    echo -e "${BLUE}▶️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

check_dependencies() {
    print_step "Checking dependencies..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is required but not installed."
        exit 1
    fi
    
    # Check pip
    if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
        print_error "pip is required but not installed."
        exit 1
    fi
    
    # Check git
    if ! command -v git &> /dev/null; then
        print_error "Git is required but not installed."
        exit 1
    fi
    
    print_success "All dependencies found"
}

install_fusion_v11() {
    print_step "Installing Fusion v11..."
    
    # Create temp directory
    mkdir -p "$TEMP_DIR"
    cd "$TEMP_DIR"
    
    # Clone repository
    if [ -d "$FUSION_V11_DIR" ]; then
        rm -rf "$FUSION_V11_DIR"
    fi
    
    git clone "$FUSION_V11_REPO" "$FUSION_V11_DIR"
    cd "$FUSION_V11_DIR"
    
    # Install Python dependencies
    if command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt
    else
        pip install -r requirements.txt
    fi
    
    # Create install directory
    mkdir -p "$INSTALL_DIR"
    
    # Copy files to install directory
    cp -r . "$INSTALL_DIR/"
    
    print_success "Fusion v11 installed to $INSTALL_DIR"
}

setup_cli_command() {
    print_step "Setting up CLI command..."
    
    # Create fusion-v11 command
    cat > "$INSTALL_DIR/fusion-v11" << 'EOF'
#!/bin/bash
FUSION_V11_DIR="$HOME/.fusion-v11"
python3 "$FUSION_V11_DIR/deploy_fusion_v11_to_projects.py" "$@"
EOF
    
    chmod +x "$INSTALL_DIR/fusion-v11"
    
    # Add to PATH
    SHELL_RC=""
    if [ -f "$HOME/.bashrc" ]; then
        SHELL_RC="$HOME/.bashrc"
    elif [ -f "$HOME/.zshrc" ]; then
        SHELL_RC="$HOME/.zshrc"
    fi
    
    if [ -n "$SHELL_RC" ]; then
        if ! grep -q "fusion-v11" "$SHELL_RC"; then
            echo 'export PATH="$HOME/.fusion-v11:$PATH"' >> "$SHELL_RC"
            print_success "Added fusion-v11 to PATH in $SHELL_RC"
        fi
    fi
    
    # Make it available immediately
    export PATH="$HOME/.fusion-v11:$PATH"
    
    print_success "CLI command 'fusion-v11' created"
}

create_quick_start_guide() {
    print_step "Creating quick start guide..."
    
    cat > "$INSTALL_DIR/QUICK_START.md" << 'EOF'
# 🚀 Fusion v11 - Quick Start Guide

## Installation Complete! 🎉

### Command Line Usage
```bash
# Install in current directory
fusion-v11 --project-path . --project-type design_innovation

# Create new project
fusion-v11 --project-name "MyProject" --project-type design_innovation

# Batch install multiple projects
fusion-v11 --batch-file projects.json

# Get help
fusion-v11 --help
```

### ChatGPT Integration
1. Go to: `~/.fusion-v11/ChatGPT_10_Files/`
2. Upload all 10 files to ChatGPT
3. Send the activation prompt from `CHATGPT_MASTER_PROMPT.md`
4. Start innovating!

### Python Usage
```python
from fusion_v11_complete_implementation import FusionV11System

# Initialize system
fusion = FusionV11System()

# Set execution mode
fusion.set_execution_mode("simulate")

# Process design challenge
result = fusion.process_challenge("Your challenge here")
```

### Next Steps
1. Run `fusion-v11 --help` to see all options
2. Check out examples in `~/.fusion-v11/examples/`
3. Read the complete guide: `~/.fusion-v11/FUSION_V11_COMPLETE_GUIDE.md`

**Happy innovating! 🚀**
EOF
    
    print_success "Quick start guide created"
}

main() {
    print_header
    
    print_step "Starting Fusion v11 installation..."
    
    check_dependencies
    install_fusion_v11
    setup_cli_command
    create_quick_start_guide
    
    # Cleanup
    rm -rf "$TEMP_DIR"
    
    echo -e "${GREEN}"
    echo "╔══════════════════════════════════════════════════════════════════════════╗"
    echo "║                     🎉 Installation Complete! 🎉                       ║"
    echo "║                                                                          ║"
    echo "║  Quick Start:                                                            ║"
    echo "║    fusion-v11 --help                                                    ║"
    echo "║    fusion-v11 --project-path . --project-type design_innovation        ║"
    echo "║                                                                          ║"
    echo "║  ChatGPT Integration:                                                    ║"
    echo "║    Upload files from: ~/.fusion-v11/ChatGPT_10_Files/                  ║"
    echo "║                                                                          ║"
    echo "║  Documentation:                                                          ║"
    echo "║    ~/.fusion-v11/QUICK_START.md                                         ║"
    echo "║    ~/.fusion-v11/FUSION_V11_COMPLETE_GUIDE.md                          ║"
    echo "║                                                                          ║"
    echo "║  🚀 Transform your projects into strategic design powerhouses!          ║"
    echo "╚══════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${YELLOW}Note: Restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to use the 'fusion-v11' command.${NC}"
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        echo "Fusion v11 Installer"
        echo "Usage: $0 [options]"
        echo ""
        echo "Options:"
        echo "  --help, -h     Show this help message"
        echo "  --uninstall    Remove Fusion v11 installation"
        echo ""
        echo "This script will:"
        echo "  1. Check for required dependencies (Python 3, pip, git)"
        echo "  2. Clone the Fusion v11 repository"
        echo "  3. Install Python dependencies"
        echo "  4. Set up the CLI command"
        echo "  5. Create quick start documentation"
        exit 0
        ;;
    --uninstall)
        print_step "Uninstalling Fusion v11..."
        rm -rf "$INSTALL_DIR"
        print_success "Fusion v11 uninstalled"
        print_warning "You may need to manually remove the PATH entry from your shell configuration"
        exit 0
        ;;
    "")
        main
        ;;
    *)
        print_error "Unknown option: $1"
        echo "Use --help for usage information"
        exit 1
        ;;
esac 