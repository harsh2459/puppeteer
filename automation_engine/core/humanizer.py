import random
import time
import math
from selenium.webdriver.common.action_chains import ActionChains

def quantum_mouse_movement(driver, element):
    """Quantum-enhanced human-like mouse movement"""
    action = ActionChains(driver)
    
    element_location = element.location_once_scrolled_into_view
    target_x = element_location['x'] + random.randint(5, 15)
    target_y = element_location['y'] + random.randint(5, 15)
    
    # Quantum path generation with more randomness
    path = generate_quantum_bezier_curve(100, 100, target_x, target_y, 12)
    
    for point in path:
        # Add micro-tremors for human-like imperfection
        tremor_x = random.randint(-2, 2)
        tremor_y = random.randint(-2, 2)
        action.move_by_offset(point['x'] + tremor_x, point['y'] + tremor_y)
        action.pause(random.uniform(0.005, 0.02))  # Faster but variable
    
    action.click()
    action.perform()

def generate_quantum_bezier_curve(start_x, start_y, end_x, end_y, points=15):
    """Quantum-enhanced Bezier curve with more natural variation"""
    curve_points = []
    
    # Multiple control points for more natural curves
    control1_x = start_x + (end_x - start_x) * random.uniform(0.2, 0.4)
    control1_y = start_y + (end_y - start_y) * random.uniform(0.1, 0.3)
    control2_x = start_x + (end_x - start_x) * random.uniform(0.6, 0.8)
    control2_y = start_y + (end_y - start_y) * random.uniform(0.7, 0.9)
    
    for i in range(points):
        t = i / (points - 1)
        # Cubic Bezier with noise
        noise_x = random.uniform(-3, 3)
        noise_y = random.uniform(-3, 3)
        
        x = (1-t)**3 * start_x + 3*(1-t)**2*t * control1_x + 3*(1-t)*t**2 * control2_x + t**3 * end_x + noise_x
        y = (1-t)**3 * start_y + 3*(1-t)**2*t * control1_y + 3*(1-t)*t**2 * control2_y + t**3 * end_y + noise_y
        
        curve_points.append({'x': int(x - start_x), 'y': int(y - start_y)})
    
    return curve_points

def quantum_delay():
    """Quantum-randomized delay using system entropy"""
    return random.SystemRandom().uniform(0.3, 2.5)  # Wider range for more natural timing

def quantum_type(element, text, personality_profile=None):
    """Quantum typing with personality-based variations"""
    profile = personality_profile or {
        "speed_variation": random.uniform(0.15, 0.35),
        "error_rate": random.uniform(0.01, 0.04),
        "thinking_pause_frequency": random.uniform(0.04, 0.08)
    }
    
    for char in text:
        element.send_keys(char)
        
        # Variable thinking pauses
        if random.random() < profile["thinking_pause_frequency"]:
            time.sleep(random.uniform(0.3, 1.5))
        else:
            base_speed = random.uniform(0.06, 0.12)  # Faster base speed
            variation = profile["speed_variation"]
            time.sleep(base_speed * (1 + random.uniform(-variation, variation)))
        
        # Typo simulation with backspace
        if random.random() < profile["error_rate"]:
            element.send_keys('\b')
            time.sleep(random.uniform(0.05, 0.2))
            element.send_keys(char)

def quantum_scroll(driver, scroll_profile=None):
    """Quantum scrolling with advanced behavioral patterns"""
    profile = scroll_profile or {
        "style": random.choice(["continuous", "bounce", "random", "reading"]),
        "speed_multiplier": random.uniform(0.8, 1.5),
        "pause_probability": random.uniform(0.1, 0.3)
    }
    
    scroll_functions = {
        "continuous": lambda: continuous_quantum_scroll(driver, profile),
        "bounce": lambda: bounce_quantum_scroll(driver, profile),
        "random": lambda: random_quantum_scrolls(driver, profile),
        "reading": lambda: reading_pattern_scroll(driver, profile)
    }
    
    scroll_function = scroll_functions.get(profile["style"], scroll_functions["continuous"])
    scroll_function()

def continuous_quantum_scroll(driver, profile):
    scroll_distance = random.randint(400, 1000) * profile["speed_multiplier"]
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    time.sleep(quantum_delay())

def bounce_quantum_scroll(driver, profile):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(0.2)
    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(0.1)
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(quantum_delay())

def random_quantum_scrolls(driver, profile):
    for _ in range(random.randint(3, 8)):
        scroll = random.randint(50, 300) * profile["speed_multiplier"]
        driver.execute_script(f"window.scrollBy(0, {scroll});")
        if random.random() < profile["pause_probability"]:
            time.sleep(random.uniform(0.2, 0.8))
        else:
            time.sleep(random.uniform(0.05, 0.2))

def reading_pattern_scroll(driver, profile):
    # Simulate reading behavior with frequent small scrolls
    for _ in range(random.randint(5, 12)):
        scroll = random.randint(80, 200) * profile["speed_multiplier"]
        driver.execute_script(f"window.scrollBy(0, {scroll});")
        time.sleep(random.uniform(0.3, 1.2))  # Reading pauses

# Update existing functions to use quantum versions
human_mouse_movement = quantum_mouse_movement
human_type = quantum_type
advanced_scroll = quantum_scroll