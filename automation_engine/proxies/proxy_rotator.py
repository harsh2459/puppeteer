import time
import random
from .free_proxy_manager import get_valid_proxies, TorProxyManager  # ADD TorProxyManager
from config import settings

class ProxyRotator:
    def __init__(self, use_tor=True):  # ADD use_tor parameter
        self.use_tor = use_tor
        if use_tor:
            self.tor_manager = TorProxyManager()
            self.ip_change_counter = 0
        else:
            self.proxies = []
            self.last_refresh = 0
            self.refresh_proxies()
        
    def refresh_proxies(self):
        if self.use_tor:
            return True
            
        current_time = time.time()
        if current_time - self.last_refresh >= settings.PROXY_REFRESH_INTERVAL or not self.proxies:
            self.proxies = get_valid_proxies()
            self.last_refresh = current_time
            return True
        return False
        
    def get_random_proxy(self):
        if self.use_tor:
            # Change IP every 3 requests
            if self.ip_change_counter >= 3:
                self.tor_manager.renew_tor_identity()
                self.ip_change_counter = 0
            self.ip_change_counter += 1
            return f"socks5://127.0.0.1:9050"
        else:
            if not self.proxies:
                self.refresh_proxies()
            return random.choice(self.proxies) if self.proxies else None
        
    def get_proxy_count(self):
        if self.use_tor:
            return 1  # Tor provides infinite IPs
        return len(self.proxies)