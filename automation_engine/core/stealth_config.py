import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import time
import json
import os
import hashlib
from datetime import datetime
from config import settings

# Import enhanced fingerprint system
from quantum_fingerprint import QuantumFingerprintSpoofer

# 📁 Enhanced persona storage with quantum encryption
PERSONA_DIR = settings.PERSONA_DIR
os.makedirs(PERSONA_DIR, exist_ok=True)

def get_quantum_user_agent():
    """Rotate realistic user agents with device-specific patterns and latest versions"""
    device_specific_agents = {
        "windows_chrome": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        ],
        "mac_chrome": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        ],
        "firefox_windows": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        ],
        "firefox_mac": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0",
        ],
        "safari": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        ],
        "edge": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        ]
    }
    
    # Weighted selection based on real market share
    browser_weights = {
        "windows_chrome": 0.42,  # Chrome on Windows (most common)
        "mac_chrome": 0.14,      # Chrome on Mac
        "firefox_windows": 0.08, # Firefox on Windows
        "firefox_mac": 0.04,     # Firefox on Mac
        "safari": 0.20,          # Safari
        "edge": 0.12             # Edge
    }
    
    selected_browser = random.choices(
        list(browser_weights.keys()), 
        weights=list(browser_weights.values())
    )[0]
    
    return random.choice(device_specific_agents[selected_browser])

def generate_quantum_hardware_fingerprint(persona_id=None, region="US"):
    """Generate quantum-hardened hardware fingerprint with regional consistency"""
    # Use hash of persona_id for deterministic randomness
    if persona_id:
        random.seed(int(hashlib.md5(persona_id.encode()).hexdigest()[:8], 16))
    
    # Regional hardware distribution
    regional_hardware = {
        "US": {"nvidia": 0.4, "amd": 0.3, "intel": 0.25, "apple": 0.05},
        "EU": {"nvidia": 0.35, "amd": 0.35, "intel": 0.25, "apple": 0.05},
        "JP": {"nvidia": 0.3, "amd": 0.2, "intel": 0.4, "apple": 0.1},
        "CN": {"nvidia": 0.25, "amd": 0.15, "intel": 0.55, "apple": 0.05},
        "global": {"nvidia": 0.35, "amd": 0.25, "intel": 0.35, "apple": 0.05}
    }
    
    region_dist = regional_hardware.get(region, regional_hardware["global"])
    gpu_type = random.choices(
        list(region_dist.keys()), 
        weights=list(region_dist.values())
    )[0]
    
    # Regional screen resolutions
    regional_resolutions = {
        "US": ['1920x1080', '2560x1440', '3840x2160', '3440x1440'],
        "EU": ['1920x1080', '2560x1440', '3840x2160', '1680x1050'],
        "JP": ['1920x1080', '1366x768', '2560x1440', '1536x864'],
        "CN": ['1920x1080', '1366x768', '2560x1440', '1440x900'],
        "global": ['1920x1080', '2560x1440', '1366x768', '3840x2160']
    }
    
    # Modern hardware specifications (2024-2025)
    fingerprint = {
        'persona_id': persona_id or f"quantum_{int(time.time())}_{random.randint(1000,9999)}",
        'cores': random.choice([4, 6, 8, 12, 16]),
        'memory': random.choice([8, 16, 32, 64]),
        'resolution': random.choice(regional_resolutions.get(region, regional_resolutions["global"])),
        'timezone': random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', 'Europe/Paris', 'Asia/Shanghai']),
        'gpu_type': gpu_type,
        'gpu_vendor': self._get_gpu_vendor(gpu_type),
        'gpu_renderer': self._get_gpu_renderer(gpu_type),
        'user_agent': get_quantum_user_agent(),
        'languages': ['en-US', 'en'] + (['es', 'fr'] if random.random() > 0.7 else []),
        'platform': random.choice(['Win32', 'MacIntel', 'Linux x86_64']),
        'region': region,
        'created_at': time.time(),
        'quantum_entropy': random.random(),
        'battery_status': generate_battery_status(),
        'network_connection': generate_network_info(region)
    }
    
    # Reset random seed
    if persona_id:
        random.seed()
    
    return fingerprint

def _get_gpu_vendor(self, gpu_type):
    """Get GPU vendor based on type"""
    vendors = {
        "nvidia": "NVIDIA Corporation",
        "amd": "AMD",
        "intel": "Intel Inc.", 
        "apple": "Apple Inc."
    }
    return vendors.get(gpu_type, "NVIDIA Corporation")

