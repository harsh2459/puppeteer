import random
import time
import math
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import settings

class Humanizer:
    def __init__(self, config):
        self.config = config
        self.movement_patterns = self._init_movement_patterns()
        self.typing_profiles = self._init_typing_profiles()
        self.scroll_behaviors = self._init_scroll_behaviors()
        self.interaction_history = []
        self.entropy_source = random.random()
        
    def _init_movement_patterns(self):
        """Initialize human-like mouse movement patterns"""
        return {
            'natural': {
                'curve_intensity': 0.7,
                'speed_variation': 0.3,
                'overshoot_chance': 0.2,
                'micro_corrections': 0.4,
                'smoothness': 0.8
            },
            'precise': {
                'curve_intensity': 0.3,
                'speed_variation': 0.1,
                'overshoot_chance': 0.05,
                'micro_corrections': 0.6,
                'smoothness': 0.9
            },
            'casual': {
                'curve_intensity': 0.9,
                'speed_variation': 0.5,
                'overshoot_chance': 0.4,
                'micro_corrections': 0.2,
                'smoothness': 0.6
            },
            'erratic': {
                'curve_intensity': 1.2,
                'speed_variation': 0.8,
                'overshoot_chance': 0.6,
                'micro_corrections': 0.8,
                'smoothness': 0.4
            },
            'analytical': {
                'curve_intensity': 0.5,
                'speed_variation': 0.2,
                'overshoot_chance': 0.1,
                'micro_corrections': 0.7,
                'smoothness': 0.85
            }
        }
    
    def _init_typing_profiles(self):
        """Initialize human-like typing profiles"""
        return {
            'professional': {
                'wpm': 65,
                'error_rate': 0.01,
                'backspace_delay': 0.1,
                'thinking_pauses': 0.3,
                'rhythm_consistency': 0.9
            },
            'average': {
                'wpm': 45,
                'error_rate': 0.03,
                'backspace_delay': 0.2,
                'thinking_pauses': 0.5,
                'rhythm_consistency': 0.7
            },
            'hunter_peck': {
                'wpm': 25,
                'error_rate': 0.08,
                'backspace_delay': 0.4,
                'thinking_pauses': 0.8,
                'rhythm_consistency': 0.4
            },
            'fast_typer': {
                'wpm': 90,
                'error_rate': 0.02,
                'backspace_delay': 0.05,
                'thinking_pauses': 0.1,
                'rhythm_consistency': 0.95
            },
            'casual': {
                'wpm': 35,
                'error_rate': 0.05,
                'backspace_delay': 0.3,
                'thinking_pauses': 0.6,
                'rhythm_consistency': 0.6
            }
        }
    
    def _init_scroll_behaviors(self):
        """Initialize human-like scrolling behaviors"""
        return {
            'smooth': {
                'scroll_speed': 1.0,
                'pause_frequency': 0.1,
                'scroll_variation': 0.2,
                'direction_changes': 0.1,
                'scroll_accuracy': 0.9
            },
            'intermittent': {
                'scroll_speed': 0.8,
                'pause_frequency': 0.3,
                'scroll_variation': 0.4,
                'direction_changes': 0.3,
                'scroll_accuracy': 0.7
            },
            'rapid': {
                'scroll_speed': 1.5,
                'pause_frequency': 0.05,
                'scroll_variation': 0.1,
                'direction_changes': 0.05,
                'scroll_accuracy': 0.8
            },
            'methodical': {
                'scroll_speed': 0.6,
                'pause_frequency': 0.4,
                'scroll_variation': 0.3,
                'direction_changes': 0.2,
                'scroll_accuracy': 0.95
            },
            'random': {
                'scroll_speed': 1.2,
                'pause_frequency': 0.6,
                'scroll_variation': 0.8,
                'direction_changes': 0.5,
                'scroll_accuracy': 0.6
            }
        }
    
    def quantum_mouse_movement(self, driver, target_element, movement_style='natural'):
        """Generate quantum-level human-like mouse movement"""
        try:
            pattern = self.movement_patterns.get(movement_style, self.movement_patterns['natural'])
            
            # Get element location
            element_location = target_element.location
            element_size = target_element.size
            
            # Calculate target coordinates (center of element)
            target_x = element_location['x'] + element_size['width'] // 2
            target_y = element_location['y'] + element_size['height'] // 2
            
            # Get current mouse position (approximate)
            current_x, current_y = self._get_estimated_mouse_position(driver)
            
            # Generate curved path
            path_points = self._generate_curved_path(
                current_x, current_y, target_x, target_y, pattern
            )
            
            # Execute movement through path points
            actions = ActionChains(driver)
            actions.move_by_offset(0, 0)  # Start from current position
            
            for point in path_points:
                actions.move_by_offset(point['dx'], point['dy'])
                actions.pause(point['pause'])
            
            # Final approach with potential overshoot and correction
            if random.random() < pattern['overshoot_chance']:
                # Overshoot slightly
                overshoot_x = random.randint(-10, 10)
                overshoot_y = random.randint(-10, 10)
                actions.move_by_offset(overshoot_x, overshoot_y)
                actions.pause(0.05)
                
                # Correct back to target
                actions.move_by_offset(-overshoot_x, -overshoot_y)
            
            # Micro-corrections
            if random.random() < pattern['micro_corrections']:
                for _ in range(random.randint(1, 3)):
                    correction_x = random.randint(-3, 3)
                    correction_y = random.randint(-3, 3)
                    actions.move_by_offset(correction_x, correction_y)
                    actions.pause(0.02)
                    actions.move_by_offset(-correction_x, -correction_y)
            
            actions.click()
            actions.perform()
            
            # Record interaction
            self._record_interaction('mouse_movement', {
                'style': movement_style,
                'distance': math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2),
                'path_points': len(path_points),
                'duration': sum(p['pause'] for p in path_points)
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Mouse movement failed: {e}")
            return False
    
    def _get_estimated_mouse_position(self, driver):
        """Estimate current mouse position (approximate)"""
        # This is an approximation - real mouse tracking would be more complex
        viewport_width = driver.execute_script("return window.innerWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        
        # Assume mouse is roughly in the center of the viewport
        return viewport_width // 2, viewport_height // 2
    
    def _generate_curved_path(self, start_x, start_y, end_x, end_y, pattern):
        """Generate curved mouse movement path"""
        path_points = []
        total_distance = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)
        
        # Number of points based on distance and smoothness
        num_points = max(5, int(total_distance * pattern['smoothness'] / 50))
        
        # Control points for Bezier curve
        control1_x = start_x + (end_x - start_x) * 0.3 + random.randint(-50, 50) * pattern['curve_intensity']
        control1_y = start_y + (end_y - start_y) * 0.3 + random.randint(-50, 50) * pattern['curve_intensity']
        control2_x = start_x + (end_x - start_x) * 0.7 + random.randint(-50, 50) * pattern['curve_intensity']
        control2_y = start_y + (end_y - start_y) * 0.7 + random.randint(-50, 50) * pattern['curve_intensity']
        
        for i in range(1, num_points + 1):
            t = i / num_points
            
            # Cubic Bezier curve calculation
            point_x = self._cubic_bezier(start_x, control1_x, control2_x, end_x, t)
            point_y = self._cubic_bezier(start_y, control1_y, control2_y, end_y, t)
            
            if i == 1:
                # First point relative to start
                dx = point_x - start_x
                dy = point_y - start_y
            else:
                # Subsequent points relative to previous
                prev_point = path_points[-1]
                dx = point_x - (start_x + prev_point['cumulative_dx'])
                dy = point_y - (start_y + prev_point['cumulative_dy'])
            
            # Speed variation
            base_pause = 0.01
            speed_variation = random.uniform(1 - pattern['speed_variation'], 1 + pattern['speed_variation'])
            pause = base_pause * speed_variation
            
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
    
    def quantum_type(self, element, text, typing_profile='average'):
        """Generate quantum-level human-like typing"""
        try:
            profile = self.typing_profiles.get(typing_profile, self.typing_profiles['average'])
            
            # Calculate typing speed in seconds per character
            chars_per_second = profile['wpm'] / 60 * 5  # Average word length = 5 chars
            base_delay = 1.0 / chars_per_second
            
            # Focus the element
            element.click()
            time.sleep(0.1)
            
            # Clear existing text if any
            element.clear()
            time.sleep(0.2)
            
            actions = ActionChains(element._parent)
            
            for i, char in enumerate(text):
                # Type the character
                actions.send_keys(char)
                
                # Calculate delay with variations
                delay_variation = random.uniform(0.7, 1.3) * (1.0 / profile['rhythm_consistency'])
                char_delay = base_delay * delay_variation
                
                # Thinking pauses between words
                if char == ' ' and random.random() < profile['thinking_pauses']:
                    thinking_pause = random.uniform(0.1, 0.5)
                    actions.pause(thinking_pause)
                
                actions.pause(char_delay)
                
                # Simulate typing errors and corrections
                if random.random() < profile['error_rate']:
                    # Type wrong character
                    wrong_char = self._get_adjacent_key(char)
                    actions.send_keys(wrong_char)
                    actions.pause(0.05)
                    
                    # Backspace
                    actions.send_keys(Keys.BACKSPACE)
                    actions.pause(profile['backspace_delay'])
                    
                    # Type correct character
                    actions.send_keys(char)
                    actions.pause(char_delay)
            
            actions.perform()
            
            # Record interaction
            self._record_interaction('typing', {
                'profile': typing_profile,
                'text_length': len(text),
                'estimated_duration': len(text) * base_delay,
                'error_simulated': profile['error_rate'] > 0
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Typing simulation failed: {e}")
            return False
    
    def _get_adjacent_key(self, char):
        """Get adjacent keyboard key for error simulation"""
        keyboard_adjacency = {
            'a': 's', 's': 'a', 'd': 'f', 'f': 'd', 'g': 'h', 'h': 'g',
            'j': 'k', 'k': 'j', 'l': 'k', 'q': 'w', 'w': 'q', 'e': 'r',
            'r': 'e', 't': 'y', 'y': 't', 'u': 'i', 'i': 'u', 'o': 'p',
            'p': 'o', 'z': 'x', 'x': 'z', 'c': 'v', 'v': 'c', 'b': 'n',
            'n': 'b', 'm': 'n', '1': '2', '2': '1', '3': '4', '4': '3',
            '5': '6', '6': '5', '7': '8', '8': '7', '9': '0', '0': '9'
        }
        
        return keyboard_adjacency.get(char.lower(), char)
    
    def quantum_scroll(self, driver, scroll_behavior='smooth', scroll_count=None):
        """Generate quantum-level human-like scrolling"""
        try:
            behavior = self.scroll_behaviors.get(scroll_behavior, self.scroll_behaviors['smooth'])
            
            if scroll_count is None:
                scroll_count = random.randint(3, 8)
            
            for scroll_index in range(scroll_count):
                # Determine scroll direction and amount
                scroll_direction = 1 if random.random() > 0.1 else -1  # 90% down, 10% up
                scroll_amount = random.randint(200, 600) * behavior['scroll_speed']
                scroll_amount *= random.uniform(1 - behavior['scroll_variation'], 1 + behavior['scroll_variation'])
                
                # Execute scroll
                driver.execute_script(f"window.scrollBy(0, {scroll_direction * scroll_amount});")
                
                # Pause between scrolls
                if random.random() < behavior['pause_frequency']:
                    pause_time = random.uniform(0.3, 1.5)
                    time.sleep(pause_time)
                else:
                    time.sleep(random.uniform(0.1, 0.3))
                
                # Occasionally change direction
                if random.random() < behavior['direction_changes']:
                    # Quick scroll in opposite direction
                    quick_back_scroll = -scroll_amount * 0.3
                    driver.execute_script(f"window.scrollBy(0, {quick_back_scroll});")
                    time.sleep(0.2)
            
            # Record interaction
            self._record_interaction('scrolling', {
                'behavior': scroll_behavior,
                'scroll_count': scroll_count,
                'total_duration': scroll_count * 0.5  # Estimate
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Scroll simulation failed: {e}")
            return False
    
    def quantum_delay(self, base_delay=1.0, variation=0.3, purpose='general'):
        """Generate human-like delays with purpose-specific variations"""
        delay_variations = {
            'thinking': (1.5, 0.4),      # Longer, more variable for thinking
            'reading': (2.0, 0.5),       # Even longer for reading
            'decision': (1.2, 0.3),      # Moderate for decisions
            'reaction': (0.5, 0.2),      # Quick for reactions
            'general': (1.0, 0.3)        # General purpose
        }
        
        base, var = delay_variations.get(purpose, delay_variations['general'])
        actual_delay = base_delay * random.uniform(1 - variation, 1 + variation)
        
        # Add micro-variations for more natural feel
        micro_variations = [random.uniform(0.95, 1.05) for _ in range(3)]
        final_delay = actual_delay * (sum(micro_variations) / len(micro_variations))
        
        time.sleep(final_delay)
        
        self._record_interaction('delay', {
            'purpose': purpose,
            'requested_delay': base_delay,
            'actual_delay': final_delay,
            'variation_applied': variation
        })
        
        return final_delay
    
    def simulate_reading_behavior(self, driver, content_complexity=1.0):
        """Simulate human reading behavior"""
        try:
            # Estimate content length from page
            content_length = driver.execute_script("""
                return document.body.innerText.length;
            """)
            
            # Calculate reading time (average reading speed: 200-300 wpm)
            words = content_length / 5  # Rough estimate
            reading_time = (words / 250) * 60  # Convert to seconds
            
            # Adjust for complexity
            reading_time *= content_complexity
            
            # Add variability
            reading_time *= random.uniform(0.7, 1.3)
            
            # Simulate reading with occasional scrolls
            total_scrolls = max(3, int(reading_time / 10))
            
            for i in range(total_scrolls):
                # Small scroll to simulate reading progress
                scroll_amount = random.randint(100, 300)
                driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                
                # Pause for reading
                pause_time = reading_time / total_scrolls * random.uniform(0.8, 1.2)
                time.sleep(pause_time)
                
                # Occasional small scroll back (rereading)
                if random.random() < 0.2:
                    driver.execute_script(f"window.scrollBy(0, {-scroll_amount // 2});")
                    time.sleep(0.5)
                    driver.execute_script(f"window.scrollBy(0, {scroll_amount // 2});")
            
            self._record_interaction('reading', {
                'estimated_content_length': content_length,
                'reading_time': reading_time,
                'scroll_count': total_scrolls
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Reading simulation failed: {e}")
            return False
    
    def _record_interaction(self, interaction_type, details):
        """Record humanizer interactions for analysis"""
        interaction_record = {
            'timestamp': time.time(),
            'type': interaction_type,
            'details': details,
            'entropy': self.entropy_source
        }
        
        self.interaction_history.append(interaction_record)
        
        # Keep only recent history
        if len(self.interaction_history) > 1000:
            self.interaction_history = self.interaction_history[-500:]
    
    def get_humanizer_report(self):
        """Get humanizer performance and usage report"""
        recent_interactions = self.interaction_history[-20:] if self.interaction_history else []
        
        # Count interaction types
        type_counts = {}
        for interaction in self.interaction_history:
            itype = interaction['type']
            type_counts[itype] = type_counts.get(itype, 0) + 1
        
        return {
            'total_interactions': len(self.interaction_history),
            'interaction_types': type_counts,
            'recent_interactions': recent_interactions,
            'movement_patterns_available': list(self.movement_patterns.keys()),
            'typing_profiles_available': list(self.typing_profiles.keys()),
            'scroll_behaviors_available': list(self.scroll_behaviors.keys())
        }

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

# Factory function
def create_humanizer(config=None):
    """Factory function for easy humanizer creation"""
    from config import settings
    config = config or settings.current_config
    return Humanizer(config)