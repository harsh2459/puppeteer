import random
import time
import json
import math
from datetime import datetime, timedelta
from config import settings

class QuantumPatternManager:
    def __init__(self, config):
        self.config = config
        self.behavior_patterns = self._init_behavior_patterns()
        self.current_pattern = 'standard'
        self.pattern_history = []
        self.entropy_source = random.random()
        self.adaptation_rate = 0.1
        self.pattern_variations = {}
        
    def _init_behavior_patterns(self):
        """Initialize comprehensive behavioral patterns with quantum variations"""
        return {
            'standard': {
                'click_accuracy': 0.92,
                'scroll_speed': 1.0,
                'typing_speed': 0.12,  # seconds per character
                'error_rate': 0.03,
                'pause_frequency': 0.08,
                'reading_speed': 1.0,
                'movement_style': 'natural',
                'attention_span': 1.0,
                'decision_delay': (0.3, 1.2),
                'scroll_behavior': 'smooth',
                'click_precision': 'high'
            },
            'casual': {
                'click_accuracy': 0.85,
                'scroll_speed': 0.7,
                'typing_speed': 0.18,
                'error_rate': 0.06,
                'pause_frequency': 0.12,
                'reading_speed': 0.8,
                'movement_style': 'relaxed',
                'attention_span': 0.7,
                'decision_delay': (0.5, 2.0),
                'scroll_behavior': 'intermittent',
                'click_precision': 'medium'
            },
            'focused': {
                'click_accuracy': 0.97,
                'scroll_speed': 1.2,
                'typing_speed': 0.08,
                'error_rate': 0.01,
                'pause_frequency': 0.04,
                'reading_speed': 1.3,
                'movement_style': 'precise',
                'attention_span': 1.5,
                'decision_delay': (0.1, 0.8),
                'scroll_behavior': 'direct',
                'click_precision': 'very_high'
            },
            'distracted': {
                'click_accuracy': 0.78,
                'scroll_speed': 1.4,
                'typing_speed': 0.25,
                'error_rate': 0.10,
                'pause_frequency': 0.20,
                'reading_speed': 0.6,
                'movement_style': 'erratic',
                'attention_span': 0.4,
                'decision_delay': (0.8, 3.0),
                'scroll_behavior': 'random',
                'click_precision': 'low'
            },
            'research': {
                'click_accuracy': 0.94,
                'scroll_speed': 0.9,
                'typing_speed': 0.15,
                'error_rate': 0.02,
                'pause_frequency': 0.15,
                'reading_speed': 0.9,
                'movement_style': 'analytical',
                'attention_span': 1.8,
                'decision_delay': (0.4, 1.5),
                'scroll_behavior': 'methodical',
                'click_precision': 'high'
            },
            'shopping': {
                'click_accuracy': 0.88,
                'scroll_speed': 1.1,
                'typing_speed': 0.20,
                'error_rate': 0.05,
                'pause_frequency': 0.10,
                'reading_speed': 1.1,
                'movement_style': 'comparative',
                'attention_span': 0.9,
                'decision_delay': (0.6, 2.5),
                'scroll_behavior': 'comparison',
                'click_precision': 'medium'
            }
        }
    
    def get_click_pattern(self, element_type='unknown', context=None):
        """Get click behavior pattern with contextual variations"""
        base_pattern = self.behavior_patterns[self.current_pattern].copy()
        context = context or {}
        
        # Apply contextual adjustments
        if element_type == 'button':
            base_pattern['click_accuracy'] *= 1.05  # More accurate on buttons
            base_pattern['decision_delay'] = (
                base_pattern['decision_delay'][0] * 0.8,
                base_pattern['decision_delay'][1] * 0.9
            )
        elif element_type == 'link':
            base_pattern['click_accuracy'] *= 0.95  # Less accurate on links
        elif element_type == 'small_element':
            base_pattern['click_accuracy'] *= 0.85  # Less accurate on small elements
        
        # Context-based adjustments
        if context.get('urgent'):
            base_pattern['decision_delay'] = (
                base_pattern['decision_delay'][0] * 0.5,
                base_pattern['decision_delay'][1] * 0.7
            )
        if context.get('important'):
            base_pattern['click_accuracy'] *= 1.1
        
        # Add quantum variations
        base_pattern = self._apply_quantum_variations(base_pattern, 'click')
        
        return base_pattern
    
    def get_typing_pattern(self, text_length=0, field_type='text'):
        """Get typing behavior pattern with field-specific variations"""
        base_pattern = self.behavior_patterns[self.current_pattern].copy()
        
        # Adjust based on text length
        if text_length > 100:
            base_pattern['typing_speed'] *= 0.9  # Slower for long texts
            base_pattern['error_rate'] *= 1.2   # More errors when tired
        elif text_length < 10:
            base_pattern['typing_speed'] *= 1.2  # Faster for short texts
        
        # Field type adjustments
        if field_type == 'password':
            base_pattern['typing_speed'] *= 1.3   # Faster typing for passwords
            base_pattern['error_rate'] *= 0.8     # More careful with passwords
        elif field_type == 'search':
            base_pattern['typing_speed'] *= 1.1   # Faster for search
        elif field_type == 'email':
            base_pattern['error_rate'] *= 0.7     # More accurate for emails
        
        # Add quantum variations
        base_pattern = self._apply_quantum_variations(base_pattern, 'typing')
        
        return {
            'speed_variation': base_pattern['typing_speed'] * random.uniform(0.8, 1.2),
            'error_rate': base_pattern['error_rate'],
            'pause_frequency': base_pattern['pause_frequency'],
            'backspace_probability': base_pattern['error_rate'] * 2,
            'thinking_pauses': random.uniform(0.5, 2.0)  # Pauses between words
        }
    
    def get_scroll_pattern(self, scroll_direction='down', content_length=0):
        """Get scrolling behavior pattern with directional variations"""
        base_pattern = self.behavior_patterns[self.current_pattern].copy()
        
        # Directional adjustments
        if scroll_direction == 'up':
            base_pattern['scroll_speed'] *= 1.3  # Faster scrolling up
        elif scroll_direction == 'down':
            base_pattern['scroll_speed'] *= 1.0  # Normal speed down
        
        # Content length adjustments
        if content_length > 5000:  # Long content
            base_pattern['scroll_speed'] *= 0.8   # Slower for long reads
            base_pattern['pause_frequency'] *= 1.5  # More pauses
        elif content_length < 500:  # Short content
            base_pattern['scroll_speed'] *= 1.4   # Faster for short content
        
        # Add quantum variations
        base_pattern = self._apply_quantum_variations(base_pattern, 'scroll')
        
        return {
            'scroll_speed': base_pattern['scroll_speed'],
            'scroll_style': base_pattern['scroll_behavior'],
            'scroll_amount': random.randint(200, 600),  # Pixels per scroll
            'pause_between': random.uniform(0.1, 0.5),  # Seconds between scrolls
            'scroll_variation': random.uniform(0.8, 1.2)  # Speed variation
        }
    
    def get_navigation_pattern(self, target_type, previous_behavior=None):
        """Get navigation behavior pattern based on target type"""
        base_pattern = self.behavior_patterns[self.current_pattern].copy()
        previous_behavior = previous_behavior or {}
        
        # Target type adjustments
        navigation_profiles = {
            'search_engine': {
                'speed_multiplier': 1.2,
                'accuracy_multiplier': 0.9,
                'pause_multiplier': 0.8
            },
            'social_media': {
                'speed_multiplier': 1.4,
                'accuracy_multiplier': 0.8,
                'pause_multiplier': 1.3
            },
            'shopping': {
                'speed_multiplier': 0.9,
                'accuracy_multiplier': 1.1,
                'pause_multiplier': 1.5
            },
            'news': {
                'speed_multiplier': 1.1,
                'accuracy_multiplier': 1.0,
                'pause_multiplier': 1.2
            },
            'work': {
                'speed_multiplier': 0.8,
                'accuracy_multiplier': 1.3,
                'pause_multiplier': 0.7
            }
        }
        
        profile = navigation_profiles.get(target_type, navigation_profiles['search_engine'])
        
        base_pattern['scroll_speed'] *= profile['speed_multiplier']
        base_pattern['click_accuracy'] *= profile['accuracy_multiplier']
        base_pattern['pause_frequency'] *= profile['pause_multiplier']
        
        # Learn from previous behavior
        if previous_behavior.get('success_rate', 0) > 0.8:
            # If previous behavior was successful, become slightly more efficient
            base_pattern['scroll_speed'] *= 1.05
            base_pattern['click_accuracy'] *= 1.02
        elif previous_behavior.get('success_rate', 0) < 0.5:
            # If struggling, slow down and be more careful
            base_pattern['scroll_speed'] *= 0.9
            base_pattern['pause_frequency'] *= 1.1
        
        # Add quantum variations
        base_pattern = self._apply_quantum_variations(base_pattern, 'navigation')
        
        return base_pattern
    
    def _apply_quantum_variations(self, pattern, pattern_type):
        """Apply quantum-level variations to behavior patterns"""
        variation_pattern = pattern.copy()
        
        # Pattern-type specific variations
        variation_ranges = {
            'click': {'range': 0.15, 'consistency': 0.8},
            'typing': {'range': 0.20, 'consistency': 0.7},
            'scroll': {'range': 0.25, 'consistency': 0.6},
            'navigation': {'range': 0.18, 'consistency': 0.75}
        }
        
        variation_config = variation_ranges.get(pattern_type, variation_ranges['click'])
        
        for key in variation_pattern:
            if isinstance(variation_pattern[key], (int, float)):
                # Apply consistent but varying adjustments
                base_value = variation_pattern[key]
                variation_range = variation_config['range']
                consistency = variation_config['consistency']
                
                # Generate consistent variation based on entropy and key
                variation_seed = f"{self.entropy_source}{key}{pattern_type}"
                random.seed(int(hashlib.md5(variation_seed.encode()).hexdigest()[:8], 16))
                
                variation = (random.random() - 0.5) * 2 * variation_range
                adjusted_variation = variation * consistency + (random.random() - 0.5) * 2 * variation_range * (1 - consistency)
                
                variation_pattern[key] = base_value * (1 + adjusted_variation)
                variation_pattern[key] = max(0.1, variation_pattern[key])  # Prevent extreme values
        
        random.seed()  # Reset random seed
        return variation_pattern
    
    def rotate_pattern(self, new_pattern=None, transition_smoothness='smooth'):
        """Rotate to a new behavior pattern"""
        available_patterns = list(self.behavior_patterns.keys())
        
        if new_pattern and new_pattern in available_patterns:
            target_pattern = new_pattern
        else:
            # Weighted random selection based on current context
            weights = self._calculate_pattern_weights()
            target_pattern = random.choices(available_patterns, weights=weights)[0]
        
        # Record the transition
        transition = {
            'timestamp': time.time(),
            'from_pattern': self.current_pattern,
            'to_pattern': target_pattern,
            'transition_type': transition_smoothness,
            'duration': random.uniform(2, 10)  # Transition duration in seconds
        }
        
        self.pattern_history.append(transition)
        self.current_pattern = target_pattern
        
        # Update pattern variations for the new pattern
        self._update_pattern_variations()
        
        if self.config.DEBUG_MODE:
            print(f"🔄 Pattern rotated: {transition['from_pattern']} → {target_pattern}")
        
        return transition
    
    def _calculate_pattern_weights(self):
        """Calculate weights for pattern selection based on context"""
        current_hour = datetime.now().hour
        weights = {}
        
        for pattern in self.behavior_patterns.keys():
            base_weight = 1.0
            
            # Time-based adjustments
            if 6 <= current_hour <= 10:  # Morning
                if pattern in ['focused', 'research']:
                    base_weight *= 1.5
                elif pattern == 'distracted':
                    base_weight *= 0.5
                    
            elif 13 <= current_hour <= 14:  # Lunch
                if pattern in ['casual', 'shopping']:
                    base_weight *= 1.8
                    
            elif 20 <= current_hour <= 23:  # Evening
                if pattern in ['casual', 'social']:
                    base_weight *= 1.6
                elif pattern == 'focused':
                    base_weight *= 0.7
                    
            elif 0 <= current_hour <= 5:  # Late night
                if pattern == 'distracted':
                    base_weight *= 2.0
                else:
                    base_weight *= 0.8
            
            # Recent pattern avoidance (don't repeat too quickly)
            recent_patterns = [h['to_pattern'] for h in self.pattern_history[-3:]]
            if pattern in recent_patterns:
                base_weight *= 0.3
            
            weights[pattern] = base_weight
        
        return [weights.get(pattern, 1.0) for pattern in self.behavior_patterns.keys()]
    
    def _update_pattern_variations(self):
        """Update pattern variations for the current pattern"""
        base_pattern = self.behavior_patterns[self.current_pattern]
        self.pattern_variations[self.current_pattern] = {}
        
        # Create multiple variations of the current pattern
        for i in range(3):  # Create 3 variations
            variation = base_pattern.copy()
            for key in variation:
                if isinstance(variation[key], (int, float)):
                    # Apply unique variation for each version
                    variation_seed = f"{self.current_pattern}{key}{i}{self.entropy_source}"
                    random.seed(int(hashlib.md5(variation_seed.encode()).hexdigest()[:8], 16))
                    variation[key] *= random.uniform(0.85, 1.15)
            
            random.seed()
            self.pattern_variations[self.current_pattern][f'variation_{i}'] = variation
    
    def adapt_pattern_based_on_performance(self, performance_metrics):
        """Adapt patterns based on operational performance"""
        success_rate = performance_metrics.get('success_rate', 0.5)
        error_rate = performance_metrics.get('error_rate', 0.1)
        avg_duration = performance_metrics.get('avg_duration', 1.0)
        
        current_pattern = self.behavior_patterns[self.current_pattern].copy()
        
        # Adaptive learning based on performance
        if success_rate < 0.6:
            # If struggling, become more careful
            current_pattern['click_accuracy'] *= 1.1
            current_pattern['decision_delay'] = (
                current_pattern['decision_delay'][0] * 1.2,
                current_pattern['decision_delay'][1] * 1.3
            )
            current_pattern['scroll_speed'] *= 0.9
            
        elif success_rate > 0.9 and avg_duration > 2.0:
            # If successful but slow, become slightly faster
            current_pattern['scroll_speed'] *= 1.1
            current_pattern['decision_delay'] = (
                current_pattern['decision_delay'][0] * 0.9,
                current_pattern['decision_delay'][1] * 0.95
            )
        
        # Update the pattern with adaptations
        self.behavior_patterns[self.current_pattern] = current_pattern
        
        if self.config.DEBUG_MODE:
            print(f"🎯 Pattern adapted: success_rate={success_rate:.1%}")
    
    def get_pattern_report(self):
        """Get comprehensive pattern management report"""
        recent_transitions = self.pattern_history[-5:] if self.pattern_history else []
        
        return {
            'current_pattern': self.current_pattern,
            'total_transitions': len(self.pattern_history),
            'pattern_variations': len(self.pattern_variations.get(self.current_pattern, {})),
            'adaptation_rate': self.adaptation_rate,
            'recent_transitions': recent_transitions,
            'available_patterns': list(self.behavior_patterns.keys()),
            'current_pattern_config': self.behavior_patterns[self.current_pattern]
        }
    
    def save_pattern_data(self, filepath=None):
        """Save pattern data for analysis and continuity"""
        if not filepath:
            filepath = f"pattern_data_{int(time.time())}.json"
        
        data = {
            'timestamp': time.time(),
            'current_pattern': self.current_pattern,
            'pattern_history': self.pattern_history,
            'behavior_patterns': self.behavior_patterns,
            'pattern_variations': self.pattern_variations,
            'entropy_source': self.entropy_source
        }
        
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Failed to save pattern data: {e}")
            return False
    
    def load_pattern_data(self, filepath):
        """Load pattern data to continue previous session"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.current_pattern = data.get('current_pattern', 'standard')
            self.pattern_history = data.get('pattern_history', [])
            self.behavior_patterns = data.get('behavior_patterns', self._init_behavior_patterns())
            self.pattern_variations = data.get('pattern_variations', {})
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Failed to load pattern data: {e}")
            return False

# Utility function
def create_pattern_manager(config=None):
    """Factory function for easy pattern manager creation"""
    from config import settings
    config = config or settings.current_config
    return QuantumPatternManager(config)