#!/bin/bash
# ============================================================================
# EdcellenceEdPEx - Python Virtual Environment Setup Script (Linux/Mac)
# ============================================================================
#
# This script automatically sets up a Python virtual environment and
# installs all required dependencies for the EdcellenceEdPEx framework.
#
# Authors: Saosing et al. (2026)
# Repository: EdcellenceEdPEx
# ============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo "============================================================================"
echo "  EdcellenceEdPEx - Python Environment Setup"
echo "============================================================================"
echo ""
echo "This script will:"
echo "  1. Create a Python virtual environment (venv-edpex)"
echo "  2. Activate the virtual environment"
echo "  3. Upgrade pip to latest version"
echo "  4. Install all required dependencies"
echo "  5. Verify installation"
echo ""
echo "============================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Python 3 is not installed or not in PATH"
    echo ""
    echo "Please install Python 3.8 or higher:"
    echo "  - Ubuntu/Debian: sudo apt-get install python3 python3-pip python3-venv"
    echo "  - macOS: brew install python3"
    echo "  - Fedora: sudo dnf install python3 python3-pip"
    echo ""
    exit 1
fi

# Check Python version
echo -e "${BLUE}[1/5]${NC} Checking Python version..."
PYTHON_VERSION=$(python3 --version)
echo "$PYTHON_VERSION"
echo ""

# Extract version number
VERSION_NUM=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if (( $(echo "$VERSION_NUM < $REQUIRED_VERSION" | bc -l) )); then
    echo -e "${RED}[ERROR]${NC} Python $REQUIRED_VERSION or higher is required"
    echo "Current version: $VERSION_NUM"
    exit 1
fi

# Create virtual environment
echo -e "${BLUE}[2/5]${NC} Creating virtual environment 'venv-edpex'..."
if [ -d "venv-edpex" ]; then
    echo ""
    echo -e "${YELLOW}WARNING:${NC} Virtual environment 'venv-edpex' already exists."
    read -p "Do you want to delete and recreate it? (y/N): " OVERWRITE
    if [[ $OVERWRITE =~ ^[Yy]$ ]]; then
        echo "Deleting existing virtual environment..."
        rm -rf venv-edpex
        python3 -m venv venv-edpex
        echo -e "${GREEN}✓${NC} Virtual environment recreated successfully."
    else
        echo "Using existing virtual environment."
    fi
else
    python3 -m venv venv-edpex
    echo -e "${GREEN}✓${NC} Virtual environment created successfully."
fi
echo ""

# Activate virtual environment
echo -e "${BLUE}[3/5]${NC} Activating virtual environment..."
source venv-edpex/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR]${NC} Failed to activate virtual environment"
    exit 1
fi
echo -e "${GREEN}✓${NC} Virtual environment activated: venv-edpex"
echo ""

# Upgrade pip
echo -e "${BLUE}[4/5]${NC} Upgrading pip to latest version..."
python -m pip install --upgrade pip --quiet
echo -e "${GREEN}✓${NC} pip upgraded successfully"
echo ""

# Install requirements
echo -e "${BLUE}[5/5]${NC} Installing dependencies from requirements.txt..."
echo "This may take a few minutes..."
echo ""
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR]${NC} Failed to install dependencies"
    echo "Please check your internet connection and try again."
    exit 1
fi
echo ""

# Verify installation
echo "============================================================================"
echo "  Installation Verification"
echo "============================================================================"
echo ""
echo "Verifying key packages..."
python -c "import numpy; print('✓ NumPy:', numpy.__version__)"
python -c "import pandas; print('✓ Pandas:', pandas.__version__)"
python -c "import matplotlib; print('✓ Matplotlib:', matplotlib.__version__)"
python -c "import plotly; print('✓ Plotly:', plotly.__version__)"
python -c "import networkx; print('✓ NetworkX:', networkx.__version__)"
echo ""

# Success message
echo "============================================================================"
echo -e "  ${GREEN}Setup Complete!${NC}"
echo "============================================================================"
echo ""
echo "Your Python environment is ready to use."
echo ""
echo "To activate the environment in the future, run:"
echo -e "  ${BLUE}source venv-edpex/bin/activate${NC}"
echo ""
echo "To run demonstrations:"
echo "  python examples/complete_demo.py"
echo "  python examples/advanced_visualizations_demo.py"
echo ""
echo "To deactivate the environment when done:"
echo "  deactivate"
echo ""
echo "============================================================================"
echo ""
