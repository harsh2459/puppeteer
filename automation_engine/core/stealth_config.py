import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random

def get_stealth_driver(proxy=None, user_agent=None, headless=False):
    options = uc.ChromeOptions()
    
    # Advanced stealth arguments
    stealth_args = [
        "--disable-blink-features=AutomationControlled",
        "--disable-blink-features",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-web-security",
        "--disable-popup-blocking",
        "--disable-translate",
        "--mute-audio",
        "--disable-logging",
        "--disable-extensions",
        "--disable-background-timer-throttling",
        "--disable-renderer-backgrounding",
        "--disable-backgrounding-occluded-windows",
        "--disable-ipc-flooding-protection",
        f"--window-size={random.choice(['1920,1080', '1366,768', '1536,864'])}"
    ]
    
    if headless:
        stealth_args.append("--headless=new")
    
    for arg in stealth_args:
        options.add_argument(arg)
    
    # Remove automation indicators
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    if user_agent:
        options.add_argument(f'--user-agent={user_agent}')
    
    # Create undetectable driver
    driver = uc.Chrome(options=options)
    
    # Advanced stealth scripts
    stealth_scripts = [
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})",
        "Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})",
        "Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})",
        "Object.defineProperty(navigator, 'platform', {get: () => 'Win32'})",
        "window.chrome = {runtime: {}};"
    ]
    
    for script in stealth_scripts:
        try:
            driver.execute_script(script)
        except:
            pass
    
    return driver