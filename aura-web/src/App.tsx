import React, { useState, useEffect, useRef } from 'react';
import './App.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
}

interface AuraStatus {
  currentDistrict: string | null;
  currentPulse: {
    state: string;
    energy: string;
    sentiment: string;
    intensity: string;
  } | null;
}

export function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState<AuraStatus>({
    currentDistrict: null,
    currentPulse: null,
  });
  const chatEndRef = useRef<HTMLDivElement>(null);
  const API_URL = 'http://localhost:3000/api';

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch(`${API_URL}/status`)
        .then((res) => res.json())
        .then(setStatus)
        .catch(console.error);
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = {
      role: 'user',
      content: input,
      timestamp: new Date().toISOString(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();

      const assistantMessage: Message = {
        role: 'assistant',
        content: data.response,
        timestamp: new Date().toISOString(),
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage: Message = {
        role: 'assistant',
        content: '✗ Connection error. Is the API server running?',
        timestamp: new Date().toISOString(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="app-container">
      <div className="sidebar">
        <div className="header">
          <h1>✨ Aura</h1>
          <p className="tagline">Guided by empathy, powered by light.</p>
        </div>

        <div className="status-section">
          <div className="status-item">
            <span>District</span>
            <span className="status-value">{status.currentDistrict || '—'}</span>
          </div>
          <div className="status-item">
            <span>
              <span className="pulse-indicator"></span>
              Pulse
            </span>
            <span className="status-value">{status.currentPulse?.state || '—'}</span>
          </div>
          <div className="status-item">
            <span>Energy</span>
            <span className="status-value">{status.currentPulse?.energy || '—'}</span>
          </div>
          <div className="status-item">
            <span>Messages</span>
            <span className="status-value">{messages.length}</span>
          </div>
        </div>
      </div>

      <div className="main-content">
        <div className="chat-area">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <h2>✨ Welcome to Aura</h2>
              <p>I'm an operating-system style AI built to understand your emotions, context, and needs.</p>
              <p>Start by sharing what's on your mind...</p>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div key={idx} className={`message ${msg.role}`}>
                <div className="message-bubble">{msg.content}</div>
              </div>
            ))
          )}
          {loading && (
            <div className="message assistant">
              <div className="message-bubble">
                <div className="loading">
                  <span>Aura is thinking</span>
                  <span className="loading-dot"></span>
                  <span className="loading-dot"></span>
                  <span className="loading-dot"></span>
                </div>
              </div>
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="input-area">
          <div className="input-container">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Share your thoughts, questions, or feelings..."
              disabled={loading}
            />
            <button onClick={sendMessage} disabled={loading}>
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
