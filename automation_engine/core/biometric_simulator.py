import math
import random
import time

class BiometricSimulator:
    def __init__(self):
        self.mouse_patterns = self._init_mouse_patterns()
        self.scroll_profiles = self._init_scroll_profiles()
        self.typing_biometrics = self._init_typing_biometrics()
    
    def _init_mouse_patterns(self):
        """Initialize human-like mouse movement patterns"""
        return {
            "direct_accurate": {"curvature": 0.1, "tremor": 0.02, "speed": 1.2},
            "casual_relaxed": {"curvature": 0.3, "tremor": 0.05, "speed": 0.8},
            "hurried_imprecise": {"curvature": 0.15, "tremor": 0.08, "speed": 1.5},
            "focused_methodical": {"curvature": 0.25, "tremor": 0.03, "speed": 1.0}
        }
    
    def _init_scroll_profiles(self):
        """Initialize human scroll behavior profiles"""
        return {
            "reader": {"speed_variation": 0.3, "pause_frequency": 0.4, "scroll_length": (200, 500)},
            "scanner": {"speed_variation": 0.6, "pause_frequency": 0.2, "scroll_length": (400, 800)},
            "researcher": {"speed_variation": 0.4, "pause_frequency": 0.3, "scroll_length": (300, 600)},
            "casual": {"speed_variation": 0.5, "pause_frequency": 0.5, "scroll_length": (150, 400)}
        }
    
    def _init_typing_biometrics(self):
        """Initialize typing biometric patterns"""
        return {
            "hunt_peck": {"speed": 0.15, "error_rate": 0.08, "pause_variation": 0.6},
            "touch_typist": {"speed": 0.08, "error_rate": 0.02, "pause_variation": 0.3},
            "hybrid": {"speed": 0.12, "error_rate": 0.04, "pause_variation": 0.4},
            "mobile": {"speed": 0.20, "error_rate": 0.06, "pause_variation": 0.5}
        }
    
    def generate_bezier_mouse_path(self, start_x, start_y, end_x, end_y, pattern_type="casual_relaxed"):
        """Generate human-like mouse path using Bezier curves"""
        pattern = self.mouse_patterns[pattern_type]
        
        # Control points with curvature variation
        cp1_x = start_x + (end_x - start_x) * (0.3 + random.uniform(-0.1, 0.1))
        cp1_y = start_y + (end_y - start_y) * (0.2 + random.uniform(-0.1, 0.1))
        cp2_x = start_x + (end_x - start_x) * (0.7 + random.uniform(-0.1, 0.1))
        cp2_y = start_y + (end_y - start_y) * (0.8 + random.uniform(-0.1, 0.1))
        
        # Generate points along Bezier curve
        points = []
        num_points = int(math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2) / 10)
        num_points = max(10, min(num_points, 50))
        
        for i in range(num_points):
            t = i / (num_points - 1)
            
            # Cubic Bezier formula
            x = (1-t)**3 * start_x + 3*(1-t)**2*t * cp1_x + 3*(1-t)*t**2 * cp2_x + t**3 * end_x
            y = (1-t)**3 * start_y + 3*(1-t)**2*t * cp1_y + 3*(1-t)*t**2 * cp2_y + t**3 * end_y
            
            # Add tremor and human imperfection
            tremor_x = (random.random() - 0.5) * pattern["tremor"] * 10
            tremor_y = (random.random() - 0.5) * pattern["tremor"] * 10
            
            points.append((x + tremor_x, y + tremor_y))
        
        return points
    
    def simulate_human_scroll(self, driver, scroll_profile="reader", scroll_count=3):
        """Simulate human-like scrolling behavior"""
        profile = self.scroll_profiles[scroll_profile]
        
        for i in range(scroll_count):
            # Vary scroll length
            scroll_length = random.randint(*profile["scroll_length"])
            
            # Add speed variation
            speed_variation = 1 + (random.random() - 0.5) * profile["speed_variation"]
            actual_scroll = int(scroll_length * speed_variation)
            
            # Execute scroll with smooth behavior
            driver.execute_script(f"""
                window.scrollBy({{
                    top: {actual_scroll},
                    behavior: 'smooth'
                }});
            """)
            
            # Human-like pauses
            if random.random() < profile["pause_frequency"]:
                pause_time = random.uniform(0.5, 2.0)
                time.sleep(pause_time)
            else:
                time.sleep(random.uniform(0.1, 0.3))
    
    def simulate_biometric_typing(self, element, text, typing_profile="hybrid"):
        """Simulate biometric typing with human imperfections"""
        profile = self.typing_biometrics[typing_profile]
        
        for char in text:
            # Type character
            element.send_keys(char)
            
            # Variable typing speed
            base_speed = profile["speed"]
            speed_variation = base_speed * profile["pause_variation"]
            actual_delay = base_speed + (random.random() - 0.5) * speed_variation
            
            time.sleep(max(0.05, actual_delay))
            
            # Simulate typing errors
            if random.random() < profile["error_rate"]:
                # Backspace and retype
                element.send_keys('\b')
                time.sleep(random.uniform(0.1, 0.3))
                element.send_keys(char)
                time.sleep(random.uniform(0.1, 0.2))
            
            # Occasional thinking pauses
            if random.random() < 0.05:  # 5% chance of thinking pause
                time.sleep(random.uniform(0.5, 1.5))