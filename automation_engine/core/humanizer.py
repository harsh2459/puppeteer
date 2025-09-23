import random
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
from config import settings

def quantum_random_delay():
    try:
        response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8', timeout=5)
        quantum_num = response.json()['data'][0]
        return quantum_num / 10.0
    except:
        return random.uniform(settings.MIN_DELAY, settings.MAX_DELAY)

def human_type(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.3))

def human_click(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.pause(quantum_random_delay())
    action.click()
    action.perform()

def random_delay(min_sec=None, max_sec=None):
    min_val = min_sec if min_sec is not None else settings.MIN_DELAY
    max_val = max_sec if max_sec is not None else settings.MAX_DELAY
    time.sleep(quantum_random_delay())

def random_scroll(driver):
    scroll_height = random.randint(200, 1000)
    driver.execute_script(f"window.scrollBy(0, {scroll_height});")
    random_delay(1, 2)