import requests
import time
import random

class TorProxyManager:
    def __init__(self):
        self.tor_port = 9050
        self.control_port = 9051
        
    def get_tor_session(self):
        """Get requests session with Tor proxy"""
        session = requests.Session()
        session.proxies = {
            'http': f'socks5://127.0.0.1:{self.tor_port}',
            'https': f'socks5://127.0.0.1:{self.tor_port}'
        }
        return session
    
    def renew_tor_identity(self):
        """Renew Tor circuit for new IP"""
        try:
            from stem import Signal
            from stem.control import Controller
            with Controller.from_port(port=self.control_port) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                time.sleep(5)  # Wait for new circuit
        except:
            # Fallback if Tor control not available
            pass

def get_valid_proxies():
    """Fallback to free proxies if Tor not available"""
    # Simple free proxy list as backup
    backup_proxies = [
        "103.150.110.10:8080",
        "45.95.147.370:8080", 
        "188.166.117.230:8080"
    ]
    return backup_proxies