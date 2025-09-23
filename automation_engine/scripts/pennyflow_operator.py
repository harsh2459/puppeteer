import time
import random
import threading
from core.bot_engine import PhantomBot
from proxies.proxy_rotator import ProxyRotator
from utils.user_agent_rotator import get_random_user_agent
from utils.self_healing import SelfHealingSystem
from utils.swarm_coordinator import SwarmCoordinator
from config import settings

class PennyFlowOperator:
    def __init__(self, use_swarm=False, swarm_size=None):
        self.proxy_rotator = ProxyRotator(use_tor=settings.USE_TOR_PROXY)
        self.self_healing = SelfHealingSystem()
        self.swarm_coordinator = SwarmCoordinator() if use_swarm else None
        self.swarm_size = swarm_size or settings.MAX_SWARM_SIZE
        self.session_count = 0
        self.successful_operations = 0
        self.failed_operations = 0
        
    def run_operation(self, target_url=None, custom_operations=None):
        """Execute a single operation with advanced features"""
        target = target_url or settings.TARGET_URL
        
        if self.swarm_coordinator and self.swarm_size > 1:
            return self._run_swarm_operation(target, custom_operations)
            
        return self._run_single_operation(target, custom_operations)
    
    def _run_single_operation(self, target_url, custom_operations):
        """Run single bot operation"""
        proxy = self.proxy_rotator.get_random_proxy()
        user_agent = get_random_user_agent()
        
        if not proxy:
            print("❌ No valid proxies available")
            return False
            
        bot = PhantomBot(
            proxy=proxy, 
            user_agent=user_agent,
            use_advanced_stealth=settings.HARDWARE_SPOOFING_ENABLED
        )
        
        try:
            print(f"🚀 Starting advanced session {self.session_count + 1}")
            bot.launch_browser()
            bot.driver.get(target_url)
            bot.random_delay(1, 3)
            
            # Execute custom operations or default behavior
            operations = custom_operations or self._get_default_operations()
            success = bot.execute_operation(operations)
            
            if success:
                self.successful_operations += 1
                print(f"✅ Session {self.session_count + 1} completed successfully")
            else:
                self.failed_operations += 1
                print(f"⚠️ Session {self.session_count + 1} completed with issues")
                
            self.session_count += 1
            return success
            
        except Exception as e:
            self.failed_operations += 1
            recovery_action = self.self_healing.diagnose_and_recover(e, self)
            self.self_healing.log_error(e, recovery_action)
            print(f"❌ Session failed, recovery: {recovery_action}")
            return False
            
        finally:
            bot.quit()
            # Intelligent delay based on success rate
            delay = self._calculate_intelligent_delay()
            time.sleep(delay)
    
    def _run_swarm_operation(self, target_url, custom_operations):
        """Run coordinated swarm operation"""
        print(f"🐝 Launching swarm of {self.swarm_size} bots")
        return self.swarm_coordinator.run_swarm_operation(
            target_url, 
            self.swarm_size, 
            custom_operations
        )
    
    def _get_default_operations(self):
        """Default money-making operations"""
        def default_ops(bot):
            # Random scrolling to generate engagement
            for _ in range(random.randint(2, 5)):
                bot.random_scroll()
                bot.random_delay(1, 2)
            
            # TODO: Add your specific revenue operations here
            # Example: bot.human_click(some_element)
            
        return [default_ops]
    
    def _calculate_intelligent_delay(self):
        """Calculate delay based on success rate"""
        total_ops = self.successful_operations + self.failed_operations
        if total_ops == 0:
            return random.randint(30, 60)
            
        success_rate = self.successful_operations / total_ops
        
        if success_rate > 0.8:  # High success - faster operations
            return random.randint(10, 30)
        elif success_rate > 0.5:  # Medium success - normal pace
            return random.randint(30, 60)
        else:  # Low success - slower, more cautious
            return random.randint(60, 120)
    
    def get_stats(self):
        """Get operation statistics"""
        total = self.successful_operations + self.failed_operations
        success_rate = (self.successful_operations / total * 100) if total > 0 else 0
        
        return {
            "total_operations": total,
            "successful": self.successful_operations,
            "failed": self.failed_operations,
            "success_rate": f"{success_rate:.1f}%",
            "current_session": self.session_count
        }

def main():
    """Main execution with enhanced features"""
    operator = PennyFlowOperator(use_swarm=True, swarm_size=3)
    print("🔥 PENNYFLOW COMMANDER - ADVANCED EDITION 🔥")
    print("🚀 Hardware Spoofing: ENABLED")
    print("🤖 Synthetic Identities: ENABLED") 
    print("🌐 Tor Proxy: ENABLED")
    print("🧠 Adaptive Behavior: ENABLED")
    
    try:
        while True:
            success = operator.run_operation()
            stats = operator.get_stats()
            print(f"📊 Stats: {stats}")
            
            if not success:
                print("💤 Waiting 60 seconds before retry...")
                time.sleep(60)
                
    except KeyboardInterrupt:
        print("\n🛑 Shutting down PennyFlow Commander...")
        final_stats = operator.get_stats()
        print(f"📈 Final Statistics: {final_stats}")

if __name__ == '__main__':
    main()