import os
from datetime import datetime

class Config:
    def __init__(self):
        self.load_environment_settings()
        
    def load_environment_settings(self):
        # Core operation settings
        self.TARGET_URL = os.getenv('TARGET_URL', "https://your-site.com")
        self.OPERATION_MODE = os.getenv('OPERATION_MODE', "standard")  # standard, stealth, aggressive
        
        # Timing and behavior settings
        self.MIN_DELAY = float(os.getenv('MIN_DELAY', '1.0'))
        self.MAX_DELAY = float(os.getenv('MAX_DELAY', '5.0'))
        self.ADAPTIVE_TIMING = os.getenv('ADAPTIVE_TIMING', 'true').lower() == 'true'
        
        # Proxy and network settings
        self.USE_TOR_PROXY = os.getenv('USE_TOR_PROXY', 'true').lower() == 'true'
        self.PROXY_ROTATION_INTERVAL = int(os.getenv('PROXY_ROTATION_INTERVAL', '10'))
        
        # Performance settings
        self.MAX_CONCURRENT_OPERATIONS = int(os.getenv('MAX_CONCURRENT_OPERATIONS', '3'))
        self.OPERATION_TIMEOUT = int(os.getenv('OPERATION_TIMEOUT', '30'))
        
        # Enhancement flags (phased activation)
        self.ENABLE_METRICS = os.getenv('ENABLE_METRICS', 'true').lower() == 'true'
        self.ENABLE_PATTERN_VARIATION = os.getenv('ENABLE_PATTERN_VARIATION', 'true').lower() == 'true'
        self.ENABLE_ADAPTIVE_BEHAVIOR = os.getenv('ENABLE_ADAPTIVE_BEHAVIOR', 'false').lower() == 'true'
        
        # Path configurations
        self.LOG_PATH = os.getenv('LOG_PATH', 'log/operation_logs/')
        self.DATA_PATH = os.getenv('DATA_PATH', 'data/')
        
    def update_setting(self, key, value):
        """Dynamically update configuration at runtime"""
        if hasattr(self, key):
            setattr(self, key, value)
            print(f"Updated setting: {key} = {value}")
            
    def get_operation_settings(self):
        """Get settings for current operation mode"""
        return {
            'mode': self.OPERATION_MODE,
            'timing': [self.MIN_DELAY, self.MAX_DELAY],
            'adaptive': self.ADAPTIVE_TIMING,
            'enhancements': {
                'metrics': self.ENABLE_METRICS,
                'pattern_variation': self.ENABLE_PATTERN_VARIATION,
                'adaptive_behavior': self.ENABLE_ADAPTIVE_BEHAVIOR
            }
        }

# Global configuration instance
current_config = Config()