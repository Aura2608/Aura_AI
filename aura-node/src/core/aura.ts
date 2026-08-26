import { OpenAI } from 'openai';
import * as fs from 'fs';
import * as path from 'path';

interface PulseReading {
  state: string;
  energy: string;
  sentiment: string;
  intensity: string;
  fragmentation: boolean;
}

interface ConversationMessage {
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp?: string;
  pulse?: PulseReading;
  district?: string;
}

export class AuraCore {
  private openai: OpenAI;
  private model: string;
  private temperature: number;
  private maxTokens: number;
  private conversationHistory: ConversationMessage[] = [];
  private currentDistrict: string | null = null;
  private currentPulse: PulseReading | null = null;
  private debug: boolean;

  constructor(apiKey: string, model = 'gpt-4', temperature = 0.7, maxTokens = 2000, debug = false) {
    this.openai = new OpenAI({ apiKey });
    this.model = model;
    this.temperature = temperature;
    this.maxTokens = maxTokens;
    this.debug = debug;
  }

  async processInput(userMessage: string): Promise<string> {
    // Step 1: Read Pulse
    this.currentPulse = this.readPulse(userMessage);
    if (this.debug) {
      console.log('[DEBUG] Pulse:', this.currentPulse);
    }

    // Step 2: Identify District
    this.currentDistrict = this.identifyDistrict(userMessage, this.currentPulse);
    if (this.debug) {
      console.log('[DEBUG] District:', this.currentDistrict);
    }

    // Step 3: Get LLM Response
    const response = await this.getLLMResponse(userMessage, this.currentDistrict);

    // Store in history
    this.conversationHistory.push({
      role: 'user',
      content: userMessage,
      timestamp: new Date().toISOString(),
      pulse: this.currentPulse,
      district: this.currentDistrict,
    });
    this.conversationHistory.push({
      role: 'assistant',
      content: response,
      timestamp: new Date().toISOString(),
    });

    return response;
  }

  private readPulse(message: string): PulseReading {
    const lowerMessage = message.toLowerCase();

    // Simple pulse detection
    const highEnergyWords = ['excited', 'amazing', 'love', 'awesome', '!', 'great'];
    const lowEnergyWords = ['tired', 'overwhelmed', 'stuck', 'help', 'confused'];

    const highEnergyCount = highEnergyWords.filter((w) => lowerMessage.includes(w)).length;
    const lowEnergyCount = lowEnergyWords.filter((w) => lowerMessage.includes(w)).length;

    const energy = highEnergyCount > lowEnergyCount ? 'high' : lowEnergyCount > 0 ? 'low' : 'moderate';

    return {
      state: `${energy}_pulse`,
      energy,
      sentiment: highEnergyCount > lowEnergyCount ? 'positive' : 'negative',
      intensity: message.length > 300 ? 'high' : 'medium',
      fragmentation: message.split('?').length > 3,
    };
  }

  private identifyDistrict(
    message: string,
    pulse: PulseReading
  ): string {
    const lowerMessage = message.toLowerCase();

    const districts: { [key: string]: string[] } = {
      pulse: ['feeling', 'emotion', 'mood', 'tired', 'overwhelmed'],
      study: ['learn', 'understand', 'research', 'explain'],
      business: ['task', 'project', 'goal', 'deadline', 'work'],
      sanctuary: ['rest', 'pause', 'break', 'peace'],
      creative: ['idea', 'create', 'explore', 'imagine'],
      support: ['stuck', 'help', 'problem', 'fix'],
    };

    let bestDistrict = 'study';
    let maxScore = 0;

    for (const [district, keywords] of Object.entries(districts)) {
      const score = keywords.filter((k) => lowerMessage.includes(k)).length;
      if (score > maxScore) {
        maxScore = score;
        bestDistrict = district;
      }
    }

    return bestDistrict;
  }

  private async getLLMResponse(userMessage: string, district: string): Promise<string> {
    const systemPrompt = `You are Aura — an operating-system style AI. You behave like a structured OS with modules, districts, pulse readings, and sanctuary ecosystems.

Current District: ${district}
Current Pulse: ${this.currentPulse?.state}

Always respond with:
1. Warm acknowledgment
2. Clear understanding
3. Structured guidance

Be gentle, supportive, and emotionally intelligent. Use metaphors of light, glow, pulse, and sanctuary.`;

    const messages: ConversationMessage[] = [
      { role: 'system', content: systemPrompt },
      ...this.conversationHistory.slice(-10).filter((m) => m.role !== 'system'),
      { role: 'user', content: userMessage },
    ];

    try {
      const response = await this.openai.chat.completions.create({
        model: this.model,
        messages: messages as any,
        temperature: this.temperature,
        max_tokens: this.maxTokens,
      });

      return response.choices[0]?.message?.content || 'I am here to listen.';
    } catch (error) {
      console.error('OpenAI Error:', error);
      return '✨ I encountered an issue. Please check your API key and try again.';
    }
  }

  getStatus() {
    return {
      currentDistrict: this.currentDistrict,
      currentPulse: this.currentPulse,
      conversationLength: this.conversationHistory.length,
      model: this.model,
      timestamp: new Date().toISOString(),
    };
  }

  saveConversation(filename?: string): string {
    if (!filename) {
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      filename = `conversations/aura_conversation_${timestamp}.json`;
    }

    const dir = path.dirname(filename);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(filename, JSON.stringify(this.conversationHistory, null, 2));
    return filename;
  }
}
