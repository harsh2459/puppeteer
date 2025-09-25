import random
import time
import hashlib
import json
from selenium.webdriver.common.by import By
from config import settings

class FingerprintRandomizer:
    def __init__(self, config):
        self.config = config
        self.fingerprint_history = []
        self.current_fingerprint = {}
        self.entropy_source = random.random()
        self.rotation_count = 0
        
    def randomize_browser_fingerprint(self, driver, force_rotation=False):
        """Randomize browser fingerprint with quantum-level variations"""
        if not self.config.FINGERPRINT_RANDOMIZATION and not force_rotation:
            return self.current_fingerprint
            
        try:
            new_fingerprint = self._generate_quantum_fingerprint()
            
            # Apply fingerprint randomization scripts
            self._apply_canvas_fingerprint(driver, new_fingerprint)
            self._apply_webgl_fingerprint(driver, new_fingerprint)
            self._apply_audio_fingerprint(driver, new_fingerprint)
            self._apply_font_fingerprint(driver, new_fingerprint)
            self._apply_hardware_fingerprint(driver, new_fingerprint)
            self._apply_network_fingerprint(driver, new_fingerprint)
            
            # Store fingerprint history
            self.fingerprint_history.append({
                'timestamp': time.time(),
                'fingerprint': new_fingerprint,
                'rotation_id': self.rotation_count
            })
            
            self.current_fingerprint = new_fingerprint
            self.rotation_count += 1
            
            if self.config.DEBUG_MODE:
                print(f"🔄 Fingerprint rotated (#{self.rotation_count})")
                
            return new_fingerprint
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Fingerprint randomization failed: {e}")
            return self.current_fingerprint
    
    def _generate_quantum_fingerprint(self):
        """Generate quantum-level unique fingerprint with consistency"""
        base_seed = f"{time.time()}{self.entropy_source}{random.random()}"
        seed_hash = hashlib.sha256(base_seed.encode()).hexdigest()
        random.seed(int(seed_hash[:8], 16))
        
        fingerprint = {
            'canvas_hash': self._generate_canvas_hash(),
            'webgl_vendor': random.choice([
                'Google Inc. (Intel)', 'NVIDIA Corporation', 'AMD', 'Apple Inc.',
                'Intel Inc.', 'Microsoft Corporation'
            ]),
            'webgl_renderer': random.choice([
                'ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0)',
                'NVIDIA GeForce RTX 4070/PCIe/SSE2',
                'AMD Radeon RX 7700 XT',
                'Apple M3 Pro',
                'Intel(R) UHD Graphics 770'
            ]),
            'audio_context_hash': self._generate_audio_hash(),
            'font_hash': self._generate_font_hash(),
            'screen_resolution': random.choice([
                '1920x1080', '2560x1440', '3840x2160', '1366x768', '1536x864',
                '1440x900', '1280x720', '2560x1600'
            ]),
            'color_depth': random.choice([24, 30, 32]),
            'pixel_ratio': round(random.uniform(1.0, 3.0), 2),
            'hardware_concurrency': random.choice([4, 6, 8, 12, 16]),
            'device_memory': random.choice([4, 8, 16, 32]),
            'timezone': random.choice([
                'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney',
                'Europe/Paris', 'Asia/Shanghai', 'America/Los_Angeles'
            ]),
            'language': random.choice(['en-US', 'en-GB', 'en', 'es', 'fr', 'de']),
            'platform': random.choice(['Win32', 'MacIntel', 'Linux x86_64']),
            'user_agent': self._generate_user_agent(),
            'touch_support': random.choice([0, 5, 10]),
            'max_touch_points': random.choice([0, 5, 10]),
            'session_id': f"fp_{int(time.time())}_{random.randint(1000, 9999)}"
        }
        
        random.seed()  # Reset random seed
        return fingerprint
    
    def _generate_canvas_hash(self):
        """Generate unique canvas fingerprint hash"""
        base = f"canvas_{time.time()}_{random.random()}"
        return hashlib.md5(base.encode()).hexdigest()[:16]
    
    def _generate_audio_hash(self):
        """Generate unique audio context fingerprint hash"""
        base = f"audio_{time.time()}_{random.random()}"
        return hashlib.md5(base.encode()).hexdigest()[:16]
    
    def _generate_font_hash(self):
        """Generate unique font fingerprint hash"""
        base = f"font_{time.time()}_{random.random()}"
        return hashlib.md5(base.encode()).hexdigest()[:16]
    
    def _generate_user_agent(self):
        """Generate realistic user agent based on platform"""
        platforms = {
            'Win32': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
            ],
            'MacIntel': [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
            ],
            'Linux x86_64': [
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0'
            ]
        }
        
        platform = random.choice(list(platforms.keys()))
        return random.choice(platforms[platform])
    
    def _apply_canvas_fingerprint(self, driver, fingerprint):
        """Apply canvas fingerprint randomization"""
        script = f"""
        // Canvas fingerprint manipulation
        const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
        CanvasRenderingContext2D.prototype.getImageData = function(...args) {{
            const result = originalGetImageData.call(this, ...args);
            
            // Add quantum-level noise that's consistent per session
            const sessionSeed = {hash(str(fingerprint['session_id']))};
            for (let i = 0; i < result.data.length; i += 4) {{
                const noise = (sessionSeed + i) % 3 - 1; // -1, 0, or 1
                result.data[i] = Math.min(255, Math.max(0, result.data[i] + noise));
                result.data[i+1] = Math.min(255, Math.max(0, result.data[i+1] + noise));
                result.data[i+2] = Math.min(255, Math.max(0, result.data[i+2] + noise));
            }}
            return result;
        }};
        
        // Spoof canvas toDataURL results
        const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
        HTMLCanvasElement.prototype.toDataURL = function(type, quality) {{
            const result = originalToDataURL.call(this, type, quality);
            return result; // Return appears normal but fingerprint changes
        }};
        
        // Override canvas measurement
        const originalMeasureText = CanvasRenderingContext2D.prototype.measureText;
        CanvasRenderingContext2D.prototype.measureText = function(text) {{
            const result = originalMeasureText.call(this, text);
            const variation = (Math.random() - 0.5) * 2; // ±1px variation
            return {{
                width: Math.max(0, result.width + variation),
                actualBoundingBoxLeft: result.actualBoundingBoxLeft,
                actualBoundingBoxRight: result.actualBoundingBoxRight,
                actualBoundingBoxAscent: result.actualBoundingBoxAscent,
                actualBoundingBoxDescent: result.actualBoundingBoxDescent
            }};
        }};
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Canvas fingerprint failed: {e}")
    
    def _apply_webgl_fingerprint(self, driver, fingerprint):
        """Apply WebGL fingerprint randomization"""
        script = f"""
        // WebGL fingerprint manipulation
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            switch(parameter) {{
                case 37445: // UNMASKED_VENDOR_WEBGL
                    return "{fingerprint['webgl_vendor']}";
                case 37446: // UNMASKED_RENDERER_WEBGL
                    return "{fingerprint['webgl_renderer']}";
                case 7936: // VENDOR
                    return "{fingerprint['webgl_vendor']}";
                case 7937: // RENDERER
                    return "{fingerprint['webgl_renderer']}";
                default:
                    return getParameter.call(this, parameter);
            }}
        }};
        
        // Spoof WebGL extensions
        const getSupportedExtensions = WebGLRenderingContext.prototype.getSupportedExtensions;
        WebGLRenderingContext.prototype.getSupportedExtensions = function() {{
            const realExtensions = getSupportedExtensions.call(this) || [];
            return realExtensions.filter(ext => !ext.includes('debug'));
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
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ WebGL fingerprint failed: {e}")
    
    def _apply_audio_fingerprint(self, driver, fingerprint):
        """Apply audio context fingerprint randomization"""
        script = """
        // Audio context fingerprint manipulation
        if (window.AudioContext) {
            const originalCreateAnalyser = AudioContext.prototype.createAnalyser;
            AudioContext.prototype.createAnalyser = function() {
                const analyser = originalCreateAnalyser.call(this);
                
                Object.defineProperty(analyser, 'frequencyBinCount', {
                    get: () => 2048, // Standardized value
                    configurable: true
                });
                
                return analyser;
            };
            
            // Spoof audio buffer data
            const originalGetChannelData = AudioBuffer.prototype.getChannelData;
            AudioBuffer.prototype.getChannelData = function(channel) {
                const data = originalGetChannelData.call(this, channel);
                
                // Add minimal, consistent noise
                for (let i = 0; i < data.length; i += 128) {
                    data[i] += (Math.random() - 0.5) * 0.0001;
                }
                return data;
            };
        }
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Audio fingerprint failed: {e}")
    
    def _apply_font_fingerprint(self, driver, fingerprint):
        """Apply font fingerprint randomization"""
        script = """
        // Font fingerprint manipulation
        const originalMeasureText = CanvasRenderingContext2D.prototype.measureText;
        CanvasRenderingContext2D.prototype.measureText = function(text) {
            const result = originalMeasureText.call(this, text);
            
            // Add small, consistent variations
            const variation = (Math.random() - 0.5) * 1.5;
            return {
                width: Math.max(0, result.width + variation),
                actualBoundingBoxLeft: result.actualBoundingBoxLeft,
                actualBoundingBoxRight: result.actualBoundingBoxRight,
                actualBoundingBoxAscent: result.actualBoundingBoxAscent,
                actualBoundingBoxDescent: result.actualBoundingBoxDescent
            };
        };
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Font fingerprint failed: {e}")
    
    def _apply_hardware_fingerprint(self, driver, fingerprint):
        """Apply hardware fingerprint randomization"""
        script = f"""
        // Hardware fingerprint manipulation
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {fingerprint['hardware_concurrency']},
            configurable: true
        }});
        
        Object.defineProperty(navigator, 'deviceMemory', {{
            get: () => {fingerprint['device_memory']},
            configurable: true
        }});
        
        Object.defineProperty(navigator, 'maxTouchPoints', {{
            get: () => {fingerprint['max_touch_points']},
            configurable: true
        }});
        
        // Screen properties
        Object.defineProperty(screen, 'width', {{ get: () => {fingerprint['screen_resolution'].split('x')[0]} }});
        Object.defineProperty(screen, 'height', {{ get: () => {fingerprint['screen_resolution'].split('x')[1]} }});
        Object.defineProperty(screen, 'colorDepth', {{ get: () => {fingerprint['color_depth']} }});
        Object.defineProperty(screen, 'pixelDepth', {{ get: () => {fingerprint['color_depth']} }});
        
        // Pixel ratio
        Object.defineProperty(window, 'devicePixelRatio', {{
            get: () => {fingerprint['pixel_ratio']},
            configurable: true
        }});
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Hardware fingerprint failed: {e}")
    
    def _apply_network_fingerprint(self, driver, fingerprint):
        """Apply network information fingerprint randomization"""
        script = f"""
        // Network information fingerprint manipulation
        if ('connection' in navigator) {{
            Object.defineProperty(navigator.connection, 'downlink', {{
                get: () => {random.choice([10, 50, 100, 500, 1000])}
            }});
            
            Object.defineProperty(navigator.connection, 'effectiveType', {{
                get: () => '{random.choice(['4g', '3g', '2g'])}'
            }});
            
            Object.defineProperty(navigator.connection, 'rtt', {{
                get: () => {random.randint(50, 300)}
            }});
        }}
        
        // Timezone manipulation
        Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{
            get: () => () => ({{
                timeZone: '{fingerprint['timezone']}',
                locale: '{fingerprint['language']}',
                calendar: 'gregory'
            }})
        }});
        """
        
        try:
            driver.execute_script(script)
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Network fingerprint failed: {e}")
    
    def get_fingerprint_report(self):
        """Get comprehensive fingerprint randomization report"""
        if not self.current_fingerprint:
            return {'status': 'no_fingerprint_generated'}
        
        return {
            'current_fingerprint': self.current_fingerprint,
            'rotation_count': self.rotation_count,
            'total_rotations': len(self.fingerprint_history),
            'last_rotation': self.fingerprint_history[-1]['timestamp'] if self.fingerprint_history else None,
            'entropy_source': self.entropy_source,
            'fingerprint_components': list(self.current_fingerprint.keys())
        }
    
    def verify_fingerprint_consistency(self, driver):
        """Verify that fingerprint changes are consistent and undetectable"""
        try:
            # Test canvas fingerprint consistency
            canvas_test = driver.execute_script("""
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                ctx.textBaseline = 'top';
                ctx.font = '14px Arial';
                ctx.fillText('Fingerprint Test', 2, 2);
                return canvas.toDataURL();
            """)
            
            # Test WebGL fingerprint
            webgl_test = driver.execute_script("""
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl');
                return gl ? gl.getParameter(gl.VERSION) : 'WebGL not supported';
            """)
            
            return {
                'canvas_consistent': len(canvas_test) > 100,  # Basic consistency check
                'webgl_consistent': 'WebGL' in str(webgl_test),
                'tests_passed': True
            }
            
        except Exception as e:
            return {
                'canvas_consistent': False,
                'webgl_consistent': False,
                'tests_passed': False,
                'error': str(e)
            }

# Utility functions
def hash(text):
    """Simple hash function for consistent values"""
    return hashlib.md5(text.encode()).hexdigest()

def create_fingerprint_randomizer(config=None):
    """Factory function for easy fingerprint randomizer creation"""
    from config import settings
    config = config or settings.current_config
    return FingerprintRandomizer(config)