import time
import random
from .free_proxy_manager import get_valid_proxies
from config import settings

class ProxyRotator:
    def __init__(self):
        self.proxies = []
        self.last_refresh = 0
        self.refresh_proxies()
        
    def refresh_proxies(self):
        current_time = time.time()
        if current_time - self.last_refresh >= settings.PROXY_REFRESH_INTERVAL or not self.proxies:
            self.proxies = get_valid_proxies()
            self.last_refresh = current_time
            return True
        return False
        
    def get_random_proxy(self):
        if not self.proxies:
            self.refresh_proxies()
        return random.choice(self.proxies) if self.proxies else None
        
    def get_proxy_count(self):
        return len(self.proxies)