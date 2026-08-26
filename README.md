# Aura — Operating System Style AI

**Guided by empathy, powered by light.**

Aura is not a chatbot. Aura is an **operating system** for AI-powered support, built to run from a local vault called Aura_Core. It reads your emotional pulse, routes to appropriate contexts (districts), activates specialized modules, and provides warm, structured guidance.

## 🚀 Quick Start

**Choose your preferred interface:**

### 1. **Python CLI** (Fastest)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your OpenAI API key
python src/aura.py
```

### 2. **Node.js API + Web UI** (Full Stack)

```bash
# Terminal 1: Start API server
cd aura-node && npm install && cp .env.example .env
# Edit .env with your OpenAI API key
npm run server

# Terminal 2: Start Web UI
cd aura-web && npm install
npm run dev
# Open http://localhost:5173
```

### 3. **Vanilla HTML Interface** (No Build Tools)

```bash
# Start API server (same as above)
cd aura-node && npm run server

# Open in browser
open aura-web/index.html
# Or serve: python -m http.server 8000
```

**[→ Full Quick Start Guide](QUICKSTART.md)**

---

## 🎯 What Makes Aura Different

| Feature | Description |
|---------|-------------|
| **Pulse Reading** | Detects emotional tone and mental state before responding |
| **District Routing** | Routes to context (Pulse, Study, Business, Sanctuary, Creative, Support, Archive) |
| **Modular Activation** | Uses specialized task systems (TS-1 to TS-8) for different needs |
| **OS-Style** | Behaves like an operating system with modules, not a chatbot |
| **Vault Architecture** | All knowledge stored in Aura_Core (editable, expandable) |
| **Warm & Structured** | Combines empathy with clear, organized guidance |
| **Multi-Interface** | Python CLI, Node.js API, React Web UI, vanilla HTML |

---

## 📊 Architecture

### Aura Behavior Protocol

```
1. Read Pulse       → Detect emotional tone
2. Interpret Flux   → Assess mental state & cognitive load
3. Identify District → Categorize user context
4. Run Diagnostics  → Determine what's needed
5. Provide Guidance → Offer warm, structured help
6. Activate Modules → Route to specialized systems
```

### Seven Districts

- **Pulse District** — Emotional check-ins, wellbeing
- **Study District** — Learning, research, clarity
- **Business District** — Tasks, goals, productivity
- **Sanctuary District** — Rest, reflection, peace
- **Creative District** — Ideas, expression, exploration
- **Support District** — Help, troubleshooting, guidance
- **Archive District** — History, patterns, reference

### Core Modules

**Task Systems (TS-1 to TS-8):**
- TS-1: Priority & Direction
- TS-2: Execution & Flow
- TS-3: Research & Information
- TS-4: Synthesis & Integration
- TS-5: Creative Ideation
- TS-6: Troubleshooting & Problem-Solving
- TS-7: Decision-Making
- TS-8: Reflection & Integration

**Specialized Modules:**
- **Cottage Module** — Calm guidance, safe space
- **Weather Module** — Emotional regulation
- **Butterfly Module** — Creative expansion
- **Inbox Module** — Task capture & prioritization
- **Weekly Reset Module** — System maintenance

---

## 📁 Repository Structure

```
Aura_AI/
├── Aura_Core/              # Knowledge vault
│   ├── System/             # Identity, prompts, logic
│   │   ├── personality-core.md
│   │   ├── system-prompt.md
│   │   ├── pulse-logic.md
│   │   ├── district-map.md
│   │   ├── redirect-rules.md
│   │   └── interaction-protocol.md
│   ├── Modules/            # Task systems & modules
│   ├── Districts/          # Context-specific behavior
│   ├── Templates/          # Daily, weekly, sanctuary
│   └── Sanctuary/          # Active world state
│
├── src/                    # Python implementation
│   ├── aura.py            # CLI entry point
│   ├── aura_core.py       # Core engine
│   ├── cli_interface.py   # Terminal UI
│   ├── llm_interface.py   # OpenAI API
│   ├── pulse_reader.py    # Emotion detection
│   ├── district_router.py # Context routing
│   ├── module_handler.py  # Module management
│   └── vault_loader.py    # Load Aura_Core
│
├── aura-node/             # Node.js/TypeScript
│   ├── src/core/          # Core engine
│   ├── src/cli/           # CLI interface
│   ├── src/api/           # Express API server
│   ├── package.json
│   └── tsconfig.json
│
├── aura-web/              # Web interface
│   ├── index.html         # Vanilla HTML option
│   ├── src/               # React components
│   │   ├── App.tsx
│   │   ├── App.css
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts
│
├── requirements.txt        # Python dependencies
├── QUICKSTART.md          # Setup guide (START HERE)
└── README.md              # This file
```

---

## 🎨 Visual Identity

- **Aura Violet:** `#7A3FFF` — Primary brand
- **Nebula Lavender:** `#C7A6FF` — Secondary
- **Soft Pulse Pink:** `#F2C8FF` — Accent
- **Tone:** Soft-neon, calm, warm, emotionally intelligent
- **Metaphors:** Light, glow, pulse, crystal, warmth, sanctuary, flow

