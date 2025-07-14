#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting setup for WellnessMate - AI Health & Posture Companion"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Please run this script as a regular user, not as root"
    exit 1
fi

# Install Rust if not installed
if ! command -v rustc &> /dev/null; then
    echo "🦀 Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source "$HOME/.cargo/env"
else
    echo "✅ Rust is already installed"
fi

# Install system dependencies for Arch Linux
if command -v pacman &> /dev/null; then
    echo "📦 Installing system dependencies..."
    sudo pacman -Syu --needed --noconfirm \
        base-devel \
        python python-pip python-virtualenv \
        nodejs npm \
        webkit2gtk \
        gtk3 \
        libappindicator-gtk3 \
        librsvg \
        libvips \
        openssl \
        wget \
        curl
else
    echo "❌ This script is designed for Arch Linux (pacman package manager)"
    exit 1
fi

# Install nvm if not installed
if [ ! -d "$HOME/.nvm" ]; then
    echo "⬇️  Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
    nvm install --lts
    nvm use --lts
fi

# Create and activate Python virtual environment
echo "🐍 Setting up Python virtual environment..."
python -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r python/requirements.txt

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Install Tauri CLI locally
if [ ! -f "node_modules/.bin/tauri" ]; then
    echo "⚙️  Installing Tauri CLI locally..."
    npm install --save-dev @tauri-apps/cli
fi

echo "✨ Setup complete!"
echo "To start developing, run the following commands:"
echo "1. source venv/bin/activate        # Activate Python virtual environment"
echo "2. npm run dev                     # Start the development server"
echo ""
echo "Note: If you encounter any permission issues, you may need to install additional"
echo "system dependencies. Refer to the Tauri documentation for more information."

# To build the application, run:
echo "   npm run tauri build "