# 🧠 WellnessMate – AI-Powered Personal Health & Posture Companion

> A native desktop app that helps improve posture, suggest micro-habits, offer symptom advice, and guide users toward better wellness — all powered by AI agents.

## 🎯 Project Goal

To build a **native desktop application** that combines:
- **Multi-Agent AI Coaching** (nutrition, fitness, therapy)
- **Webcam-based Posture Detection**
- **Symptom Checker + First Aid Assistant**
- **Micro-Habit Reminders**

This will be a **cross-platform**, installable desktop app built using **Rust + Tauri + Python + CrewAI**.

## 🧩 Key Features

| Feature | Description |
|---------|-------------|
| **Multi-Agent Coaching System** | Nutritionist + Trainer + Therapist collaborate to give advice |
| **Posture Detection** | Real-time webcam analysis to detect poor posture |
| **Micro-Habit Suggestions** | Daily reminders to stretch, hydrate, breathe, move |
| **Symptom Checker** | Ask about minor injuries or discomfort and get guidance |
| **Memory System** | Learn user preferences, schedule, and progress over time |
| **Native App Packaging** | Ships as `.AppImage`, `.exe`, or `.dmg` |

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| **Frontend UI** | Tauri (HTML/CSS/JavaScript) |
| **Backend Logic** | Rust (Tauri commands, timers, settings) |
| **AI Agents** | Python (CrewAI / LangChain / OpenAI API) |
| **Posture Detection** | Python (OpenCV + MediaPipe) |
| **Symptom Checker** | RAG-based lookup using Python |
| **Agent ↔ Rust Bridge** | `PyO3` or `maturin` |
| **Packaging** | Native binaries via Tauri CLI |

## 🧱 MVP Scope

### ✅ Phase 1: Foundation (In Progress)

#### Completed
- [x] Project setup and configuration
- [x] Basic Tauri + React frontend structure
- [x] Python virtual environment setup
- [x] Basic AI engine scaffolding
- [x] Rust-Python bridge implementation

#### In Progress
- [ ] User input form (goal/symptom)
- [ ] Multi-agent response (Nutritionist, Trainer, Therapist)
- [ ] Basic posture detection using webcam
- [ ] Symptom checker (FAQ/RAG-based)
- [ ] Hourly micro-habit reminders
- [ ] Native packaging for Linux/macOS/Windows

### ✅ Phase 2: Enhancement (After MVP)

- Webcam-based eye strain detection
- Calendar integration for habit scheduling
- Export PDF reports
- Sync with wearable devices
- Dark/light mode support
- Language localization

## 📦 Folder Structure
wellnessmate/
│
├── src-tauri/              # Rust backend + Tauri config
│   ├── src/
│   │   └── main.rs         # Entry point, calls Python logic
│   └── Cargo.toml          # Rust dependencies
│
├── python/                 # AI logic
│   ├── agents/
│   │   ├── nutritionist.py
│   │   ├── trainer.py
│   │   └── therapist.py
│   ├── ai_engine.py        # CrewAI orchestrator
│   ├── posture.py          # Webcam posture detection
│   └── symptom_checker.py  # RAG-based health Q&A
│
├── web/                    # Tauri frontend
│   ├── index.html
│   ├── style.css
│   └── script.js           # Talks to Rust backend
│
└── README.md               # Build + run instructions

## 🧪 Development Roadmap

| Week   | Goal |
|--------|------|
| Week 1 | Setup Tauri + Rust environment, basic UI |
| Week 2 | Integrate Python backend with Rust using PyO3 |
| Week 3 | Implement CrewAI agents and test prompts |
| Week 4 | Add posture detection using webcam |
| Week 5 | Build symptom checker with RAG |
| Week 6 | Implement reminder system |
| Week 7 | Package as native app (Linux/macOS/Windows) |
| Week 8 | Polish UI, add settings/preferences, write documentation |

## 🚀 Deployment Strategy

- **Local Dev**: Run with `cargo tauri dev`
- **Build**: Use `cargo tauri build` to create binaries
- **Distribution**:
  - Linux: `.AppImage`, `.deb`, or Flatpak
  - Windows: `.exe` installer
  - macOS: `.dmg` file
- Optional: Submit to Flathub, Snap Store, or GitHub Releases

## 💡 Future Ideas

- Add voice input/output (Whisper + TTS)
- Connect with Notion/Google Calendar for tracking
- Create a companion mobile app
- Offer premium features (e.g., custom meal plans)

## 👨‍💻 Skills You’ll Learn

- Building native apps with **Tauri**
- Using **Rust** for safe, performant backend logic
- Integrating **Python AI models** into native apps
- Working with **LLMs**, **NLP**, and **Computer Vision**
- Shipping software as standalone products

## 🙌 Final Thought

WellnessMate is more than just an app — it’s a tool that helps people live healthier, more balanced lives using smart AI and modern tech.

Let’s build something amazing together 🚀
