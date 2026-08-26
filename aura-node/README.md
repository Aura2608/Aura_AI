# Aura Node.js Implementation

## Setup

```bash
cd aura-node
npm install
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Running

```bash
# CLI
npm run cli

# API Server
npm run server

# Web Interface
npm run dev
```

## Structure

```
aura-node/
├── src/
│   ├── core/
│   │   ├── aura.ts          # Main Aura instance
│   │   ├── pulse-reader.ts  # Emotional detection
│   │   └── district-router.ts
│   ├── cli/
│   │   └── index.ts         # CLI interface
│   ├── api/
│   │   ├── server.ts        # Express server
│   │   └── routes.ts        # API routes
│   └── web/
│       ├── index.html       # Web UI
│       └── app.tsx          # React components
├── package.json
├── tsconfig.json
└── .env.example
```
