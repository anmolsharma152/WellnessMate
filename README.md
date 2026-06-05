# 🧠 WellnessMate

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)](https://github.com/yourusername/wellnessmate)

> An AI-Powered Personal Health & Posture Companion that helps improve your wellness through intelligent coaching and real-time posture monitoring.

## 🚧 Current Status (July 2024)

✅ **Completed**

- Project structure and setup
- Basic Tauri + React frontend
- Python AI engine scaffolding
- Rust-Python bridge implementation

🔄 **In Progress**

- AI agent implementations (Nutritionist, Trainer, Therapist)
- Posture detection integration
- Frontend-backend communication

📅 **Up Next**

- Implement CrewAI agent orchestration
- Add real-time posture monitoring
- Build the symptom checker component

![WellnessMate Demo](assets/wellnessmate-demo.gif)

## ✨ Features

- 🤖 Multi-Agent AI Coaching (Nutritionist, Trainer, Therapist)
- 🎥 Real-time Posture Detection
- 💡 Smart Micro-Habit Suggestions
- 🩺 Symptom Checker & First Aid Assistant
- 📅 Personalized Reminders & Progress Tracking
- 🖥️ Native Desktop Experience (Windows, macOS, Linux)

## 🚀 Getting Started

### Prerequisites

- Linux (Arch recommended)
- Git
- Basic command line knowledge

### 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/anmolsharma152/wellnessmate.git
   cd wellnessmate
   ```

2. **Run the setup script**
   This will install all necessary dependencies (Rust, Python 3.11, Node.js, etc.)

   ```bash
   chmod +x setup.sh  # Make the script executable if not already
   ./setup.sh         # Run the setup script
   ```

3. **Activate the virtual environment** (if not already activated by the setup script)

   ```bash
   source venv/bin/activate
   ```

4. **Start the development server**

   ```bash
   npm run tauri dev
   ```

### 🖥️ Development

- **Frontend**: The web interface is in the `web/` directory
- **Backend**: The Rust backend is in `src-tauri/`
- **AI Logic**: Python code is in the `python/` directory

### 🏗️ Building for Production

```bash
npm run tauri build
```

## 🛠️ Development

### Project Structure

```
wellnessmate/
├── src-tauri/              # Rust backend + Tauri config
├── python/                 # AI logic and agents
└── web/                    # Frontend UI
```

### Building

```bash
# Build for production
npm run tauri build
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Tauri](https://tauri.app/), [Rust](https://www.rust-lang.org/), and [Python](https://www.python.org/)
- Uses [CrewAI](https://www.crewai.com/) for multi-agent orchestration
- Posture detection powered by [MediaPipe](https://mediapipe.dev/)

---

Made with ❤️ by [Anmol Sharma] | [Website](https://anmolsharma152.vercel.app)
