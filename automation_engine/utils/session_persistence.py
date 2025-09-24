import json
import time
import os
from datetime import datetime, timedelta

class QuantumSessionManager:
    def __init__(self, config):
        self.config = config
        self.sessions_dir = "sessions/quantum/"
        os.makedirs(self.sessions_dir, exist_ok=True)
        
    def save_session_state(self, bot_instance, session_id):
        """Save complete session state for persistence"""
        session_data = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "identity": bot_instance.identity,
            "fingerprint_hash": bot_instance.fingerprint_randomizer.get_fingerprint_hash(bot_instance.driver) if hasattr(bot_instance, 'fingerprint_randomizer') else "unknown",
            "behavioral_pattern": bot_instance.quantum_pattern_manager.current_pattern if hasattr(bot_instance, 'quantum_pattern_manager') else {},
            "operation_count": getattr(bot_instance, 'operation_count', 0),
            "cookies": bot_instance.driver.get_cookies() if bot_instance.driver else [],
            "local_storage": self._get_local_storage(bot_instance.driver) if bot_instance.driver else {}
        }
        
        filename = f"{self.sessions_dir}{session_id}.json"
        with open(filename, 'w') as f:
            json.dump(session_data, f, indent=2)
            
        return filename
    
    def load_session_state(self, session_id, bot_instance):
        """Load and restore session state"""
        filename = f"{self.sessions_dir}{session_id}.json"
        
        if not os.path.exists(filename):
            return False
            
        with open(filename, 'r') as f:
            session_data = json.load(f)
            
        # Restore session data
        if 'cookies' in session_data and bot_instance.driver:
            bot_instance.driver.delete_all_cookies()
            for cookie in session_data['cookies']:
                try:
                    bot_instance.driver.add_cookie(cookie)
                except:
                    pass
                    
        # Refresh page to apply cookies
        bot_instance.driver.refresh()
        
        print(f"✅ Session restored: {session_id}")
        return True
    
    def rotate_session_identity(self, bot_instance, new_session_id):
        """Rotate session while maintaining some continuity"""
        if hasattr(bot_instance, 'identity'):
            # Keep demographic data but change technical fingerprint
            old_identity = bot_instance.identity
            new_identity = bot_instance.identity_factory.create_quantum_identity(
                age_group=old_identity.get('demographics', {}).get('age_group', 'adult'),
                location=old_identity.get('demographics', {}).get('location', 'US')
            )
            bot_instance.identity = new_identity
            
        # Save new session
        self.save_session_state(bot_instance, new_session_id)
        return new_session_id
    
    def _get_local_storage(self, driver):
        """Extract local storage data"""
        try:
            return driver.execute_script("return JSON.stringify(window.localStorage);")
        except:
            return "{}"
    
    def cleanup_old_sessions(self, max_age_hours=24):
        """Clean up sessions older than max_age_hours"""
        cutoff_time = datetime.now() - timedelta(hours=max_age_hours)
        
        for filename in os.listdir(self.sessions_dir):
            filepath = os.path.join(self.sessions_dir, filename)
            file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            
            if file_time < cutoff_time:
                os.remove(filepath)
                print(f"🧹 Cleaned up old session: {filename}")

class ProfileCycler:
    def __init__(self, config):
        self.config = config
        self.current_profile_index = 0
        self.profile_rotation_count = 0
        
    def get_next_technical_profile(self):
        """Cycle through technical characteristics"""
        profiles = [
            {"type": "desktop", "os": "windows", "browser": "chrome"},
            {"type": "desktop", "os": "mac", "browser": "safari"},
            {"type": "desktop", "os": "linux", "browser": "firefox"},
            {"type": "mobile", "os": "android", "browser": "chrome"},
            {"type": "mobile", "os": "ios", "browser": "safari"}
        ]
        
        profile = profiles[self.current_profile_index]
        self.current_profile_index = (self.current_profile_index + 1) % len(profiles)
        self.profile_rotation_count += 1
        
        return profile
    
    def should_rotate_profile(self, operation_count):
        """Determine when to rotate technical profile"""
        rotation_interval = self.config.PROFILE_ROTATION_INTERVAL
        return operation_count % rotation_interval == 0