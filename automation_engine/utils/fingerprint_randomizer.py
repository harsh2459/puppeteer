import random
import time
import hashlib

class FingerprintRandomizer:
    def __init__(self):
        self.fingerprint_history = []
        
    def randomize_browser_fingerprint(self, driver):
        """Randomize all detectable browser fingerprints"""
        randomization_actions = [
            self._randomize_user_agent(driver),
            self._randomize_screen_properties(driver),
            self._randomize_timezone(driver),
            self._randomize_language_settings(driver),
            self._randomize_hardware_properties(driver),
            self._randomize_plugin_fingerprint(driver)
        ]
        
        return randomization_actions
    
    def _randomize_user_agent(self, driver):
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        ]
        
        new_agent = random.choice(agents)
        script = f"Object.defineProperty(navigator, 'userAgent', {{get: () => '{new_agent}'}});"
        
        try:
            driver.execute_script(script)
            return f"user_agent_updated: {new_agent[:30]}..."
        except:
            return "user_agent_update_failed"
    
    def _randomize_screen_properties(self, driver):
        resolutions = [
            {"width": 1920, "height": 1080},
            {"width": 1366, "height": 768},
            {"width": 1536, "height": 864},
            {"width": 1440, "height": 900},
            {"width": 1600, "height": 900}
        ]
        
        resolution = random.choice(resolutions)
        scripts = [
            f"Object.defineProperty(screen, 'width', {{get: () => {resolution['width']}}});",
            f"Object.defineProperty(screen, 'height', {{get: () => {resolution['height']}}});",
            f"Object.defineProperty(screen, 'availWidth', {{get: () => {resolution['width'] - 100}}});",
            f"Object.defineProperty(screen, 'availHeight', {{get: () => {resolution['height'] - 100}}});",
            f"window.screen.width = {resolution['width']};",
            f"window.screen.height = {resolution['height']};"
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except: pass
        
        return f"screen_resolution_updated: {resolution['width']}x{resolution['height']}"
    
    def _randomize_timezone(self, driver):
        timezones = [
            "America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney",
            "Europe/Paris", "Asia/Shanghai", "America/Los_Angeles", "Europe/Berlin"
        ]
        
        new_tz = random.choice(timezones)
        script = f"""
        Object.defineProperty(Intl.DateTimeFormat.prototype, 'resolvedOptions', {{
            get: () => () => ({{
                timeZone: '{new_tz}',
                locale: 'en-US'
            }})
        }});
        """
        
        try:
            driver.execute_script(script)
            return f"timezone_updated: {new_tz}"
        except:
            return "timezone_update_failed"
    
    def _randomize_language_settings(self, driver):
        language_sets = [
            ["en-US", "en"],
            ["en-GB", "en"],
            ["en-US", "en", "es"],
            ["en-US", "en", "fr"]
        ]
        
        languages = random.choice(language_sets)
        scripts = [
            f"Object.defineProperty(navigator, 'language', {{get: () => '{languages[0]}'}});",
            f"Object.defineProperty(navigator, 'languages', {{get: () => {languages}}});"
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except: pass
        
        return f"languages_updated: {languages}"
    
    def _randomize_hardware_properties(self, driver):
        hardware_configs = [
            {"cores": 4, "memory": 4},
            {"cores": 8, "memory": 8},
            {"cores": 12, "memory": 16},
            {"cores": 16, "memory": 32}
        ]
        
        config = random.choice(hardware_configs)
        scripts = [
            f"Object.defineProperty(navigator, 'hardwareConcurrency', {{get: () => {config['cores']}}});",
            f"Object.defineProperty(navigator, 'deviceMemory', {{get: () => {config['memory']}}});"
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except: pass
        
        return f"hardware_updated: {config['cores']} cores, {config['memory']}GB"
    
    def _randomize_plugin_fingerprint(self, driver):
        plugin_counts = [3, 5, 8, 12]
        plugin_count = random.choice(plugin_counts)
        
        script = f"""
        Object.defineProperty(navigator, 'plugins', {{
            get: () => ({{
                length: {plugin_count},
                item: (index) => ({{ name: `Plugin${{index}}`, filename: `plugin${{index}}.dll` }}),
                namedItem: (name) => null
            }})
        }});
        """
        
        try:
            driver.execute_script(script)
            return f"plugins_updated: {plugin_count} plugins"
        except:
            return "plugins_update_failed"
    
    def get_fingerprint_hash(self, driver):
        """Generate current fingerprint hash for tracking"""
        try:
            fingerprint_data = driver.execute_script("""
            return {
                userAgent: navigator.userAgent,
                platform: navigator.platform,
                language: navigator.language,
                languages: navigator.languages,
                hardwareConcurrency: navigator.hardwareConcurrency,
                deviceMemory: navigator.deviceMemory,
                screen: {width: screen.width, height: screen.height},
                timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
            };
            """)
            
            fingerprint_str = str(fingerprint_data)
            return hashlib.md5(fingerprint_str.encode()).hexdigest()
            
        except:
            return "unknown_fingerprint"