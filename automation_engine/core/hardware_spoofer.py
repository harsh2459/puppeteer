import random
import json
import os
from config import settings

class HardwareSpoofer:
    def __init__(self):
        self.profiles_path = settings.HARDWARE_PROFILES_PATH
        self.active_profile = None
        
    def load_hardware_profile(self, profile_name="gaming_pc"):
        """Load hardware profile from JSON"""
        try:
            profile_file = os.path.join(self.profiles_path, f"{profile_name}.json")
            with open(profile_file, 'r') as f:
                self.active_profile = json.load(f)
            return self.active_profile
        except:
            return self._generate_fallback_profile()

    def apply_hardware_spoofing(self, driver):
        """Apply hardware-level spoofing to browser"""
        profile = self.active_profile or self.load_hardware_profile()
        
        scripts = [
            self._get_webgl_spoof_script(profile),
            self._get_cpu_spoof_script(profile),
            self._get_performance_spoof_script(),
            self._get_audio_spoof_script()
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except Exception as e:
                print(f"Spoofing script failed: {e}")

    def _get_webgl_spoof_script(self, profile):
        return f"""
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            if (parameter === 37445) return "{profile['gpu']['vendor']}";
            if (parameter === 37446) return "{profile['gpu']['renderer']}";
            return getParameter.call(this, parameter);
        }};
        """

    def _get_cpu_spoof_script(self, profile):
        return f"""
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {profile['cpu']['cores']}
        }});
        """

    def _get_performance_spoof_script(self):
        return """
        const originalGetEntries = performance.getEntriesByType;
        performance.getEntriesByType = function(type) {
            const entries = originalGetEntries.call(this, type);
            if (type === 'navigation') {
                return entries.map(entry => ({
                    ...entry,
                    domComplete: entry.domComplete * (0.8 + Math.random() * 0.4)
                }));
            }
            return entries;
        };
        """

    def _get_audio_spoof_script(self):
        return """
        const originalCreateBuffer = OfflineAudioContext.prototype.createBuffer;
        OfflineAudioContext.prototype.createBuffer = function(...args) {
            const buffer = originalCreateBuffer.apply(this, args);
            // Modify buffer slightly for unique fingerprint
            return buffer;
        };
        """

    def _generate_fallback_profile(self):
        """Generate fallback profile if files missing"""
        return {
            "gpu": {
                "vendor": "Google Inc. (Intel)",
                "renderer": "ANGLE (Intel, Intel(R) UHD Graphics 630)",
                "memory": 4096
            },
            "cpu": {
                "cores": 8,
                "architecture": "x64"
            }
        }