def _get_gpu_renderer(self, gpu_type):
    """Get GPU renderer based on type"""
    renderers = {
        "nvidia": "NVIDIA GeForce RTX 4080/PCIe/SSE2",
        "amd": "AMD Radeon RX 7900 XT", 
        "intel": "Intel(R) UHD Graphics 630",
        "apple": "Apple M2 Pro"
    }
    return renderers.get(gpu_type, "NVIDIA GeForce RTX 4080/PCIe/SSE2")

def generate_battery_status():
    """Generate realistic battery status"""
    return {
        'charging': random.choice([True, False]),
        'level': round(random.uniform(0.2, 0.95), 2),
        'charging_time': random.randint(0, 3600) if random.random() > 0.5 else 0,
        'discharging_time': random.randint(1800, 7200)
    }

def generate_network_info(region="US"):
    """Generate realistic network information with regional variations"""
    regional_networks = {
        "US": {"type": "wifi", "downlink": 100, "rtt": 50, "effectiveType": "4g"},
        "EU": {"type": "wifi", "downlink": 75, "rtt": 70, "effectiveType": "4g"},
        "JP": {"type": "wifi", "downlink": 150, "rtt": 40, "effectiveType": "4g"},
        "CN": {"type": "wifi", "downlink": 50, "rtt": 100, "effectiveType": "3g"},
        "global": {"type": "wifi", "downlink": 75, "rtt": 75, "effectiveType": "4g"}
    }
    
    return regional_networks.get(region, regional_networks["global"])

def load_or_create_persona(persona_id=None, stable=True, region="US"):
    """Enhanced persona management with regional consistency"""
    if stable and persona_id:
        persona_file = f"{PERSONA_DIR}{persona_id}.json"
        if os.path.exists(persona_file):
            try:
                with open(persona_file, "r") as f:
                    persona = json.load(f)
                # Verify persona is not too old (max 7 days) and region matches
                if (time.time() - persona.get('created_at', 0) < 604800 and 
                    persona.get('region') == region):
                    return persona
            except (json.JSONDecodeError, KeyError):
                pass  # File corrupted, create new one
    
    # Create new persona with regional consistency
    persona = generate_quantum_hardware_fingerprint(persona_id, region)
    
    if stable and persona_id:
        persona_file = f"{PERSONA_DIR}{persona_id}.json"
        try:
            with open(persona_file, "w") as f:
                json.dump(persona, f, indent=2)
        except IOError:
            pass  # Couldn't save, but continue with persona
    
    return persona

def rotate_persona(old_persona_id=None, new_region=None):
    """Rotate to new persona while maintaining geographic continuity"""
    old_region = "US"
    if old_persona_id and os.path.exists(f"{PERSONA_DIR}{old_persona_id}.json"):
        try:
            with open(f"{PERSONA_DIR}{old_persona_id}.json", "r") as f:
                old_persona = json.load(f)
                old_region = old_persona.get('region', 'US')
        except:
            pass
    
    # Use same region unless specified
    region = new_region or old_region
    new_persona = generate_quantum_hardware_fingerprint(region=region)
    
    # Carry over stable characteristics for continuity
    if old_persona_id and os.path.exists(f"{PERSONA_DIR}{old_persona_id}.json"):
        try:
            with open(f"{PERSONA_DIR}{old_persona_id}.json", "r") as f:
                old_persona = json.load(f)
                # Maintain geographic consistency
                new_persona['timezone'] = old_persona['timezone']
                new_persona['languages'] = old_persona['languages']
                new_persona['region'] = old_persona['region']
                # Gradual hardware evolution (not abrupt changes)
                if 'cores' in old_persona:
                    # Small variation in core count (±2)
                    old_cores = old_persona['cores']
                    new_persona['cores'] = max(2, min(32, old_cores + random.randint(-2, 2)))
        except:
            pass
    
    return new_persona

