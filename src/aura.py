#!/usr/bin/env python3
"""
Aura — Operating System Style AI
Main entry point for CLI interface
"""

import os
from dotenv import load_dotenv
from aura_core import AuraCore
from cli_interface import CLIInterface


def main():
    """Initialize and run Aura."""
    load_dotenv()
    
    # Initialize Aura Core
    aura = AuraCore(
        api_key=os.getenv('OPENAI_API_KEY'),
        model=os.getenv('AURA_MODEL', 'gpt-4'),
        temperature=float(os.getenv('AURA_TEMPERATURE', 0.7)),
        max_tokens=int(os.getenv('AURA_MAX_TOKENS', 2000)),
        debug=os.getenv('AURA_DEBUG', 'false').lower() == 'true'
    )
    
    # Initialize CLI Interface
    cli = CLIInterface(aura)
    
    # Run Aura
    cli.run()


if __name__ == '__main__':
    main()
