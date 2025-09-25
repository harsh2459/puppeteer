import random
import time
import hashlib
from selenium.webdriver.common.by import By
from config import settings

class HardwareSpoofer:
    def __init__(self, config):
        self.config = config
        self.hardware_profiles = self._init_hardware_profiles()
        self.current_profile = {}
        self.spoofing_history = []
        self.entropy_source = random.random()
        
    def _init_hardware_profiles(self):
        """Initialize realistic hardware profiles for different device types"""
        return {
            'gaming_pc': {
                'cores': 12,
                'threads': 24,
                'memory': 32,
                'gpu_vendor': 'NVIDIA Corporation',
                'gpu_renderer': 'NVIDIA GeForce RTX 4080/PCIe/SSE2',
                'max_touch_points': 0,
                'device_memory': 32,
                'hardware_concurrency': 12,
                'screen_resolution': '3840x2160',
                'color_depth': 30,
                'pixel_ratio': 1.0
            },
            'office_desktop': {
                'cores': 8,
                'threads': 16,
                'memory': 16,
                'gpu_vendor': 'Intel Inc.',
                'gpu_renderer': 'Intel(R) UHD Graphics 770',
                'max_touch_points': 0,
                'device_memory': 16,
                'hardware_concurrency': 8,
                'screen_resolution': '1920x1080',
                'color_depth': 24,
                'pixel_ratio': 1.0
            },
            'macbook_pro': {
                'cores': 10,
                'threads': 10,
                'memory': 16,
                'gpu_vendor': 'Apple Inc.',
                'gpu_renderer': 'Apple M2 Pro',
                'max_touch_points': 5,
                'device_memory': 16,
                'hardware_concurrency': 10,
                'screen_resolution': '3024x1964',
                'color_depth': 30,
                'pixel_ratio': 2.0
            },
            'ultrabook': {
                'cores': 4,
                'threads': 8,
                'memory': 8,
                'gpu_vendor': 'Intel Inc.',
                'gpu_renderer': 'Intel Iris Xe Graphics',
                'max_touch_points': 10,
                'device_memory': 8,
                'hardware_concurrency': 4,
                'screen_resolution': '1920x1080',
                'color_depth': 24,
                'pixel_ratio': 1.25
            },
            'budget_laptop': {
                'cores': 2,
                'threads': 4,
                'memory': 4,
                'gpu_vendor': 'AMD',
                'gpu_renderer': 'AMD Radeon Graphics',
                'max_touch_points': 0,
                'device_memory': 4,
                'hardware_concurrency': 2,
                'screen_resolution': '1366x768',
                'color_depth': 24,
                'pixel_ratio': 1.0
            }
        }
    
    def apply_hardware_spoofing(self, driver, profile_name=None):
        """Apply comprehensive hardware spoofing to browser"""
        if not self.config.ENABLE_BIOMETRIC_SIMULATION:
            return self.current_profile
            
        try:
            # Select or generate hardware profile
            if profile_name and profile_name in self.hardware_profiles:
                hardware_profile = self.hardware_profiles[profile_name].copy()
            else:
                hardware_profile = self._generate_dynamic_profile()
            
            # Apply hardware spoofing scripts
            self._spoof_cpu_characteristics(driver, hardware_profile)
            self._spoof_gpu_characteristics(driver, hardware_profile)
            self._spoof_memory_characteristics(driver, hardware_profile)
            self._spoof_screen_characteristics(driver, hardware_profile)
            self._spoof_input_characteristics(driver, hardware_profile)
            self._spoof_audio_characteristics(driver, hardware_profile)
            self._spoof_battery_characteristics(driver, hardware_profile)
            
            # Store current profile and history
            self.current_profile = hardware_profile
            self.spoofing_history.append({
                'timestamp': time.time(),
                'profile': hardware_profile,
                'profile_name': profile_name or 'dynamic'
            })
            
            if self.config.DEBUG_MODE:
                print(f"🖥️ Hardware spoofing applied: {profile_name or 'dynamic'}")
            
            return hardware_profile
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Hardware spoofing failed: {e}")
            return self.current_profile
    
    def _generate_dynamic_profile(self):
        """Generate dynamic hardware profile with realistic variations"""
        base_profiles = list(self.hardware_profiles.values())
        base_profile = random.choice(base_profiles).copy()
        
        # Apply realistic variations
        variations = {
            'cores': random.randint(-2, 2),
            'memory': random.choice([-4, -2, 0, 2, 4]),
            'hardware_concurrency': random.randint(-2, 2)
        }
        
        # Apply variations
        base_profile['cores'] = max(1, base_profile['cores'] + variations['cores'])
        base_profile['threads'] = base_profile['cores'] * 2
        base_profile['memory'] = max(4, base_profile['memory'] + variations['memory'])
        base_profile['device_memory'] = base_profile['memory']
        base_profile['hardware_concurrency'] = max(1, base_profile['hardware_concurrency'] + variations['hardware_concurrency'])
        
        # Add unique identifier
        base_profile['hardware_hash'] = self._generate_hardware_hash(base_profile)
        
        return base_profile
    
    def _generate_hardware_hash(self, profile):
        """Generate unique hardware hash for consistency"""
        profile_str = ''.join(f"{k}{v}" for k, v in sorted(profile.items()))
        return hashlib.md5(profile_str.encode()).hexdigest()[:16]
    
    def _spoof_cpu_characteristics(self, driver, profile):
        """Spoof CPU-related characteristics"""
        script = f"""
        // CPU characteristics spoofing
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {profile['hardware_concurrency']},
            configurable: true
        }});
        
        // Additional CPU information
        Object.defineProperty(navigator, 'cpuClass', {{
            get: () => 'unknown',
            configurable: true
        }});
        
        // Processor architecture
        Object.defineProperty(navigator, 'platform', {{
            get: () => '{random.choice(['Win32', 'MacIntel', 'Linux x86_64'])}',
            configurable: true
        }});
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ CPU spoofing failed: {e}")
    
    def _spoof_gpu_characteristics(self, driver, profile):
        """Spoof GPU-related characteristics"""
        script = f"""
        // WebGL vendor and renderer spoofing
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            switch(parameter) {{
                case 37445: // UNMASKED_VENDOR_WEBGL
                    return "{profile['gpu_vendor']}";
                case 37446: // UNMASKED_RENDERER_WEBGL
                    return "{profile['gpu_renderer']}";
                case 7936: // VENDOR
                    return "{profile['gpu_vendor']}";
                case 7937: // RENDERER
                    return "{profile['gpu_renderer']}";
                case 7938: // VERSION
                    return "WebGL 1.0";
                default:
                    return getParameter.call(this, parameter);
            }}
        }};
        
        // WebGL context attributes
        const originalGetContext = HTMLCanvasElement.prototype.getContext;
        HTMLCanvasElement.prototype.getContext = function(type, attributes) {{
            if (type === 'webgl' || type === 'webgl2') {{
                attributes = attributes || {{}};
                attributes.preserveDrawingBuffer = false;
                attributes.failIfMajorPerformanceCaveat = false;
            }}
            return originalGetContext.call(this, type, attributes);
        }};
        
        // GPU memory information (if available)
        if (navigator.gpu) {{
            Object.defineProperty(navigator.gpu, 'memory', {{
                get: () => ({{
                    total: {profile['memory']} * 1024 * 1024 * 1024,
                    used: Math.floor(Math.random() * {profile['memory']} * 1024 * 1024 * 1024 * 0.7)
                }}),
                configurable: true
            }});
        }}
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ GPU spoofing failed: {e}")
    
    def _spoof_memory_characteristics(self, driver, profile):
        """Spoof memory-related characteristics"""
        script = f"""
        // Device memory spoofing
        Object.defineProperty(navigator, 'deviceMemory', {{
            get: () => {profile['device_memory']},
            configurable: true
        }});
        
        // Performance memory spoofing
        if (performance.memory) {{
            Object.defineProperty(performance.memory, 'jsHeapSizeLimit', {{
                get: () => {profile['memory']} * 1024 * 1024 * 1024 * 0.7,
                configurable: true
            }});
            
            Object.defineProperty(performance.memory, 'totalJSHeapSize', {{
                get: () => Math.floor({profile['memory']} * 1024 * 1024 * 1024 * 0.3),
                configurable: true
            }});
            
            Object.defineProperty(performance.memory, 'usedJSHeapSize', {{
                get: () => Math.floor({profile['memory']} * 1024 * 1024 * 1024 * 0.1),
                configurable: true
            }});
        }}
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Memory spoofing failed: {e}")
    
    def _spoof_screen_characteristics(self, driver, profile):
        """Spoof screen and display characteristics"""
        width, height = profile['screen_resolution'].split('x')
        
        script = f"""
        // Screen resolution spoofing
        Object.defineProperty(screen, 'width', {{ 
            get: () => {width},
            configurable: true
        }});
        
        Object.defineProperty(screen, 'height', {{ 
            get: () => {height},
            configurable: true
        }});
        
        Object.defineProperty(screen, 'availWidth', {{ 
            get: () => {int(width) - random.randint(80, 120)},
            configurable: true
        }});
        
        Object.defineProperty(screen, 'availHeight', {{ 
            get: () => {int(height) - random.randint(80, 120)},
            configurable: true
        }});
        
        Object.defineProperty(screen, 'colorDepth', {{ 
            get: () => {profile['color_depth']},
            configurable: true
        }});
        
        Object.defineProperty(screen, 'pixelDepth', {{ 
            get: () => {profile['color_depth']},
            configurable: true
        }});
        
        // Pixel ratio spoofing
        Object.defineProperty(window, 'devicePixelRatio', {{
            get: () => {profile['pixel_ratio']},
            configurable: true
        }});
        
        // Screen orientation
        Object.defineProperty(screen, 'orientation', {{
            get: () => ({{
                type: 'landscape-primary',
                angle: 0,
                onchange: null
            }}),
            configurable: true
        }});
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Screen spoofing failed: {e}")
    
    def _spoof_input_characteristics(self, driver, profile):
        """Spoof input device characteristics"""
        script = f"""
        // Touch support spoofing
        Object.defineProperty(navigator, 'maxTouchPoints', {{
            get: () => {profile['max_touch_points']},
            configurable: true
        }});
        
        // Pointer capabilities
        if (navigator.pointerEnabled !== undefined) {{
            Object.defineProperty(navigator, 'pointerEnabled', {{
                get: () => true,
                configurable: true
            }});
        }}
        
        if (navigator.msPointerEnabled !== undefined) {{
            Object.defineProperty(navigator, 'msPointerEnabled', {{
                get: () => true,
                configurable: true
            }});
        }}
        
        // Keyboard layout
        Object.defineProperty(navigator, 'keyboard', {{
            get: () => ({{
                getLayoutMap: () => Promise.resolve(new Map([['key', 'value']])),
                lock: () => Promise.resolve(),
                unlock: () => {{}}
            }}),
            configurable: true
        }});
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Input spoofing failed: {e}")
    
    def _spoof_audio_characteristics(self, driver, profile):
        """Spoof audio device characteristics"""
        script = """
        // Audio context spoofing
        if (window.AudioContext) {
            const originalCreateAnalyser = AudioContext.prototype.createAnalyser;
            AudioContext.prototype.createAnalyser = function() {
                const analyser = originalCreateAnalyser.call(this);
                
                Object.defineProperty(analyser, 'frequencyBinCount', {
                    get: () => 2048,
                    configurable: true
                });
                
                return analyser;
            };
            
            // Spoof audio capabilities
            Object.defineProperty(AudioContext.prototype, 'sampleRate', {
                get: () => 44100,
                configurable: true
            });
        }
        
        // Media devices spoofing
        if (navigator.mediaDevices) {
            const originalGetUserMedia = navigator.mediaDevices.getUserMedia;
            navigator.mediaDevices.getUserMedia = function(constraints) {
                // Return a rejected promise to simulate no media access
                return Promise.reject(new Error('Permission denied'));
            };
        }
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Audio spoofing failed: {e}")
    
    def _spoof_battery_characteristics(self, driver, profile):
        """Spoof battery characteristics (for mobile/laptop devices)"""
        script = f"""
        // Battery API spoofing
        if ('getBattery' in navigator) {{
            const originalGetBattery = navigator.getBattery;
            navigator.getBattery = function() {{
                return Promise.resolve({{
                    charging: {str(random.choice([True, False])).lower()},
                    chargingTime: {random.randint(0, 3600)},
                    dischargingTime: {random.randint(1800, 7200)},
                    level: {round(random.uniform(0.2, 0.95), 2)},
                    addEventListener: function() {{}},
                    removeEventListener: function() {{}}
                }});
            }};
        }}
        
        // Power monitoring spoofing
        if (navigator.power !== undefined) {{
            Object.defineProperty(navigator.power, 'request', {{
                get: () => () => Promise.resolve('allowed'),
                configurable: true
            }});
        }}
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Battery spoofing failed: {e}")
    
    def rotate_hardware_profile(self, driver, new_profile=None):
        """Rotate to a new hardware profile"""
        try:
            if new_profile and new_profile in self.hardware_profiles:
                profile_name = new_profile
            else:
                # Select random profile, avoiding recent ones
                recent_profiles = [h['profile_name'] for h in self.spoofing_history[-3:]]
                available_profiles = [p for p in self.hardware_profiles.keys() if p not in recent_profiles]
                
                if available_profiles:
                    profile_name = random.choice(available_profiles)
                else:
                    profile_name = random.choice(list(self.hardware_profiles.keys()))
            
            # Apply new profile
            self.apply_hardware_spoofing(driver, profile_name)
            
            if self.config.DEBUG_MODE:
                print(f"🔄 Hardware profile rotated to: {profile_name}")
            
            return profile_name
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Hardware profile rotation failed: {e}")
            return None
    
    def get_hardware_report(self):
        """Get hardware spoofing report"""
        recent_spoofs = self.spoofing_history[-5:] if self.spoofing_history else []
        
        profile_usage = {}
        for spoof in self.spoofing_history:
            profile = spoof['profile_name']
            profile_usage[profile] = profile_usage.get(profile, 0) + 1
        
        return {
            'current_profile': self.current_profile,
            'total_spoofs': len(self.spoofing_history),
            'profile_usage': profile_usage,
            'recent_spoofs': recent_spoofs,
            'available_profiles': list(self.hardware_profiles.keys())
        }
    
    def verify_spoofing_consistency(self, driver):
        """Verify that hardware spoofing is consistent and undetectable"""
        try:
            tests = []
            
            # Test hardware concurrency
            hw_concurrency = driver.execute_script("return navigator.hardwareConcurrency;")
            tests.append({
                'test': 'hardware_concurrency',
                'expected': self.current_profile.get('hardware_concurrency'),
                'actual': hw_concurrency,
                'consistent': hw_concurrency == self.current_profile.get('hardware_concurrency')
            })
            
            # Test device memory
            device_memory = driver.execute_script("return navigator.deviceMemory;")
            tests.append({
                'test': 'device_memory',
                'expected': self.current_profile.get('device_memory'),
                'actual': device_memory,
                'consistent': device_memory == self.current_profile.get('device_memory')
            })
            
            # Test screen resolution
            screen_width = driver.execute_script("return screen.width;")
            expected_width = int(self.current_profile.get('screen_resolution', '1920x1080').split('x')[0])
            tests.append({
                'test': 'screen_width',
                'expected': expected_width,
                'actual': screen_width,
                'consistent': screen_width == expected_width
            })
            
            # Calculate overall consistency
            consistent_tests = sum(1 for test in tests if test['consistent'])
            consistency_rate = consistent_tests / len(tests) if tests else 0
            
            return {
                'tests': tests,
                'consistency_rate': consistency_rate,
                'overall_consistent': consistency_rate > 0.8
            }
            
        except Exception as e:
            return {
                'tests': [],
                'consistency_rate': 0,
                'overall_consistent': False,
                'error': str(e)
            }

# Utility function
def create_hardware_spoofer(config=None):
    """Factory function for easy hardware spoofer creation"""
    from config import settings
    config = config or settings.current_config
    return HardwareSpoofer(config)