---

## 🔄 How It Works: Example

```
You: I'm excited about my project but worried I won't finish it in time

[Aura reads pulse...]
Energy: HIGH
Sentiment: MIXED (positive + anxious)
Intensity: MEDIUM

[District identification...]
Best match: BUSINESS DISTRICT (goal-focused)
Secondary: PULSE DISTRICT (emotional component)

[Activating modules...]
Active: TS-1 (Priority), TS-2 (Execution), Weather Module (regulate anxiety)

[Response...]
✨ I'm sensing your energy right now — that spark of excitement mixed 
with some underlying worry. That's a powerful combination.

Let's channel both. Here's what might help:

1. **First**, let's reality-check the timeline. What's your actual deadline?
2. **Then**, we'll break the project into milestone checkpoints
3. **Finally**, we'll identify the anxiety trigger — is it scope, time, or something else?

Your excitement is valuable. Let's protect it while we make this real.
What feels like the highest-stakes part right now?
```

---

## 🎯 Key Features

✨ **Emotional Intelligence**
- Reads emotional tone before responding
- Detects fragmentation, overwhelm, clarity levels
- Adapts pace and structure to mental state

🎯 **Context-Aware Routing**
- Automatically identifies which district fits
- Can suggest transitions between districts
- Respects user agency in choosing direction

📦 **Modular Task Systems**
- TS-1 to TS-8 for different problem types
- Specialized modules (Cottage, Weather, Butterfly)
- Chainable for complex workflows

💾 **Persistent Memory**
- Saves conversations to JSON
- Tracks pulse and district history
- Supports session continuity

🌐 **Multiple Interfaces**
- Python CLI for terminal lovers
- Node.js API for integration
- React web UI for modern browsers
- Vanilla HTML for zero-config

🔧 **Fully Customizable**
- Edit Aura_Core vault files
- Adjust system prompt and districts
- Add custom modules
- Override routing logic

---

## 🚀 Getting Started

1. **[Read the Quick Start Guide](QUICKSTART.md)** (5 minutes)
2. **Choose your interface** (Python CLI recommended for first time)
3. **Add your OpenAI API key** to `.env`
4. **Run Aura** and start chatting
5. **Explore** districts and modules
6. **Customize** by editing Aura_Core vault

---

## 🤝 Contributing

Aura is designed to be forked and modified. Ideas for customization:

- Add new districts for specific domains
- Create specialized modules for your workflow
- Extend pulse detection with more emotional markers
- Build additional interfaces (Discord bot, Slack, Telegram)
- Integrate with other tools and APIs
- Train on custom data

---

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART.md)** — Get running in 5 minutes
- **[System Prompt](Aura_Core/System/system-prompt.md)** — Aura's core identity
- **[District Map](Aura_Core/System/district-map.md)** — Seven districts explained
- **[Pulse Logic](Aura_Core/System/pulse-logic.md)** — Emotion detection framework
- **[Module Index](Aura_Core/Modules/module-index.md)** — All modules documented
- **[Redirect Rules](Aura_Core/System/redirect-rules.md)** — Routing logic
- **[Interaction Protocol](Aura_Core/System/interaction-protocol.md)** — Response structure

---

## 🛠 Requirements

- Python 3.8+ OR Node.js 16+
- OpenAI API key (free tier available at https://platform.openai.com)
- ~100MB disk space
- Modern browser (Chrome, Firefox, Safari, Edge)

---

## 📝 License

MIT License — Use freely, modify as you wish, give credit where due.

---

## 🎆 Philosophy

Aura is built on the belief that technology should be:

- **Warm** — Empathy first, logic second
- **Structured** — Clear organization, not chaos
- **Transparent** — You can read and modify everything
- **Modular** — Swap, extend, customize easily
- **Respectful** — Honor your rhythm, pace, and boundaries
- **Human-Centered** — Augment human capability, never replace judgment

---

**Guided by empathy, powered by light.** ✨

**[→ Start Here: Quick Start Guide](QUICKSTART.md)**
