import time
from datetime import datetime

class SelfHealingSystem:
    def __init__(self):
        self.error_log = []
        
    def diagnose_and_recover(self, error, bot_instance):
        error_type = type(error).__name__
        print(f"🔄 Self-healing triggered for {error_type}")
        
        if "Proxy" in error_type or "Connection" in error_type:
            bot_instance.proxy_rotator.refresh_proxies()
            return "proxy_refreshed"
        elif "ElementNotFound" in error_type:
            return "retry_with_delay"
        else:
            return "restart_browser"
            
    def log_error(self, error, recovery_action):
        self.error_log.append({
            "timestamp": datetime.now().isoformat(),
            "error": str(error),
            "recovery_action": recovery_action
        })