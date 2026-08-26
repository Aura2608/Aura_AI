#!/usr/bin/env python3
"""
Pulse Reader
Detects emotional tone and mental state from user input
"""

from typing import List, Dict, Optional
import re


class PulseReader:
    """Reads emotional pulse and mental state from text."""
    
    # Emotional indicators
    HIGH_ENERGY_WORDS = ['excited', 'amazing', 'love', 'awesome', 'great', '!', '!!', '!!!',
                         'energized', 'pumped', 'thrilled', 'fantastic', 'wonderful']
    LOW_ENERGY_WORDS = ['tired', 'exhausted', 'drained', 'overwhelmed', 'stuck', 'confused',
                        'lost', 'uncertain', 'help', 'struggling', 'difficult']
    POSITIVE_WORDS = ['happy', 'good', 'well', 'fine', 'okay', 'grateful', 'blessed',
                      'peaceful', 'calm', 'clear']
    NEGATIVE_WORDS = ['sad', 'angry', 'frustrated', 'anxious', 'worried', 'scared',
                      'depressed', 'hopeless', 'useless', 'broken']
    FRAGMENTED_INDICATORS = ['?', '...', 'um', 'uh', 'i dont know', 'not sure',
                             'confused', 'scattered']
    
    def read_pulse(self, user_message: str, history: List[Dict]) -> Dict:
        """Analyze emotional tone and state."""
        
        message_lower = user_message.lower()
        
        # Detect energy level
        energy = self._detect_energy(message_lower)
        
        # Detect emotional valence
        valence = self._detect_valence(message_lower)
        
        # Detect fragmentation
        fragmentation = self._detect_fragmentation(message_lower, user_message)
        
        # Determine pulse state
        pulse_state = self._determine_state(energy, valence, fragmentation)
        
        # Calculate intensity
        intensity = self._calculate_intensity(energy, valence, fragmentation, user_message)
        
        return {
            'state': pulse_state,
            'energy': energy,
            'valence': valence,
            'fragmentation': fragmentation,
            'intensity': intensity,
            'message_length': len(user_message),
            'sentiment': 'positive' if valence > 0.5 else 'negative' if valence < 0.3 else 'neutral'
        }
    
    def interpret_flux(self, user_message: str, history: List[Dict]) -> Dict:
        """Assess mental state and cognitive load."""
        
        message_lower = user_message.lower()
        
        # Clarity assessment
        clarity = self._assess_clarity(message_lower)
        
        # Cognitive load
        cognitive_load = self._assess_cognitive_load(user_message, history)
        
        # Focus level
        focus_level = self._assess_focus(message_lower, user_message)
        
        return {
            'clarity': clarity,  # high, medium, low
            'cognitive_load': cognitive_load,  # high, medium, low
            'focus_level': focus_level,  # sharp, moderate, scattered
            'needs_structure': cognitive_load != 'low',
            'recommended_pace': 'slow' if cognitive_load == 'high' else 'moderate' if cognitive_load == 'medium' else 'fast'
        }
    
    def _detect_energy(self, message: str) -> str:
        """Detect energy level: high, moderate, low."""
        
        high_energy_count = sum(1 for word in self.HIGH_ENERGY_WORDS if word in message)
        low_energy_count = sum(1 for word in self.LOW_ENERGY_WORDS if word in message)
        
        exclamation_count = message.count('!')
        question_count = message.count('?')
        
        if high_energy_count > low_energy_count and (exclamation_count > 1 or len(message) > 200):
            return 'high'
        elif low_energy_count > high_energy_count or (question_count > exclamation_count and low_energy_count > 0):
            return 'low'
        else:
            return 'moderate'
    
    def _detect_valence(self, message: str) -> float:
        """Detect emotional valence (0-1, where 0.5 is neutral)."""
        
        positive_count = sum(1 for word in self.POSITIVE_WORDS if word in message)
        negative_count = sum(1 for word in self.NEGATIVE_WORDS if word in message)
        
        if positive_count + negative_count == 0:
            return 0.5  # neutral
        
        return positive_count / (positive_count + negative_count)
    
    def _detect_fragmentation(self, message_lower: str, original: str) -> bool:
        """Detect if message is fragmented/scattered."""
        
        fragmented_count = sum(1 for indicator in self.FRAGMENTED_INDICATORS 
                              if indicator in message_lower)
        
        # Check for multiple unrelated topics
        sentences = original.split('.')
        
        if fragmented_count > 2 or len(sentences) > 5:
            return True
        
        return False
    
    def _determine_state(self, energy: str, valence: float, fragmented: bool) -> str:
        """Determine overall pulse state."""
        
        if fragmented:
            return 'fragmented'
        elif energy == 'high' and valence > 0.6:
            return 'bright_and_high'
        elif energy == 'high' and valence < 0.4:
            return 'chaotic'
        elif energy == 'moderate' and valence > 0.5:
            return 'steady_and_clear'
        elif energy == 'low' and valence > 0.5:
            return 'soft_and_quiet'
        elif energy == 'low' and valence < 0.4:
            return 'heavy_and_dim'
        elif 'help' in fragmented or 'unclear' in str(valence):
            return 'seeking'
        else:
            return 'stable'
    
    def _calculate_intensity(self, energy: str, valence: float, fragmented: bool, message: str) -> str:
        """Calculate pulse intensity: low, medium, high."""
        
        score = 0
        
        if energy == 'high':
            score += 2
        elif energy == 'low':
            score += 1
        
        if valence < 0.3 or valence > 0.7:
            score += 2
        
        if fragmented:
            score += 2
        
        if len(message) > 300:
            score += 1
        
        if score >= 5:
            return 'high'
        elif score >= 3:
            return 'medium'
        else:
            return 'low'
    
    def _assess_clarity(self, message: str) -> str:
        """Assess message clarity."""
        
        # Check for questions
        question_ratio = message.count('?') / max(len(message.split()), 1)
        
        if question_ratio > 0.2:
            return 'low'
        elif 'clarif' in message or 'confus' in message or 'uncertain' in message:
            return 'low'
        else:
            return 'high'
    
    def _assess_cognitive_load(self, message: str, history: List[Dict]) -> str:
        """Assess cognitive load."""
        
        # Many tasks or goals mentioned
        task_indicators = ['task', 'goal', 'need to', 'should', 'must', 'have to']
        task_count = sum(1 for indicator in task_indicators if indicator in message.lower())
        
        if task_count > 3 or len(message) > 500:
            return 'high'
        elif task_count > 1:
            return 'medium'
        else:
            return 'low'
    
    def _assess_focus(self, message: str, original: str) -> str:
        """Assess focus level."""
        
        # Single topic vs scattered
        periods = original.count('.')
        sentences = len(original.split('.'))
        
        if sentences > 5:
            return 'scattered'
        elif sentences > 3:
            return 'moderate'
        else:
            return 'sharp'
