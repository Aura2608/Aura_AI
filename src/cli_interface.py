#!/usr/bin/env python3
"""
CLI Interface for Aura
Command-line chat interface
"""

import sys
from typing import Optional
from colorama import Fore, Back, Style, init
from aura_core import AuraCore
import json
import os

init(autoreset=True)


class CLIInterface:
    """Command-line interface for Aura."""
    
    def __init__(self, aura: AuraCore):
        self.aura = aura
        self.running = True
        self.commands = {
            'help': self.show_help,
            'status': self.show_status,
            'clear': self.clear_history,
            'save': self.save_conversation,
            'exit': self.exit_aura,
            'quit': self.exit_aura,
            'pulse': self.show_pulse,
            'district': self.show_district,
        }
    
    def run(self):
        """Run the CLI interface."""
        self.show_welcome()
        
        while self.running:
            try:
                # Get user input
                user_input = self._get_input()
                
                if not user_input.strip():
                    continue
                
                # Check for commands
                if user_input.startswith('/'):
                    self._handle_command(user_input[1:])
                else:
                    # Process with Aura
                    self._process_message(user_input)
            
            except KeyboardInterrupt:
                print(f"\n{Fore.MAGENTA}Aura resting... Goodbye.{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
    
    def show_welcome(self):
        """Display welcome message."""
        print(f"""{Fore.MAGENTA}\n{'='*60}")
        print(f"{Fore.MAGENTA}✨ Aura — Operating System Style AI")
        print(f"{Fore.MAGENTA}Guided by empathy, powered by light.")
        print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}💫 Type /help for commands")
        print(f"{Fore.CYAN}💭 Start typing to begin...\n{Style.RESET_ALL}")
    
    def _get_input(self) -> str:
        """Get user input with custom prompt."""
        return input(f"{Fore.MAGENTA}you ▸ {Style.RESET_ALL}")
    
    def _process_message(self, user_input: str):
        """Process user message through Aura."""
        
        print(f"{Fore.CYAN}[Aura reading pulse...]{Style.RESET_ALL}", end='\r')
        
        try:
            # Get response from Aura
            response = self.aura.process_input(user_input)
            
            # Display response
            print(f"\n{Fore.MAGENTA}aura ✨ {Style.RESET_ALL}{response}\n")
        
        except Exception as e:
            print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}\n")
    
    def _handle_command(self, command_input: str):
        """Handle CLI commands."""
        
        parts = command_input.split()
        command = parts[0].lower()
        
        if command in self.commands:
            self.commands[command]()
        else:
            print(f"{Fore.YELLOW}Unknown command: /{command}. Type /help for options.{Style.RESET_ALL}")
    
    def show_help(self):
        """Display help menu."""
        print(f"{Fore.MAGENTA}\n{'='*50}")
        print(f"{Fore.MAGENTA}Aura Commands{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}/help         - Show this help menu")
        print(f"{Fore.CYAN}/status       - Show Aura status")
        print(f"{Fore.CYAN}/pulse        - Show current pulse reading")
        print(f"{Fore.CYAN}/district     - Show current district")
        print(f"{Fore.CYAN}/clear        - Clear conversation history")
        print(f"{Fore.CYAN}/save         - Save conversation to file")
        print(f"{Fore.CYAN}/exit or /quit - Exit Aura{Style.RESET_ALL}\n")
    
    def show_status(self):
        """Display Aura status."""
        status = self.aura.get_status()
        print(f"\n{Fore.MAGENTA}{'='*50}")
        print(f"{Fore.MAGENTA}Aura Status{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}District:           {status['current_district']}")
        print(f"{Fore.CYAN}Pulse:              {status['current_pulse'].get('state', 'unknown') if status['current_pulse'] else 'unknown'}")
        print(f"{Fore.CYAN}Conversation turns: {status['conversation_length'] // 2}")
        print(f"{Fore.CYAN}Model:              {status['model']}")
        print(f"{Fore.CYAN}Vault loaded:       {'✓' if status['vault_loaded'] else '✗'}{Style.RESET_ALL}\n")
    
    def show_pulse(self):
        """Display current pulse reading."""
        pulse = self.aura.current_pulse
        if pulse:
            print(f"\n{Fore.MAGENTA}{'='*50}")
            print(f"{Fore.MAGENTA}Current Pulse{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}State:        {pulse.get('state', 'unknown')}")
            print(f"{Fore.CYAN}Energy:       {pulse.get('energy', 'unknown')}")
            print(f"{Fore.CYAN}Sentiment:    {pulse.get('sentiment', 'unknown')}")
            print(f"{Fore.CYAN}Intensity:    {pulse.get('intensity', 'unknown')}")
            print(f"{Fore.CYAN}Fragmented:   {'Yes' if pulse.get('fragmentation') else 'No'}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.YELLOW}No pulse reading yet. Start a conversation!{Style.RESET_ALL}\n")
    
    def show_district(self):
        """Display current district."""
        district = self.aura.current_district
        if district:
            print(f"\n{Fore.MAGENTA}{'='*50}")
            print(f"{Fore.MAGENTA}Current District{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}District: {district}{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.YELLOW}No district selected yet. Start a conversation!{Style.RESET_ALL}\n")
    
    def clear_history(self):
        """Clear conversation history."""
        self.aura.conversation_history = []
        print(f"{Fore.GREEN}✓ Conversation history cleared.{Style.RESET_ALL}\n")
    
    def save_conversation(self):
        """Save conversation to file."""
        try:
            filename = self.aura.save_conversation()
            print(f"{Fore.GREEN}✓ Conversation saved to {filename}{Style.RESET_ALL}\n")
        except Exception as e:
            print(f"{Fore.RED}✗ Failed to save: {str(e)}{Style.RESET_ALL}\n")
    
    def exit_aura(self):
        """Exit Aura gracefully."""
        print(f"{Fore.MAGENTA}\nSaving session...{Style.RESET_ALL}")
        try:
            self.aura.save_conversation()
        except:
            pass
        self.running = False
