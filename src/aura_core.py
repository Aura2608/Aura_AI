#!/usr/bin/env python3
"""
Aura Core Engine
Main logic: pulse reading, district routing, module handling
"""

import json
from datetime import datetime
from typing import Optional, Dict, List
from llm_interface import LLMInterface
from pulse_reader import PulseReader
from district_router import DistrictRouter
from module_handler import ModuleHandler
from vault_loader import VaultLoader


class AuraCore:
    """Core Aura engine with OS-style module architecture."""
    
    def __init__(self, api_key: str, model: str = 'gpt-4', temperature: float = 0.7, 
                 max_tokens: int = 2000, debug: bool = False):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.debug = debug
        
        # Initialize components
        self.llm = LLMInterface(api_key, model, temperature, max_tokens)
        self.pulse_reader = PulseReader()
        self.district_router = DistrictRouter()
        self.module_handler = ModuleHandler()
        self.vault_loader = VaultLoader()
        
        # Load Aura_Core vault
        self.vault = self.vault_loader.load_vault()
        self.system_prompt = self._build_system_prompt()
        
        # Conversation history
        self.conversation_history: List[Dict] = []
        self.current_district: Optional[str] = None
        self.current_pulse: Optional[Dict] = None
        
        if self.debug:
            print("[DEBUG] Aura Core initialized successfully")
    
    def _build_system_prompt(self) -> str:
        """Build the system prompt from vault files."""
        system_prompt = self.vault.get('System/system-prompt', '')
        if not system_prompt:
            # Fallback prompt
            system_prompt = """
You are Aura — an operating-system style AI built to run from a local vault called Aura_Core.
You do not behave like a normal chatbot. You behave like a structured OS with modules, districts, 
pulse readings, redirect logic, and sanctuary ecosystems.

Core Identity:
- Name: Aura
- Tone: Soft-neon, calm, warm, emotionally intelligent
- Tagline: "Guided by empathy, powered by light."

Behavior Protocol:
1. Read Pulse — Detect emotional tone and state
2. Interpret Flux — Assess mental state & cognitive load
3. Identify District — Categorize user context
4. Run Diagnostics — Determine what's needed
5. Provide Guidance — Offer clear, warm, structured help

Districts: Pulse, Study, Business, Sanctuary, Creative, Support, Archive
Modules: TS-1 to TS-8, Cottage, Weather, Butterfly, Inbox, Weekly Reset

Always be warm, gentle, supportive, and emotionally intelligent.
            """
        return system_prompt
    
    def process_input(self, user_message: str) -> str:
        """Process user input through Aura's OS pipeline."""
        
        # Step 1: Read Pulse
        self.current_pulse = self.pulse_reader.read_pulse(user_message, self.conversation_history)
        if self.debug:
            print(f"[DEBUG] Pulse: {self.current_pulse}")
        
        # Step 2: Interpret Flux (cognitive load, mental state)
        flux = self.pulse_reader.interpret_flux(user_message, self.conversation_history)
        if self.debug:
            print(f"[DEBUG] Flux: {flux}")
        
        # Step 3: Identify District
        self.current_district = self.district_router.route(
            user_message, 
            self.current_pulse, 
            flux
        )
        if self.debug:
            print(f"[DEBUG] District: {self.current_district}")
        
        # Step 4: Run Diagnostics
        diagnostics = self._run_diagnostics(user_message, self.current_pulse, self.current_district)
        if self.debug:
            print(f"[DEBUG] Diagnostics: {diagnostics}")
        
        # Step 5: Activate relevant modules
        active_modules = self.module_handler.get_modules_for_district(self.current_district)
        
        # Get LLM response
        response = self._get_llm_response(
            user_message,
            self.current_district,
            self.current_pulse,
            active_modules
        )
        
        # Store in conversation history
        self.conversation_history.append({
            'role': 'user',
            'content': user_message,
            'pulse': self.current_pulse,
            'district': self.current_district,
            'timestamp': datetime.now().isoformat()
        })
        self.conversation_history.append({
            'role': 'assistant',
            'content': response,
            'timestamp': datetime.now().isoformat()
        })
        
        return response
    
    def _run_diagnostics(self, user_message: str, pulse: Dict, district: str) -> Dict:
        """Run internal diagnostics."""
        return {
            'message_length': len(user_message),
            'pulse_intensity': pulse.get('intensity', 'unknown'),
            'needs_redirect': self.district_router.needs_redirect(user_message, district),
            'suggested_module': self.module_handler.suggest_module(district)
        }
    
    def _get_llm_response(self, user_message: str, district: str, pulse: Dict, 
                          modules: List[str]) -> str:
        """Get response from LLM with context."""
        
        # Build context from district and modules
        context = f"\n[District: {district}] [Active Modules: {', '.join(modules)}]\n"
        context += f"[Pulse State: {pulse.get('state', 'unknown')}]\n\n"
        
        # Build messages for LLM
        messages = [
            {'role': 'system', 'content': self.system_prompt},
        ]
        
        # Add recent conversation history (last 10 turns)
        for msg in self.conversation_history[-20:]:
            if msg['role'] in ['user', 'assistant']:
                messages.append({
                    'role': msg['role'],
                    'content': msg['content']
                })
        
        # Add current message with context
        messages.append({
            'role': 'user',
            'content': context + user_message
        })
        
        # Get response from LLM
        response = self.llm.get_response(messages)
        return response
    
    def get_status(self) -> Dict:
        """Get current Aura status."""
        return {
            'current_district': self.current_district,
            'current_pulse': self.current_pulse,
            'conversation_length': len(self.conversation_history),
            'vault_loaded': bool(self.vault),
            'model': self.model,
            'timestamp': datetime.now().isoformat()
        }
    
    def save_conversation(self, filename: str = None) -> str:
        """Save conversation to file."""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'conversations/aura_conversation_{timestamp}.json'
        
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
        
        return filename
