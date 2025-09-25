import random
import time
import re
import hashlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuantumEvasion:
    def __init__(self, config):
        self.config = config
        self.evasion_tactics = self._init_evasion_tactics()
        self.detection_patterns = self._init_detection_patterns()
        self.evasion_history = []
        self.threat_level = 0
        self.last_evasion_time = 0
        
    def _init_evasion_tactics(self):
        """Initialize quantum-level evasion tactics"""
        return {
            'fingerprint_spoofing': {
                'priority': 'critical',
                'techniques': [
                    'canvas_randomization',
                    'webgl_spoofing', 
                    'audio_context_noise',
                    'font_fingerprint_obfuscation',
                    'hardware_concurrency_spoofing'
                ],
                'activation_threshold': 0.1
            },
            'behavioral_mimicry': {
                'priority': 'high',
                'techniques': [
                    'mouse_trajectory_simulation',
                    'typing_rhythm_variation',
                    'scroll_pattern_diversification',
                    'attention_span_modeling',
                    'click_accuracy_randomization'
                ],
                'activation_threshold': 0.3
            },
            'timing_obfuscation': {
                'priority': 'medium',
                'techniques': [
                    'request_timing_randomization',
                    'event_interval_variation',
                    'load_time_manipulation',
                    'performance_api_spoofing',
                    'timestamp_anomaly_injection'
                ],
                'activation_threshold': 0.5
            },
            'network_stealth': {
                'priority': 'high',
                'techniques': [
                    'user_agent_rotation',
                    'ip_reputation_spoofing',
                    'protocol_fingerprint_masking',
                    'tls_fingerprint_randomization',
                    'http_header_normalization'
                ],
                'activation_threshold': 0.2
            }
        }
    
    def _init_detection_patterns(self):
        """Initialize advanced detection patterns"""
        return {
            'bot_signatures': [
                r'webdriver', r'selenium', r'phantomjs', r'headless', r'automation',
                r'chrome-headless', r'undetected-chromedriver', r'puppeteer',
                r'playwright', r'selenium-webdriver', r'browser automation'
            ],
            'behavior_anomalies': [
                r'too_fast', r'perfect_timing', r'no_errors', r'linear_navigation',
                r'machine_precision', r'consistent_intervals', r'pattern_repetition'
            ],
            'fingerprint_redflags': [
                r'missing_plugins', r'empty_canvas', r'webgl_disabled', r'timezone_mismatch',
                r'font_anomalies', r'audio_context_void', r'battery_api_missing'
            ],
            'network_suspicious': [
                r'suspicious_headers', r'invalid_user_agent', r'proxy_detected',
                r'tor_network', r'data_center_ip', r'geolocation_mismatch'
            ]
        }

    def detect_anti_bot_measures(self, driver):
        """Advanced detection of anti-bot measures with quantum scanning"""
        detected_threats = []
        current_url = driver.current_url.lower()
        
        try:
            # Comprehensive page source analysis
            page_source = driver.page_source.lower()
            current_domain = self._extract_domain(current_url)
            
            # Pattern-based threat detection
            threats_found = self._scan_for_threats(page_source, current_domain)
            detected_threats.extend(threats_found)
            
            # JavaScript environment analysis
            js_threats = self._analyze_js_environment(driver)
            detected_threats.extend(js_threats)
            
            # Network request monitoring
            network_threats = self._analyze_network_requests(driver)
            detected_threats.extend(network_threats)
            
            # Behavioral analysis triggers
            behavioral_threats = self._check_behavioral_triggers(driver)
            detected_threats.extend(behavioral_threats)
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Threat detection error: {e}")
            detected_threats.append('detection_system_error')
        
        # Update threat level
        self._update_threat_level(detected_threats)
        
        if self.config.DEBUG_MODE and detected_threats:
            print(f"🔍 Detected threats: {detected_threats}")
            
        return detected_threats

    def _scan_for_threats(self, page_source, domain):
        """Scan page source for threat patterns"""
        threats = []
        
        # Bot detection scripts
        bot_scripts = [
            'distil', 'perimeterx', 'cloudflare', 'akamai', 'imperva',
            'datadome', 'f5', 'radware', 'reblaze', 'shield'
        ]
        
        for script in bot_scripts:
            if script in page_source:
                threats.append(f'anti_bot_{script}')
        
        # Challenge detection
        challenge_indicators = [
            'challenge', 'captcha', 'verify', 'human', 'bot check',
            'security check', 'access denied', 'blocked'
        ]
        
        for indicator in challenge_indicators:
            if indicator in page_source:
                threats.append(f'challenge_{indicator}')
        
        # Domain-specific threats
        domain_threats = self._get_domain_specific_threats(domain)
        threats.extend(domain_threats)
        
        return threats

    def _analyze_js_environment(self, driver):
        """Analyze JavaScript environment for detection scripts"""
        threats = []
        
        try:
            # Check for common detection variables
            detection_checks = [
                ("window.webdriver", "webdriver_present"),
                ("window.__webdriver_evaluate", "webdriver_internal"),
                ("window.__selenium_evaluate", "selenium_detected"),
                ("window.__webdriver_script_func", "webdriver_function"),
                ("window.__webdriver_script_fn", "webdriver_function"),
                ("window._phantom", "phantomjs_detected"),
                ("window.callPhantom", "phantomjs_callback"),
                ("window.chrome", "chrome_runtime"),
                ("window.phantom", "phantomjs_runtime")
            ]
            
            for check, threat_name in detection_checks:
                result = driver.execute_script(f"return typeof {check} !== 'undefined'")
                if result:
                    threats.append(threat_name)
            
            # Check for headless browser detection
            headless_checks = [
                "navigator.webdriver",
                "navigator.plugins.length === 0",
                "navigator.languages === ''",
                "window.chrome && window.chrome.runtime",
                "typeof window.InstallTrigger === 'undefined'",
                "document.__webdriver_script_fn"
            ]
            
            for check in headless_checks:
                try:
                    result = driver.execute_script(f"return {check}")
                    if result:
                        threats.append('headless_detected')
                except:
                    pass
                    
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ JS environment analysis error: {e}")
        
        return threats

    def _analyze_network_requests(self, driver):
        """Analyze network requests for monitoring patterns"""
        threats = []
        
        try:
            # Check for analytics and tracking scripts
            scripts = driver.find_elements(By.TAG_NAME, 'script')
            for script in scripts:
                src = script.get_attribute('src') or ''
                if any(tracker in src for tracker in ['google-analytics', 'googletag', 'facebook.com/tr', 'hotjar']):
                    threats.append('tracking_script_detected')
            
            # Check for monitoring iframes
            iframes = driver.find_elements(By.TAG_NAME, 'iframe')
            for iframe in iframes:
                src = iframe.get_attribute('src') or ''
                if any(monitor in src for monitor in ['beacon', 'monitoring', 'telemetry']):
                    threats.append('monitoring_iframe')
                    
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Network analysis error: {e}")
        
        return threats

    def _check_behavioral_triggers(self, driver):
        """Check for behavioral analysis triggers"""
        threats = []
        
        try:
            # Check for mouse tracking
            mouse_scripts = driver.execute_script("""
                return Array.from(document.querySelectorAll('script')).filter(script => 
                    script.textContent.includes('mousemove') || 
                    script.textContent.includes('click tracking') ||
                    script.textContent.includes('user behavior')
                ).length > 0;
            """)
            
            if mouse_scripts:
                threats.append('behavioral_tracking_active')
            
            # Check for performance monitoring
            perf_monitoring = driver.execute_script("""
                return performance.getEntriesByType('navigation').length > 0 ||
                       performance.getEntriesByType('resource').length > 50;
            """)
            
            if perf_monitoring:
                threats.append('performance_monitoring')
                
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Behavioral trigger check error: {e}")
        
        return threats

    def execute_evasion_protocol(self, driver, threats):
        """Execute quantum evasion protocols based on detected threats"""
        evasion_actions = []
        current_time = time.time()
        
        # Rate limiting evasion attempts
        if current_time - self.last_evasion_time < 2.0:  # 2 second cooldown
            return ['evasion_cooldown_active']
        
        self.last_evasion_time = current_time
        
        for threat in threats:
            try:
                evasion_tactic = self._select_evasion_tactic(threat)
                if evasion_tactic:
                    action_result = self._execute_tactic(driver, evasion_tactic, threat)
                    evasion_actions.append(f"{threat}_{action_result}")
                    
            except Exception as e:
                evasion_actions.append(f"{threat}_error:{str(e)}")
        
        # Log evasion attempt
        self._log_evasion_attempt(threats, evasion_actions)
        
        return evasion_actions

    def _select_evasion_tactic(self, threat):
        """Select appropriate evasion tactic based on threat type"""
        threat_mapping = {
            'webdriver_detected': 'fingerprint_spoofing',
            'headless_detected': 'behavioral_mimicry',
            'anti_bot_': 'network_stealth',
            'challenge_': 'timing_obfuscation',
            'tracking_script': 'fingerprint_spoofing',
            'behavioral_tracking': 'behavioral_mimicry',
            'performance_monitoring': 'timing_obfuscation'
        }
        
        for pattern, tactic in threat_mapping.items():
            if pattern in threat:
                return tactic
        
        return 'fingerprint_spoofing'  # Default tactic

    def _execute_tactic(self, driver, tactic, threat):
        """Execute specific evasion tactic"""
        tactic_config = self.evasion_tactics.get(tactic, {})
        techniques = tactic_config.get('techniques', [])
        
        executed_techniques = []
        
        for technique in techniques[:3]:  # Execute up to 3 techniques per tactic
            try:
                if technique == 'canvas_randomization':
                    self._randomize_canvas_fingerprint(driver)
                elif technique == 'webgl_spoofing':
                    self._spoof_webgl_fingerprint(driver)
                elif technique == 'mouse_trajectory_simulation':
                    self._simulate_mouse_trajectories(driver)
                elif technique == 'typing_rhythm_variation':
                    self._vary_typing_rhythm(driver)
                elif technique == 'request_timing_randomization':
                    self._randomize_request_timing(driver)
                elif technique == 'user_agent_rotation':
                    self._rotate_user_agent(driver)
                
                executed_techniques.append(technique)
                
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Evasion technique {technique} failed: {e}")
        
        return f"executed_{len(executed_techniques)}_techniques"

    def _randomize_canvas_fingerprint(self, driver):
        """Randomize canvas fingerprint with quantum noise"""
        script = """
        // Canvas fingerprint randomization
        const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
        CanvasRenderingContext2D.prototype.getImageData = function(...args) {
            const result = originalGetImageData.call(this, ...args);
            
            // Add quantum-level noise
            for (let i = 0; i < result.data.length; i += 4) {
                const noise = Math.random() * 2 - 1; // -1 to 1
                result.data[i] = Math.min(255, Math.max(0, result.data[i] + noise));
                result.data[i+1] = Math.min(255, Math.max(0, result.data[i+1] + noise));
                result.data[i+2] = Math.min(255, Math.max(0, result.data[i+2] + noise));
            }
            return result;
        };
        """
        driver.execute_script(script)

    def _spoof_webgl_fingerprint(self, driver):
        """Spoof WebGL fingerprint with realistic variations"""
        script = """
        // WebGL fingerprint spoofing
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {
            const vendors = ['Google Inc. (Intel)', 'NVIDIA Corporation', 'AMD', 'Apple Inc.'];
            const renderers = [
                'ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0)',
                'NVIDIA GeForce RTX 3080/PCIe/SSE2',
                'AMD Radeon RX 6800 XT',
                'Apple M1 Pro'
            ];
            
            if (parameter === 37445) { // UNMASKED_VENDOR_WEBGL
                return vendors[Math.floor(Math.random() * vendors.length)];
            }
            if (parameter === 37446) { // UNMASKED_RENDERER_WEBGL
                return renderers[Math.floor(Math.random() * renderers.length)];
            }
            return getParameter.call(this, parameter);
        };
        """
        driver.execute_script(script)

    def _simulate_mouse_trajectories(self, driver):
        """Simulate human-like mouse trajectories"""
        script = """
        // Mouse trajectory simulation
        const originalAddEventListener = EventTarget.prototype.addEventListener;
        EventTarget.prototype.addEventListener = function(type, listener, options) {
            if (type === 'mousemove') {
                const wrappedListener = function(event) {
                    // Add slight randomness to mouse positions
                    event.clientX += Math.random() * 4 - 2;
                    event.clientY += Math.random() * 4 - 2;
                    return listener.call(this, event);
                };
                return originalAddEventListener.call(this, type, wrappedListener, options);
            }
            return originalAddEventListener.call(this, type, listener, options);
        };
        """
        driver.execute_script(script)

    def _vary_typing_rhythm(self, driver):
        """Vary typing rhythm and patterns"""
        script = """
        // Typing rhythm variation
        const originalDispatchEvent = EventTarget.prototype.dispatchEvent;
        EventTarget.prototype.dispatchEvent = function(event) {
            if (event.type === 'keydown' || event.type === 'keyup') {
                // Randomize timing between key events
                const delay = Math.random() * 50 + 25; // 25-75ms variation
                setTimeout(() => originalDispatchEvent.call(this, event), delay);
                return true;
            }
            return originalDispatchEvent.call(this, event);
        };
        """
        driver.execute_script(script)

    def _randomize_request_timing(self, driver):
        """Randomize network request timing"""
        script = """
        // Request timing randomization
        const originalFetch = window.fetch;
        window.fetch = function(...args) {
            const delay = Math.random() * 1000 + 500; // 500-1500ms delay
            return new Promise((resolve) => {
                setTimeout(() => resolve(originalFetch.apply(this, args)), delay);
            });
        };
        """
        driver.execute_script(script)

    def _rotate_user_agent(self, driver):
        """Rotate user agent dynamically"""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
        ]
        
        script = f"""
        // User agent rotation
        Object.defineProperty(navigator, 'userAgent', {{
            get: () => '{random.choice(user_agents)}',
            configurable: true
        }});
        """
        driver.execute_script(script)

    def _update_threat_level(self, threats):
        """Update current threat level based on detected threats"""
        threat_weights = {
            'critical': 2.0,
            'high': 1.5,
            'medium': 1.0,
            'low': 0.5
        }
        
        current_level = 0
        for threat in threats:
            # Determine threat priority
            priority = 'medium'
            if 'webdriver' in threat or 'headless' in threat:
                priority = 'critical'
            elif 'anti_bot' in threat or 'challenge' in threat:
                priority = 'high'
            
            current_level += threat_weights.get(priority, 1.0)
        
        # Apply exponential decay to threat level
        time_since_last_update = time.time() - self.last_evasion_time
        decay_factor = 0.9 ** (time_since_last_update / 60)  # Decay over minutes
        
        self.threat_level = (self.threat_level * decay_factor) + current_level
        self.threat_level = min(10.0, self.threat_level)  # Cap at 10

    def _log_evasion_attempt(self, threats, actions):
        """Log evasion attempts for analysis"""
        log_entry = {
            'timestamp': time.time(),
            'threats_detected': threats,
            'evasion_actions': actions,
            'threat_level': self.threat_level,
            'success_rate': len(actions) / max(1, len(threats))
        }
        
        self.evasion_history.append(log_entry)
        
        # Keep only last 100 entries
        if len(self.evasion_history) > 100:
            self.evasion_history.pop(0)

    def get_evasion_analytics(self):
        """Get evasion performance analytics"""
        if not self.evasion_history:
            return {'total_attempts': 0, 'success_rate': 0.0}
        
        total_attempts = len(self.evasion_history)
        successful_attempts = sum(
            1 for entry in self.evasion_history 
            if entry['success_rate'] > 0.7
        )
        
        recent_threats = []
        for entry in self.evasion_history[-10:]:
            recent_threats.extend(entry['threats_detected'])
        
        threat_frequency = {}
        for threat in recent_threats:
            threat_frequency[threat] = threat_frequency.get(threat, 0) + 1
        
        return {
            'total_attempts': total_attempts,
            'success_rate': successful_attempts / total_attempts if total_attempts > 0 else 0,
            'current_threat_level': round(self.threat_level, 2),
            'recent_threat_frequency': threat_frequency,
            'evasion_tactics_used': list(self.evasion_tactics.keys())
        }

    def _extract_domain(self, url):
        """Extract domain from URL"""
        try:
            return url.split('//')[-1].split('/')[0].split('?')[0]
        except:
            return url

    def _get_domain_specific_threats(self, domain):
        """Get domain-specific threat patterns"""
        domain_patterns = {
            'google.com': ['recaptcha', 'challenge', 'bot_check'],
            'facebook.com': ['bot_detection', 'security_check'],
            'cloudflare.com': ['challenge', 'security_check'],
            'amazon.com': ['bot_detection', 'captcha']
        }
        
        for pattern, threats in domain_patterns.items():
            if pattern in domain:
                return threats
        
        return []