def get_quantum_stealth_driver(proxy=None, user_agent=None, headless=False, persona_id=None, config=None, region="US"):
    """Quantum-enhanced stealth driver with advanced fingerprint integration"""
    config = config or settings.current_config
    
    # 🎭 Enhanced persona management with regional consistency
    should_rotate = (config.FINGERPRINT_ROTATION and 
                    random.random() < config.PERSONA_ROTATION_CHANCE)
    
    if should_rotate:
        persona = rotate_persona(persona_id, region)
        if config.DEBUG_MODE:
            print(f"🔄 Persona rotated to: {persona['persona_id']} (Region: {persona['region']})")
    else:
        persona = load_or_create_persona(persona_id, config.STABLE_PERSONA, region)

    options = uc.ChromeOptions()

    # 🕵️ QUANTUM STEALTH ARGUMENTS - ENHANCED FOR 2025
    stealth_args = [
        # Core stealth - Enhanced for 2025
        "--disable-blink-features=AutomationControlled",
        "--disable-blink-features",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-dev-shm-usage",
        "--no-sandbox",
        
        # Performance optimization
        "--disable-background-timer-throttling",
        "--disable-renderer-backgrounding",
        "--disable-backgrounding-occluded-windows",
        "--disable-ipc-flooding-protection",
        
        # Privacy & security - Enhanced for Google services
        "--disable-web-security",
        "--disable-popup-blocking", 
        "--disable-translate",
        "--mute-audio",
        "--disable-logging",
        "--disable-extensions",
        
        # Advanced features disable - Specifically for Google detection
        "--disable-features=VizDisplayCompositor,TranslateUI,BlinkGenPropertyTrees,PrivacySandboxAdsAPIs",
        "--disable-component-extensions-with-background-pages",
        "--disable-default-apps",
        "--disable-domain-reliability",
        "--disable-client-side-phishing-detection",
        
        # Network enhancements
        "--aggressive-cache-discard",
        "--media-cache-size=1",
        "--disk-cache-size=1",
        
        # Window settings with realistic variations
        f"--window-size={persona['resolution'].replace('x', ',')}",
        f"--user-agent={user_agent or persona['user_agent']}"
    ]

    if headless:
        stealth_args.extend([
            "--headless=new",
            "--disable-gpu",
            "--remote-debugging-port=0",
            "--no-zygote",
            "--disable-software-rasterizer"
        ])
    else:
        # Add realistic window position and behavior for visible mode
        stealth_args.extend([
            f"--window-position={random.randint(0,500)},{random.randint(0,300)}",
            "--disable-backgrounding-occluded-windows=false",  # More natural for visible
            "--disable-renderer-backgrounding=false"
        ])

    # Add all stealth arguments
    for arg in stealth_args:
        options.add_argument(arg)

    # 🚫 Enhanced automation detection removal for Google services
    options.add_experimental_option("excludeSwitches", [
        "enable-automation", 
        "enable-logging", 
        "load-extension",
        "test-type",
        "ignore-certificate-errors",
        "disable-component-extensions",
        "disable-background-timer-throttling"
    ])
    
    options.add_experimental_option('useAutomationExtension', False)
    
    # Advanced preferences for realistic behavior
    options.add_experimental_option("prefs", {
        # Privacy settings
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        
        # Advanced preferences for Google evasion
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.images": 1,
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.camera": 2,
        "profile.default_content_setting_values.microphone": 2,
        
        # Anti-fingerprinting enhancements
        "profile.managed_default_content_settings.stylesheets": 1,
        "profile.managed_default_content_settings.plugins": 1,
        "profile.managed_default_content_settings.media_stream": 2,
        
        # Google-specific evasion
        "profile.managed_default_content_settings.clipboard": 2,
        "profile.default_content_setting_values.cookies": 1,
        
        # Performance optimizations
        "profile.default_content_setting_values.javascript": 1,
        "profile.managed_default_content_settings.scripts": 1,
    })

    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    # 🚀 Create driver with optimized settings
    driver = uc.Chrome(
        options=options, 
        use_subprocess=False,
        headless=headless,
        version_main=125  # Force Chrome 125 for consistency
    )

    # 💉 ENHANCED QUANTUM STEALTH SCRIPTS WITH ADVANCED FINGERPRINTING
    stealth_scripts = []
    
    # Initialize quantum fingerprint spoofer
    fingerprint_spoofer = QuantumFingerprintSpoofer()
    
    # 1. COMPREHENSIVE FINGERPRINT PROTECTION
    comprehensive_script = fingerprint_spoofer.get_comprehensive_fingerprint_protection(
        region=persona.get('region', 'US'),
        gpu_type=persona.get('gpu_type', 'nvidia')
    )
    stealth_scripts.append(comprehensive_script)
    
    # 2. CORE AUTOMATION REMOVAL - ENHANCED
    stealth_scripts.append("""
    // ENHANCED AUTOMATION DETECTION REMOVAL
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined,
        configurable: true
    });
    
    // Remove all automation traces
    delete navigator.__proto__.webdriver;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl;
    delete window.document.$cdc_asdjflasutopfhvcZLmcfl;
    
    // Override permissions API
    const originalQuery = Permissions.prototype.query;
    Permissions.prototype.query = function(permissionDesc) {
        if (permissionDesc.name === 'notifications') {
            return Promise.resolve({ state: 'denied' });
        }
        return originalQuery.call(this, permissionDesc);
    };
    """)
    
    # 3. ENHANCED HARDWARE SPOOFING
    stealth_scripts.append(f"""
    // ENHANCED HARDWARE CHARACTERISTICS SPOOFING
    Object.defineProperty(navigator, 'hardwareConcurrency', {{
        get: () => {persona['cores']},
        configurable: true
    }});
    
    Object.defineProperty(navigator, 'deviceMemory', {{
        get: () => {persona['memory']},
        configurable: true
    }});
    
    Object.defineProperty(navigator, 'maxTouchPoints', {{
        get: () => {random.choice([0, 5, 10])},
        configurable: true
    }});
    
    // Advanced CPU architecture spoofing
    Object.defineProperty(navigator, 'cpuClass', {{
        get: () => 'unknown',
        configurable: true
    }});
    
    Object.defineProperty(navigator, 'platform', {{
        get: () => '{persona['platform']}',
        configurable: true
    }});
    """)
    
    # 4. REGIONAL LANGUAGE AND LOCALE SPOOFING
    stealth_scripts.append(f"""
    // REGIONAL LANGUAGE AND LOCALE CONSISTENCY
    Object.defineProperty(navigator, 'language', {{ 
        get: () => '{persona['languages'][0]}',
        configurable: true 
    }});
    
    Object.defineProperty(navigator, 'languages', {{ 
        get: () => {persona['languages']},
        configurable: true 
    }});
    
    Object.defineProperty(navigator, 'userAgent', {{
        get: () => '{persona['user_agent']}',
        configurable: true
    }});
    """)
    
    # 5. ENHANCED SCREEN PROPERTIES WITH REGIONAL CONSISTENCY
    width, height = persona['resolution'].split('x')
    stealth_scripts.append(f"""
    // ENHANCED SCREEN PROPERTIES SPOOFING
    Object.defineProperty(screen, 'width', {{ get: () => {width} }});
    Object.defineProperty(screen, 'height', {{ get: () => {height} }});
    Object.defineProperty(screen, 'availWidth', {{ get: () => {int(width) - random.randint(80, 120)} }});
    Object.defineProperty(screen, 'availHeight', {{ get: () => {int(height) - random.randint(80, 120)} }});
    Object.defineProperty(screen, 'colorDepth', {{ get: () => 24 }});
    Object.defineProperty(screen, 'pixelDepth', {{ get: () => 24 }});
    Object.defineProperty(screen, 'availLeft', {{ get: () => 0 }});
    Object.defineProperty(screen, 'availTop', {{ get: () => 0 }});
    
    // Enhanced pixel ratio based on device type
    const pixelRatios = {{
        'Win32': 1.0,
        'MacIntel': 2.0,
        'Linux x86_64': 1.0
    }};
    Object.defineProperty(window, 'devicePixelRatio', {{
        get: () => pixelRatios['{persona['platform']}'] || 1.0,
        configurable: true
    }});
    """)
    
    # 6. TIMEZONE AND LOCALE SPOOFING WITH CONSISTENCY
    stealth_scripts.append(f"""
    // TIMEZONE AND LOCALE CONSISTENCY
    Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{
        get: () => () => ({{
            timeZone: '{persona['timezone']}',
            locale: 'en-US',
            calendar: 'gregory',
            numberingSystem: 'latn'
        }}),
        configurable: true
    }});
    
    // Override Date.toString for timezone consistency
    const originalDateToString = Date.prototype.toString;
    Date.prototype.toString = function() {{
        const offset = this.getTimezoneOffset();
        return originalDateToString.call(this).replace(/GMT[+-]\\d{{4}}/, `GMT${{offset > 0 ? '-' : '+'}}${{Math.abs(offset/60).toString().padStart(2, '0')}}00`);
    }};
    
    // Locale-aware number formatting
    const originalToLocaleString = Number.prototype.toLocaleString;
    Number.prototype.toLocaleString = function(locale, options) {{
        return originalToLocaleString.call(this, '{persona['languages'][0]}', options);
    }};
    """)
    
    # 7. BATTERY API SPOOFING WITH REALISTIC PATTERNS
    stealth_scripts.append(f"""
    // BATTERY API SPOOFING WITH REALISTIC PATTERNS
    if ('getBattery' in navigator) {{
        const originalGetBattery = navigator.getBattery;
        navigator.getBattery = function() {{
            return Promise.resolve({{
                charging: {str(persona['battery_status']['charging']).lower()},
                chargingTime: {persona['battery_status']['charging_time']},
                dischargingTime: {persona['battery_status']['discharging_time']},
                level: {persona['battery_status']['level']},
                addEventListener: function() {{}},
                removeEventListener: function() {{}}
            }});
        }};
    }}
    
    // Simulate battery level changes over time
    let batterySimulation = {{
        level: {persona['battery_status']['level']},
        charging: {str(persona['battery_status']['charging']).lower()}
    }};
    
    setInterval(() => {{
        if (!batterySimulation.charging) {{
            batterySimulation.level = Math.max(0.05, batterySimulation.level - 0.001);
        }} else {{
            batterySimulation.level = Math.min(1.0, batterySimulation.level + 0.002);
        }}
    }}, 60000); // Update every minute
    """)
    
    # 8. PERFORMANCE API SPOOFING WITH REALISTIC METRICS
    stealth_scripts.append("""
    // PERFORMANCE API SPOOFING WITH REALISTIC METRICS
    const originalNow = performance.now;
    let timeOffset = 0;
    performance.now = function() {
        const realTime = originalNow.call(this);
        // Small, consistent offset that changes slowly
        timeOffset += (Math.random() - 0.5) * 0.1;
        return realTime + timeOffset;
    };
    
    // Spoof performance memory with realistic values
    if (performance.memory) {
        Object.defineProperty(performance.memory, 'usedJSHeapSize', {
            get: () => Math.floor(Math.random() * 100000000) + 50000000
        });
        
        Object.defineProperty(performance.memory, 'totalJSHeapSize', {
            get: () => Math.floor(Math.random() * 200000000) + 100000000
        });
        
        Object.defineProperty(performance.memory, 'jsHeapSizeLimit', {
            get: () => Math.floor(Math.random() * 400000000) + 200000000
        });
    }
    
    // Spoof navigation timing
    const originalGetEntriesByType = performance.getEntriesByType;
    performance.getEntriesByType = function(type) {
        if (type === 'navigation') {
            const realEntries = originalGetEntriesByType.call(this, type);
            if (realEntries.length > 0) {
                const navEntry = realEntries[0];
                // Add small variations to timing
                navEntry.domainLookupStart += Math.random() * 10;
                navEntry.connectStart += Math.random() * 15;
                navEntry.responseStart += Math.random() * 20;
            }
            return realEntries;
        }
        return originalGetEntriesByType.call(this, type);
    };
    """)
    
    # 9. GOOGLE-SPECIFIC EVASION ENHANCEMENTS
    stealth_scripts.append("""
    // ENHANCED GOOGLE-SPECIFIC EVASION TECHNIQUES
    // reCAPTCHA v3 evasion
    if (typeof window.grecaptcha !== 'undefined') {
        window.grecaptcha.execute = function() {
            return Promise.resolve('fake_recaptcha_token_' + Math.random().toString(36).substr(2));
        };
        
        window.grecaptcha.ready = function(callback) {
            if (callback) setTimeout(callback, 100);
        };
    }
    
    // Google Analytics evasion
    window['ga-disable-GA_MEASUREMENT_ID'] = true;
    if (window.ga) {
        const originalGa = window.ga;
        window.ga = function() {
            console.log('GA call intercepted:', arguments);
            return originalGa.apply(this, arguments);
        };
    }
    
    // Google Tag Manager evasion
    if (window.dataLayer) {
        const originalPush = window.dataLayer.push;
        window.dataLayer.push = function() {
            console.log('GTM push intercepted:', arguments);
            return originalPush.apply(this, arguments);
        };
    }
    
    // Google Fonts evasion
    const originalCreateElement = document.createElement;
    document.createElement = function(tagName) {
        const element = originalCreateElement.call(this, tagName);
        if (tagName.toLowerCase() === 'link') {
            const originalSetAttribute = element.setAttribute;
            element.setAttribute = function(name, value) {
                if (name === 'href' && value && value.includes('fonts.googleapis.com')) {
                    return; // Block Google Fonts
                }
                return originalSetAttribute.call(this, name, value);
            };
        }
        return element;
    };
    """)

    # Execute all enhanced stealth scripts with error handling
    for i, script in enumerate(stealth_scripts):
        try:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
            if config.DEBUG_MODE:
                print(f"✅ Enhanced stealth script {i+1}/{len(stealth_scripts)} injected")
            time.sleep(0.02)  # Optimized delay for faster injection
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"⚠️ Enhanced stealth script {i+1} injection warning: {e}")
            continue

    # Additional quantum evasion: behavioral realism initialization
    try:
        driver.execute_script("""
            // Initialize behavioral realism metrics
            window.quantumBehavior = {
                mouseMovements: 0,
                clicks: 0,
                scrolls: 0,
                startTime: Date.now()
            };
            
            // Simulate human-like initial behaviors
            setTimeout(() => { 
                // Micro-movements for realism
                window.moveBy(1, 1); 
                setTimeout(() => window.moveBy(-1, -1), 100);
                
                // Initial focus behavior
                if (document.activeElement) {
                    document.activeElement.blur();
                    setTimeout(() => document.activeElement.focus(), 50);
                }
            }, 500);
        """)
    except:
        pass

    return driver, persona

# Backward compatibility
def get_stealth_driver(proxy=None, headless=False, user_agent=None):
    """Legacy function for backward compatibility"""
    return get_quantum_stealth_driver(proxy, user_agent, headless)

def cleanup_old_personas(max_age_days=7):
    """Clean up personas older than max_age_days"""
    cutoff_time = time.time() - (max_age_days * 24 * 60 * 60)
    
    for filename in os.listdir(PERSONA_DIR):
        if filename.endswith('.json'):
            filepath = os.path.join(PERSONA_DIR, filename)
            try:
                file_time = os.path.getmtime(filepath)
                if file_time < cutoff_time:
                    os.remove(filepath)
                    print(f"🧹 Cleaned up old persona: {filename}")
            except OSError:
                pass  # Couldn't delete, skip

# Persona management utilities
def get_persona_stats():
    """Get statistics about stored personas"""
    personas = []
    for filename in os.listdir(PERSONA_DIR):
        if filename.endswith('.json'):
            filepath = os.path.join(PERSONA_DIR, filename)
            try:
                with open(filepath, 'r') as f:
                    persona = json.load(f)
                    personas.append({
                        'id': persona.get('persona_id', 'unknown'),
                        'created': datetime.fromtimestamp(persona.get('created_at', 0)),
                        'user_agent': persona.get('user_agent', 'unknown'),
                        'platform': persona.get('platform', 'unknown'),
                        'region': persona.get('region', 'unknown')
                    })
            except:
                continue
    
    return {
        'total_personas': len(personas),
        'personas': personas[:10],  # First 10
        'oldest': min([p['created'] for p in personas]) if personas else None,
        'newest': max([p['created'] for p in personas]) if personas else None,
        'regions': list(set([p['region'] for p in personas]))
    }

# Regional utility functions
def get_regional_persona(region="US"):
    """Get a persona specifically for a region"""
    return generate_quantum_hardware_fingerprint(region=region)

def validate_persona_consistency(persona):
    """Validate that persona attributes are consistent"""
    checks = []
    
    # Check region and language consistency
    if persona.get('region') == 'US' and 'en' not in str(persona.get('languages', [])):
        checks.append('Language inconsistent with region')
    
    # Check platform and resolution consistency
    if persona.get('platform') == 'MacIntel' and '1920x1080' in persona.get('resolution', ''):
        checks.append('Resolution uncommon for Mac')
    
    # Check GPU and platform consistency
    if persona.get('gpu_type') == 'apple' and persona.get('platform') != 'MacIntel':
        checks.append('GPU inconsistent with platform')
    
    return len(checks) == 0, checks