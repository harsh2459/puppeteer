from .stealth_config import get_stealth_driver
from .humanizer import human_mouse_movement, human_type, quantum_delay, advanced_scroll
from .hardware_spoofer import HardwareSpoofer
from ai.adaptive_behavior import AdaptiveBehavior
from ai.identity_factory import SyntheticIdentityFactory
import time
import random

class PhantomBot:
    def __init__(self, proxy=None, user_agent=None, use_advanced_stealth=True):
        self.proxy = proxy
        self.user_agent = user_agent
        self.use_advanced_stealth = use_advanced_stealth
        self.driver = None
        self.hardware_spoofer = HardwareSpoofer() if use_advanced_stealth else None
        self.identity_factory = SyntheticIdentityFactory() if use_advanced_stealth else None
        self.adaptive_behavior = AdaptiveBehavior()
        self.operation_start_time = None
        self.identity = None
        
        # Behavioral settings that can be adjusted by identity
        self.MIN_DELAY = 0.5
        self.MAX_DELAY = 3.0

    def launch_browser(self):
        """Launch browser with advanced stealth features"""
        self.driver = get_stealth_driver(
            proxy=self.proxy, 
            user_agent=self.user_agent,
            headless=False
        )
        
        self.operation_start_time = time.time()
        
        # Apply advanced stealth features
        if self.use_advanced_stealth:
            self._apply_advanced_stealth()
            
        return self.driver

    def _apply_advanced_stealth(self):
        """Apply hardware spoofing and synthetic identity"""
        # Apply hardware spoofing first
        if self.hardware_spoofer:
            success = self.hardware_spoofer.apply_hardware_spoofing(self.driver)
            if success:
                print("✅ Hardware spoofing applied")
            
        # Create and inject synthetic identity
        if self.identity_factory:
            self.identity = self.identity_factory.create_basic_identity()
            self._inject_identity_data()
            self._apply_behavioral_patterns()

    def _inject_identity_data(self):
        """Inject complete synthetic identity into browser"""
        if not self.identity:
            return
            
        # Get technical profile with fallbacks
        tech_profile = self.identity.get('technical_profile', {})
        timezone = tech_profile.get('timezone', 'America/New_York')
        screen_res = tech_profile.get('screen_resolutions', ['1920x1080'])[0]
        width, height = screen_res.split('x') if 'x' in screen_res else ('1920', '1080')
        languages = tech_profile.get('language_preferences', ['en-US', 'en'])
        hw_concurrency = tech_profile.get('hardware_concurrency', 8)
        device_memory = tech_profile.get('device_memory', 8)
        browser_plugins = tech_profile.get('browser_plugins', 5)
        
        identity_script = f"""
        // Comprehensive identity injection
        Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{
            get: () => () => ({{
                timeZone: '{timezone}',
                locale: 'en-US'
            }})
        }});
        
        // Screen properties
        window.screen = {{
            width: {width},
            height: {height},
            colorDepth: 24,
            pixelDepth: 24
        }};
        
        // Language preferences
        Object.defineProperty(navigator, 'language', {{ get: () => 'en-US' }});
        Object.defineProperty(navigator, 'languages', {{ get: () => {languages} }});
        
        // Hardware properties
        Object.defineProperty(navigator, 'hardwareConcurrency', {{ get: () => {hw_concurrency} }});
        Object.defineProperty(navigator, 'deviceMemory', {{ get: () => {device_memory} }});
        
        // Plugins simulation
        Object.defineProperty(navigator, 'plugins', {{ get: () => {{
            length: {browser_plugins},
            item: (index) => ({{ name: `Plugin${{index}}` }}),
            namedItem: (name) => null
        }}}});
        """
        
        try:
            self.driver.execute_script(identity_script)
            print(f"✅ Injected identity: {self.identity.get('id', 'unknown')}")
        except Exception as e:
            print(f"❌ Identity injection failed: {e}")

    def _apply_behavioral_patterns(self):
        """Apply behavioral patterns from identity"""
        if not self.identity:
            return
            
        patterns = self.identity.get('behavioral_patterns', {})
        
        # Adjust delays based on behavioral profile
        click_speed = patterns.get('click_speed', 'moderate')
        if click_speed == 'fast':
            self.MIN_DELAY = 0.3
            self.MAX_DELAY = 1.5
        elif click_speed == 'slow':
            self.MIN_DELAY = 1.5
            self.MAX_DELAY = 4.0
        else:  # moderate
            self.MIN_DELAY = 0.5
            self.MAX_DELAY = 3.0
            
        print(f"🎯 Applied behavioral pattern: {click_speed} click speed")

    def human_click(self, element, use_advanced_movement=True):
        """Advanced human-like click"""
        if use_advanced_movement and self.use_advanced_stealth:
            try:
                human_mouse_movement(self.driver, element)
            except Exception as e:
                print(f"Advanced click failed, using standard: {e}")
                element.click()
        else:
            element.click()

    def human_type(self, element, text, speed_variation=0.2):
        """Human-like typing with advanced features"""
        human_type(element, text, speed_variation)

    def random_delay(self, min_sec=None, max_sec=None):
        """Quantum-randomized delay with identity-based adjustments"""
        min_delay = min_sec if min_sec is not None else self.MIN_DELAY
        max_delay = max_sec if max_sec is not None else self.MAX_DELAY
        time.sleep(random.uniform(min_delay, max_delay))

    def random_scroll(self):
        """Advanced scrolling patterns"""
        advanced_scroll(self.driver)

    def navigate_to(self, url):
        """Navigate to URL with human-like delays"""
        self.driver.get(url)
        self.random_delay(2, 4)  # Human-like page load wait

    def execute_operation(self, operations):
        """Execute a series of operations with adaptive learning"""
        actions_count = 0
        success = True
        
        try:
            for operation in operations:
                operation(self)  # Execute the operation function
                actions_count += 1
                self.random_delay()
                
        except Exception as e:
            success = False
            print(f"Operation failed: {e}")
            
        finally:
            # Record for adaptive learning
            if self.operation_start_time:
                duration = time.time() - self.operation_start_time
                self.adaptive_behavior.record_operation(success, duration, actions_count)
            
        return success

    def take_screenshot(self, filename=None):
        """Take screenshot for debugging"""
        if not filename:
            filename = f"screenshot_{int(time.time())}.png"
        self.driver.save_screenshot(filename)
        return filename

    def get_page_info(self):
        """Get current page information"""
        return {
            "url": self.driver.current_url,
            "title": self.driver.title,
            "source_length": len(self.driver.page_source)
        }

    def wait_for_element(self, by, value, timeout=10):
        """Wait for element to be present"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Element not found: {e}")
            return None

    def quit(self):
        """Safely quit browser"""
        if self.driver:
            try:
                self.driver.quit()
                self.driver = None
                print("✅ Browser session ended cleanly")
            except Exception as e:
                print(f"❌ Error quitting browser: {e}")