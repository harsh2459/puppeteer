import time
import random
from core.bot_engine import PhantomBot
from proxies.proxy_rotator import ProxyRotator
from utils.user_agent_rotator import get_random_user_agent
from utils.self_healing import SelfHealingSystem
from utils.swarm_coordinator import SwarmCoordinator
from config import settings

class PennyFlowOperator:
    def __init__(self, use_swarm=False):
        self.proxy_rotator = ProxyRotator()
        self.self_healing = SelfHealingSystem()
        self.swarm_coordinator = SwarmCoordinator() if use_swarm else None
        self.session_count = 0
        
    def run_operation(self, target_url=None):
        target = target_url or settings.TARGET_URL
        
        if self.swarm_coordinator:
            self.swarm_coordinator.run_swarm_operation(target)
            return True
            
        proxy = self.proxy_rotator.get_random_proxy()
        user_agent = get_random_user_agent()
        
        if not proxy:
            print("❌ No valid proxies available")
            return False
            
        bot = PhantomBot(proxy=proxy, user_agent=user_agent)
        
        try:
            print(f"🚀 Starting session {self.session_count + 1}")
            bot.launch_browser()
            bot.driver.get(target)
            bot.random_delay(2, 4)
            
            # === YOUR MONEY-MAKING LOGIC HERE ===
            actions_count = 0
            
            # Example actions (customize these):
            # bot.random_scroll()
            # actions_count += 1
            
            # Record successful operation
            bot.record_success(True, actions_count)
            self.session_count += 1
            print(f"✅ Session {self.session_count} completed")
            return True
            
        except Exception as e:
            recovery_action = self.self_healing.diagnose_and_recover(e, self)
            self.self_healing.log_error(e, recovery_action)
            print(f"❌ Session failed, recovery: {recovery_action}")
            return False
            
        finally:
            bot.quit()
            time.sleep(random.randint(10, 30))

def main():
    operator = PennyFlowOperator(use_swarm=True)
    print("🔥 PennyFlow Commander - Advanced Edition Started 🔥")
    
    while True:
        success = operator.run_operation()
        if not success:
            time.sleep(60)

if __name__ == '__main__':
    main()