from seleniumbase import Driver
from selenium.webdriver.chrome.options import Options
import random

def get_stealth_driver(proxy=None, user_agent=None):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    resolutions = ["1920,1080", "1366,768", "1536,864", "1440,900"]
    chrome_options.add_argument(f"--window-size={random.choice(resolutions)}")
    
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')
    if user_agent:
        chrome_options.add_argument(f'--user-agent={user_agent}')
        
    driver = Driver(browser="chrome", headless=False, undetectable=True, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver