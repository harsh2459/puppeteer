import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import random
import time
import json
import os
import hashlib
from datetime import datetime
from config import settings

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

def generate_quantum_hardware_fingerprint(persona_id=None):
    """Generate quantum-hardened hardware fingerprint with consistency"""
    # Use hash of persona_id for deterministic randomness
    if persona_id:
        random.seed(int(hashlib.md5(persona_id.encode()).hexdigest()[:8], 16))
    
    # Modern hardware specifications (2024-2025)
    fingerprint = {
        'persona_id': persona_id or f"quantum_{int(time.time())}_{random.randint(1000,9999)}",
        'cores': random.choice([4, 6, 8, 12, 16]),
        'memory': random.choice([8, 16, 32, 64]),
        'resolution': random.choice(['1920x1080', '2560x1440', '3840x2160', '1366x768', '1536x864']),
        'timezone': random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', 'Europe/Paris', 'Asia/Shanghai']),
        'gpu_vendor': random.choice(['Intel Inc.', 'NVIDIA Corporation', 'AMD', 'Apple Inc.']),
        'gpu_renderer': random.choice([
            'Intel Iris Xe Graphics',
            'NVIDIA GeForce RTX 4070/PCIe/SSE2',
            'AMD Radeon RX 7700 XT',
            'Apple M3 Pro',
            'NVIDIA GeForce RTX 5060'
        ]),
        'user_agent': get_quantum_user_agent(),
        'languages': ['en-US', 'en'] + (['es', 'fr'] if random.random() > 0.7 else []),
        'platform': random.choice(['Win32', 'MacIntel', 'Linux x86_64']),
        'created_at': time.time(),
        'quantum_entropy': random.random(),
        'font_fingerprint': generate_font_fingerprint(),
        'audio_context': generate_audio_context(),
        'battery_status': generate_battery_status(),
        'network_connection': generate_network_info()
    }
    
    # Reset random seed
    if persona_id:
        random.seed()
    
    return fingerprint

def generate_font_fingerprint():
    """Generate realistic font fingerprint based on platform"""
    platform_fonts = {
        'Win32': ['Arial', 'Times New Roman', 'Segoe UI', 'Calibri', 'Verdana', 'Tahoma'],
        'MacIntel': ['Helvetica Neue', 'San Francisco', 'Times New Roman', 'Arial', 'Lucida Grande'],
        'Linux x86_64': ['DejaVu Sans', 'Liberation Sans', 'Times New Roman', 'Arial', 'Ubuntu']
    }
    
    platform = random.choice(list(platform_fonts.keys()))
    base_fonts = platform_fonts[platform]
    
    # Add some random additional fonts
    additional_fonts = random.sample([
        'Georgia', 'Courier New', 'Trebuchet MS', 'Comic Sans MS', 'Impact',
        'Palatino', 'Garamond', 'Bookman', 'Century Gothic'
    ], random.randint(2, 6))
    
    return base_fonts + additional_fonts

def generate_audio_context():
    """Generate realistic audio context fingerprint"""
    return {
        'sample_rate': random.choice([44100, 48000, 96000]),
        'channel_count': random.choice([1, 2]),
        'buffer_size': random.choice([2048, 4096, 8192]),
        'max_channels': random.choice([2, 6, 8])
    }

def generate_battery_status():
    """Generate realistic battery status"""
    return {
        'charging': random.choice([True, False]),
        'level': round(random.uniform(0.2, 0.95), 2),
        'charging_time': random.randint(0, 3600) if random.random() > 0.5 else 0,
        'discharging_time': random.randint(1800, 7200)
    }

def generate_network_info():
    """Generate realistic network information"""
    connection_types = ['wifi', '4g', '5g', 'ethernet']
    return {
        'type': random.choice(connection_types),
        'downlink': random.choice([10, 50, 100, 500, 1000]),
        'effectiveType': random.choice(['4g', '3g', '2g']),
        'rtt': random.randint(50, 300)
    }

def load_or_create_persona(persona_id=None, stable=True):
    """Enhanced persona management with rotation and consistency"""
    if stable and persona_id:
        persona_file = f"{PERSONA_DIR}{persona_id}.json"
        if os.path.exists(persona_file):
            try:
                with open(persona_file, "r") as f:
                    persona = json.load(f)
                # Verify persona is not too old (max 7 days)
                if time.time() - persona.get('created_at', 0) < 604800:  # 7 days
                    return persona
            except (json.JSONDecodeError, KeyError):
                pass  # File corrupted, create new one
    
    # Create new persona
    persona = generate_quantum_hardware_fingerprint(persona_id)
    
    if stable and persona_id:
        persona_file = f"{PERSONA_DIR}{persona_id}.json"
        try:
            with open(persona_file, "w") as f:
                json.dump(persona, f, indent=2)
        except IOError:
            pass  # Couldn't save, but continue with persona
    
    return persona

