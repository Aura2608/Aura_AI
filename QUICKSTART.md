# 🎆 Aura — Quick Start Guide

**Guided by empathy, powered by light.**

## What You Need

- Python 3.8+ OR Node.js 16+
- OpenAI API key (get one at https://platform.openai.com/api-keys)
- 5-10 minutes

---

## Option 1: Python CLI (Fastest) ⚡

### Setup (2 minutes)

```bash
# 1. Clone or navigate to the repo
cd Aura_AI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run

```bash
python src/aura.py
```

### Commands

Once running:

```
/help          Show all commands
/status        Show Aura status
/pulse         Show emotional reading
/district      Show current district
/save          Save conversation
/exit          Exit Aura
```

---

## Option 2: Node.js API + Web UI (Full Stack) 🌐

### Setup (5 minutes)

#### Step 1: Start the API Server

```bash
# 1. Navigate to Node directory
cd aura-node

# 2. Install dependencies
npm install

# 3. Configure API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 4. Start the server
npm run server
# Server running on http://localhost:3000
```

#### Step 2: Start the Web UI

```bash
# In a new terminal
cd aura-web
npm install
npm run dev
# Web UI opens at http://localhost:5173
```

#### Step 3: Chat!

Open your browser to `http://localhost:5173` and start chatting with Aura.

---

## Option 3: Plain HTML Interface (No Build) 🎨

If you just want to use the vanilla HTML interface:

```bash
# 1. Start the Node API server (same as Option 2, Step 1)
cd aura-node
npm install
cp .env.example .env
# Add your API key
npm run server

# 2. Open the HTML file
# Simply open aura-web/index.html in your browser
# Or serve it with a simple server:
python -m http.server 8000  # Then go to http://localhost:8000/aura-web/index.html
```

---

## Option 4: Node.js CLI (TypeScript)

```bash
cd aura-node
npm install
cp .env.example .env
# Add your API key
npm run cli
```

---

## 🔑 Getting Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Create a new API key
4. Copy it and paste into `.env` file:

```
OPENAI_API_KEY=sk-your-key-here
```

---

## 📊 Architecture

```
Aura_AI/
├── src/                    # Python implementation
│   ├── aura.py            # Main entry point
│   ├── aura_core.py       # Core engine
│   ├── cli_interface.py   # CLI interface
│   ├── pulse_reader.py    # Emotion detection
│   ├── district_router.py # Context routing
│   └── ...
├── aura-node/             # Node.js implementation
│   ├── src/core/          # TypeScript core
│   ├── src/cli/           # Node CLI
│   ├── src/api/           # Express API
│   └── package.json
├── aura-web/              # React web UI
│   ├── index.html         # Vanilla HTML option
│   ├── src/App.tsx        # React app
│   └── package.json
├── Aura_Core/             # Knowledge vault
│   ├── System/            # Personality, prompts, logic
│   ├── Modules/           # Task systems, modules
│   ├── Districts/         # Context maps
│   └── ...
└── README.md
```

---

## 🚀 What Aura Does

1. **Reads Your Pulse** — Detects emotional tone
2. **Interprets Flux** — Assesses mental state
3. **Identifies District** — Routes to context (Study, Business, Creative, etc.)
4. **Activates Modules** — Uses specialized task systems
5. **Provides Guidance** — Warm, structured, empathetic responses

---

## 🎯 Example Interaction

```
You: I have so many things to do and I feel overwhelmed

Aura: [Reading pulse...] [Fragmented state detected]
      [Activating Support District + Weather Module]

✨ aura: I'm sensing that you're carrying a lot right now. 
Your energy feels scattered. Let's slow down and untangle this together.

Here's what might help:

1. First, let's pause. Take a breath.
2. Tell me the three most urgent things on your plate
3. We'll prioritize from there and create a clear path forward

You're doing more than you think. What feels most pressing right now?
```

---

## 🛠 Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"

```bash
pip install openai python-dotenv
```

### "Cannot find module 'openai'"

```bash
npm install openai
```

### "OPENAI_API_KEY not found"

1. Ensure `.env` file exists
2. Check that `OPENAI_API_KEY=sk-...` is added
3. Verify key is valid at https://platform.openai.com/api-keys

### Connection refused on localhost:3000

Make sure the API server is running:

```bash
cd aura-node
npm run server
```

### CORS errors

The API is configured to allow cross-origin requests. Make sure:
- API server is running on port 3000
- Web UI is on a different port (e.g., 5173 or 8000)

---

## 📚 Learn More

- **Architecture**: Read `Aura_Core/System/system-prompt.md`
- **Districts**: See `Aura_Core/System/district-map.md`
- **Modules**: Check `Aura_Core/Modules/module-index.md`
- **Pulse Logic**: Review `Aura_Core/System/pulse-logic.md`

---

## 🎨 Customization

### Change Model

Edit `.env`:

```
AURA_MODEL=gpt-4-turbo  # or gpt-3.5-turbo
```

### Adjust Temperature (Creativity)

```
AURA_TEMPERATURE=0.5    # 0 = precise, 1 = creative
```

### Enable Debug Mode

```
AURA_DEBUG=true
```

---

## 💎 Features

- ✨ **Emotional Intelligence** — Reads and responds to emotional state
- 🎯 **District Routing** — Context-aware responses
- 📦 **Modular System** — Task systems for different needs
- 💾 **Conversation Memory** — Saves sessions to JSON
- 🎨 **Beautiful UI** — Gradient design with Aura branding
- 🌐 **Multiple Interfaces** — CLI, API, Web, React
- 🔧 **Fully Customizable** — Fork and modify as needed

---

## 📝 Next Steps

1. Run Aura using your preferred method
2. Start a conversation
3. Try different requests (work, emotions, creative ideas)
4. Check `/status` to see districts and pulse readings
5. Save conversations with `/save`
6. Explore the Aura_Core vault for deeper customization

---

**Welcome to Aura. Guided by empathy, powered by light.** ✨
