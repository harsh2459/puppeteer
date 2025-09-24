from .stealth_config import get_quantum_stealth_driver
from .humanizer import quantum_mouse_movement, quantum_type, quantum_delay, quantum_scroll
from .hardware_spoofer import HardwareSpoofer
from .biometric_simulator import BiometricSimulator
from ai.identity_factory import SyntheticIdentityFactory
from ai.quantum_evasion import QuantumEvasion
from utils.fingerprint_randomizer import FingerprintRandomizer
from utils.pattern_manager import QuantumPatternManager
from utils.navigation_diversifier import NavigationDiversifier
from utils.session_persistence import QuantumSessionManager
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

class QuantumBot:
    def __init__(self, proxy=None, user_agent=None, use_quantum_stealth=True, config=None):
        self.proxy = proxy
        self.user_agent = user_agent
        self.use_quantum_stealth = use_quantum_stealth
        self.config = config or settings.current_config
        self.driver = None
        self.current_persona = None
        
        # 🎭 Quantum stealth components
        if self.use_quantum_stealth:
            self.hardware_spoofer = HardwareSpoofer()
            self.identity_factory = SyntheticIdentityFactory()
            self.quantum_evasion = QuantumEvasion()
            self.fingerprint_randomizer = FingerprintRandomizer(self.config)
            self.biometric_simulator = BiometricSimulator()
            self.quantum_pattern_manager = QuantumPatternManager(self.config)
            self.navigation_diversifier = NavigationDiversifier(self.config)
            self.session_manager = QuantumSessionManager(self.config)
        
        self.operation_count = 0
        self.identity = None
        self.session_id = None
        self.performance_metrics = {
            'operations_completed': 0,
            'success_rate': 0.0,
            'average_duration': 0.0,
            'last_activity': time.time()
        }

    def launch_quantum_browser(self, persona_id=None, restore_session=False):
        """Launch with quantum stealth enhancements"""
        try:
            # 🚀 Launch quantum stealth driver
            self.driver, self.current_persona = get_quantum_stealth_driver(
                proxy=self.proxy,
                user_agent=self.user_agent,
                headless=False,
                persona_id=persona_id or (self.identity.get('id') if self.identity else None),
                config=self.config
            )
            
            # 🔧 Apply additional quantum enhancements
            if self.use_quantum_stealth:
                self._apply_quantum_stealth()
                
                # 🔄 Session restoration
                if restore_session and self.session_id:
                    self.session_manager.load_session_state(self.session_id, self)
            
            # 📊 Performance monitoring
            self.performance_metrics['last_activity'] = time.time()
            
            if self.config.DEBUG_MODE:
                print(f"✅ Quantum browser launched with persona: {self.current_persona['persona_id']}")
                
            return self.driver
            
        except Exception as e:
            print(f"❌ Quantum browser launch failed: {e}")
            raise

    def _apply_quantum_stealth(self):
        """Apply quantum-level stealth enhancements"""
        # 🖥️ Hardware spoofing
        if self.hardware_spoofer:
            self.hardware_spoofer.apply_hardware_spoofing(self.driver)
            
        # 🆔 Quantum identity creation and injection
        if self.identity_factory:
            self.identity = self.identity_factory.create_quantum_identity()
            self._inject_quantum_identity()
            
        # 🔀 Initial fingerprint randomization
        if self.fingerprint_randomizer:
            self.fingerprint_randomizer.randomize_browser_fingerprint(self.driver)
            
        # 🛡️ Initial anti-detection check
        if self.quantum_evasion and self.config.ANTI_DETECTION_CHECKS:
            threats = self.quantum_evasion.detect_anti_bot_measures(self.driver)
            if threats:
                evasion_actions = self.quantum_evasion.execute_evasion_protocol(self.driver, threats)
                if self.config.DEBUG_MODE:
                    print(f"🛡️ Evasion actions taken: {evasion_actions}")

    def _inject_quantum_identity(self):
        """Inject quantum identity with enhanced spoofing"""
        if not self.identity:
            return
            
        tech_profile = self.identity.get('technical_profile', {})
        quantum_fp = self.identity.get('quantum_fingerprint', {})
        
        identity_script = f"""
        // 🔧 Quantum identity injection
        Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{
            get: () => () => ({{
                timeZone: '{tech_profile.get('timezone', 'America/New_York')}',
                locale: 'en-US',
                calendar: 'gregory'
            }})
        }});
        
        // 💾 Enhanced hardware properties
        Object.defineProperty(navigator, 'hardwareConcurrency', {{ 
            get: () => {quantum_fp.get('hardware_concurrency', 8)} 
        }});
        Object.defineProperty(navigator, 'deviceMemory', {{ 
            get: () => {quantum_fp.get('device_memory', 8)} 
        }});
        
        // 🎮 WebGL spoofing
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            if (parameter === 37445) return "{quantum_fp.get('webgl_vendor', 'Google Inc. (Intel)')}";
            if (parameter === 37446) return "{quantum_fp.get('webgl_renderer', 'ANGLE (Intel)')}";
            return getParameter.call(this, parameter);
        }};
        """
        
        try:
            self.driver.execute_script(identity_script)
            if self.config.DEBUG_MODE:
                print("✅ Quantum identity injected successfully")
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Quantum identity injection warning: {e}")

    def quantum_click(self, element, element_description="unknown"):
        """Quantum-enhanced click with biometric simulation"""
        if not self.use_quantum_stealth:
            element.click()
            return True
            
        try:
            pattern = self.quantum_pattern_manager.get_click_pattern()
            
            if self.config.ENABLE_BIOMETRIC_SIMULATION:
                # 🎯 Biometric mouse movement
                if pattern["movement_style"] == "curved":
                    quantum_mouse_movement(self.driver, element)
                else:
                    # Direct click with human imperfections
                    action = ActionChains(self.driver)
                    action.move_to_element(element)
                    action.pause(random.uniform(0.1, 0.3))
                    action.click()
                    action.perform()
            else:
                element.click()
                
            # 📊 Metrics recording
            self._record_operation_metric('clicks')
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Quantum click failed: {e}")
            # Fallback to standard click
            try:
                element.click()
                return True
            except:
                return False

    def quantum_type(self, element, text, typing_profile=None):
        """Quantum typing with behavioral patterns"""
        if self.use_quantum_stealth and self.config.ENABLE_BIOMETRIC_SIMULATION:
            pattern = typing_profile or self.quantum_pattern_manager.get_typing_pattern()
            quantum_type(element, text, pattern)
        else:
            element.send_keys(text)
        
        self._record_operation_metric('typing_actions')

    def quantum_scroll(self, scroll_count=None, scroll_profile=None):
        """Quantum scrolling with pattern variation"""
        if self.use_quantum_stealth:
            pattern = scroll_profile or self.quantum_pattern_manager.get_scroll_pattern()
            quantum_scroll(self.driver, pattern, scroll_count)
        else:
            # Fallback scrolling
            for _ in range(scroll_count or random.randint(2, 5)):
                self.driver.execute_script("window.scrollBy(0, 300);")
                time.sleep(random.uniform(0.5, 1.5))

    def execute_quantum_operation(self, operations, operation_type="standard"):
        """Execute operations with quantum enhancements"""
        start_time = time.time()
        self.operation_count += 1
        
        try:
            # 🔄 Dynamic fingerprint rotation
            if (self.use_quantum_stealth and 
                self.operation_count % self.config.FINGERPRINT_ROTATION_INTERVAL == 0):
                self.fingerprint_randomizer.randomize_browser_fingerprint(self.driver)
                if self.config.DEBUG_MODE:
                    print("🔄 Fingerprint rotated")
            
            # 🔀 Pattern rotation
            if self.operation_count % self.config.PATTERN_ROTATION_FREQUENCY == 0:
                self.quantum_pattern_manager.rotate_pattern()
                if self.config.DEBUG_MODE:
                    print("🔄 Behavioral pattern rotated")
            
            # 🛡️ Real-time anti-detection
            if (self.quantum_evasion and 
                self.config.ANTI_DETECTION_CHECKS and
                self.operation_count % 5 == 0):  # Check every 5 operations
                threats = self.quantum_evasion.detect_anti_bot_measures(self.driver)
                if threats:
                    self.quantum_evasion.execute_evasion_protocol(self.driver, threats)
            
            # 🎯 Execute the actual operations
            success = self._execute_operations(operations)
            duration = time.time() - start_time
            
            # 📊 Update performance metrics
            self._update_performance_metrics(success, duration)
            
            return success
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Quantum operation failed: {e}")
            self._update_performance_metrics(False, time.time() - start_time)
            return False

    def _execute_operations(self, operations):
        """Execute the actual operation functions"""
        for operation in operations:
            try:
                operation(self)
                # ⏳ Quantum delay between operations
                quantum_delay()
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Operation step failed: {e}")
                return False
        return True

    def diversified_navigate(self, target_url, pattern_name=None, save_session=True):
        """Enhanced navigation with diversification"""
        if self.use_quantum_stealth:
            navigation_plan = self.navigation_diversifier.get_diversified_navigation_plan(
                target_url, pattern_name
            )
            success = self.navigation_diversifier.execute_diversified_navigation(self, navigation_plan)
            
            # 💾 Session persistence
            if success and save_session and self.config.SESSION_PERSISTENCE:
                if not self.session_id:
                    self.session_id = f"session_{int(time.time())}_{random.randint(1000,9999)}"
                self.session_manager.save_session_state(self, self.session_id)
            
            return success
        else:
            # Fallback navigation
            self.driver.get(target_url)
            return True

    def manage_session_persistence(self, action="save", session_id=None):
        """Manage session persistence with enhanced features"""
        if not self.use_quantum_stealth:
            return False
            
        session_id = session_id or self.session_id
        
        if action == "save" and session_id:
            return self.session_manager.save_session_state(self, session_id)
        elif action == "load" and session_id:
            return self.session_manager.load_session_state(session_id, self)
        elif action == "rotate" and session_id:
            new_id = f"{session_id}_rotated_{int(time.time())}"
            success = self.session_manager.rotate_session_identity(self, new_id)
            if success:
                self.session_id = new_id
            return success
        elif action == "cleanup":
            return self.session_manager.cleanup_old_sessions()

    def _record_operation_metric(self, metric_type):
        """Record operation metrics for optimization"""
        if metric_type not in self.performance_metrics:
            self.performance_metrics[metric_type] = 0
        self.performance_metrics[metric_type] += 1

    def _update_performance_metrics(self, success, duration):
        """Update overall performance metrics"""
        self.performance_metrics['operations_completed'] += 1
        self.performance_metrics['last_activity'] = time.time()
        
        # Update success rate (moving average)
        total_ops = self.performance_metrics['operations_completed']
        current_rate = self.performance_metrics['success_rate']
        new_rate = (current_rate * (total_ops - 1) + (1 if success else 0)) / total_ops
        self.performance_metrics['success_rate'] = new_rate
        
        # Update average duration
        current_avg = self.performance_metrics['average_duration']
        new_avg = (current_avg * (total_ops - 1) + duration) / total_ops
        self.performance_metrics['average_duration'] = new_avg

    def get_performance_report(self):
        """Get comprehensive performance report"""
        return {
            'session_id': self.session_id,
            'persona_id': self.current_persona['persona_id'] if self.current_persona else 'unknown',
            'operations_completed': self.performance_metrics['operations_completed'],
            'success_rate': f"{self.performance_metrics['success_rate']:.1%}",
            'average_duration': f"{self.performance_metrics['average_duration']:.2f}s",
            'uptime': f"{(time.time() - self.performance_metrics['last_activity']) / 60:.1f} min",
            'quantum_features_active': self.use_quantum_stealth
        }

    def quit(self):
        """Safely quit quantum browser"""
        if self.driver:
            try:
                # 💾 Save session before quitting
                if self.session_id and self.config.SESSION_PERSISTENCE:
                    self.session_manager.save_session_state(self, self.session_id)
                
                self.driver.quit()
                self.driver = None
                
                if self.config.DEBUG_MODE:
                    print("✅ Quantum browser session ended cleanly")
                    
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Error quitting browser: {e}")

# Backward compatibility
PhantomBot = QuantumBot