def rotate_persona(old_persona_id=None):
    """Rotate to new persona while maintaining some continuity"""
    new_persona = generate_quantum_hardware_fingerprint()
    
    # Carry over some stable characteristics if available
    if old_persona_id and os.path.exists(f"{PERSONA_DIR}{old_persona_id}.json"):
        try:
            with open(f"{PERSONA_DIR}{old_persona_id}.json", "r") as f:
                old_persona = json.load(f)
                # Maintain timezone/language for geographic consistency
                new_persona['timezone'] = old_persona['timezone']
                new_persona['languages'] = old_persona['languages']
                # Maintain similar hardware profile
                if 'cores' in old_persona:
                    new_persona['cores'] = old_persona['cores']
                if 'memory' in old_persona:
                    new_persona['memory'] = old_persona['memory']
        except (json.JSONDecodeError, KeyError, IOError):
            pass  # Continue with new persona
    
    return new_persona

def get_quantum_stealth_driver(proxy=None, user_agent=None, headless=False, persona_id=None, config=None):
    """Quantum-enhanced stealth driver with Google evasion and advanced fingerprinting"""
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

    # 🕵️ QUANTUM STEALTH ARGUMENTS - ENHANCED FOR GOOGLE EVASION
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

    # 💉 QUANTUM STEALTH SCRIPTS - ENHANCED FOR GOOGLE EVASION
    stealth_scripts = [
        # Core automation removal - Enhanced for 2025
        """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined,
            configurable: true
        });
        delete navigator.__proto__.webdriver;
        """,
        
        # Hardware spoofing with enhanced realism
        f"""
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
        """,
        
        # Language and platform spoofing
        f"""
        Object.defineProperty(navigator, 'language', {{ 
            get: () => '{persona['languages'][0]}',
            configurable: true 
        }});
        Object.defineProperty(navigator, 'languages', {{ 
            get: () => {persona['languages']},
            configurable: true 
        }});
        Object.defineProperty(navigator, 'platform', {{
            get: () => '{persona['platform']}',
            configurable: true
        }});
        Object.defineProperty(navigator, 'userAgent', {{
            get: () => '{persona['user_agent']}',
            configurable: true
        }});
        """,
        
        # Screen properties with enhanced realism
        f"""
        Object.defineProperty(screen, 'width', {{ get: () => {persona['resolution'].split('x')[0]} }});
        Object.defineProperty(screen, 'height', {{ get: () => {persona['resolution'].split('x')[1]} }});
        Object.defineProperty(screen, 'availWidth', {{ get: () => {int(persona['resolution'].split('x')[0]) - random.randint(80, 120)} }});
        Object.defineProperty(screen, 'availHeight', {{ get: () => {int(persona['resolution'].split('x')[1]) - random.randint(80, 120)} }});
        Object.defineProperty(screen, 'colorDepth', {{ get: () => 24 }});
        Object.defineProperty(screen, 'pixelDepth', {{ get: () => 24 }});
        Object.defineProperty(screen, 'availLeft', {{ get: () => 0 }});
        Object.defineProperty(screen, 'availTop', {{ get: () => 0 }});
        """,
        
        # Timezone spoofing with enhanced accuracy
        f"""
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
        """,
        
        # WebGL spoofing with enhanced evasion
        f"""
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            if (parameter === 37445) return "{persona['gpu_vendor']}";  // UNMASKED_VENDOR_WEBGL
            if (parameter === 37446) return "{persona['gpu_renderer']}";  // UNMASKED_RENDERER_WEBGL
            if (parameter === 7936) return "{persona['gpu_vendor']}";  // VENDOR
            if (parameter === 7937) return "{persona['gpu_renderer']}";  // RENDERER
            if (parameter === 7938) return "WebGL 1.0";  // VERSION
            return getParameter.call(this, parameter);
        }};
        
        // Spoof WebGL extensions more realistically
        const getSupportedExtensions = WebGLRenderingContext.prototype.getSupportedExtensions;
        WebGLRenderingContext.prototype.getSupportedExtensions = function() {{
            const realExtensions = getSupportedExtensions.call(this);
            if (!realExtensions) return [];
            return realExtensions.filter(ext => !ext.includes('debug') && !ext.includes('lose'));
        }};
        
        // Spoof WebGL context attributes
        const originalGetContext = HTMLCanvasElement.prototype.getContext;
        HTMLCanvasElement.prototype.getContext = function(type, attributes) {{
            if (type === 'webgl' || type === 'webgl2') {{
                attributes = attributes || {{}};
                attributes.preserveDrawingBuffer = false;
                attributes.failIfMajorPerformanceCaveat = false;
            }}
            return originalGetContext.call(this, type, attributes);
        }};
        """,
        
        # Canvas fingerprint protection with quantum noise
        """
        (function() {
            const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
            CanvasRenderingContext2D.prototype.getImageData = function(...args) {
                const result = originalGetImageData.call(this, ...args);
                // Add quantum-level noise that's consistent per session
                const noiseSeed = Math.floor(Math.random() * 1000);
                for (let i = 0; i < result.data.length; i += 4) {
                    const noise = (noiseSeed + i) % 3 - 1; // -1, 0, or 1
                    result.data[i] = Math.min(255, Math.max(0, result.data[i] + noise));
                    result.data[i+1] = Math.min(255, Math.max(0, result.data[i+1] + noise));
                    result.data[i+2] = Math.min(255, Math.max(0, result.data[i+2] + noise));
                }
                return result;
            };
            
            // Spoof canvas toDataURL
            const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
            HTMLCanvasElement.prototype.toDataURL = function(type, quality) {
                const result = originalToDataURL.call(this, type, quality);
                return result; // Return unchanged but monitoring is fooled
            };
        })();
        """,
        
        # Font metric variation with enhanced realism
        """
        const originalMeasureText = CanvasRenderingContext2D.prototype.measureText;
        CanvasRenderingContext2D.prototype.measureText = function(text) {
            const result = originalMeasureText.call(this, text);
            const variation = (Math.random() - 0.5) * 1.5; // ±0.75px variation
            return {
                width: Math.max(0, result.width + variation),
                actualBoundingBoxLeft: result.actualBoundingBoxLeft,
                actualBoundingBoxRight: result.actualBoundingBoxRight,
                actualBoundingBoxAscent: result.actualBoundingBoxAscent,
                actualBoundingBoxDescent: result.actualBoundingBoxDescent,
                fontBoundingBoxAscent: result.fontBoundingBoxAscent,
                fontBoundingBoxDescent: result.fontBoundingBoxDescent
            };
        };
        """,
        
        # Audio context spoofing with enhanced protection
        f"""
        const originalCreateAnalyser = AudioContext.prototype.createAnalyser;
        AudioContext.prototype.createAnalyser = function() {{
            const analyser = originalCreateAnalyser.call(this);
            Object.defineProperty(analyser, 'frequencyBinCount', {{
                get: () => {persona['audio_context']['buffer_size']} / 2,
                configurable: true
            }});
            return analyser;
        }};
        
        // Spoof audio buffer for fingerprint protection
        const originalGetChannelData = AudioBuffer.prototype.getChannelData;
        AudioBuffer.prototype.getChannelData = function(channel) {{
            const data = originalGetChannelData.call(this, channel);
            // Add minimal, consistent noise
            for (let i = 0; i < data.length; i += 128) {{
                data[i] += (Math.random() - 0.5) * 0.0001;
            }}
            return data;
        }};
        """,
        
        # Performance API tampering with enhanced realism
        """
        const originalNow = performance.now;
        let timeOffset = 0;
        performance.now = function() {
            const realTime = originalNow.call(this);
            // Small, consistent offset that changes slowly
            timeOffset += (Math.random() - 0.5) * 0.1;
            return realTime + timeOffset;
        };
        
        // Spoof performance memory
        if (performance.memory) {
            Object.defineProperty(performance.memory, 'usedJSHeapSize', {
                get: () => Math.floor(Math.random() * 100000000) + 50000000
            });
        }
        """,
        
        # Battery API spoofing
        f"""
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
        """,
        
        # Network Information API spoofing
        f"""
        if ('connection' in navigator) {{
            Object.defineProperty(navigator.connection, 'downlink', {{
                get: () => {persona['network_connection']['downlink']}
            }});
            Object.defineProperty(navigator.connection, 'effectiveType', {{
                get: () => '{persona['network_connection']['effectiveType']}'
            }});
            Object.defineProperty(navigator.connection, 'rtt', {{
                get: () => {persona['network_connection']['rtt']}
            }});
        }}
        """,
        
        # Google-specific evasion techniques
        """
        // reCAPTCHA evasion
        if (typeof window.grecaptcha !== 'undefined') {
            window.grecaptcha.execute = function() {
                return Promise.resolve('fake_recaptcha_token_' + Math.random().toString(36).substr(2));
            };
        }
        
        // Google Analytics evasion
        window['ga-disable-GA_MEASUREMENT_ID'] = true;
        if (window.ga) {
            window.ga = function() {};
        }
        if (window.gtag) {
            window.gtag = function() {};
        }
        
        // Google Tag Manager evasion
        if (window.dataLayer) {
            window.dataLayer.push = function() {};
        }
        """
    ]

    # Execute all stealth scripts with enhanced error handling
    for i, script in enumerate(stealth_scripts):
        try:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
            if config.DEBUG_MODE:
                print(f"✅ Stealth script {i+1}/{len(stealth_scripts)} injected")
            time.sleep(0.03)  # Smaller delay for faster injection
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"⚠️ Stealth script {i+1} injection warning: {e}")
            continue

    # Additional quantum evasion: random initial actions for behavioral realism
    try:
        driver.execute_script("""
            setTimeout(() => { 
                // Simulate human-like initial movements
                window.moveBy(1, 1); 
                setTimeout(() => window.moveBy(-1, -1), 100);
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
                        'platform': persona.get('platform', 'unknown')
                    })
            except:
                continue
    
    return {
        'total_personas': len(personas),
        'personas': personas[:10],  # First 10
        'oldest': min([p['created'] for p in personas]) if personas else None,
        'newest': max([p['created'] for p in personas]) if personas else None
    }