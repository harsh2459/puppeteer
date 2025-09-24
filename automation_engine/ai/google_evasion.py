import random
import time
import re
import hashlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, urljoin

class GoogleEvasionEngine:
    def __init__(self, config):
        self.config = config
        self.google_services = self._init_google_services()
        self.evasion_history = []
        self.detection_patterns = self._init_detection_patterns()
        
    def _init_google_services(self):
        """Initialize Google services with evasion strategies"""
        return {
            'analytics': {
                'evasion_scripts': self._get_ga_evasion_scripts(),
                'detection_patterns': ['ga.js', 'analytics.js', 'gtag.js', 'google-analytics.com'],
                'evasion_level': 'high',
                'simulation_required': True
            },
            'recaptcha': {
                'evasion_scripts': self._get_recaptcha_evasion(),
                'detection_patterns': ['recaptcha', 'grecaptcha', 'google.com/recaptcha'],
                'evasion_level': 'critical',
                'simulation_required': True
            },
            'tag_manager': {
                'evasion_scripts': self._get_gtm_evasion(),
                'detection_patterns': ['googletagmanager.com', 'gtm.js'],
                'evasion_level': 'high',
                'simulation_required': False
            },
            'fonts': {
                'evasion_scripts': self._get_fonts_evasion(),
                'detection_patterns': ['fonts.googleapis.com', 'fonts.gstatic.com'],
                'evasion_level': 'medium',
                'simulation_required': False
            },
            'safe_browsing': {
                'evasion_scripts': self._get_safe_browsing_evasion(),
                'detection_patterns': ['safebrowsing.googleapis.com', 'sb-ssl.google.com'],
                'evasion_level': 'medium',
                'simulation_required': False
            },
            'apis': {
                'evasion_scripts': self._get_apis_evasion(),
                'detection_patterns': ['apis.google.com', 'googleapis.com'],
                'evasion_level': 'low',
                'simulation_required': True
            }
        }
    
    def _init_detection_patterns(self):
        """Initialize Google detection patterns"""
        return {
            'bot_signatures': [
                'webdriver', 'selenium', 'phantomjs', 'headless', 'automation',
                'chrome-headless', 'undetected-chromedriver'
            ],
            'behavior_patterns': [
                'too_fast', 'perfect_timing', 'no_errors', 'linear_navigation'
            ],
            'fingerprint_anomalies': [
                'missing_plugins', 'empty_canvas', 'webgl_disabled', 'timezone_mismatch'
            ]
        }
    
    def evade_google_detection(self, driver):
        """Execute comprehensive Google evasion"""
        evasion_results = {}
        current_url = driver.current_url
        
        for service_name, service_config in self.google_services.items():
            if not self.config.GOOGLE_SERVICES_EVASION.get(service_name, True):
                evasion_results[service_name] = 'disabled_by_config'
                continue
                
            try:
                # Check if service is present on current page
                if self._detect_google_service(driver, service_config['detection_patterns']):
                    # Execute evasion scripts
                    evasion_success = self._execute_evasion_scripts(driver, service_config['evasion_scripts'])
                    
                    # Simulate legitimate usage if required
                    if service_config['simulation_required'] and evasion_success:
                        self._simulate_legitimate_usage(driver, service_name)
                    
                    evasion_results[service_name] = 'evaded' if evasion_success else 'evasion_failed'
                else:
                    evasion_results[service_name] = 'not_detected'
                    
            except Exception as e:
                evasion_results[service_name] = f'error: {str(e)}'
        
        # Log evasion attempt
        self._log_evasion_attempt(current_url, evasion_results)
        
        return evasion_results
    
    def _detect_google_service(self, driver, patterns):
        """Detect if Google service is present on page"""
        try:
            page_source = driver.page_source.lower()
            for pattern in patterns:
                if pattern.lower() in page_source:
                    return True
            
            # Check script tags
            scripts = driver.find_elements(By.TAG_NAME, 'script')
            for script in scripts:
                src = script.get_attribute('src') or ''
                for pattern in patterns:
                    if pattern.lower() in src.lower():
                        return True
                        
            return False
        except:
            return False
    
    def _execute_evasion_scripts(self, driver, scripts):
        """Execute evasion scripts for a service"""
        success_count = 0
        for script in scripts:
            try:
                driver.execute_script(script)
                success_count += 1
                time.sleep(0.1)  # Small delay between scripts
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Evasion script failed: {e}")
                continue
        
        return success_count > 0
    
    def _get_ga_evasion_scripts(self):
        """Get Google Analytics evasion scripts"""
        return [
            # Block Google Analytics tracking
            """
            window['ga-disable-GA_MEASUREMENT_ID'] = true;
            window['ga-disable-UA-'] = true;
            
            // Override ga function
            if (window.ga) {
                window.ga = function() { 
                    console.log('GA call blocked:', arguments);
                    return { hit: function() {} };
                };
                window.ga.getAll = function() { return []; };
                window.ga.create = function() { return { get: function() {} }; };
            }
            
            // Override gtag function
            if (window.gtag) {
                window.gtag = function() { 
                    console.log('GTAG call blocked:', arguments);
                };
            }
            
            // Block dataLayer
            if (window.dataLayer) {
                const originalPush = window.dataLayer.push;
                window.dataLayer.push = function() {
                    console.log('DataLayer push blocked:', arguments);
                    return originalPush.apply(this, arguments);
                };
            }
            """,
            
            # Spoof analytics data
            """
            // Create fake analytics data
            window.ga = window.ga || function() {
                (window.ga.q = window.ga.q || []).push(arguments);
            };
            window.ga.l = +new Date;
            
            // Fake initialization
            ga('create', 'UA-' + Math.floor(Math.random() * 1000000) + '-1', 'auto');
            ga('set', 'transport', 'beacon');
            ga('send', 'pageview', {
                'page': window.location.pathname,
                'title': document.title,
                'location': window.location.href
            });
            """
        ]
    
    def _get_recaptcha_evasion(self):
        """Get reCAPTCHA evasion scripts"""
        return [
            # reCAPTCHA v3 evasion
            """
            // Override grecaptcha
            if (typeof window.grecaptcha !== 'undefined') {
                window.grecaptcha.execute = function(siteKey, options) {
                    console.log('reCAPTCHA execute blocked');
                    return Promise.resolve('fake_recaptcha_token_' + Math.random().toString(36).substr(2, 10));
                };
                
                window.grecaptcha.ready = function(callback) {
                    if (callback) setTimeout(callback, 100);
                };
                
                window.grecaptcha.render = function(container, parameters) {
                    console.log('reCAPTCHA render blocked');
                    return 'fake_widget_id';
                };
            }
            
            // Remove reCAPTCHA iframes
            const recaptchaFrames = document.querySelectorAll('iframe[src*="recaptcha"]');
            recaptchaFrames.forEach(frame => {
                frame.style.display = 'none';
                frame.src = 'about:blank';
            });
            """,
            
            # reCAPTCHA v2 evasion
            """
            // Block reCAPTCHA challenge rendering
            const originalCreateElement = document.createElement;
            document.createElement = function(tagName) {
                const element = originalCreateElement.call(this, tagName);
                if (tagName.toLowerCase() === 'div') {
                    const originalAppendChild = element.appendChild;
                    element.appendChild = function(child) {
                        if (child && child.className && child.className.includes('g-recaptcha')) {
                            console.log('reCAPTCHA div blocked');
                            return child;
                        }
                        return originalAppendChild.call(this, child);
                    };
                }
                return element;
            };
            """
        ]
    
    def _get_gtm_evasion(self):
        """Get Google Tag Manager evasion scripts"""
        return [
            """
            // Block GTM initialization
            if (window.google_tag_manager) {
                window.google_tag_manager = undefined;
            }
            
            // Block GTM data layer
            if (window.dataLayer) {
                Object.defineProperty(window, 'dataLayer', {
                    get: function() {
                        console.log('DataLayer access blocked');
                        return [];
                    },
                    set: function(value) {
                        console.log('DataLayer set blocked');
                    }
                });
            }
            
            // Remove GTM iframes and scripts
            const gtmElements = document.querySelectorAll('iframe[src*="googletagmanager"], script[src*="googletagmanager"]');
            gtmElements.forEach(element => {
                element.remove();
            });
            """
        ]
    
    def _get_fonts_evasion(self):
        """Get Google Fonts evasion scripts"""
        return [
            """
            // Block Google Fonts loading
            const originalCreateElement = document.createElement;
            document.createElement = function(tagName) {
                const element = originalCreateElement.call(this, tagName);
                if (tagName.toLowerCase() === 'link') {
                    const originalSetAttribute = element.setAttribute;
                    element.setAttribute = function(name, value) {
                        if (name === 'href' && value && value.includes('fonts.googleapis.com')) {
                            console.log('Google Fonts blocked:', value);
                            return; // Don't set the attribute
                        }
                        return originalSetAttribute.call(this, name, value);
                    };
                }
                return element;
            };
            
            // Remove existing Google Fonts links
            const fontLinks = document.querySelectorAll('link[href*="fonts.googleapis.com"]');
            fontLinks.forEach(link => link.remove());
            """
        ]
    
    def _get_safe_browsing_evasion(self):
        """Get Safe Browsing evasion scripts"""
        return [
            """
            // Block Safe Browsing API calls
            const originalFetch = window.fetch;
            window.fetch = function(...args) {
                if (args[0] && typeof args[0] === 'string' && args[0].includes('safebrowsing')) {
                    console.log('Safe Browsing API call blocked');
                    return Promise.reject(new Error('Blocked by evasion'));
                }
                return originalFetch.apply(this, args);
            };
            
            // Block XMLHttpRequest to Safe Browsing
            const originalXHROpen = XMLHttpRequest.prototype.open;
            XMLHttpRequest.prototype.open = function(method, url, ...args) {
                if (url && url.includes('safebrowsing')) {
                    console.log('Safe Browsing XHR blocked');
                    this._blocked = true;
                    return;
                }
                return originalXHROpen.call(this, method, url, ...args);
            };
            """
        ]
    
    def _get_apis_evasion(self):
        """Get Google APIs evasion scripts"""
        return [
            """
            // Block Google APIs
            const googleAPIPatterns = [
                'apis.google.com', 'googleapis.com', 'gstatic.com'
            ];
            
            // Override fetch for Google APIs
            const originalFetch = window.fetch;
            window.fetch = function(...args) {
                const url = args[0];
                if (url && typeof url === 'string') {
                    for (const pattern of googleAPIPatterns) {
                        if (url.includes(pattern)) {
                            console.log('Google API call blocked:', url);
                            return Promise.reject(new Error('Blocked by evasion'));
                        }
                    }
                }
                return originalFetch.apply(this, args);
            };
            
            // Override XMLHttpRequest for Google APIs
            const originalXHROpen = XMLHttpRequest.prototype.open;
            XMLHttpRequest.prototype.open = function(method, url, ...args) {
                if (url) {
                    for (const pattern of googleAPIPatterns) {
                        if (url.includes(pattern)) {
                            console.log('Google API XHR blocked:', url);
                            this._blocked = true;
                            return;
                        }
                    }
                }
                return originalXHROpen.call(this, method, url, ...args);
            };
            """
        ]
    
    def _simulate_legitimate_usage(self, driver, service_name):
        """Simulate legitimate Google service usage"""
        simulation_methods = {
            'analytics': self._simulate_analytics_usage,
            'recaptcha': self._simulate_recaptcha_usage,
            'apis': self._simulate_api_usage
        }
        
        if service_name in simulation_methods:
            try:
                simulation_methods[service_name](driver)
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ {service_name} simulation failed: {e}")
    
    def _simulate_analytics_usage(self, driver):
        """Simulate legitimate Analytics usage patterns"""
        # Simulate random page views and events
        scripts = [
            """
            // Simulate pageview after delay
            setTimeout(() => {
                if (window.ga) {
                    ga('send', 'pageview', {
                        'page': window.location.pathname + '?ref=organic',
                        'title': document.title,
                        'hitCallback': function() {
                            console.log('Simulated pageview sent');
                        }
                    });
                }
            }, Math.random() * 5000 + 2000);
            """,
            """
            // Simulate events
            setTimeout(() => {
                if (window.ga) {
                    const events = ['click', 'scroll', 'hover', 'download'];
                    const event = events[Math.floor(Math.random() * events.length)];
                    ga('send', 'event', 'engagement', event, window.location.pathname);
                }
            }, Math.random() * 8000 + 5000);
            """
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except:
                pass
    
    def _simulate_recaptcha_usage(self, driver):
        """Simulate legitimate reCAPTCHA usage"""
        script = """
        // Simulate reCAPTCHA token generation
        setTimeout(() => {
            if (typeof window.grecaptcha !== 'undefined') {
                // Simulate token generation for forms
                const forms = document.querySelectorAll('form');
                forms.forEach(form => {
                    if (form.querySelector('.g-recaptcha')) {
                        console.log('Simulating reCAPTCHA for form');
                    }
                });
            }
        }, 3000);
        """
        
        try:
            driver.execute_script(script)
        except:
            pass
    
    def _simulate_api_usage(self, driver):
        """Simulate legitimate Google API usage"""
        script = """
        // Simulate API readiness
        if (window.gapi) {
            setTimeout(() => {
                if (window.gapi.load) {
                    // Simulate loading common APIs
                    window.gapi.load('auth2', {
                        callback: function() {
                            console.log('Simulated Google Auth loaded');
                        },
                        onerror: function() {
                            console.log('Simulated Google Auth error');
                        }
                    });
                }
            }, 2000);
        }
        """
        
        try:
            driver.execute_script(script)
        except:
            pass
    
    def detect_google_anti_bot_measures(self, driver):
        """Detect Google-specific anti-bot measures"""
        detected_measures = []
        
        try:
            page_source = driver.page_source.lower()
            current_url = driver.current_url.lower()
            
            # Check for common Google anti-bot signatures
            bot_indicators = [
                'distil', 'perimeterx', 'cloudflare', 'akamai',
                'bot detection', 'anti-bot', 'challenge', 'captcha'
            ]
            
            for indicator in bot_indicators:
                if indicator in page_source:
                    detected_measures.append(f'anti_bot_{indicator}')
            
            # Check URL for Google security pages
            if any(pattern in current_url for pattern in ['/sorry/', '/challenge/', '/signin/v2/']):
                detected_measures.append('google_security_challenge')
            
            # Check for challenge forms
            challenge_selectors = [
                '#captcha', '.g-recaptcha', '#challenge-form', '.verify-you-are-human'
            ]
            
            for selector in challenge_selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    detected_measures.append(f'challenge_element_{selector}')
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Google anti-bot detection failed: {e}")
        
        return detected_measures
    
    def evade_google_anti_bot(self, driver, detected_measures):
        """Evade detected Google anti-bot measures"""
        evasion_actions = []
        
        for measure in detected_measures:
            try:
                if 'challenge' in measure:
                    action = self._handle_challenge(driver)
                    evasion_actions.append(f'challenge_handled_{action}')
                elif 'captcha' in measure:
                    action = self._handle_captcha(driver)
                    evasion_actions.append(f'captcha_handled_{action}')
                elif 'anti_bot' in measure:
                    action = self._evade_anti_bot(driver)
                    evasion_actions.append(f'anti_bot_evaded_{action}')
                
            except Exception as e:
                evasion_actions.append(f'error_{measure}:{str(e)}')
        
        return evasion_actions
    
    def _handle_challenge(self, driver):
        """Handle Google security challenges"""
        try:
            # Try to navigate away from challenge page
            driver.get("https://www.google.com")
            time.sleep(2)
            return "navigated_away"
        except:
            return "navigation_failed"
    
    def _handle_captcha(self, driver):
        """Handle CAPTCHA challenges"""
        try:
            # Simple CAPTCHA avoidance - refresh page
            driver.refresh()
            time.sleep(3)
            return "page_refreshed"
        except:
            return "refresh_failed"
    
    def _evade_anti_bot(self, driver):
        """Evade general anti-bot measures"""
        try:
            # Add random delays and human-like behavior
            time.sleep(random.uniform(2, 5))
            
            # Simulate human interaction
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            
            return "behavior_simulated"
        except:
            return "simulation_failed"
    
    def _log_evasion_attempt(self, url, results):
        """Log evasion attempt for analysis"""
        log_entry = {
            'timestamp': time.time(),
            'url': url,
            'results': results,
            'user_agent': 'quantum_bot'  # Would be actual UA in real implementation
        }
        
        self.evasion_history.append(log_entry)
        
        # Keep only last 100 entries
        if len(self.evasion_history) > 100:
            self.evasion_history.pop(0)
        
        if self.config.DEBUG_MODE:
            print(f"🔍 Google evasion results for {url}: {results}")
    
    def get_evasion_stats(self):
        """Get evasion statistics"""
        total_attempts = len(self.evasion_history)
        successful_evasions = sum(
            1 for entry in self.evasion_history 
            if all('evaded' in result or 'not_detected' in result 
                   for result in entry['results'].values())
        )
        
        service_stats = {}
        for service_name in self.google_services.keys():
            service_evasions = [
                entry['results'].get(service_name, 'unknown')
                for entry in self.evasion_history
            ]
            service_stats[service_name] = {
                'total': len(service_evasions),
                'evaded': service_evasions.count('evaded'),
                'not_detected': service_evasions.count('not_detected'),
                'failed': service_evasions.count('evasion_failed')
            }
        
        return {
            'total_attempts': total_attempts,
            'success_rate': successful_evasions / total_attempts if total_attempts > 0 else 0,
            'service_stats': service_stats,
            'recent_attempts': self.evasion_history[-10:] if self.evasion_history else []
        }