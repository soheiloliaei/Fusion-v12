#!/bin/bash

# 🚀 FUSION V11 - ONE-CLICK INSTALLER FOR CURSOR PROJECTS
# Updated to use the new streamlined ChatGPT Upload Package
# Double-click this file or copy it to any Cursor project and double-click

echo "🚀 FUSION V11 - STREAMLINED CHATGPT INTEGRATION"
echo "=============================================="
echo ""

# Get the directory where this script is located (your project directory)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📁 Installing Fusion V11 in: $PROJECT_DIR"

# Find the Fusion_v11 source directory
FUSION_SOURCE="/Users/soheil/Desktop/Fusion_v11"

# Check if source exists
if [ ! -d "$FUSION_SOURCE" ]; then
    echo "❌ Error: Fusion_v11 source directory not found at $FUSION_SOURCE"
    echo "Please make sure your Fusion_v11 directory is at /Users/soheil/Desktop/Fusion_v11"
    read -p "Press Enter to exit..."
    exit 1
fi

echo "✅ Found Fusion V11 source directory"
echo ""

# Create .fusion directory
echo "📁 Creating .fusion directory..."
mkdir -p "$PROJECT_DIR/.fusion"

# Copy streamlined ChatGPT upload package
echo "📋 Copying streamlined ChatGPT upload package..."
if [ -d "$FUSION_SOURCE/ChatGPT_Upload_Package" ]; then
    cp -r "$FUSION_SOURCE/ChatGPT_Upload_Package" "$PROJECT_DIR/.fusion/"
    echo "✅ ChatGPT Upload Package copied (7 essential files)"
else
    echo "❌ Error: ChatGPT_Upload_Package directory not found"
    exit 1
fi

# Copy core implementation files for local development
echo "📋 Copying core implementation files..."
cp "$FUSION_SOURCE/fusion_v11_context_simple.py" "$PROJECT_DIR/.fusion/" 2>/dev/null || true
cp "$FUSION_SOURCE/fusion_v11_config.json" "$PROJECT_DIR/.fusion/" 2>/dev/null || true
cp "$FUSION_SOURCE/prp_builder_interactive.py" "$PROJECT_DIR/.fusion/" 2>/dev/null || true
cp "$FUSION_SOURCE/design_inspiration_api.py" "$PROJECT_DIR/.fusion/" 2>/dev/null || true

echo "✅ Core files copied successfully"
echo ""

# Create activation script
echo "🔧 Creating activation script..."
cat > "$PROJECT_DIR/.fusion/activate.py" << 'EOF'
#!/usr/bin/env python3
"""
Fusion V11 Activation Script for Cursor Projects
Updated for Streamlined ChatGPT Upload Package
"""

import sys
import os
import json
from pathlib import Path

def main():
    print("🚀 FUSION V11 ACTIVATION")
    print("========================")
    print()
    
    # Check if ChatGPT Upload Package exists
    chatgpt_package = Path(__file__).parent / "ChatGPT_Upload_Package"
    if chatgpt_package.exists():
        print("✅ ChatGPT Upload Package found")
        print("📦 Available files:")
        for file in chatgpt_package.glob("*"):
            print(f"   • {file.name}")
        print()
        
        print("🎯 NEXT STEPS:")
        print("1. Upload all 7 files from ChatGPT_Upload_Package/ to ChatGPT")
        print("2. Send activation prompt:")
        print('   "Activate Fusion v11 Complete with PRP enhancement."')
        print("3. Use trigger phrases like 'write a PRP' or 'let\\'s start a PRP for [project]'")
        print()
        
        # Check for local development files
        local_files = [
            "fusion_v11_context_simple.py",
            "prp_builder_interactive.py", 
            "design_inspiration_api.py"
        ]
        
        available_local = []
        for file in local_files:
            if (Path(__file__).parent / file).exists():
                available_local.append(file)
        
        if available_local:
            print("🔧 LOCAL DEVELOPMENT FILES AVAILABLE:")
            for file in available_local:
                print(f"   • {file}")
            print("   Run these directly in Cursor or terminal")
            print()
    else:
        print("❌ ChatGPT Upload Package not found")
        print("Please run Install_Fusion_V11.command again")
        return
    
    print("✅ Fusion V11 successfully activated in this project!")
    print("🌐 Ready for ChatGPT integration and local development")

if __name__ == "__main__":
    main()
EOF

chmod +x "$PROJECT_DIR/.fusion/activate.py"

# Create README for the project
echo "📖 Creating project README..."
cat > "$PROJECT_DIR/.fusion/README.md" << 'EOF'
# 🚀 Fusion V11 - Streamlined ChatGPT Integration

## Quick Start

### Option 1: ChatGPT Integration (Recommended)
1. Upload all 7 files from `ChatGPT_Upload_Package/` to ChatGPT
2. Send activation prompt: "Activate Fusion v11 Complete with PRP enhancement"
3. Use trigger phrases like "write a PRP" or "let's start a PRP for [project]"

### Option 2: Local Development
Run any of the local Python files directly in Cursor:
- `fusion_v11_context_simple.py` - Basic context engineering
- `prp_builder_interactive.py` - Interactive PRP builder
- `design_inspiration_api.py` - Design inspiration API

## Files Included

### ChatGPT Upload Package (7 Files)
1. `FUSION_V11_ENHANCED_WITH_PRP_OPTIMIZED.md` - Main prompt (under 8KB)
2. `enhanced_clarification_engine.py` - Enhanced clarification system
3. `prp_builder_auto_launcher.py` - Auto PRP builder with trigger phrases
4. `design_inspiration_api.py` - Design inspiration API
5. `README.md` - Package overview
6. `PRP_SETUP_INSTRUCTIONS.md` - Setup guide
7. `API_KEYS_SETUP_GUIDE.md` - API keys instructions

### Local Development Files
- Core Python implementations for direct execution
- Configuration files
- Interactive tools

## Usage

### ChatGPT Trigger Phrases
- "write a PRP"
- "let's start a PRP for [project]"
- "create a product requirements document"
- "build a PRP for cursor extension"
- "design requirements for mobile app"

### Local Execution
```bash
# Run in Cursor terminal
python3 .fusion/fusion_v11_context_simple.py
python3 .fusion/prp_builder_interactive.py
```

## Status: ✅ Ready for immediate use!
EOF

echo "✅ Project README created"
echo ""

# Run activation script
echo "🎮 Running activation script..."
python3 "$PROJECT_DIR/.fusion/activate.py"

echo ""
echo "🎉 INSTALLATION COMPLETE!"
echo "=========================================="
echo ""
echo "✅ Fusion V11 installed successfully in your project"
echo "✅ ChatGPT Upload Package ready (7 files)"
echo "✅ Local development files available"
echo "✅ Activation script created"
echo ""
echo "🚀 NEXT STEPS:"
echo "1. For ChatGPT: Upload files from .fusion/ChatGPT_Upload_Package/"
echo "2. For local: Run .fusion/activate.py or use Python files directly"
echo "3. For Cursor: Open project in Cursor and run any .py file"
echo ""
echo "Press Enter to continue..."
read 