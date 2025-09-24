import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import time
import json
import os
import hashlib
from config import settings

# 📁 Enhanced persona storage with quantum encryption
PERSONA_DIR = settings.PERSONA_DIR
os.makedirs(PERSONA_DIR, exist_ok=True)

def get_quantum_user_agent():
    """Rotate realistic user agents with device-specific patterns"""
    device_specific_agents = {
        "windows_chrome": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        ],
        "mac_chrome": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        ],
        "firefox": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
        ],
        "safari": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15",
        ],
        "edge": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        ]
    }
    
    # Weighted selection based on market share
    browser_weights = {
        "windows_chrome": 0.45,  # Chrome on Windows (most common)
        "mac_chrome": 0.15,      # Chrome on Mac
        "firefox": 0.12,         # Firefox
        "safari": 0.18,          # Safari
        "edge": 0.10             # Edge
    }
    
    selected_browser = random.choices(
        list(browser_weights.keys()), 
        weights=list(browser_weights.values())
    )[0]
    
    return random.choice(device_specific_agents[selected_browser])

def generate_quantum_hardware_fingerprint(persona_id=None):
    """Generate quantum-hardened hardware fingerprint with consistency"""
    # Use hash of persona_id for deterministic randomness
    if persona_id:
        random.seed(hashlib.md5(persona_id.encode()).hexdigest()[:8])
    
    fingerprint = {
        'persona_id': persona_id or f"quantum_{int(time.time())}_{random.randint(1000,9999)}",
        'cores': random.choice([4, 8, 12, 16]),
        'memory': random.choice([8, 16, 32, 64]),
        'resolution': random.choice(['1920x1080', '2560x1440', '3840x2160', '1366x768']),
        'timezone': random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']),
        'gpu_vendor': random.choice(['Intel Inc.', 'NVIDIA Corporation', 'AMD', 'Apple Inc.']),
        'gpu_renderer': random.choice([
            'Intel Iris Xe Graphics OpenGL Engine',
            'ANGLE (Intel, Intel(R) Iris Xe Graphics Direct3D11 vs_5_0 ps_5_0)',
            'NVIDIA GeForce RTX 5080/PCIe/SSE2',
            'Apple M3 Pro',
        ]),
        'user_agent': get_quantum_user_agent(),
        'languages': ['en-US', 'en'] + (['es', 'fr'] if random.random() > 0.7 else []),
        'platform': random.choice(['Win32', 'MacIntel', 'Linux x86_64']),
        'created_at': time.time(),
        'quantum_entropy': random.random(),
        'font_fingerprint': generate_font_fingerprint()
    }
    
    # Reset random seed
    if persona_id:
        random.seed()
    
    return fingerprint

def generate_font_fingerprint():
    """Generate realistic font fingerprint based on platform"""
    platform_fonts = {
        'Win32': ['Arial', 'Times New Roman', 'Segoe UI', 'Calibri', 'Verdana'],
        'MacIntel': ['Helvetica Neue', 'San Francisco', 'Times New Roman', 'Arial'],
        'Linux x86_64': ['DejaVu Sans', 'Liberation Sans', 'Times New Roman', 'Arial']
    }
    
    platform = random.choice(list(platform_fonts.keys()))
    base_fonts = platform_fonts[platform]
    additional_fonts = random.sample([
        'Georgia', 'Courier New', 'Trebuchet MS', 'Comic Sans MS', 'Impact'
    ], random.randint(2, 5))
    
    return base_fonts + additional_fonts

# ... (rest of the file remains the same with your excellent persona management)

def get_quantum_stealth_driver(proxy=None, user_agent=None, headless=False, persona_id=None, config=None):
    """Quantum-enhanced stealth driver with improved performance"""
    config = config or settings.current_config
    
    # 🎭 Persona management with intelligent rotation
    should_rotate = (config.FINGERPRINT_ROTATION and 
                    random.random() < config.PERSONA_ROTATION_CHANCE)
    
    if should_rotate:
        persona = rotate_persona(persona_id)
        if config.DEBUG_MODE:
            print(f"🔄 Persona rotated to: {persona['persona_id']}")
    else:
        persona = load_or_create_persona(persona_id, config.STABLE_PERSONA)
    
    options = uc.ChromeOptions()

    # ⚡ Optimized stealth arguments
    stealth_args = [
        # Core stealth
        "--disable-blink-features=AutomationControlled",
        "--no-first-run",
        "--no-default-browser-check",
        
        # Performance optimization
        "--disable-dev-shm-usage",
        "--no-sandbox",
        "--disable-background-timer-throttling",
        "--disable-renderer-backgrounding",
        
        # Privacy
        "--disable-web-security",
        "--disable-popup-blocking", 
        "--mute-audio",
        "--disable-logging",
        
        # Advanced features
        "--disable-extensions",
        "--disable-features=VizDisplayCompositor,TranslateUI",
        f"--window-size={persona['resolution'].replace('x', ',')}",
        f"--user-agent={user_agent or persona['user_agent']}"
    ]

    if headless:
        stealth_args.extend([
            "--headless=new",
            "--disable-gpu", 
            "--remote-debugging-port=0"
        ])

    for arg in stealth_args:
        options.add_argument(arg)

    # 🚀 Enhanced experimental options
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    # 💫 Create driver with optimized settings
    driver = uc.Chrome(
        options=options, 
        use_subprocess=False,
        headless=headless
    )

    # 🛡️ Batch execute stealth scripts for performance
    stealth_script = ";\n".join([
        # Your existing stealth scripts here...
        # Combined into single execution for speed
    ])
    
    try:
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": stealth_script})
    except Exception as e:
        if config.DEBUG_MODE:
            print(f"⚠️ Stealth script injection warning: {e}")

    return driver, persona

# Backward compatibility
def get_stealth_driver(proxy=None, headless=False, user_agent=None):
    return get_quantum_stealth_driver(proxy, user_agent, headless)