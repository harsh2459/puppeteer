import random
import time
from datetime import datetime, timedelta

class TrafficObfuscator:
    def __init__(self, config):
        self.config = config
        self.traffic_patterns = self._init_traffic_patterns()
        self.request_history = []
        
    def _init_traffic_patterns(self):
        """Initialize realistic traffic patterns"""
        return {
            "business_day": {
                "peak_hours": [9, 10, 11, 14, 15, 16],
                "off_peak_multiplier": 0.3,
                "weekend_multiplier": 0.5
            },
            "evening_user": {
                "peak_hours": [19, 20, 21, 22],
                "off_peak_multiplier": 0.2,
                "weekend_multiplier": 1.2
            },
            "night_owl": {
                "peak_hours": [23, 0, 1, 2],
                "off_peak_multiplier": 0.8,
                "weekend_multiplier": 1.5
            },
            "all_day": {
                "peak_hours": list(range(24)),
                "off_peak_multiplier": 1.0,
                "weekend_multiplier": 1.0
            }
        }
    
    def get_obfuscated_delay(self, pattern_type="business_day"):
        """Get delay that mimics human traffic patterns"""
        pattern = self.traffic_patterns[pattern_type]
        current_hour = datetime.now().hour
        is_weekend = datetime.now().weekday() >= 5
        
        # Base delay based on time of day
        if current_hour in pattern["peak_hours"]:
            base_delay = random.uniform(2, 5)  # Shorter delays during peak
        else:
            base_delay = random.uniform(5, 15) * pattern["off_peak_multiplier"]
        
        # Weekend adjustment
        if is_weekend:
            base_delay *= pattern["weekend_multiplier"]
        
        # Add random jitter
        jitter = random.uniform(0.7, 1.3)
        final_delay = base_delay * jitter
        
        # Ensure minimum delay
        return max(1, final_delay)
    
    def simulate_natural_browsing_session(self, driver, session_duration=300):
        """Simulate complete natural browsing session"""
        start_time = time.time()
        actions_performed = 0
        
        while time.time() - start_time < session_duration:
            # Random browsing actions
            action_type = random.choice(["scroll", "click", "hover", "read"])
            
            if action_type == "scroll":
                self._natural_scroll(driver)
            elif action_type == "click":
                self._simulate_random_click(driver)
            elif action_type == "hover":
                self._simulate_hover_behavior(driver)
            elif action_type == "read":
                self._simulate_reading_behavior(driver)
            
            actions_performed += 1
            
            # Variable delays between actions
            delay = self.get_obfuscated_delay()
            time.sleep(delay)
        
        return actions_performed
    
    def _natural_scroll(self, driver):
        """Simulate natural scrolling behavior"""
        scroll_types = [
            {"direction": "down", "distance": (200, 500), "speed": "medium"},
            {"direction": "up", "distance": (100, 300), "speed": "slow"},
            {"direction": "down", "distance": (50, 150), "speed": "fast"},
        ]
        
        scroll = random.choice(scroll_types)
        distance = random.randint(*scroll["distance"])
        
        if scroll["direction"] == "up":
            distance = -distance
        
        driver.execute_script(f"window.scrollBy(0, {distance});")
    
    def _simulate_random_click(self, driver):
        """Simulate random click on plausible elements"""
        try:
            # Find clickable elements
            clickable_selectors = [
                "a", "button", ".btn", "[onclick]", "[role='button']"
            ]
            
            all_clickables = []
            for selector in clickable_selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                all_clickables.extend(elements)
            
            if all_clickables:
                # Filter visible and clickable elements
                visible_clickables = [
                    el for el in all_clickables
                    if el.is_displayed() and el.is_enabled()
                ]
                
                if visible_clickables:
                    element = random.choice(visible_clickables)
                    
                    # Human-like click with hover
                    action = ActionChains(driver)
                    action.move_to_element(element)
                    action.pause(random.uniform(0.2, 0.5))
                    action.click()
                    action.perform()
                    
                    # Brief post-click pause
                    time.sleep(random.uniform(1, 3))
        
        except:
            pass  # Silently fail if click doesn't work
    
    def _simulate_hover_behavior(self, driver):
        """Simulate mouse hover behavior"""
        try:
            hoverable_elements = driver.find_elements(By.CSS_SELECTOR, 
                "a, button, [title], [data-tooltip]")
            
            if hoverable_elements:
                element = random.choice(hoverable_elements)
                action = ActionChains(driver)
                action.move_to_element(element)
                action.pause(random.uniform(0.5, 1.5))
                action.perform()
                
        except:
            pass
    
    def _simulate_reading_behavior(self, driver):
        """Simulate reading behavior with micro-scrolls"""
        read_time = random.uniform(5, 15)
        start_time = time.time()
        
        while time.time() - start_time < read_time:
            # Occasional micro-scrolls while "reading"
            if random.random() < 0.3:
                micro_scroll = random.randint(20, 80)
                driver.execute_script(f"window.scrollBy(0, {micro_scroll});")
            
            time.sleep(random.uniform(0.5, 1.5))