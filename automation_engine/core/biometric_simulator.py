import random
import time
import math
import hashlib
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import settings

class BiometricSimulator:
    def __init__(self, config):
        self.config = config
        self.biometric_profiles = self._init_biometric_profiles()
        self.current_profile = 'standard'
        self.behavior_history = []
        self.biometric_entropy = random.random()
        self.fatigue_level = 0.0
        self.attention_span = 1.0
        
    def _init_biometric_profiles(self):
        """Initialize biometric behavior profiles"""
        return {
            'standard': {
                'mouse_steadiness': 0.8,
                'click_pressure': 0.7,
                'typing_rhythm': 0.6,
                'gaze_stability': 0.75,
                'reaction_time': 0.5,
                'micro_movements': 0.4,
                'breathing_pattern': 0.6,
                'cognitive_load': 0.5
            },
            'focused': {
                'mouse_steadiness': 0.95,
                'click_pressure': 0.9,
                'typing_rhythm': 0.8,
                'gaze_stability': 0.9,
                'reaction_time': 0.3,
                'micro_movements': 0.2,
                'breathing_pattern': 0.8,
                'cognitive_load': 0.8
            },
            'casual': {
                'mouse_steadiness': 0.6,
                'click_pressure': 0.5,
                'typing_rhythm': 0.4,
                'gaze_stability': 0.5,
                'reaction_time': 0.7,
                'micro_movements': 0.6,
                'breathing_pattern': 0.4,
                'cognitive_load': 0.3
            },
            'fatigued': {
                'mouse_steadiness': 0.4,
                'click_pressure': 0.3,
                'typing_rhythm': 0.2,
                'gaze_stability': 0.3,
                'reaction_time': 0.9,
                'micro_movements': 0.8,
                'breathing_pattern': 0.2,
                'cognitive_load': 0.1
            },
            'excited': {
                'mouse_steadiness': 0.7,
                'click_pressure': 0.8,
                'typing_rhythm': 0.9,
                'gaze_stability': 0.6,
                'reaction_time': 0.4,
                'micro_movements': 0.7,
                'breathing_pattern': 0.9,
                'cognitive_load': 0.7
            }
        }
    
    def simulate_biometric_behavior(self, driver, behavior_type, element=None, context=None):
        """Simulate comprehensive biometric behavior"""
        context = context or {}
        profile = self.biometric_profiles[self.current_profile]
        
        try:
            if behavior_type == 'mouse_click':
                return self._simulate_biometric_click(driver, element, profile, context)
            elif behavior_type == 'typing':
                return self._simulate_biometric_typing(driver, element, profile, context)
            elif behavior_type == 'scrolling':
                return self._simulate_biometric_scrolling(driver, profile, context)
            elif behavior_type == 'reading':
                return self._simulate_biometric_reading(driver, profile, context)
            elif behavior_type == 'decision_making':
                return self._simulate_biometric_decision(driver, profile, context)
            else:
                return self._simulate_general_biometrics(driver, profile, context)
                
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric simulation failed: {e}")
            return False
    
    def _simulate_biometric_click(self, driver, element, profile, context):
        """Simulate biometric mouse click behavior"""
        try:
            # Get element position
            element_location = element.location
            element_size = element.size
            
            target_x = element_location['x'] + element_size['width'] // 2
            target_y = element_location['y'] + element_size['height'] // 2
            
            # Generate biometric mouse path
            path = self._generate_biometric_mouse_path(
                target_x, target_y, profile['mouse_steadiness']
            )
            
            actions = ActionChains(driver)
            
            # Follow biometric path
            for point in path:
                actions.move_by_offset(point['dx'], point['dy'])
                actions.pause(point['pause'])
            
            # Simulate click pressure variations
            click_delay = self._calculate_click_pressure(profile['click_pressure'])
            actions.pause(click_delay)
            
            # Add micro-movements before click
            if random.random() < profile['micro_movements']:
                micro_dx = random.randint(-2, 2)
                micro_dy = random.randint(-2, 2)
                actions.move_by_offset(micro_dx, micro_dy)
                actions.pause(0.02)
                actions.move_by_offset(-micro_dx, -micro_dy)
            
            # Execute click
            actions.click()
            actions.perform()
            
            # Record biometric data
            self._record_biometric_behavior('click', {
                'steadiness': profile['mouse_steadiness'],
                'pressure': profile['click_pressure'],
                'path_complexity': len(path),
                'reaction_time': click_delay
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric click failed: {e}")
            return False
    
    def _generate_biometric_mouse_path(self, target_x, target_y, steadiness):
        """Generate biometric mouse movement path with human imperfections"""
        path_points = []
        current_x, current_y = 0, 0  # Relative to current position
        
        distance = math.sqrt(target_x**2 + target_y**2)
        num_points = max(3, int(distance * (1 - steadiness) * 0.1))
        
        for i in range(num_points):
            progress = (i + 1) / num_points
            
            # Ideal position
            ideal_x = target_x * progress
            ideal_y = target_y * progress
            
            # Add biometric imperfections based on steadiness
            imperfection_range = (1 - steadiness) * 20
            actual_x = ideal_x + random.uniform(-imperfection_range, imperfection_range)
            actual_y = ideal_y + random.uniform(-imperfection_range, imperfection_range)
            
            if i == 0:
                dx = actual_x
                dy = actual_y
            else:
                prev_point = path_points[-1]
                dx = actual_x - prev_point['cumulative_x']
                dy = actual_y - prev_point['cumulative_y']
            
            # Speed variations based on biometric rhythm
            pause_variation = random.uniform(0.8, 1.2) * (1 - steadiness)
            pause = 0.01 * pause_variation
            
            path_points.append({
                'dx': int(dx),
                'dy': int(dy),
                'pause': pause,
                'cumulative_x': actual_x,
                'cumulative_y': actual_y
            })
        
        return path_points
    
    def _calculate_click_pressure(self, pressure_factor):
        """Calculate click delay based on simulated pressure"""
        base_delay = 0.1
        pressure_variation = random.uniform(0.5, 1.5) * pressure_factor
        return base_delay * pressure_variation
    
    def _simulate_biometric_typing(self, driver, element, profile, context):
        """Simulate biometric typing behavior"""
        try:
            text = context.get('text', '')
            if not text:
                return False
            
            # Focus element
            element.click()
            time.sleep(0.1)
            
            actions = ActionChains(driver)
            
            for i, char in enumerate(text):
                # Type character with biometric rhythm
                char_delay = self._calculate_typing_rhythm(profile['typing_rhythm'], i, char)
                actions.send_keys(char)
                actions.pause(char_delay)
                
                # Simulate biometric errors
                if random.random() > profile['typing_rhythm']:
                    # Mistype
                    wrong_char = self._get_biometric_mistype(char)
                    actions.send_keys(wrong_char)
                    actions.pause(0.05)
                    
                    # Correction with biometric delay
                    correction_delay = char_delay * random.uniform(1.5, 2.5)
                    actions.send_keys(Keys.BACKSPACE)
                    actions.pause(correction_delay)
                    actions.send_keys(char)
                    actions.pause(char_delay)
                
                # Breathing pauses between words
                if char == ' ' and random.random() < profile['breathing_pattern']:
                    breath_pause = random.uniform(0.2, 0.8)
                    actions.pause(breath_pause)
            
            actions.perform()
            
            self._record_biometric_behavior('typing', {
                'rhythm_consistency': profile['typing_rhythm'],
                'text_length': len(text),
                'breathing_pattern': profile['breathing_pattern'],
                'error_rate': 1 - profile['typing_rhythm']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric typing failed: {e}")
            return False
    
    def _calculate_typing_rhythm(self, rhythm_factor, char_index, char):
        """Calculate typing rhythm with biometric variations"""
        base_delay = 0.08  # 80ms per character average
        
        # Rhythm patterns (fast start, slow middle, fast end)
        position_factor = 1.0
        if char_index < len(str(char_index)) * 0.2:  # First 20%
            position_factor = 0.9  # Faster
        elif char_index > len(str(char_index)) * 0.8:  # Last 20%
            position_factor = 0.95  # Slightly faster
        else:
            position_factor = 1.1  # Slower middle
        
        # Character difficulty
        difficulty_factor = 1.0
        if char in 'qwertyuiop':
            difficulty_factor = 0.9  # Home row - easier
        elif char in 'asdfghjkl':
            difficulty_factor = 1.0  # Middle row
        else:
            difficulty_factor = 1.2  # Harder keys
        
        # Final delay calculation
        rhythm_variation = random.uniform(0.8, 1.2) * rhythm_factor
        final_delay = base_delay * position_factor * difficulty_factor * rhythm_variation
        
        return max(0.02, final_delay)  # Minimum 20ms delay
    
    def _get_biometric_mistype(self, char):
        """Get realistic mistype based on keyboard proximity and biometric factors"""
        keyboard_proximity = {
            'a': ['q', 'w', 's', 'z'],
            's': ['a', 'w', 'e', 'd', 'x', 'z'],
            'd': ['s', 'e', 'r', 'f', 'c', 'x'],
            'f': ['d', 'r', 't', 'g', 'v', 'c'],
            'g': ['f', 't', 'y', 'h', 'b', 'v'],
            'h': ['g', 'y', 'u', 'j', 'n', 'b'],
            'j': ['h', 'u', 'i', 'k', 'm', 'n'],
            'k': ['j', 'i', 'o', 'l', 'm'],
            'l': ['k', 'o', 'p'],
            'q': ['a', 'w', 's'],
            'w': ['q', 'a', 's', 'd', 'e'],
            'e': ['w', 's', 'd', 'f', 'r'],
            'r': ['e', 'd', 'f', 'g', 't'],
            't': ['r', 'f', 'g', 'h', 'y'],
            'y': ['t', 'g', 'h', 'j', 'u'],
            'u': ['y', 'h', 'j', 'k', 'i'],
            'i': ['u', 'j', 'k', 'l', 'o'],
            'o': ['i', 'k', 'l', 'p'],
            'p': ['o', 'l'],
            'z': ['a', 's', 'x'],
            'x': ['z', 's', 'd', 'c'],
            'c': ['x', 'd', 'f', 'v'],
            'v': ['c', 'f', 'g', 'b'],
            'b': ['v', 'g', 'h', 'n'],
            'n': ['b', 'h', 'j', 'm'],
            'm': ['n', 'j', 'k']
        }
        
        lower_char = char.lower()
        if lower_char in keyboard_proximity:
            return random.choice(keyboard_proximity[lower_char])
        return char  # Fallback to same char if no proximity data
    
    def _simulate_biometric_scrolling(self, driver, profile, context):
        """Simulate biometric scrolling behavior"""
        try:
            scroll_count = context.get('scroll_count', random.randint(3, 8))
            scroll_direction = context.get('direction', 'down')
            
            base_scroll_amount = 300
            gaze_stability = profile['gaze_stability']
            
            for i in range(scroll_count):
                # Vary scroll amount based on gaze stability
                scroll_variation = random.uniform(0.7, 1.3) * gaze_stability
                scroll_amount = int(base_scroll_amount * scroll_variation)
                
                # Determine direction
                direction = 1 if scroll_direction == 'down' else -1
                
                # Execute scroll with biometric imperfections
                driver.execute_script(f"window.scrollBy(0, {direction * scroll_amount});")
                
                # Gaze stability affects pause duration
                gaze_pause = random.uniform(0.3, 1.0) * (1 - gaze_stability)
                time.sleep(gaze_pause)
                
                # Micro-scroll corrections
                if random.random() < profile['micro_movements']:
                    correction = scroll_amount // 10 * (-1 if random.random() > 0.5 else 1)
                    driver.execute_script(f"window.scrollBy(0, {correction});")
                    time.sleep(0.1)
            
            self._record_biometric_behavior('scrolling', {
                'gaze_stability': gaze_stability,
                'scroll_count': scroll_count,
                'micro_movements': profile['micro_movements']
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric scrolling failed: {e}")
            return False
    
    def _simulate_biometric_reading(self, driver, profile, context):
        """Simulate biometric reading behavior"""
        try:
            reading_time = context.get('reading_time', random.randint(10, 30))
            content_complexity = context.get('complexity', 1.0)
            
            # Adjust reading time based on cognitive load and complexity
            adjusted_time = reading_time * content_complexity * profile['cognitive_load']
            
            # Simulate eye movements and focus shifts
            scan_intervals = max(3, int(adjusted_time / 3))
            
            for scan in range(scan_intervals):
                # Simulate focus shift (small scroll)
                focus_shift = random.randint(50, 150)
                driver.execute_script(f"window.scrollBy(0, {focus_shift});")
                
                # Reading pause with biometric variations
                scan_duration = adjusted_time / scan_intervals
                biometric_variation = random.uniform(0.8, 1.2) * profile['gaze_stability']
                actual_pause = scan_duration * biometric_variation
                
                time.sleep(actual_pause)
                
                # Blink simulation (tiny scroll back)
                if random.random() < 0.3:
                    driver.execute_script(f"window.scrollBy(0, {-focus_shift // 3});")
                    time.sleep(0.1)
                    driver.execute_script(f"window.scrollBy(0, {focus_shift // 3});")
            
            self._record_biometric_behavior('reading', {
                'cognitive_load': profile['cognitive_load'],
                'gaze_stability': profile['gaze_stability'],
                'reading_duration': adjusted_time,
                'scan_intervals': scan_intervals
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric reading failed: {e}")
            return False
    
    def _simulate_biometric_decision(self, driver, profile, context):
        """Simulate biometric decision-making behavior"""
        try:
            decision_complexity = context.get('complexity', 1.0)
            
            # Decision time based on reaction time and complexity
            base_decision_time = 1.0
            decision_time = base_decision_time * decision_complexity * (1 - profile['reaction_time'])
            
            # Add biometric variations
            biometric_variation = random.uniform(0.5, 2.0) * profile['cognitive_load']
            actual_decision_time = decision_time * biometric_variation
            
            # Simulate decision process with micro-movements
            decision_steps = random.randint(2, 5)
            for step in range(decision_steps):
                # Small cursor movements while "thinking"
                if random.random() < profile['micro_movements']:
                    micro_move = random.randint(-10, 10)
                    driver.execute_script(f"window.scrollBy(0, {micro_move});")
                    time.sleep(0.05)
                    driver.execute_script(f"window.scrollBy(0, {-micro_move});")
                
                # Pause between decision steps
                step_pause = actual_decision_time / decision_steps
                time.sleep(step_pause)
            
            self._record_biometric_behavior('decision_making', {
                'reaction_time': profile['reaction_time'],
                'cognitive_load': profile['cognitive_load'],
                'decision_duration': actual_decision_time,
                'decision_steps': decision_steps
            })
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Biometric decision failed: {e}")
            return False
    
    def _simulate_general_biometrics(self, driver, profile, context):
        """Simulate general biometric behaviors"""
        try:
            # Random biometric activities
            activities = [
                self._simulate_breathing_pattern,
                self._simulate_attention_shift,
                self._simulate_fatigue_manifestation
            ]
            
            # Execute random biometric activity
            activity = random.choice(activities)
            activity(driver, profile)
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ General biometric simulation failed: {e}")
            return False
    
    def _simulate_breathing_pattern(self, driver, profile):
        """Simulate breathing pattern through scroll rhythms"""
        breath_cycle = random.uniform(3, 6)  # Breathing cycle in seconds
        scroll_intensity = profile['breathing_pattern']
        
        # Simulate inhalation (scroll down)
        inhale_scroll = int(100 * scroll_intensity)
        driver.execute_script(f"window.scrollBy(0, {inhale_scroll});")
        time.sleep(breath_cycle / 2)
        
        # Simulate exhalation (scroll up slightly)
        exhale_scroll = int(-inhale_scroll * 0.3)
        driver.execute_script(f"window.scrollBy(0, {exhale_scroll});")
        time.sleep(breath_cycle / 2)
    
    def _simulate_attention_shift(self, driver, profile):
        """Simulate attention shifts through viewport changes"""
        attention_span = profile['gaze_stability']
        
        # Random viewport shift based on attention span
        shift_x = random.randint(-100, 100) * (1 - attention_span)
        shift_y = random.randint(-50, 50) * (1 - attention_span)
        
        driver.execute_script(f"window.scrollBy({shift_x}, {shift_y});")
        time.sleep(0.5)
        driver.execute_script(f"window.scrollBy({-shift_x}, {-shift_y});")
    
    def _simulate_fatigue_manifestation(self, driver, profile):
        """Simulate fatigue through slower interactions"""
        fatigue_level = self.fatigue_level
        
        if fatigue_level > 0.5:
            # Slower scrolls when fatigued
            slow_scroll = random.randint(50, 100)
            driver.execute_script(f"window.scrollBy(0, {slow_scroll});")
            time.sleep(fatigue_level * 2)  # Longer pauses when tired
    
    def update_biometric_profile(self, new_profile=None, fatigue_increase=0.0):
        """Update current biometric profile"""
        available_profiles = list(self.biometric_profiles.keys())
        
        if new_profile and new_profile in available_profiles:
            self.current_profile = new_profile
        else:
            # Weighted random selection based on time and fatigue
            weights = self._calculate_profile_weights()
            self.current_profile = random.choices(available_profiles, weights=weights)[0]
        
        # Update fatigue level
        self.fatigue_level = min(1.0, self.fatigue_level + fatigue_increase)
        
        # Update attention span based on fatigue
        self.attention_span = max(0.1, 1.0 - self.fatigue_level * 0.8)
        
        if self.config.DEBUG_MODE:
            print(f"🧠 Biometric profile updated: {self.current_profile} (fatigue: {self.fatigue_level:.1f})")
    
    def _calculate_profile_weights(self):
        """Calculate weights for profile selection"""
        current_hour = datetime.now().hour
        weights = {}
        
        for profile in self.biometric_profiles.keys():
            base_weight = 1.0
            
            # Time-based adjustments
            if 6 <= current_hour <= 10:  # Morning
                if profile in ['focused', 'standard']:
                    base_weight *= 1.5
            elif 13 <= current_hour <= 14:  # Lunch
                if profile in ['casual', 'fatigued']:
                    base_weight *= 1.8
            elif 20 <= current_hour <= 23:  # Evening
                if profile in ['casual', 'excited']:
                    base_weight *= 1.6
            elif 0 <= current_hour <= 5:  # Late night
                if profile == 'fatigued':
                    base_weight *= 2.0
            
            # Fatigue-based adjustments
            if self.fatigue_level > 0.7:
                if profile == 'fatigued':
                    base_weight *= 3.0
                elif profile == 'focused':
                    base_weight *= 0.3
            
            weights[profile] = base_weight
        
        return [weights.get(profile, 1.0) for profile in self.biometric_profiles.keys()]
    
    def _record_biometric_behavior(self, behavior_type, metrics):
        """Record biometric behavior data"""
        record = {
            'timestamp': time.time(),
            'behavior_type': behavior_type,
            'profile': self.current_profile,
            'metrics': metrics,
            'fatigue_level': self.fatigue_level,
            'attention_span': self.attention_span
        }
        
        self.behavior_history.append(record)
        
        # Keep history manageable
        if len(self.behavior_history) > 1000:
            self.behavior_history = self.behavior_history[-500:]
    
    def get_biometric_report(self):
        """Get comprehensive biometric simulation report"""
        recent_behaviors = self.behavior_history[-10:] if self.behavior_history else []
        
        # Calculate behavior statistics
        behavior_counts = {}
        for behavior in self.behavior_history:
            btype = behavior['behavior_type']
            behavior_counts[btype] = behavior_counts.get(btype, 0) + 1
        
        return {
            'current_profile': self.current_profile,
            'fatigue_level': self.fatigue_level,
            'attention_span': self.attention_span,
            'total_behaviors': len(self.behavior_history),
            'behavior_distribution': behavior_counts,
            'recent_behaviors': recent_behaviors,
            'available_profiles': list(self.biometric_profiles.keys())
        }

# Utility function
def create_biometric_simulator(config=None):
    """Factory function for easy biometric simulator creation"""
    from config import settings
    config = config or settings.current_config
    return BiometricSimulator(config)