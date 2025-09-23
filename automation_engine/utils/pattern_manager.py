import random
import time
from datetime import datetime

class PatternManager:
    def __init__(self, config):
        self.config = config
        self.pattern_variations = self._initialize_patterns()
        self.current_pattern_index = 0
        
    def _initialize_patterns(self):
        """Initialize different behavioral patterns"""
        return {
            'standard': {
                'click_variation': 0.1,
                'scroll_intensity': 'medium',
                'navigation_style': 'direct',
                'delay_variation': 0.2
            },
            'stealth': {
                'click_variation': 0.3,
                'scroll_intensity': 'high',
                'navigation_style': 'exploratory',
                'delay_variation': 0.4
            },
            'aggressive': {
                'click_variation': 0.05,
                'scroll_intensity': 'low',
                'navigation_style': 'focused',
                'delay_variation': 0.1
            }
        }
        
    def get_current_pattern(self):
        """Get current pattern based on configuration"""
        if not self.config.ENABLE_PATTERN_VARIATION:
            return self.pattern_variations['standard']
            
        # Rotate patterns periodically
        if datetime.now().minute % 15 == 0:  # Change every 15 minutes
            self.current_pattern_index = (self.current_pattern_index + 1) % len(self.pattern_variations)
            
        pattern_name = list(self.pattern_variations.keys())[self.current_pattern_index]
        return self.pattern_variations[pattern_name]
        
    def apply_timing_variation(self, base_delay):
        """Apply pattern-based timing variations"""
        if not self.config.ENABLE_PATTERN_VARIATION:
            return base_delay
            
        pattern = self.get_current_pattern()
        variation = pattern['delay_variation']
        varied_delay = base_delay * (1 + random.uniform(-variation, variation))
        return max(0.1, varied_delay)  # Ensure minimum delay
        
    def get_scroll_pattern(self):
        """Get scroll behavior based on current pattern"""
        pattern = self.get_current_pattern()
        intensity = pattern['scroll_intensity']
        
        scroll_patterns = {
            'low': {'count': (1, 2), 'distance': (100, 300)},
            'medium': {'count': (2, 4), 'distance': (200, 500)},
            'high': {'count': (3, 6), 'distance': (300, 800)}
        }
        
        return scroll_patterns.get(intensity, scroll_patterns['medium'])