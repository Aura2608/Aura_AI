#!/usr/bin/env python3
"""
LLM Interface
Handles communication with OpenAI API
"""

from typing import List, Dict, Optional
import openai


class LLMInterface:
    """Interface to OpenAI LLM."""
    
    def __init__(self, api_key: str, model: str = 'gpt-4', temperature: float = 0.7, 
                 max_tokens: int = 2000):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        openai.api_key = api_key
    
    def get_response(self, messages: List[Dict], 
                    temperature: Optional[float] = None,
                    max_tokens: Optional[int] = None) -> str:
        """Get response from LLM."""
        
        temperature = temperature or self.temperature
        max_tokens = max_tokens or self.max_tokens
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=0.9,
                frequency_penalty=0.0,
                presence_penalty=0.6
            )
            
            return response['choices'][0]['message']['content'].strip()
        
        except openai.error.AuthenticationError:
            return "❌ Authentication failed. Check your OPENAI_API_KEY."
        except openai.error.APIError as e:
            return f"❌ API Error: {str(e)}"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def get_response_stream(self, messages: List[Dict]) -> None:
        """Stream response from LLM (for CLI)."""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stream=True
            )
            
            for chunk in response:
                if 'choices' in chunk and len(chunk['choices']) > 0:
                    delta = chunk['choices'][0].get('delta', {})
                    if 'content' in delta:
                        print(delta['content'], end='', flush=True)
        
        except Exception as e:
            print(f"\n❌ Stream Error: {str(e)}")
