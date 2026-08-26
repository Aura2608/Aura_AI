#!/usr/bin/env python3
"""
Vault Loader
Loads Aura_Core vault files into memory
"""

import os
import json
from typing import Dict, Optional


class VaultLoader:
    """Loads and manages Aura_Core vault."""
    
    def __init__(self, vault_path: str = 'Aura_Core'):
        self.vault_path = vault_path
        self.vault: Dict = {}
    
    def load_vault(self) -> Dict:
        """Load all vault files into memory."""
        
        if not os.path.exists(self.vault_path):
            print(f"⚠️  Vault not found at {self.vault_path}")
            return {}
        
        # Load all markdown files from vault
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    # Create key from relative path
                    key = os.path.relpath(filepath, self.vault_path).replace('.md', '')
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            self.vault[key] = content
                    except Exception as e:
                        print(f"Error loading {filepath}: {e}")
        
        return self.vault
    
    def get_file(self, key: str) -> Optional[str]:
        """Get a specific file from vault."""
        return self.vault.get(key)
    
    def get_district_info(self, district: str) -> Optional[str]:
        """Get district information from vault."""
        key = f'Districts/{district}'
        return self.vault.get(key)
    
    def get_module_info(self, module_name: str) -> Optional[str]:
        """Get module information from vault."""
        key = f'Modules/{module_name}'
        return self.vault.get(key)
    
    def list_vault_contents(self) -> List[str]:
        """List all files in vault."""
        return list(self.vault.keys())
