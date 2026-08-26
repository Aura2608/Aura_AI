# Aura Web Interface

## Setup

```bash
cd aura-web
npm install
```

## Running

```bash
# Development
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Features

- Beautiful gradient UI with Aura branding
- Real-time status updates
- Smooth animations and interactions
- Responsive design
- Live pulse and district tracking
- Message history
- Auto-scrolling to latest messages

## Architecture

React + Vite + TypeScript

- **App.tsx** — Main React component
- **App.css** — Styling
- **main.tsx** — Entry point

Connects to the API server on `http://localhost:3000/api`
