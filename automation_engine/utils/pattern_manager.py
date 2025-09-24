import random
import time
from datetime import datetime

class QuantumPatternManager:
    def __init__(self, config):
        self.config = config
        self.pattern_history = []
        self.current_pattern = self._generate_quantum_pattern()
        
    def _generate_quantum_pattern(self):
        """Generate quantum-resistant behavioral pattern"""
        base_pattern = {
            "timing_variation": random.uniform(0.1, 0.4),
            "click_variation": random.uniform(0.15, 0.35),
            "scroll_variation": random.uniform(0.2, 0.5),
            "typing_variation": random.uniform(0.1, 0.3),
            "movement_style": random.choice(["direct", "curved", "tremor"]),
            "attention_span": random.uniform(0.7, 1.5)
        }
        
        # Add quantum noise to pattern
        base_pattern.update({
            "quantum_entropy": random.uniform(0.01, 0.1),
            "pattern_signature": self._generate_pattern_signature(),
            "last_updated": datetime.now().isoformat()
        })
        
        return base_pattern
    
    def apply_timing_variation(self, base_delay):
        """Apply quantum timing variations"""
        variation = self.current_pattern["timing_variation"]
        quantum_noise = random.uniform(-0.1, 0.1) * self.current_pattern["quantum_entropy"]
        
        varied_delay = base_delay * (1 + random.uniform(-variation, variation) + quantum_noise)
        return max(0.1, varied_delay)  # Minimum 0.1 second delay
    
    def get_click_pattern(self):
        """Get quantum click behavior pattern"""
        return {
            "movement_style": self.current_pattern["movement_style"],
            "tremor_intensity": self.current_pattern["click_variation"],
            "precision_bias": random.uniform(0.8, 1.2)
        }
    
    def get_scroll_pattern(self):
        """Get quantum scroll behavior pattern"""
        scroll_types = [
            {"count": (2, 5), "distance": (200, 600), "style": "continuous"},
            {"count": (3, 8), "distance": (50, 300), "style": "bounce"},
            {"count": (4, 10), "distance": (100, 400), "style": "random"}
        ]
        
        pattern = random.choice(scroll_types)
        pattern["velocity_variation"] = self.current_pattern["scroll_variation"]
        return pattern
    
    def get_typing_pattern(self):
        """Get quantum typing behavior pattern"""
        return {
            "speed_variation": self.current_pattern["typing_variation"],
            "error_rate": random.uniform(0.01, 0.04),
            "pause_frequency": random.uniform(0.03, 0.07)
        }
    
    def rotate_pattern(self):
        """Rotate to new quantum pattern"""
        old_pattern = self.current_pattern
        self.current_pattern = self._generate_quantum_pattern()
        self.pattern_history.append({
            "old": old_pattern,
            "new": self.current_pattern,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 patterns
        if len(self.pattern_history) > 100:
            self.pattern_history.pop(0)
        
        return self.current_pattern
    
    def _generate_pattern_signature(self):
        """Generate unique pattern signature"""
        import hashlib
        base_data = str(random.random()) + str(datetime.now())
        return hashlib.md5(base_data.encode()).hexdigest()[:8]
    
    def detect_anti_pattern(self, recent_operations):
        """Detect if current pattern is being flagged"""
        if len(recent_operations) < 10:
            return False
            
        failure_rate = sum(1 for op in recent_operations[-10:] if not op.get('success', True)) / 10
        return failure_rate > 0.7  # Rotate if 70% failure rate
    
    def get_pattern_stats(self):
        """Get pattern management statistics"""
        return {
            "current_pattern": self.current_pattern["pattern_signature"],
            "pattern_history_count": len(self.pattern_history),
            "last_rotation": self.pattern_history[-1]["timestamp"] if self.pattern_history else "never"
        }