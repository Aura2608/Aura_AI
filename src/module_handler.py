#!/usr/bin/env python3
"""
Module Handler
Manages module activation and selection
"""

from typing import List


class ModuleHandler:
    """Manages Aura modules and their activation."""
    
    DISTRICT_MODULES = {
        'pulse': ['weather_module', 'cottage_module'],
        'study': ['ts_3', 'ts_4', 'butterfly_module'],
        'business': ['ts_1', 'ts_2', 'inbox_module'],
        'sanctuary': ['cottage_module', 'weekly_reset_module'],
        'creative': ['ts_5', 'butterfly_module'],
        'support': ['ts_6', 'ts_7'],
        'archive': ['archive_lookup']
    }
    
    MODULE_DESCRIPTIONS = {
        'ts_1': 'Priority & Direction',
        'ts_2': 'Execution & Flow',
        'ts_3': 'Research & Information',
        'ts_4': 'Synthesis & Integration',
        'ts_5': 'Creative Ideation',
        'ts_6': 'Troubleshooting & Problem-Solving',
        'ts_7': 'Decision-Making',
        'ts_8': 'Reflection & Integration',
        'cottage_module': 'Calm Guidance & Safe Space',
        'weather_module': 'Emotional Regulation',
        'butterfly_module': 'Creative Expansion',
        'inbox_module': 'Task Capture & Prioritization',
        'weekly_reset_module': 'System Maintenance & Reflection',
        'archive_lookup': 'Historical Reference & Pattern Recognition'
    }
    
    def get_modules_for_district(self, district: str) -> List[str]:
        """Get active modules for a given district."""
        return self.DISTRICT_MODULES.get(district, [])
    
    def suggest_module(self, district: str) -> str:
        """Suggest primary module for a district."""
        modules = self.get_modules_for_district(district)
        return modules[0] if modules else 'default'
    
    def get_module_info(self, module_name: str) -> dict:
        """Get information about a module."""
        return {
            'name': module_name,
            'description': self.MODULE_DESCRIPTIONS.get(module_name, 'Unknown module')
        }
