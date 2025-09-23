import random
import time
import math
from selenium.webdriver.common.action_chains import ActionChains
from config import settings

def human_mouse_movement(driver, element):
    """Generate human-like mouse movement with Bezier curves"""
    action = ActionChains(driver)
    
    # Get element position
    element_location = element.location_once_scrolled_into_view
    target_x = element_location['x'] + random.randint(5, 15)
    target_y = element_location['y'] + random.randint(5, 15)
    
    # Generate curved path
    path = generate_bezier_curve(100, 100, target_x, target_y, 8)
    
    # Move through path points
    for point in path:
        action.move_by_offset(point['x'], point['y'])
        action.pause(random.uniform(0.01, 0.03))
    
    action.click()
    action.perform()

def generate_bezier_curve(start_x, start_y, end_x, end_y, points=10):
    """Generate Bezier curve points for human-like movement"""
    curve_points = []
    
    # Control points for natural curve
    control1_x = start_x + (end_x - start_x) * 0.3
    control1_y = start_y + (end_y - start_y) * 0.2
    control2_x = start_x + (end_x - start_x) * 0.7
    control2_y = start_y + (end_y - start_y) * 0.8
    
    for i in range(points):
        t = i / (points - 1)
        # Cubic Bezier formula
        x = (1-t)**3 * start_x + 3*(1-t)**2*t * control1_x + 3*(1-t)*t**2 * control2_x + t**3 * end_x
        y = (1-t)**3 * start_y + 3*(1-t)**2*t * control1_y + 3*(1-t)*t**2 * control2_y + t**3 * end_y
        curve_points.append({'x': int(x - start_x), 'y': int(y - start_y)})
    
    return curve_points

def quantum_delay():
    """Ultra-random delay using system entropy"""
    return random.SystemRandom().uniform(settings.MIN_DELAY, settings.MAX_DELAY)

def human_type(element, text, speed_variation=0.2):
    """Human-like typing with speed variations and occasional errors"""
    for char in text:
        element.send_keys(char)
        # Variable typing speed with occasional pauses
        if random.random() < 0.05:  # 5% chance of "thinking" pause
            time.sleep(random.uniform(0.5, 1.2))
        else:
            base_speed = random.uniform(0.08, 0.15)
            time.sleep(base_speed * (1 + random.uniform(-speed_variation, speed_variation)))
        
        # 2% chance of backspace typo
        if random.random() < 0.02:
            element.send_keys('\b')
            time.sleep(0.1)
            element.send_keys(char)

def advanced_scroll(driver):
    """Multiple scroll patterns for human-like behavior"""
    patterns = [
        lambda: continuous_scroll(driver),
        lambda: bounce_scroll(driver),
        lambda: random_scrolls(driver)
    ]
    random.choice(patterns)()

def continuous_scroll(driver):
    """Smooth continuous scrolling"""
    scroll_distance = random.randint(300, 800)
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    time.sleep(quantum_delay())

def bounce_scroll(driver):
    """Bounce scroll like human reading"""
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(0.3)
    driver.execute_script("window.scrollBy(0, -150);")
    time.sleep(0.2)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(quantum_delay())

def random_scrolls(driver):
    """Random small scroll movements"""
    for _ in range(random.randint(2, 5)):
        scroll = random.randint(50, 200)
        driver.execute_script(f"window.scrollBy(0, {scroll});")
        time.sleep(random.uniform(0.1, 0.3))