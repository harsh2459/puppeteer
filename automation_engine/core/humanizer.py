import random
import time
import math
import json
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import settings

class Humanizer:
    def __init__(self, config):
        self.config = config
        self.movement_patterns = self._init_regional_movement_patterns()
        self.typing_profiles = self._init_regional_typing_profiles()
        self.scroll_behaviors = self._init_regional_scroll_behaviors()
        self.interaction_history = []
        self.entropy_source = random.random()
        self.regional_adapters = self._init_regional_adapters()
        self.cultural_patterns = self._load_cultural_patterns()
        
    def _init_regional_adapters(self):
        """Initialize regional behavior adapters"""
        return {
            'US': RegionalBehaviorAdapter('US'),
            'EU': RegionalBehaviorAdapter('EU'), 
            'JP': RegionalBehaviorAdapter('JP'),
            'CN': RegionalBehaviorAdapter('CN')
        }
    
    def _load_cultural_patterns(self):
        """Load comprehensive cultural interaction patterns"""
        return {
            'US': {
                'motor_skills': {'precision': 0.8, 'speed': 1.0, 'consistency': 0.7},
                'cognitive_rhythm': {'decision_speed': 1.0, 'attention_span': 0.8, 'multitasking': 0.9},
                'interaction_style': {'directness': 0.9, 'formality': 0.3, 'thoroughness': 0.6},
                'temporal_patterns': {'punctuality': 0.7, 'patience': 0.5, 'urgency': 0.8}
            },
            'EU': {
                'motor_skills': {'precision': 0.9, 'speed': 0.8, 'consistency': 0.8},
                'cognitive_rhythm': {'decision_speed': 0.7, 'attention_span': 0.9, 'multitasking': 0.6},
                'interaction_style': {'directness': 0.6, 'formality': 0.8, 'thoroughness': 0.9},
                'temporal_patterns': {'punctuality': 0.9, 'patience': 0.8, 'urgency': 0.4}
            },
            'JP': {
                'motor_skills': {'precision': 0.95, 'speed': 0.7, 'consistency': 0.9},
                'cognitive_rhythm': {'decision_speed': 0.6, 'attention_span': 0.95, 'multitasking': 0.5},
                'interaction_style': {'directness': 0.4, 'formality': 0.95, 'thoroughness': 0.95},
                'temporal_patterns': {'punctuality': 0.95, 'patience': 0.9, 'urgency': 0.3}
            },
            'CN': {
                'motor_skills': {'precision': 0.7, 'speed': 1.2, 'consistency': 0.6},
                'cognitive_rhythm': {'decision_speed': 1.1, 'attention_span': 0.6, 'multitasking': 0.8},
                'interaction_style': {'directness': 0.8, 'formality': 0.5, 'thoroughness': 0.7},
                'temporal_patterns': {'punctuality': 0.6, 'patience': 0.4, 'urgency': 0.9}
            }
        }
    
    def _init_regional_movement_patterns(self):
        """Initialize human-like mouse movement patterns with regional variations"""
        return {
            'US_natural': {
                'curve_intensity': 0.7,
                'speed_variation': 0.3,
                'overshoot_chance': 0.2,
                'micro_corrections': 0.4,
                'smoothness': 0.8,
                'regional_traits': {'assertiveness': 0.7, 'deliberation': 0.5}
            },
            'EU_precise': {
                'curve_intensity': 0.3,
                'speed_variation': 0.1,
                'overshoot_chance': 0.05,
                'micro_corrections': 0.6,
                'smoothness': 0.9,
                'regional_traits': {'assertiveness': 0.4, 'deliberation': 0.9}
            },
            'JP_methodical': {
                'curve_intensity': 0.5,
                'speed_variation': 0.2,
                'overshoot_chance': 0.1,
                'micro_corrections': 0.7,
                'smoothness': 0.85,
                'regional_traits': {'assertiveness': 0.3, 'deliberation': 0.95}
            },
            'CN_efficient': {
                'curve_intensity': 0.9,
                'speed_variation': 0.5,
                'overshoot_chance': 0.4,
                'micro_corrections': 0.2,
                'smoothness': 0.6,
                'regional_traits': {'assertiveness': 0.8, 'deliberation': 0.3}
            },
            'global_standard': {
                'curve_intensity': 0.6,
                'speed_variation': 0.3,
                'overshoot_chance': 0.2,
                'micro_corrections': 0.5,
                'smoothness': 0.75,
                'regional_traits': {'assertiveness': 0.6, 'deliberation': 0.6}
            }
        }
    
    def _init_regional_typing_profiles(self):
        """Initialize human-like typing profiles with regional variations"""
        return {
            'US_professional': {
                'wpm': 65,
                'error_rate': 0.01,
                'backspace_delay': 0.1,
                'thinking_pauses': 0.3,
                'rhythm_consistency': 0.9,
                'regional_traits': {'formality': 0.7, 'deliberation': 0.6}
            },
            'EU_accurate': {
                'wpm': 55,
                'error_rate': 0.005,
                'backspace_delay': 0.15,
                'thinking_pauses': 0.4,
                'rhythm_consistency': 0.95,
                'regional_traits': {'formality': 0.9, 'deliberation': 0.8}
            },
            'JP_precise': {
                'wpm': 45,
                'error_rate': 0.002,
                'backspace_delay': 0.2,
                'thinking_pauses': 0.5,
                'rhythm_consistency': 0.98,
                'regional_traits': {'formality': 0.95, 'deliberation': 0.9}
            },
            'CN_fast': {
                'wpm': 75,
                'error_rate': 0.02,
                'backspace_delay': 0.08,
                'thinking_pauses': 0.2,
                'rhythm_consistency': 0.8,
                'regional_traits': {'formality': 0.5, 'deliberation': 0.4}
            },
            'global_average': {
                'wpm': 45,
                'error_rate': 0.03,
                'backspace_delay': 0.2,
                'thinking_pauses': 0.5,
                'rhythm_consistency': 0.7,
                'regional_traits': {'formality': 0.6, 'deliberation': 0.6}
            }
        }
    
    def _init_regional_scroll_behaviors(self):
        """Initialize human-like scrolling behaviors with regional variations"""
        return {
            'US_balanced': {
                'scroll_speed': 1.0,
                'pause_frequency': 0.1,
                'scroll_variation': 0.2,
                'direction_changes': 0.1,
                'scroll_accuracy': 0.9,
                'regional_traits': {'thoroughness': 0.6, 'patience': 0.5}
            },
            'EU_thorough': {
                'scroll_speed': 0.8,
                'pause_frequency': 0.3,
                'scroll_variation': 0.4,
                'direction_changes': 0.3,
                'scroll_accuracy': 0.95,
                'regional_traits': {'thoroughness': 0.9, 'patience': 0.8}
            },
            'JP_methodical': {
                'scroll_speed': 0.6,
                'pause_frequency': 0.4,
                'scroll_variation': 0.3,
                'direction_changes': 0.2,
                'scroll_accuracy': 0.98,
                'regional_traits': {'thoroughness': 0.95, 'patience': 0.9}
            },
            'CN_efficient': {
                'scroll_speed': 1.2,
                'pause_frequency': 0.05,
                'scroll_variation': 0.1,
                'direction_changes': 0.05,
                'scroll_accuracy': 0.8,
                'regional_traits': {'thoroughness': 0.4, 'patience': 0.3}
            },
            'global_standard': {
                'scroll_speed': 1.0,
                'pause_frequency': 0.2,
                'scroll_variation': 0.3,
                'direction_changes': 0.2,
                'scroll_accuracy': 0.85,
                'regional_traits': {'thoroughness': 0.7, 'patience': 0.6}
            }
        }
    
    def quantum_mouse_movement(self, driver, target_element, movement_style='regional', region='US'):
        """Generate quantum-level human-like mouse movement with regional adaptation"""
        try:
            # Get regional movement pattern
            if movement_style == 'regional':
                pattern = self._get_regional_movement_pattern(region)
            else:
                pattern = self.movement_patterns.get(movement_style, self.movement_patterns['global_standard'])
            
            # Get element location
            element_location = target_element.location
            element_size = target_element.size
            
            # Calculate target coordinates (center of element)
            target_x = element_location['x'] + element_size['width'] // 2
            target_y = element_location['y'] + element_size['height'] // 2
            
            # Get current mouse position (approximate)
            current_x, current_y = self._get_estimated_mouse_position(driver)
            
            # Generate culturally-appropriate curved path
            path_points = self._generate_cultural_mouse_path(
                current_x, current_y, target_x, target_y, pattern, region
            )
            
            # Execute movement through path points with regional timing
            actions = ActionChains(driver)
            actions.move_by_offset(0, 0)  # Start from current position
            
            for point in path_points:
                actions.move_by_offset(point['dx'], point['dy'])
                actions.pause(point['pause'])
            
            # Regional overshoot and correction patterns
            cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
            overshoot_probability = pattern['overshoot_chance'] * cultural_traits['motor_skills']['precision']
            
            if random.random() < overshoot_probability:
                # Cultural overshoot patterns
                overshoot_x = random.randint(-10, 10) * (1.0 - cultural_traits['motor_skills']['precision'])
                overshoot_y = random.randint(-10, 10) * (1.0 - cultural_traits['motor_skills']['precision'])
                actions.move_by_offset(overshoot_x, overshoot_y)
                actions.pause(0.05)
                
                # Cultural correction speed
                correction_delay = 0.05 * cultural_traits['temporal_patterns']['patience']
                actions.move_by_offset(-overshoot_x, -overshoot_y)
                actions.pause(correction_delay)
            
            # Cultural micro-corrections
            micro_correction_prob = pattern['micro_corrections'] * cultural_traits['motor_skills']['consistency']
            if random.random() < micro_correction_prob:
                correction_count = random.randint(1, 3)
                for _ in range(correction_count):
                    correction_x = random.randint(-3, 3) * cultural_traits['motor_skills']['precision']
                    correction_y = random.randint(-3, 3) * cultural_traits['motor_skills']['precision']
                    actions.move_by_offset(correction_x, correction_y)
                    actions.pause(0.02 * cultural_traits['temporal_patterns']['patience'])
                    actions.move_by_offset(-correction_x, -correction_y)
            
            actions.click()
            actions.perform()
            
            # Record interaction with cultural context
            self._record_cultural_interaction('mouse_movement', {
                'region': region,
                'style': movement_style,
                'distance': math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2),
                'path_points': len(path_points),
                'duration': sum(p['pause'] for p in path_points),
                'cultural_traits': cultural_traits['motor_skills']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Regional mouse movement failed: {e}")
            return False
    
    def _get_regional_movement_pattern(self, region):
        """Get movement pattern appropriate for region"""
        regional_patterns = {
            'US': 'US_natural',
            'EU': 'EU_precise', 
            'JP': 'JP_methodical',
            'CN': 'CN_efficient'
        }
        pattern_key = regional_patterns.get(region, 'global_standard')
        return self.movement_patterns.get(pattern_key, self.movement_patterns['global_standard'])
    
    def _generate_cultural_mouse_path(self, start_x, start_y, end_x, end_y, pattern, region):
        """Generate mouse movement path with cultural characteristics"""
        path_points = []
        total_distance = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
        
        # Cultural path complexity
        cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
        base_points = max(5, int(total_distance * pattern['smoothness'] / 50))
        cultural_complexity = cultural_traits['motor_skills']['precision'] * cultural_traits['cognitive_rhythm']['attention_span']
        num_points = int(base_points * (1.0 + cultural_complexity * 0.5))
        
        # Cultural control points for Bezier curve
        cultural_assertiveness = cultural_traits['interaction_style']['directness']
        control1_x = start_x + (end_x - start_x) * 0.3 + random.randint(-50, 50) * pattern['curve_intensity'] * (1.0 - cultural_assertiveness)
        control1_y = start_y + (end_y - start_y) * 0.3 + random.randint(-50, 50) * pattern['curve_intensity'] * (1.0 - cultural_assertiveness)
        control2_x = start_x + (end_x - start_x) * 0.7 + random.randint(-50, 50) * pattern['curve_intensity'] * (1.0 - cultural_assertiveness)
        control2_y = start_y + (end_y - start_y) * 0.7 + random.randint(-50, 50) * pattern['curve_intensity'] * (1.0 - cultural_assertiveness)
        
        for i in range(1, num_points + 1):
            t = i / num_points
            
            # Cubic Bezier curve calculation
            point_x = self._cubic_bezier(start_x, control1_x, control2_x, end_x, t)
            point_y = self._cubic_bezier(start_y, control1_y, control2_y, end_y, t)
            
            if i == 1:
                dx = point_x - start_x
                dy = point_y - start_y
            else:
                prev_point = path_points[-1]
                dx = point_x - (start_x + prev_point['cumulative_dx'])
                dy = point_y - (start_y + prev_point['cumulative_dy'])
            
            # Cultural speed variations
            cultural_speed = cultural_traits['motor_skills']['speed']
            base_pause = 0.01
            speed_variation = random.uniform(0.7, 1.3) * (1.0 / pattern['smoothness']) * cultural_speed
            pause = base_pause * speed_variation
            
            # Cultural deliberation affects pause duration
            pause *= cultural_traits['temporal_patterns']['patience']
            
            path_points.append({
                'dx': int(dx),
                'dy': int(dy),
                'pause': pause,
                'cumulative_dx': (path_points[-1]['cumulative_dx'] + dx) if path_points else dx,
                'cumulative_dy': (path_points[-1]['cumulative_dy'] + dy) if path_points else dy
            })
        
        return path_points
    
    def _cubic_bezier(self, p0, p1, p2, p3, t):
        """Calculate cubic Bezier curve point"""
        return (1-t)**3 * p0 + 3*(1-t)**2*t * p1 + 3*(1-t)*t**2 * p2 + t**3 * p3
    
    def quantum_type(self, element, text, typing_profile='regional', region='US'):
        """Generate quantum-level human-like typing with regional patterns"""
        try:
            # Get regional typing profile
            if typing_profile == 'regional':
                profile = self._get_regional_typing_profile(region)
            else:
                profile = self.typing_profiles.get(typing_profile, self.typing_profiles['global_average'])
            
            cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
            
            # Calculate typing speed with cultural adjustments
            base_wpm = profile['wpm'] * cultural_traits['motor_skills']['speed']
            chars_per_second = base_wpm / 60 * 5  # Average word length = 5 chars
            base_delay = 1.0 / chars_per_second
            
            # Focus the element with cultural timing
            element.click()
            cultural_focus_delay = 0.1 * cultural_traits['temporal_patterns']['patience']
            time.sleep(cultural_focus_delay)
            
            # Clear existing text if any
            element.clear()
            cultural_clear_delay = 0.2 * cultural_traits['temporal_patterns']['patience']
            time.sleep(cultural_clear_delay)
            
            actions = ActionChains(element._parent)
            
            for i, char in enumerate(text):
                # Type the character
                actions.send_keys(char)
                
                # Cultural delay variations
                rhythm_consistency = profile['rhythm_consistency'] * cultural_traits['motor_skills']['consistency']
                delay_variation = random.uniform(0.7, 1.3) * (1.0 / rhythm_consistency)
                char_delay = base_delay * delay_variation
                
                # Cultural thinking pauses between words
                if char == ' ' and random.random() < profile['thinking_pauses']:
                    thinking_multiplier = cultural_traits['cognitive_rhythm']['decision_speed']
                    breath_pause = random.uniform(0.1, 0.5) * thinking_multiplier
                    actions.pause(breath_pause)
                
                actions.pause(char_delay)
                
                # Cultural error patterns
                cultural_error_rate = profile['error_rate'] * (1.0 - cultural_traits['motor_skills']['precision'])
                if random.random() < cultural_error_rate:
                    # Type wrong character with cultural keyboard patterns
                    wrong_char = self._get_cultural_mistype(char, region)
                    actions.send_keys(wrong_char)
                    actions.pause(0.05)
                    
                    # Cultural backspace delay
                    backspace_delay = profile['backspace_delay'] * cultural_traits['temporal_patterns']['patience']
                    actions.send_keys(Keys.BACKSPACE)
                    actions.pause(backspace_delay)
                    
                    # Type correct character
                    actions.send_keys(char)
                    actions.pause(char_delay)
            
            actions.perform()
            
            # Record interaction with cultural context
            self._record_cultural_interaction('typing', {
                'region': region,
                'profile': typing_profile,
                'text_length': len(text),
                'estimated_duration': len(text) * base_delay,
                'error_simulated': cultural_error_rate > 0,
                'cultural_traits': cultural_traits['motor_skills']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Regional typing simulation failed: {e}")
            return False
    
    def _get_regional_typing_profile(self, region):
        """Get typing profile appropriate for region"""
        regional_profiles = {
            'US': 'US_professional',
            'EU': 'EU_accurate',
            'JP': 'JP_precise', 
            'CN': 'CN_fast'
        }
        profile_key = regional_profiles.get(region, 'global_average')
        return self.typing_profiles.get(profile_key, self.typing_profiles['global_average'])
    
    def _get_cultural_mistype(self, char, region):
        """Get realistic mistype based on cultural keyboard usage"""
        # Different cultures have different common mistypes
        cultural_mistypes = {
            'US': {
                'a': 's', 's': 'a', 'd': 'f', 'f': 'd', 'g': 'h', 'h': 'g',
                'j': 'k', 'k': 'j', 'l': 'k', 'q': 'w', 'w': 'q', 'e': 'r'
            },
            'EU': {
                'a': 'q', 'q': 'a', 'z': 'y', 'y': 'z', 'm': ',', ',': 'm',
                ';': ':', ':': ';', "'": '"', '"': "'", '\\': '|', '|': '\\'
            },
            'JP': {
                'a': 'q', 'q': 'a', 'z': 'y', 'y': 'z', 'm': ',', ',': 'm',
                ';': ':', ':': ';', '[': '{', '{': '[', ']': '}', '}': ']'
            },
            'CN': {
                'a': 's', 's': 'a', 'd': 'f', 'f': 'd', 'g': 'h', 'h': 'g',
                'j': 'k', 'k': 'j', 'l': 'k', 'q': 'w', 'w': 'q', 'e': 'r'
            }
        }
        
        region_mistypes = cultural_mistypes.get(region, cultural_mistypes['US'])
        lower_char = char.lower()
        
        if lower_char in region_mistypes:
            return region_mistypes[lower_char]
        return char  # Fallback to same char if no cultural data
    
    def quantum_scroll(self, driver, scroll_behavior='regional', scroll_count=None, region='US'):
        """Generate quantum-level human-like scrolling with regional behavior"""
        try:
            # Get regional scroll behavior
            if scroll_behavior == 'regional':
                behavior = self._get_regional_scroll_behavior(region)
            else:
                behavior = self.scroll_behaviors.get(scroll_behavior, self.scroll_behaviors['global_standard'])
            
            cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
            
            if scroll_count is None:
                # Cultural scroll count preferences
                base_count = random.randint(behavior['min_scrolls'], behavior['max_scrolls'])
                cultural_thoroughness = cultural_traits['interaction_style']['thoroughness']
                scroll_count = int(base_count * (1.0 + cultural_thoroughness * 0.5))
            
            for scroll_index in range(scroll_count):
                # Cultural scroll characteristics
                cultural_speed = cultural_traits['motor_skills']['speed']
                scroll_variation = behavior['scroll_variation'] * (1.0 - cultural_traits['motor_skills']['consistency'])
                
                scroll_amount = random.randint(
                    behavior['min_distance'], 
                    behavior['max_distance']
                ) * cultural_speed
                
                scroll_amount *= random.uniform(1 - scroll_variation, 1 + scroll_variation)
                
                # Cultural direction preferences
                cultural_patience = cultural_traits['temporal_patterns']['patience']
                up_scroll_bias = behavior['direction_changes'] * (1.0 - cultural_patience)
                scroll_direction = 1 if random.random() > up_scroll_bias else -1
                
                # Execute scroll
                driver.execute_script(f"window.scrollBy(0, {scroll_direction * scroll_amount});")
                
                # Cultural pause patterns
                if random.random() < behavior['pause_frequency']:
                    pause_time = random.uniform(behavior['min_pause'], behavior['max_pause'])
                    pause_time *= cultural_traits['temporal_patterns']['patience']
                    time.sleep(pause_time)
                else:
                    quick_pause = random.uniform(0.1, 0.3) * cultural_speed
                    time.sleep(quick_pause)
                
                # Cultural direction changes
                if random.random() < behavior['direction_changes']:
                    cultural_uncertainty = 1.0 - cultural_traits['cognitive_rhythm']['attention_span']
                    if random.random() < cultural_uncertainty:
                        quick_back_scroll = -scroll_amount * 0.3
                        driver.execute_script(f"window.scrollBy(0, {quick_back_scroll});")
                        re_read_pause = 0.2 * cultural_traits['temporal_patterns']['patience']
                        time.sleep(re_read_pause)
                        driver.execute_script(f"window.scrollBy(0, {-quick_back_scroll});")
            
            # Record interaction with cultural context
            self._record_cultural_interaction('scrolling', {
                'region': region,
                'behavior': scroll_behavior,
                'scroll_count': scroll_count,
                'cultural_traits': cultural_traits['motor_skills']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Regional scroll simulation failed: {e}")
            return False
    
    def _get_regional_scroll_behavior(self, region):
        """Get scroll behavior appropriate for region"""
        regional_behaviors = {
            'US': 'US_balanced',
            'EU': 'EU_thorough',
            'JP': 'JP_methodical',
            'CN': 'CN_efficient'
        }
        behavior_key = regional_behaviors.get(region, 'global_standard')
        return self.scroll_behaviors.get(behavior_key, self.scroll_behaviors['global_standard'])
    
    def quantum_delay(self, base_delay=1.0, variation=0.3, purpose='general', region='US'):
        """Generate human-like delays with regional and purpose-specific variations"""
        cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
        
        # Regional timing adjustments
        regional_timing_factor = cultural_traits['temporal_patterns']['patience']
        
        # Purpose-specific variations with cultural context
        delay_variations = {
            'thinking': (1.5, 0.4, cultural_traits['cognitive_rhythm']['decision_speed']),
            'reading': (2.0, 0.5, cultural_traits['cognitive_rhythm']['attention_span']),
            'decision': (1.2, 0.3, cultural_traits['cognitive_rhythm']['decision_speed']),
            'reaction': (0.5, 0.2, cultural_traits['motor_skills']['speed']),
            'general': (1.0, 0.3, 1.0)
        }
        
        base, var, purpose_factor = delay_variations.get(purpose, delay_variations['general'])
        
        # Calculate delay with cultural and purpose adjustments
        actual_delay = base_delay * base * regional_timing_factor * purpose_factor
        actual_delay *= random.uniform(1 - variation, 1 + variation)
        
        # Cultural micro-variations
        micro_variations = [random.uniform(0.95, 1.05) for _ in range(3)]
        cultural_consistency = cultural_traits['motor_skills']['consistency']
        consistency_factor = 1.0 + (cultural_consistency - 0.5) * 0.2
        final_delay = actual_delay * (sum(micro_variations) / len(micro_variations)) * consistency_factor
        
        time.sleep(final_delay)
        
        self._record_cultural_interaction('delay', {
            'region': region,
            'purpose': purpose,
            'requested_delay': base_delay,
            'actual_delay': final_delay,
            'cultural_timing': regional_timing_factor
        })
        
        return final_delay
    
    def simulate_cultural_reading_behavior(self, driver, content_complexity=1.0, region='US'):
        """Simulate human reading behavior with cultural variations"""
        try:
            cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
            
            # Estimate content length from page
            content_length = driver.execute_script("""
                return document.body.innerText.length;
            """)
            
            # Cultural reading speed variations
            base_reading_speed = 250  # words per minute (average)
            cultural_reading_speed = base_reading_speed * cultural_traits['cognitive_rhythm']['attention_span']
            
            # Adjust for content complexity and cultural education level
            complexity_factor = 1.0 / content_complexity
            cultural_education_bias = 1.0 + (cultural_traits['interaction_style']['formality'] * 0.2)
            
            words = content_length / 5  # Rough word estimate
            reading_time = (words / cultural_reading_speed) * 60 * complexity_factor * cultural_education_bias
            
            # Cultural reading pattern variations
            cultural_thoroughness = cultural_traits['interaction_style']['thoroughness']
            total_scrolls = max(3, int(reading_time / 10 * (1.0 + cultural_thoroughness)))
            
            for i in range(total_scrolls):
                # Cultural scroll distance
                scroll_intensity = cultural_traits['motor_skills']['speed'] * cultural_thoroughness
                scroll_amount = random.randint(100, 300) * scroll_intensity
                driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                
                # Cultural reading pause
                reading_pace = reading_time / total_scrolls
                cultural_pause_variation = random.uniform(0.8, 1.2) * cultural_traits['temporal_patterns']['patience']
                actual_pause = reading_pace * cultural_pause_variation
                time.sleep(actual_pause)
                
                # Cultural re-reading patterns (more thorough cultures re-read more)
                if random.random() < cultural_thoroughness * 0.3:
                    driver.execute_script(f"window.scrollBy(0, {-scroll_amount // 2});")
                    re_read_pause = actual_pause * 0.3 * cultural_traits['cognitive_rhythm']['attention_span']
                    time.sleep(re_read_pause)
                    driver.execute_script(f"window.scrollBy(0, {scroll_amount // 2});")
            
            self._record_cultural_interaction('reading', {
                'region': region,
                'estimated_content_length': content_length,
                'reading_time': reading_time,
                'scroll_count': total_scrolls,
                'cultural_attention': cultural_traits['cognitive_rhythm']['attention_span']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Cultural reading simulation failed: {e}")
            return False
    
    def simulate_cultural_decision_making(self, driver, elements, context=None, region='US'):
        """Simulate cultural decision-making processes"""
        try:
            cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
            
            # Cultural decision time
            base_decision_time = 1.0
            cultural_deliberation = cultural_traits['cognitive_rhythm']['decision_speed']
            decision_time = base_decision_time * cultural_deliberation
            
            # Cultural decision patterns
            if cultural_traits['interaction_style']['directness'] > 0.7:
                # Direct cultures make quicker decisions
                decision_time *= 0.7
            else:
                # Indirect cultures take more time
                decision_time *= 1.3
            
            # Simulate cultural decision process
            decision_steps = random.randint(2, 5)
            cultural_attention = cultural_traits['cognitive_rhythm']['attention_span']
            
            for step in range(decision_steps):
                # Cultural "thinking" movements
                if random.random() < cultural_attention:
                    micro_move = random.randint(-10, 10)
                    driver.execute_script(f"window.scrollBy(0, {micro_move});")
                    cultural_reflection_pause = 0.05 * cultural_traits['temporal_patterns']['patience']
                    time.sleep(cultural_reflection_pause)
                    driver.execute_script(f"window.scrollBy(0, {-micro_move});")
                
                # Cultural decision step pause
                step_pause = decision_time / decision_steps
                cultural_step_variation = random.uniform(0.9, 1.1) * cultural_deliberation
                time.sleep(step_pause * cultural_step_variation)
            
            self._record_cultural_interaction('decision_making', {
                'region': region,
                'decision_time': decision_time,
                'decision_steps': decision_steps,
                'cultural_deliberation': cultural_deliberation
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Cultural decision simulation failed: {e}")
            return False
    
    def _get_estimated_mouse_position(self, driver):
        """Estimate current mouse position (approximate)"""
        viewport_width = driver.execute_script("return window.innerWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        
        # Assume mouse is roughly in the center of the viewport
        return viewport_width // 2, viewport_height // 2
    
    def _record_cultural_interaction(self, interaction_type, details):
        """Record humanizer interactions with cultural context"""
        interaction_record = {
            'timestamp': time.time(),
            'type': interaction_type,
            'details': details,
            'entropy': self.entropy_source,
            'cultural_signature': self._generate_cultural_signature(details.get('region', 'US'))
        }
        
        self.interaction_history.append(interaction_record)
        
        # Keep only recent history
        if len(self.interaction_history) > 1000:
            self.interaction_history = self.interaction_history[-500:]
    
    def _generate_cultural_signature(self, region):
        """Generate a signature representing cultural behavior patterns"""
        cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
        
        signature = {
            'motor_precision': cultural_traits['motor_skills']['precision'],
            'cognitive_speed': cultural_traits['cognitive_rhythm']['decision_speed'],
            'interaction_formality': cultural_traits['interaction_style']['formality'],
            'temporal_patience': cultural_traits['temporal_patterns']['patience']
        }
        
        return signature
    
    def get_cultural_behavior_report(self, region='US'):
        """Get comprehensive cultural behavior analysis report"""
        recent_interactions = [i for i in self.interaction_history[-20:] if i['details'].get('region') == region]
        
        # Count interaction types by region
        type_counts = {}
        cultural_patterns = {}
        
        for interaction in self.interaction_history:
            if interaction['details'].get('region') == region:
                itype = interaction['type']
                type_counts[itype] = type_counts.get(itype, 0) + 1
                
                # Analyze cultural patterns
                cultural_sig = interaction.get('cultural_signature', {})
                for trait, value in cultural_sig.items():
                    if trait not in cultural_patterns:
                        cultural_patterns[trait] = []
                    cultural_patterns[trait].append(value)
        
        # Calculate average cultural traits
        avg_cultural_traits = {}
        for trait, values in cultural_patterns.items():
            avg_cultural_traits[trait] = sum(values) / len(values) if values else 0
        
        return {
            'region': region,
            'total_interactions': len([i for i in self.interaction_history if i['details'].get('region') == region]),
            'interaction_types': type_counts,
            'recent_interactions': recent_interactions,
            'average_cultural_traits': avg_cultural_traits,
            'cultural_consistency_score': self._calculate_cultural_consistency(region),
            'behavioral_adaptation_level': self._calculate_adaptation_level(region)
        }
    
    def _calculate_cultural_consistency(self, region):
        """Calculate how consistent our behavior is with cultural norms"""
        if not self.interaction_history:
            return 0.0
        
        regional_interactions = [i for i in self.interaction_history if i['details'].get('region') == region]
        
        if not regional_interactions:
            return 0.0
        
        consistency_scores = []
        cultural_traits = self.cultural_patterns.get(region, self.cultural_patterns['US'])
        
        for interaction in regional_interactions[-10:]:  # Last 10 interactions
            cultural_sig = interaction.get('cultural_signature', {})
            if not cultural_sig:
                continue
            
            score = 0.0
            traits_matched = 0
            
            for trait, expected_value in cultural_traits.items():
                if trait in cultural_sig:
                    actual_value = cultural_sig[trait]
                    # Score based on how close we are to cultural norm
                    trait_score = 1.0 - abs(actual_value - expected_value)
                    score += max(0, trait_score)
                    traits_matched += 1
            
            if traits_matched > 0:
                consistency_scores.append(score / traits_matched)
        
        return sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0
    
    def _calculate_adaptation_level(self, region):
        """Calculate how well we've adapted to regional behavior patterns"""
        regional_interactions = [i for i in self.interaction_history if i['details'].get('region') == region]
        
        if len(regional_interactions) < 5:
            return 0.0  # Not enough data
        
        # Adaptation improves with more regional experience
        base_adaptation = min(1.0, len(regional_interactions) / 50)  # Cap at 50 interactions
        
        # Consistency bonus
        consistency_bonus = self._calculate_cultural_consistency(region) * 0.3
        
        return min(1.0, base_adaptation + consistency_bonus)

class RegionalBehaviorAdapter:
    """Adapter for regional behavior patterns"""
    
    def __init__(self, region):
        self.region = region
        self.regional_profiles = self._load_regional_profiles()
    
    def _load_regional_profiles(self):
        """Load detailed regional behavior profiles"""
        return {
            'US': {
                'interaction_style': 'assertive',
                'attention_pattern': 'focused_scanning',
                'decision_making': 'quick_decisions',
                'error_tolerance': 'medium',
                'learning_style': 'experimental'
            },
            'EU': {
                'interaction_style': 'deliberate',
                'attention_pattern': 'thorough_reading',
                'decision_making': 'considered_decisions',
                'error_tolerance': 'low',
                'learning_style': 'analytical'
            },
            'JP': {
                'interaction_style': 'precise',
                'attention_pattern': 'methodical_review',
                'decision_making': 'consensus_building',
                'error_tolerance': 'very_low',
                'learning_style': 'perfectionist'
            },
            'CN': {
                'interaction_style': 'efficient',
                'attention_pattern': 'rapid_scanning',
                'decision_making': 'pragmatic_decisions',
                'error_tolerance': 'high',
                'learning_style': 'practical'
            }
        }
    
    def get_regional_profile(self):
        """Get the regional behavior profile"""
        return self.regional_profiles.get(self.region, self.regional_profiles['US'])

# Utility functions for backward compatibility
def quantum_mouse_movement(driver, element, style='natural'):
    """Standalone function for mouse movement"""
    humanizer = Humanizer(settings.current_config)
    return humanizer.quantum_mouse_movement(driver, element, style)

def quantum_type(element, text, profile='average'):
    """Standalone function for typing"""
    humanizer = Humanizer(settings.current_config)
    return humanizer.quantum_type(element, text, profile)

def quantum_scroll(driver, behavior='smooth', count=None):
    """Standalone function for scrolling"""
    humanizer = Humanizer(settings.current_config)
    return humanizer.quantum_scroll(driver, behavior, count)

def quantum_delay(base_delay=1.0, variation=0.3, purpose='general'):
    """Standalone function for delays"""
    humanizer = Humanizer(settings.current_config)
    return humanizer.quantum_delay(base_delay, variation, purpose)

# Enhanced factory function with regional support
def create_regional_humanizer(config=None, region='US'):
    """Factory function for regional humanizer creation"""
    from config import settings
    config = config or settings.current_config
    humanizer = Humanizer(config)
    
    # Pre-load regional patterns
    humanizer._get_regional_movement_pattern(region)
    humanizer._get_regional_typing_profile(region)
    humanizer._get_regional_scroll_behavior(region)
    
    return humanizer

# Cultural analysis utilities
def analyze_cultural_behavior(humanizer, region='US'):
    """Analyze cultural behavior patterns"""
    return humanizer.get_cultural_behavior_report(region)

def get_supported_cultures():
    """Get list of supported cultures/regions"""
    return ['US', 'EU', 'JP', 'CN']

def get_cultural_characteristics(region):
    """Get characteristics of a specific culture"""
    cultural_descriptions = {
        'US': {
            'description': 'Direct, efficient, moderately formal',
            'strengths': ['Quick decision making', 'Adaptability', 'Pragmatism'],
            'behavioral_traits': ['Assertive mouse movements', 'Moderate typing speed', 'Balanced scrolling']
        },
        'EU': {
            'description': 'Precise, thorough, formal',
            'strengths': ['Attention to detail', 'Methodical approach', 'High accuracy'],
            'behavioral_traits': ['Precise mouse movements', 'Slower, accurate typing', 'Thorough scrolling']
        },
        'JP': {
            'description': 'Methodical, precise, highly formal',
            'strengths': ['Extreme precision', 'Patience', 'Perfectionism'],
            'behavioral_traits': ['Very precise mouse movements', 'Slow, perfect typing', 'Methodical scrolling']
        },
        'CN': {
            'description': 'Efficient, pragmatic, moderately formal',
            'strengths': ['Speed', 'Efficiency', 'Pragmatism'],
            'behavioral_traits': ['Efficient mouse movements', 'Fast typing with some errors', 'Rapid scrolling']
        }
    }
    return cultural_descriptions.get(region, cultural_descriptions['US'])