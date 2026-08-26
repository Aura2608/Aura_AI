#!/usr/bin/env python3
"""
District Router
Routes user input to appropriate district
"""

from typing import Dict, Optional


class DistrictRouter:
    """Routes conversations to appropriate districts."""
    
    DISTRICT_KEYWORDS = {
        'pulse': ['feeling', 'emotion', 'mood', 'pulse', 'tired', 'overwhelmed', 
                  'anxious', 'happy', 'sad', 'emotional', 'weather', 'how am i'],
        'study': ['learn', 'understand', 'research', 'explain', 'how does', 'why is',
                  'clarify', 'curious', 'figure out', 'study', 'curious', 'teach'],
        'business': ['task', 'project', 'goal', 'deadline', 'progress', 'execute',
                     'productivity', 'priority', 'done', 'work', 'project', 'business'],
        'sanctuary': ['rest', 'slow', 'pause', 'break', 'recover', 'peace', 'sanctuary',
                      'timeout', 'quiet', 'breathe', 'relax', 'chill'],
        'creative': ['idea', 'create', 'imagine', 'explore', 'play', 'design', 'brainstorm',
                     'express', 'experiment', 'fun', 'creative', 'art'],
        'support': ['stuck', 'help', 'fix', 'confused', 'blocked', 'unsure', 'unclear',
                    'not working', 'how do i', 'problem', 'issue', 'trouble'],
        'archive': ['remember', 'looking back', 'history', 'how did', 'pattern', 
                    'learned before', 'similar to', 'past', 'before']
    }
    
    def route(self, user_message: str, pulse: Dict, flux: Dict) -> str:
        """Route user to appropriate district."""
        
        message_lower = user_message.lower()
        
        # Step 1: Check for explicit keywords
        district_scores = self._score_by_keywords(message_lower)
        
        # Step 2: Use pulse state to adjust routing
        district_scores = self._adjust_by_pulse(district_scores, pulse)
        
        # Step 3: Use flux to adjust routing
        district_scores = self._adjust_by_flux(district_scores, flux)
        
        # Get highest scoring district
        best_district = max(district_scores, key=district_scores.get)
        
        return best_district
    
    def _score_by_keywords(self, message: str) -> Dict[str, int]:
        """Score districts based on keyword matches."""
        
        scores = {district: 0 for district in self.DISTRICT_KEYWORDS}
        
        for district, keywords in self.DISTRICT_KEYWORDS.items():
            for keyword in keywords:
                if keyword in message:
                    scores[district] += 1
        
        # Normalize to at least 1 point for each
        if max(scores.values()) == 0:
            scores = {k: 1 for k in scores}
        
        return scores
    
    def _adjust_by_pulse(self, scores: Dict[str, int], pulse: Dict) -> Dict[str, int]:
        """Adjust routing based on pulse state."""
        
        pulse_state = pulse.get('state', 'stable')
        
        # Route based on pulse state
        if pulse_state == 'bright_and_high':
            scores['business'] += 3
            scores['creative'] += 2
        elif pulse_state == 'steady_and_clear':
            scores['business'] += 2
            scores['study'] += 2
        elif pulse_state == 'soft_and_quiet':
            scores['sanctuary'] += 3
            scores['pulse'] += 2
        elif pulse_state == 'fragmented':
            scores['support'] += 3
            scores['sanctuary'] += 2
        elif pulse_state == 'heavy_and_dim':
            scores['support'] += 3
            scores['sanctuary'] += 2
            scores['pulse'] += 2
        elif pulse_state == 'seeking':
            scores['study'] += 2
            scores['support'] += 2
        
        return scores
    
    def _adjust_by_flux(self, scores: Dict[str, int], flux: Dict) -> Dict[str, int]:
        """Adjust routing based on mental state and cognitive load."""
        
        if flux.get('cognitive_load') == 'high':
            scores['support'] += 2
            scores['sanctuary'] += 1
        
        if flux.get('clarity') == 'low':
            scores['support'] += 1
            scores['study'] += 1
        
        if flux.get('focus_level') == 'scattered':
            scores['support'] += 2
            scores['pulse'] += 1
        
        return scores
    
    def needs_redirect(self, user_message: str, current_district: str) -> bool:
        """Check if a redirect to another district would be helpful."""
        
        # Simple heuristic: if current district has low score, suggest redirect
        scores = self._score_by_keywords(user_message.lower())
        current_score = scores.get(current_district, 0)
        max_score = max(scores.values())
        
        return current_score < max_score - 2
