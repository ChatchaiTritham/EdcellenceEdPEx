@echo off
REM ============================================================================
REM EdcellenceEdPEx - Python Virtual Environment Setup Script (Windows)
REM ============================================================================
REM
REM This script automatically sets up a Python virtual environment and
REM installs all required dependencies for the EdcellenceEdPEx framework.
REM
REM Authors: Saosing et al. (2026)
REM Repository: EdcellenceEdPEx
REM ============================================================================

echo.
echo ============================================================================
echo  EdcellenceEdPEx - Python Environment Setup
echo ============================================================================
echo.
echo This script will:
echo   1. Create a Python virtual environment (venv-edpex)
echo   2. Activate the virtual environment
echo   3. Upgrade pip to latest version
echo   4. Install all required dependencies
echo   5. Verify installation
echo.
echo ============================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/5] Checking Python version...
python --version
echo.

REM Check Python version (must be 3.8+)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Detected Python version: %PYTHON_VERSION%
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment 'venv-edpex'...
if exist venv-edpex (
    echo.
    echo WARNING: Virtual environment 'venv-edpex' already exists.
    set /p OVERWRITE="Do you want to delete and recreate it? (Y/N): "
    if /i "%OVERWRITE%"=="Y" (
        echo Deleting existing virtual environment...
        rmdir /s /q venv-edpex
        python -m venv venv-edpex
        echo Virtual environment recreated successfully.
    ) else (
        echo Using existing virtual environment.
    )
) else (
    python -m venv venv-edpex
    echo Virtual environment created successfully.
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv-edpex\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
echo Virtual environment activated: venv-edpex
echo.

REM Upgrade pip
echo [4/5] Upgrading pip to latest version...
python -m pip install --upgrade pip
echo.

REM Install requirements
echo [5/5] Installing dependencies from requirements.txt...
echo This may take a few minutes...
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install dependencies
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)
echo.

REM Verify installation
echo ============================================================================
echo  Installation Verification
echo ============================================================================
echo.
echo Verifying key packages...
python -c "import numpy; print('✓ NumPy:', numpy.__version__)"
python -c "import pandas; print('✓ Pandas:', pandas.__version__)"
python -c "import matplotlib; print('✓ Matplotlib:', matplotlib.__version__)"
python -c "import plotly; print('✓ Plotly:', plotly.__version__)"
python -c "import networkx; print('✓ NetworkX:', networkx.__version__)"
echo.

REM Success message
echo ============================================================================
echo  Setup Complete!
echo ============================================================================
echo.
echo Your Python environment is ready to use.
echo.
echo To activate the environment in the future, run:
echo   venv-edpex\Scripts\activate
echo.
echo To run demonstrations:
echo   python examples\complete_demo.py
echo   python examples\advanced_visualizations_demo.py
echo.
echo To deactivate the environment when done:
echo   deactivate
echo.
echo ============================================================================
echo.

pause
