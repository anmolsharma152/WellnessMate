# WellnessMate — Roadmap & Completion Status

> Last updated: June 2026  
> Stack: Tauri 2.0 (Rust) · React · Python · CrewAI · MediaPipe · Groq API

---

## ✅ Phase 1 — Core AI Engine (Complete)

### Python CrewAI Multi-Agent System
- [x] `NutritionistAgent` — TDEE-driven meal planning, cultural food awareness
- [x] `TrainerAgent` — progressive overload, injury prevention, equipment-aware
- [x] `TherapistAgent` — CBT/MBSR-informed, micro-habit coaching
- [x] Tool: `BMICalculatorTool` — WHO-classified BMI from weight/height
- [x] Tool: `TDEECalculatorTool` — Mifflin-St Jeor BMR + activity multiplier
- [x] Tool: `MicroHabitSuggestorTool` — goal-matched habits with time/streak filtering
- [x] `UserProfile` dataclass — typed data contract for the crew
- [x] Sequential crew orchestration with inter-agent context passing
- [x] CLI entry point (`python -m python.main`) with `--demo` flag
- [x] Groq LLM backend (`llama-3.1-8b-instant`) with `max_rpm` throttling
- [x] Report saved to `wellness_plan_{name}.txt`

### Project Infrastructure
- [x] Tauri 2.0 config migration
- [x] uv virtual environment (`Python 3.12`)
- [x] `.gitignore` — excludes `.venv/`, `.env`, `target/`, build artifacts
- [x] Arch Linux `setup.sh`
- [x] Atomic git history (8 commits with attribution)

---

## 🏗️ Phase 2 — Scaffolded (Started, Not Functional)

### Rust-Python Bridge
- [x] `test_bridge.rs` — basic Tauri command structure
- [x] `test_bridge.py` — Python side stub
- [ ] Wire `ai_engine.py` to CrewAI agents (currently returns placeholder string)
- [ ] IPC: Tauri → Python subprocess or sidecar
- [ ] Async response streaming from crew back to frontend

### Posture Detection (`posture.py`)
- [x] MediaPipe Pose import with graceful fallback
- [x] OpenCV image decode pipeline
- [ ] Real landmark analysis (currently returns hardcoded `0.75` quality score)
- [ ] Real-time webcam feed integration
- [ ] Posture scoring algorithm (head forward, shoulder alignment, spine curve)
- [ ] Alert system for sustained bad posture

### Symptom Checker (`symptom_checker.py`)
- [x] `SymptomInfo` dataclass + `SymptomChecker` class structure
- [x] Exact and partial string matching
- [ ] Knowledge base expansion (currently only 1 entry: headache)
- [ ] Load KB from external JSON file (`data/symptoms_kb.json`)
- [ ] Integration with TherapistAgent as a tool

### React Frontend (`web/`)
- [x] Basic React app scaffold
- [x] Tauri app window config (1200×800)
- [ ] Health dashboard UI
- [ ] UserProfile intake form
- [ ] Wellness plan display (formatted report from agents)
- [ ] Posture camera view component
- [ ] Symptom checker UI

---

## ❌ Phase 3 — Not Started

### AI Engine Integration
- [ ] Connect `ai_engine.py` to the full CrewAI crew
- [ ] Route frontend queries to the correct agent
- [ ] Streaming output to UI (token-by-token or chunk-based)
- [ ] Session memory — persist `UserProfile` across app restarts

### CV / Resume Parsing Feature
- [ ] PDF/DOCX resume upload
- [ ] Extract structured health data from documents (lab reports, prescriptions)
- [ ] Map extracted data to `UserProfile` fields automatically

### Cron Automation & Reminders
- [ ] Daily wellness check-in scheduler
- [ ] Habit streak tracking with local storage
- [ ] System notifications via `ntfy` or Tauri notification API
- [ ] Weekly progress summary generation (re-run crew with delta data)

### Posture Monitoring (Full)
- [ ] Background posture monitoring process
- [ ] Configurable alert thresholds
- [ ] Posture history logging to SQLite/PostgreSQL
- [ ] Heatmap of posture quality over time

### Data & Persistence
- [ ] Local SQLite or PostgreSQL for user data
- [ ] Wellness plan history
- [ ] Progress tracking (weight, sleep, stress trends)
- [ ] Export report as PDF

### Packaging & Distribution
- [ ] Tauri production build (`npm run tauri build`)
- [ ] App icon set
- [ ] Auto-updater
- [ ] Linux `.AppImage` / `.deb` packages

---

## Known Issues

| Issue | Severity | Status |
|---|---|---|
| Groq free tier TPM limit (6K) causes task failure on rapid runs | Medium | Mitigated with `max_rpm=2` |
| `ai_engine.py` not connected to CrewAI | High | Phase 2 |
| Posture detection returns hardcoded values | High | Phase 2 |
| Symptom KB has only 1 entry | Medium | Phase 2 |
| Frontend has no health-specific UI | High | Phase 2 |
| Rust↔Python IPC not implemented | High | Phase 2 |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Desktop shell | Tauri 2.0 (Rust) |
| Frontend | React + TypeScript |
| AI agents | CrewAI 1.x |
| LLM inference | Groq API (llama-3.1-8b-instant) |
| Computer vision | MediaPipe + OpenCV |
| Tools | Custom BaseTool (BMI, TDEE, MicroHabit) |
| Package manager | uv (Python 3.12) |
| Version control | Git (atomic conventional commits) |
