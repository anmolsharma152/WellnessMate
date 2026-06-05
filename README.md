# 🧠 WellnessMate

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.x-green.svg)](https://crewai.com)
[![Tauri](https://img.shields.io/badge/Tauri-2.0-purple.svg)](https://tauri.app)
[![Project Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)](https://github.com/anmolsharma152/WellnessMate)

> An AI-powered personal health companion — multi-agent coaching system with real-time posture monitoring and a native desktop experience.

---

## 🤖 What Works Right Now

The Python AI engine is fully functional as a CLI tool:

```bash
# Run with demo profile
python -m python.main --demo

# Run interactively
python -m python.main
```

Three CrewAI agents collaborate sequentially to produce a unified wellness plan:

| Agent | Role | Tools |
|---|---|---|
| **Nutritionist** | TDEE-based meal planning, macro targets, food swaps | BMI Calculator, TDEE Calculator |
| **Trainer** | Weekly training split, progressive overload, mobility | BMI Calculator |
| **Therapist** | Stress assessment, micro-habits, morning/evening routines | Micro-Habit Suggestor |

Each agent receives context from the previous one — the trainer aligns intensity with the nutritionist's calorie targets; the therapist supports both plans through sleep and habit optimization.

---

## 🏗️ Architecture

```
WellnessMate/
├── python/
│   ├── agents/              # CrewAI agent definitions
│   │   ├── nutritionist.py
│   │   ├── trainer.py
│   │   └── therapist.py
│   ├── tasks/
│   │   └── health_tasks.py  # Task definitions + UserProfile dataclass
│   ├── tools/
│   │   └── health_tools.py  # BMI, TDEE, MicroHabit tools
│   ├── crew.py              # Crew orchestration
│   ├── main.py              # CLI entry point
│   ├── posture.py           # MediaPipe posture detection (Phase 2)
│   └── symptom_checker.py   # Symptom KB (Phase 2)
├── src-tauri/               # Rust backend + Tauri 2.0 config
└── web/                     # React frontend (Phase 2)
```

---

## 🚀 Getting Started

### Prerequisites

- Linux (Arch recommended)
- Python 3.12
- [uv](https://docs.astral.sh/uv/) — fast Python package manager
- Rust + Cargo (for Tauri desktop build)
- Node.js + npm (for frontend)
- [Groq API key](https://console.groq.com) (free tier works)

### Installation

```bash
git clone https://github.com/anmolsharma152/WellnessMate.git
cd WellnessMate

# Create virtual environment
uv venv
source .venv/bin/activate

# Install Python dependencies
uv pip install "crewai>=0.80.0" groq python-dotenv loguru

# Add your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# Run the wellness assessment CLI
python -m python.main --demo
```

### Desktop App (Work in Progress)

```bash
# Install frontend dependencies
npm install

# Start development server
npm run tauri dev
```

> ⚠️ The Tauri desktop UI is scaffolded but the Python↔Rust IPC bridge is not yet connected. The CLI is the working interface for now.

---

## 📋 Roadmap

See [ROADMAP.md](ROADMAP.md) for the full completion status across all phases.

**Phase 1 ✅** — CrewAI agents, tools, CLI  
**Phase 2 🏗️** — Rust↔Python bridge, posture detection, React UI  
**Phase 3 ❌** — CV parsing, cron automation, data persistence, packaging  

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Desktop shell | Tauri 2.0 (Rust) |
| Frontend | React + TypeScript |
| AI agents | CrewAI 1.x |
| LLM inference | Groq API (llama-3.1-8b-instant) |
| Computer vision | MediaPipe + OpenCV |
| Tools | Custom CrewAI BaseTool |
| Package manager | uv (Python 3.12) |

---

## 🙏 Acknowledgments

- [Tauri](https://tauri.app/) — native desktop shell
- [CrewAI](https://crewai.com/) — multi-agent orchestration
- [Groq](https://groq.com/) — LLM inference
- [MediaPipe](https://mediapipe.dev/) — posture detection

---

Made with ❤️ by [Anmol Sharma](https://anmolsharma152.vercel.app)
