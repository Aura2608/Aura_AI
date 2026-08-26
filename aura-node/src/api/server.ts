import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
import { AuraCore } from '../core/aura';
import * as dotenv from 'dotenv';

dotenv.config();

const app = express();
const aura = new AuraCore(process.env.OPENAI_API_KEY || '', process.env.AURA_MODEL as string, 0.7, 2000);

app.use(cors());
app.use(bodyParser.json());

// API Routes
app.post('/api/chat', async (req, res) => {
  try {
    const { message } = req.body;
    if (!message) {
      return res.status(400).json({ error: 'Message required' });
    }
    const response = await aura.processInput(message);
    res.json({ response });
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
});

app.get('/api/status', (req, res) => {
  res.json(aura.getStatus());
});

app.post('/api/save', (req, res) => {
  try {
    const filename = aura.saveConversation();
    res.json({ success: true, filename });
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Aura API running on http://localhost:${PORT}`);
});
