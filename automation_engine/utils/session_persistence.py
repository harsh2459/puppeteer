import json
import time
import random
import hashlib
import pickle
import os
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from config import settings

class QuantumSessionManager:
    def __init__(self, config):
        self.config = config
        self.sessions_dir = "sessions/quantum"
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.active_sessions = {}
        self.session_cleanup_interval = 3600  # 1 hour
        self.last_cleanup = time.time()
        
        # Create sessions directory
        os.makedirs(self.sessions_dir, exist_ok=True)
    
    def save_session_state(self, bot, session_id, metadata=None):
        """Save complete bot session state with encryption"""
        try:
            session_data = self._capture_session_state(bot)
            metadata = metadata or {}
            
            # Enhance metadata
            metadata.update({
                'save_timestamp': time.time(),
                'session_size': len(str(session_data)),
                'bot_metrics': bot.get_performance_report() if hasattr(bot, 'get_performance_report') else {},
                'entropy_source': random.random()
            })
            
            # Create session package
            session_package = {
                'session_id': session_id,
                'data': session_data,
                'metadata': metadata,
                'encryption_version': '2.0',
                'checksum': self._calculate_checksum(session_data)
            }
            
            # Encrypt session data
            encrypted_session = self._encrypt_session(session_package)
            
            # Save to file
            session_file = os.path.join(self.sessions_dir, f"{session_id}.qsession")
            with open(session_file, 'wb') as f:
                f.write(encrypted_session)
            
            # Update active sessions
            self.active_sessions[session_id] = {
                'last_save': time.time(),
                'file_path': session_file,
                'metadata': metadata
            }
            
            if self.config.DEBUG_MODE:
                print(f"💾 Session saved: {session_id}")
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Session save failed: {e}")
            return False
    
    def _capture_session_state(self, bot):
        """Capture comprehensive session state from bot"""
        session_state = {
            'browser_state': self._capture_browser_state(bot.driver),
            'bot_state': self._capture_bot_state(bot),
            'navigation_state': self._capture_navigation_state(bot),
            'fingerprint_state': self._capture_fingerprint_state(bot),
            'timing_state': self._capture_timing_state(),
            'quantum_entropy': random.random()
        }
        
        return session_state
    
    def _capture_browser_state(self, driver):
        """Capture browser-specific state"""
        try:
            browser_state = {
                'current_url': driver.current_url,
                'page_title': driver.title,
                'cookies': driver.get_cookies(),
                'local_storage': self._get_local_storage(driver),
                'session_storage': self._get_session_storage(driver),
                'window_handle': driver.current_window_handle,
                'window_size': driver.get_window_size(),
                'page_source_hash': hashlib.md5(driver.page_source.encode()).hexdigest()[:16]
            }
            
            # Capture form data if any
            browser_state['form_data'] = self._capture_form_data(driver)
            
            return browser_state
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Browser state capture failed: {e}")
            return {}
    
    def _get_local_storage(self, driver):
        """Get local storage data"""
        try:
            return driver.execute_script("return Object.assign({}, localStorage);")
        except:
            return {}
    
    def _get_session_storage(self, driver):
        """Get session storage data"""
        try:
            return driver.execute_script("return Object.assign({}, sessionStorage);")
        except:
            return {}
    
    def _capture_form_data(self, driver):
        """Capture form field data"""
        try:
            form_data = {}
            inputs = driver.find_elements_by_tag_name('input')
            
            for input_field in inputs:
                try:
                    field_name = input_field.get_attribute('name') or input_field.get_attribute('id')
                    field_value = input_field.get_attribute('value')
                    if field_name and field_value:
                        form_data[field_name] = field_value
                except:
                    continue
            
            return form_data
        except:
            return {}
    
    def _capture_bot_state(self, bot):
        """Capture bot-specific state"""
        bot_state = {
            'performance_metrics': getattr(bot, 'performance_metrics', {}),
            'operation_count': getattr(bot, 'operation_count', 0),
            'current_persona': getattr(bot, 'current_persona', {}),
            'identity': getattr(bot, 'identity', {}),
            'cognitive_state': self._capture_cognitive_state(bot),
            'pattern_state': self._capture_pattern_state(bot)
        }
        
        return bot_state
    
    def _capture_cognitive_state(self, bot):
        """Capture cognitive/behavioral state"""
        if hasattr(bot, 'neuromorphic_engine'):
            return {
                'current_state': bot.neuromorphic_engine.current_state,
                'current_emotion': bot.neuromorphic_engine.current_emotion,
                'attention_span': bot.neuromorphic_engine.attention_span,
                'fatigue_level': bot.neuromorphic_engine.fatigue_level
            }
        return {}
    
    def _capture_pattern_state(self, bot):
        """Capture pattern management state"""
        if hasattr(bot, 'quantum_pattern_manager'):
            return {
                'current_pattern': bot.quantum_pattern_manager.current_pattern,
                'pattern_history': bot.quantum_pattern_manager.pattern_history[-10:]  # Last 10
            }
        return {}
    
    def _capture_navigation_state(self, bot):
        """Capture navigation state"""
        if hasattr(bot, 'navigation_diversifier'):
            return {
                'current_pattern': bot.navigation_diversifier.current_pattern,
                'navigation_history': bot.navigation_diversifier.navigation_history[-5:]  # Last 5
            }
        return {}
    
    def _capture_fingerprint_state(self, bot):
        """Capture fingerprint state"""
        if hasattr(bot, 'fingerprint_randomizer'):
            return {
                'current_fingerprint': bot.fingerprint_randomizer.current_fingerprint,
                'rotation_count': bot.fingerprint_randomizer.rotation_count
            }
        return {}
    
    def _capture_timing_state(self):
        """Capture timing and temporal state"""
        return {
            'capture_timestamp': time.time(),
            'system_uptime': time.time() - self.last_cleanup,
            'time_dilation': random.uniform(0.95, 1.05)
        }
    
    def _calculate_checksum(self, data):
        """Calculate checksum for data integrity"""
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_str.encode()).hexdigest()
    
    def _encrypt_session(self, session_package):
        """Encrypt session data"""
        serialized_data = pickle.dumps(session_package)
        return self.cipher_suite.encrypt(serialized_data)
    
    def load_session_state(self, session_id, bot):
        """Load and restore session state"""
        try:
            session_file = os.path.join(self.sessions_dir, f"{session_id}.qsession")
            
            if not os.path.exists(session_file):
                if self.config.DEBUG_MODE:
                    print(f"❌ Session file not found: {session_id}")
                return False
            
            # Load and decrypt session
            with open(session_file, 'rb') as f:
                encrypted_data = f.read()
            
            session_package = self._decrypt_session(encrypted_data)
            
            # Verify checksum
            if not self._verify_checksum(session_package):
                if self.config.DEBUG_MODE:
                    print(f"❌ Session checksum verification failed: {session_id}")
                return False
            
            # Restore session state
            self._restore_session_state(bot, session_package['data'])
            
            # Update active sessions
            self.active_sessions[session_id] = {
                'last_load': time.time(),
                'file_path': session_file,
                'metadata': session_package.get('metadata', {})
            }
            
            if self.config.DEBUG_MODE:
                print(f"🔄 Session loaded: {session_id}")
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Session load failed: {e}")
            return False
    
    def _decrypt_session(self, encrypted_data):
        """Decrypt session data"""
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return pickle.loads(decrypted_data)
    
    def _verify_checksum(self, session_package):
        """Verify session data integrity"""
        expected_checksum = session_package.get('checksum')
        actual_checksum = self._calculate_checksum(session_package['data'])
        return expected_checksum == actual_checksum
    
    def _restore_session_state(self, bot, session_data):
        """Restore session state to bot"""
        try:
            # Restore browser state
            if 'browser_state' in session_data:
                self._restore_browser_state(bot.driver, session_data['browser_state'])
            
            # Restore bot state
            if 'bot_state' in session_data:
                self._restore_bot_state(bot, session_data['bot_state'])
            
            # Restore navigation state
            if 'navigation_state' in session_data:
                self._restore_navigation_state(bot, session_data['navigation_state'])
            
            # Restore fingerprint state
            if 'fingerprint_state' in session_data:
                self._restore_fingerprint_state(bot, session_data['fingerprint_state'])
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Session restoration partial failure: {e}")
            return False
    
    def _restore_browser_state(self, driver, browser_state):
        """Restore browser state"""
        try:
            # Navigate to saved URL
            if browser_state.get('current_url'):
                driver.get(browser_state['current_url'])
                time.sleep(2)
            
            # Restore cookies
            if browser_state.get('cookies'):
                driver.delete_all_cookies()
                for cookie in browser_state['cookies']:
                    try:
                        driver.add_cookie(cookie)
                    except:
                        continue
            
            # Restore local storage
            if browser_state.get('local_storage'):
                driver.execute_script("localStorage.clear();")
                for key, value in browser_state['local_storage'].items():
                    driver.execute_script(f"localStorage.setItem('{key}', '{value}');")
            
            # Restore window size
            if browser_state.get('window_size'):
                driver.set_window_size(
                    browser_state['window_size']['width'],
                    browser_state['window_size']['height']
                )
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Browser state restoration failed: {e}")
    
    def _restore_bot_state(self, bot, bot_state):
        """Restore bot state"""
        try:
            # Restore performance metrics
            if 'performance_metrics' in bot_state:
                bot.performance_metrics.update(bot_state['performance_metrics'])
            
            # Restore operation count
            if 'operation_count' in bot_state:
                bot.operation_count = bot_state['operation_count']
            
            # Restore persona and identity
            if 'current_persona' in bot_state:
                bot.current_persona = bot_state['current_persona']
            if 'identity' in bot_state:
                bot.identity = bot_state['identity']
            
            # Restore cognitive state
            if 'cognitive_state' in bot_state and hasattr(bot, 'neuromorphic_engine'):
                cognitive_state = bot_state['cognitive_state']
                bot.neuromorphic_engine.current_state = cognitive_state.get('current_state', 'casual')
                bot.neuromorphic_engine.current_emotion = cognitive_state.get('current_emotion', 'neutral')
                bot.neuromorphic_engine.attention_span = cognitive_state.get('attention_span', 1.0)
                bot.neuromorphic_engine.fatigue_level = cognitive_state.get('fatigue_level', 0.0)
            
            # Restore pattern state
            if 'pattern_state' in bot_state and hasattr(bot, 'quantum_pattern_manager'):
                pattern_state = bot_state['pattern_state']
                bot.quantum_pattern_manager.current_pattern = pattern_state.get('current_pattern', 'standard')
                # Append history instead of replacing to maintain continuity
                new_history = pattern_state.get('pattern_history', [])
                bot.quantum_pattern_manager.pattern_history.extend(new_history)
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Bot state restoration failed: {e}")
    
    def _restore_navigation_state(self, bot, navigation_state):
        """Restore navigation state"""
        if hasattr(bot, 'navigation_diversifier') and navigation_state:
            bot.navigation_diversifier.current_pattern = navigation_state.get('current_pattern', 'organic')
            new_history = navigation_state.get('navigation_history', [])
            bot.navigation_diversifier.navigation_history.extend(new_history)
    
    def _restore_fingerprint_state(self, bot, fingerprint_state):
        """Restore fingerprint state"""
        if hasattr(bot, 'fingerprint_randomizer') and fingerprint_state:
            bot.fingerprint_randomizer.current_fingerprint = fingerprint_state.get('current_fingerprint', {})
            bot.fingerprint_randomizer.rotation_count = fingerprint_state.get('rotation_count', 0)
    
    def rotate_session_identity(self, bot, new_session_id):
        """Rotate session with new identity while maintaining continuity"""
        try:
            # Save current session
            current_metadata = {
                'rotation_source': bot.session_id if hasattr(bot, 'session_id') else 'unknown',
                'rotation_timestamp': time.time(),
                'rotation_type': 'identity_rotation'
            }
            
            success = self.save_session_state(bot, new_session_id, current_metadata)
            
            if success:
                # Update bot session ID
                bot.session_id = new_session_id
                
                # Slight fingerprint rotation for continuity
                if hasattr(bot, 'fingerprint_randomizer'):
                    bot.fingerprint_randomizer.randomize_browser_fingerprint(bot.driver, force_rotation=True)
                
                if self.config.DEBUG_MODE:
                    print(f"🔄 Session identity rotated: {new_session_id}")
            
            return success
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Session rotation failed: {e}")
            return False
    
    def cleanup_old_sessions(self, max_age_hours=24):
        """Clean up old session files"""
        try:
            current_time = time.time()
            max_age_seconds = max_age_hours * 3600
            
            deleted_count = 0
            for filename in os.listdir(self.sessions_dir):
                if filename.endswith('.qsession'):
                    filepath = os.path.join(self.sessions_dir, filename)
                    file_time = os.path.getmtime(filepath)
                    
                    if current_time - file_time > max_age_seconds:
                        os.remove(filepath)
                        deleted_count += 1
            
            self.last_cleanup = current_time
            
            if self.config.DEBUG_MODE:
                print(f"🧹 Cleaned up {deleted_count} old sessions")
            
            return deleted_count
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Session cleanup failed: {e}")
            return 0
    
    def get_session_stats(self):
        """Get session management statistics"""
        session_files = [f for f in os.listdir(self.sessions_dir) if f.endswith('.qsession')]
        
        # Calculate total size
        total_size = 0
        for filename in session_files:
            filepath = os.path.join(self.sessions_dir, filename)
            total_size += os.path.getsize(filepath)
        
        # Get oldest and newest sessions
        session_times = []
        for filename in session_files:
            filepath = os.path.join(self.sessions_dir, filename)
            session_times.append(os.path.getmtime(filepath))
        
        return {
            'total_sessions': len(session_files),
            'active_sessions': len(self.active_sessions),
            'total_size_mb': round(total_size / 1024 / 1024, 2),
            'oldest_session': min(session_times) if session_times else None,
            'newest_session': max(session_times) if session_times else None,
            'last_cleanup': self.last_cleanup
        }
    
    def auto_cleanup(self):
        """Automatic cleanup based on interval"""
        current_time = time.time()
        if current_time - self.last_cleanup > self.session_cleanup_interval:
            self.cleanup_old_sessions()

# Utility function
def create_session_manager(config=None):
    """Factory function for easy session manager creation"""
    from config import settings
    config = config or settings.current_config
    return QuantumSessionManager(config)