import random
import time
import math
from datetime import datetime, timedelta
import json

class NeuromorphicBehaviorEngine:
    def __init__(self, config):
        self.config = config
        self.cognitive_states = self._init_cognitive_states()
        self.emotional_states = self._init_emotional_states()
        self.current_state = 'focused'
        self.current_emotion = 'neutral'
        self.attention_span = random.uniform(0.7, 1.3)
        self.cognitive_load = 1.0
        self.fatigue_level = 0.0
        self.learning_rate = random.uniform(0.8, 1.2)
        self.behavior_history = []
        self.last_state_change = time.time()
        
    def _init_cognitive_states(self):
        """Initialize comprehensive cognitive states with behavioral parameters"""
        return {
            'focused': {
                'click_accuracy': 0.95,
                'scroll_speed': 1.0,
                'reading_speed': 1.2,
                'error_rate': 0.01,
                'decision_speed': 0.8,
                'multitasking_ability': 0.9,
                'duration_range': (300, 600),  # 5-10 minutes
                'transition_probability': 0.1,
                'typical_activities': ['reading', 'research', 'work']
            },
            'casual': {
                'click_accuracy': 0.85,
                'scroll_speed': 0.7,
                'reading_speed': 0.8,
                'error_rate': 0.03,
                'decision_speed': 1.2,
                'multitasking_ability': 0.6,
                'duration_range': (180, 300),  # 3-5 minutes
                'transition_probability': 0.3,
                'typical_activities': ['browsing', 'social_media', 'entertainment']
            },
            'distracted': {
                'click_accuracy': 0.75,
                'scroll_speed': 1.3,
                'reading_speed': 0.6,
                'error_rate': 0.08,
                'decision_speed': 1.5,
                'multitasking_ability': 0.3,
                'duration_range': (60, 180),  # 1-3 minutes
                'transition_probability': 0.4,
                'typical_activities': ['quick_browsing', 'checking', 'scanning']
            },
            'rushed': {
                'click_accuracy': 0.80,
                'scroll_speed': 1.5,
                'reading_speed': 1.5,
                'error_rate': 0.05,
                'decision_speed': 0.5,
                'multitasking_ability': 0.7,
                'duration_range': (120, 240),  # 2-4 minutes
                'transition_probability': 0.2,
                'typical_activities': ['shopping', 'booking', 'time_sensitive']
            },
            'curious': {
                'click_accuracy': 0.88,
                'scroll_speed': 0.9,
                'reading_speed': 1.1,
                'error_rate': 0.02,
                'decision_speed': 1.0,
                'multitasking_ability': 0.8,
                'duration_range': (240, 480),  # 4-8 minutes
                'transition_probability': 0.25,
                'typical_activities': ['learning', 'exploring', 'discovery']
            }
        }
    
    def _init_emotional_states(self):
        """Initialize emotional states that influence behavior"""
        return {
            'neutral': {
                'risk_taking': 0.5,
                'patience': 0.7,
                'curiosity': 0.6,
                'impulsivity': 0.4,
                'thoroughness': 0.8
            },
            'frustrated': {
                'risk_taking': 0.7,
                'patience': 0.3,
                'curiosity': 0.4,
                'impulsivity': 0.8,
                'thoroughness': 0.5
            },
            'excited': {
                'risk_taking': 0.8,
                'patience': 0.4,
                'curiosity': 0.9,
                'impulsivity': 0.7,
                'thoroughness': 0.6
            },
            'bored': {
                'risk_taking': 0.6,
                'patience': 0.2,
                'curiosity': 0.3,
                'impulsivity': 0.9,
                'thoroughness': 0.4
            },
            'focused_emotion': {
                'risk_taking': 0.3,
                'patience': 0.9,
                'curiosity': 0.7,
                'impulsivity': 0.2,
                'thoroughness': 0.9
            }
        }
    
    def update_cognitive_state(self, external_factors=None, current_activity=None):
        """Update cognitive state based on multiple factors with machine learning"""
        factors = external_factors or {}
        current_time = time.time()
        
        # Check if we should transition based on time spent in current state
        time_in_state = current_time - self.last_state_change
        current_state_config = self.cognitive_states[self.current_state]
        avg_duration = sum(current_state_config['duration_range']) / 2
        
        if time_in_state > avg_duration * random.uniform(0.8, 1.2):
            return self._transition_to_new_state(factors, current_activity)
        
        # Otherwise, check probabilistic transition
        if random.random() < current_state_config['transition_probability']:
            return self._transition_to_new_state(factors, current_activity)
        
        # Update state parameters based on fatigue and learning
        self._update_state_parameters()
        
        return self.current_state
    
    def _transition_to_new_state(self, factors, current_activity):
        """Transition to a new cognitive state based on context"""
        possible_states = list(self.cognitive_states.keys())
        
        # Weight states based on context
        weights = self._calculate_state_weights(factors, current_activity)
        
        # Select new state
        new_state = random.choices(possible_states, weights=weights)[0]
        
        # Log the transition
        transition_data = {
            'timestamp': time.time(),
            'from_state': self.current_state,
            'to_state': new_state,
            'factors': factors,
            'activity': current_activity
        }
        self.behavior_history.append(transition_data)
        
        # Update state
        self.current_state = new_state
        self.last_state_change = time.time()
        
        # Update emotional state based on cognitive state
        self._update_emotional_state()
        
        if self.config.DEBUG_MODE:
            print(f"🧠 Cognitive state transition: {transition_data['from_state']} → {new_state}")
        
        return new_state
    
    def _calculate_state_weights(self, factors, current_activity):
        """Calculate weights for state transition based on context"""
        weights = {}
        
        for state in self.cognitive_states.keys():
            base_weight = 1.0
            
            # Time-based adjustments
            current_hour = datetime.now().hour
            if current_hour >= 22 or current_hour <= 6:  # Late night
                if state in ['distracted', 'casual']:
                    base_weight *= 1.5
                else:
                    base_weight *= 0.7
            
            # Activity-based adjustments
            if current_activity:
                state_activities = self.cognitive_states[state]['typical_activities']
                if current_activity in state_activities:
                    base_weight *= 2.0
            
            # Fatigue-based adjustments
            if self.fatigue_level > 0.7 and state == 'distracted':
                base_weight *= 1.8
            elif self.fatigue_level > 0.7 and state == 'focused':
                base_weight *= 0.3
            
            # External factors
            if factors.get('complex_task') and state == 'focused':
                base_weight *= 1.5
            if factors.get('time_pressure') and state == 'rushed':
                base_weight *= 2.0
            if factors.get('boring_content') and state == 'distracted':
                base_weight *= 1.8
            
            weights[state] = base_weight
        
        return [weights.get(state, 1.0) for state in self.cognitive_states.keys()]
    
    def _update_emotional_state(self):
        """Update emotional state based on cognitive state and history"""
        emotion_mapping = {
            'focused': 'focused_emotion',
            'casual': 'neutral',
            'distracted': 'bored',
            'rushed': 'frustrated',
            'curious': 'excited'
        }
        
        # Base emotion from cognitive state
        base_emotion = emotion_mapping.get(self.current_state, 'neutral')
        
        # Add some randomness and history consideration
        recent_emotions = [entry.get('emotion', 'neutral') 
                          for entry in self.behavior_history[-5:]]
        
        if recent_emotions:
            # Tend to continue recent emotional trends
            emotion_counts = {emotion: recent_emotions.count(emotion) 
                            for emotion in set(recent_emotions)}
            most_common_emotion = max(emotion_counts.items(), key=lambda x: x[1])[0]
            
            if random.random() < 0.3:  # 30% chance to follow trend
                base_emotion = most_common_emotion
        
        self.current_emotion = base_emotion
        
        # Update emotional parameters
        self._update_emotional_parameters()
    
    def _update_state_parameters(self):
        """Update dynamic state parameters based on fatigue and learning"""
        # Fatigue accumulation
        time_since_last_change = time.time() - self.last_state_change
        self.fatigue_level = min(1.0, self.fatigue_level + (time_since_last_change / 3600) * 0.1)
        
        # Learning effect - improve with experience
        total_operations = len(self.behavior_history)
        self.learning_rate = min(1.5, 1.0 + (total_operations / 1000) * 0.5)
        
        # Attention span fluctuation
        base_attention = self.cognitive_states[self.current_state].get('attention_span', 1.0)
        self.attention_span = base_attention * (1.0 + (random.random() - 0.5) * 0.2)
        self.attention_span *= (1.0 - self.fatigue_level * 0.3)  # Reduce with fatigue
        
        # Cognitive load adjustment
        self.cognitive_load = 1.0 + (self.fatigue_level * 0.5) - (self.learning_rate * 0.3)
    
    def _update_emotional_parameters(self):
        """Update parameters based on emotional state"""
        emotion_config = self.emotional_states[self.current_emotion]
        
        # Emotional state affects various behavioral parameters
        self.risk_taking = emotion_config['risk_taking']
        self.patience = emotion_config['patience']
        self.curiosity = emotion_config['curiosity']
        self.impulsivity = emotion_config['impulsivity']
        self.thoroughness = emotion_config['thoroughness']
    
    def get_behavioral_parameters(self):
        """Get comprehensive behavioral parameters for current state"""
        state_params = self.cognitive_states[self.current_state].copy()
        emotion_params = self.emotional_states[self.current_emotion].copy()
        
        # Combine state and emotion parameters
        combined_params = {}
        
        # Cognitive parameters with state and emotion influence
        combined_params['click_accuracy'] = state_params['click_accuracy'] * (1.0 - emotion_params['impulsivity'] * 0.2)
        combined_params['scroll_speed'] = state_params['scroll_speed'] * (1.0 + emotion_params['impulsivity'] * 0.3)
        combined_params['reading_speed'] = state_params['reading_speed'] * (1.0 + emotion_params['patience'] * 0.2)
        combined_params['error_rate'] = state_params['error_rate'] * (1.0 + emotion_params['risk_taking'] * 0.5)
        combined_params['decision_speed'] = state_params['decision_speed'] * (1.0 - emotion_params['thoroughness'] * 0.3)
        
        # Add dynamic parameters
        combined_params['attention_span'] = self.attention_span
        combined_params['fatigue_level'] = self.fatigue_level
        combined_params['learning_rate'] = self.learning_rate
        combined_params['cognitive_load'] = self.cognitive_load
        
        # Emotional parameters
        combined_params.update(emotion_params)
        
        # Add individual variation
        for key in combined_params:
            if isinstance(combined_params[key], (int, float)):
                variation = random.uniform(0.9, 1.1)
                combined_params[key] *= variation
        
        return combined_params
    
    def simulate_decision_making(self, elements, element_types, context=None):
        """Simulate human decision making process with emotional influence"""
        if not elements:
            return None
        
        context = context or {}
        behavior_params = self.get_behavioral_parameters()
        
        # Calculate weights for each element based on multiple factors
        weights = []
        for i, element in enumerate(elements):
            weight = 1.0
            
            # Element type preference based on cognitive state
            element_type = element_types[i] if i < len(element_types) else 'unknown'
            
            if self.current_state == 'focused':
                if element_type in ['button', 'link']:
                    weight *= 1.5
            elif self.current_state == 'distracted':
                if element_type in ['image', 'video']:
                    weight *= 2.0
            elif self.current_state == 'curious':
                if element_type in ['link', 'expandable']:
                    weight *= 1.8
            
            # Emotional influence
            weight *= (1.0 + self.curiosity * 0.5)  # Curiosity increases exploration
            weight *= (1.0 - self.risk_taking * 0.3)  # Risk aversion affects choice
            
            # Contextual factors
            if context.get('urgent'):
                weight *= (1.0 + self.impulsivity * 0.4)
            if context.get('important'):
                weight *= (1.0 + self.thoroughness * 0.3)
            
            # Position bias (humans prefer certain screen positions)
            try:
                location = element.location
                # Prefer center of screen
                distance_from_center = abs(location['x'] - 960) + abs(location['y'] - 540)
                position_bias = max(0.1, 1.0 - (distance_from_center / 2000))
                weight *= position_bias
            except:
                pass
            
            # Add some randomness
            weight *= random.uniform(0.8, 1.2)
            
            weights.append(weight)
        
        # Normalize weights
        total_weight = sum(weights)
        if total_weight > 0:
            normalized_weights = [w / total_weight for w in weights]
        else:
            normalized_weights = [1.0 / len(weights)] * len(weights)
        
        # Select element based on weights
        selected_index = random.choices(range(len(elements)), weights=normalized_weights)[0]
        
        # Simulate decision time based on cognitive load
        decision_time = behavior_params['decision_speed'] * random.uniform(0.5, 1.5)
        time.sleep(decision_time)
        
        return elements[selected_index]
    
    def generate_reading_pattern(self, content_length, content_complexity=1.0):
        """Generate human-like reading pattern with cognitive variations"""
        words_per_minute = {
            'focused': 250,
            'casual': 180, 
            'distracted': 120,
            'rushed': 300,
            'curious': 220
        }[self.current_state]
        
        # Adjust for content complexity and fatigue
        words_per_minute *= (1.0 / content_complexity)
        words_per_minute *= (1.0 - self.fatigue_level * 0.2)
        
        reading_time = (content_length / words_per_minute) * 60  # Convert to seconds
        reading_time *= random.uniform(0.8, 1.2)  # Individual variation
        
        # Generate detailed reading pattern with cognitive breaks
        pattern = []
        segments = max(3, int(reading_time / 15))  # Segments of ~15 seconds
        
        for segment in range(segments):
            segment_time = reading_time / segments
            
            # Add cognitive variations
            if random.random() < 0.2:  # 20% chance of re-reading
                pattern.append(('reread', segment_time * 0.3))
                segment_time *= 0.7
            
            # Main reading segment
            pattern.append(('read', segment_time))
            
            # Micro-breaks based on attention span
            if random.random() < (0.3 * (1.0 - self.attention_span)):
                break_time = random.uniform(0.5, 2.0)
                pattern.append(('pause', break_time))
            
            # Scanning breaks (quick look-aways)
            if random.random() < 0.4:
                scan_time = random.uniform(0.1, 0.5)
                pattern.append(('scan', scan_time))
        
        return pattern
    
    def simulate_typing_behavior(self, text_length, complexity=1.0):
        """Simulate human typing behavior with cognitive variations"""
        behavior_params = self.get_behavioral_parameters()
        
        typing_profile = {
            'base_speed': random.uniform(0.08, 0.15) * (1.0 / complexity),
            'error_rate': behavior_params['error_rate'],
            'pause_frequency': 0.05 + (1.0 - behavior_params['patience']) * 0.1,
            'thinking_pauses': 0.03 + (1.0 - behavior_params['thoroughness']) * 0.05,
            'correction_delay': random.uniform(0.1, 0.3)
        }
        
        # Adjust for cognitive state
        if self.current_state == 'rushed':
            typing_profile['base_speed'] *= 1.3
            typing_profile['error_rate'] *= 1.5
        elif self.current_state == 'focused':
            typing_profile['error_rate'] *= 0.7
        
        return typing_profile
    
    def get_behavioral_report(self):
        """Get comprehensive behavioral analysis report"""
        recent_transitions = self.behavior_history[-10:] if self.behavior_history else []
        
        # Calculate state distribution
        state_counts = {}
        for entry in self.behavior_history[-50:]:  # Last 50 entries
            state = entry.get('to_state', 'unknown')
            state_counts[state] = state_counts.get(state, 0) + 1
        
        total_entries = sum(state_counts.values())
        state_distribution = {state: count/total_entries for state, count in state_counts.items()} if total_entries > 0 else {}
        
        return {
            'current_cognitive_state': self.current_state,
            'current_emotional_state': self.current_emotion,
            'attention_span': round(self.attention_span, 2),
            'fatigue_level': round(self.fatigue_level, 2),
            'learning_rate': round(self.learning_rate, 2),
            'cognitive_load': round(self.cognitive_load, 2),
            'total_behavior_entries': len(self.behavior_history),
            'state_distribution': state_distribution,
            'recent_transitions': recent_transitions,
            'behavioral_parameters': self.get_behavioral_parameters()
        }
    
    def save_behavioral_data(self, filepath=None):
        """Save behavioral data for analysis and learning"""
        if not filepath:
            filepath = f"behavior_data_{int(time.time())}.json"
        
        data = {
            'timestamp': time.time(),
            'behavior_history': self.behavior_history,
            'current_state': self.current_state,
            'parameters': self.get_behavioral_parameters()
        }
        
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Failed to save behavioral data: {e}")
            return False
    
    def load_behavioral_data(self, filepath):
        """Load behavioral data to continue previous session"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.behavior_history = data.get('behavior_history', [])
            self.current_state = data.get('current_state', 'casual')
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Failed to load behavioral data: {e}")
            return False