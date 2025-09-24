import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import time

def get_stealth_driver(proxy=None, user_agent=None, headless=False):
    options = uc.ChromeOptions()
    
    # QUANTUM STEALTH ARGUMENTS
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
        "--disable-features=VizDisplayCompositor",
        "--disable-component-extensions-with-background-pages",
        "--disable-default-apps",
        "--disable-device-discovery-notifications",
        "--disable-client-side-phishing-detection",
        "--disable-hang-monitor",
        "--disable-prompt-on-repost",
        "--disable-domain-reliability",
        "--disable-sync",
        "--disable-webrtc-hiding",
        "--no-pings",
        "--disable-search-engine-choice-screen",
        f"--window-size={random.choice(['1920,1080', '1366,768', '1536,864', '1440,900'])}",
        f"--user-agent={user_agent or get_quantum_user_agent()}"
    ]
    
    if headless:
        stealth_args.extend(["--headless=new", "--disable-gpu", "--remote-debugging-port=0"])
    
    for arg in stealth_args:
        options.add_argument(arg)
    
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging", "load-extension"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    })
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    
    driver = uc.Chrome(options=options, use_subprocess=False)
    
    # QUANTUM STEALTH SCRIPTS
    stealth_scripts = [
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})",
        "Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})",
        "Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})",
        "Object.defineProperty(navigator, 'platform', {get: () => 'Win32'})",
        "window.chrome = {runtime: {}, loadTimes: function() {}, csi: function() {}, app: {}};",
        "Object.defineProperty(document, 'hidden', {get: () => false})",
        f"Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{get: () => () => ({{timeZone: '{random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo'])}', locale: 'en-US'}})}});"
    ]
    
    for script in stealth_scripts:
        try:
            driver.execute_script(script)
            time.sleep(0.05)
        except: pass
    
    return driver

def get_quantum_user_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    ]
    return random.choice(agents)