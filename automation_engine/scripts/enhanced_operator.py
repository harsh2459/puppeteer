import time
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.enhanced_bot import EnhancedBot
from proxies.proxy_rotator import ProxyRotator
from utils.user_agent_rotator import get_random_user_agent
from config.settings import current_config

class EnhancedPennyFlowOperator:
    def __init__(self, config=None):
        self.config = config or current_config
        self.proxy_rotator = ProxyRotator(use_tor=self.config.USE_TOR_PROXY)
        self.session_stats = {
            'total_operations': 0,
            'successful_operations': 0,
            'failed_operations': 0,
            'start_time': time.time()
        }
        
    def run_enhanced_operation(self, target_url=None, operation_type="revenue_generation"):
        """Run operation with enhanced features"""
        target_url = target_url or self.config.TARGET_URL
        
        # Create enhanced bot instance
        proxy = self.proxy_rotator.get_random_proxy()
        user_agent = get_random_user_agent()
        
        bot = EnhancedBot(
            proxy=proxy, 
            user_agent=user_agent, 
            config=self.config
        )
        
        try:
            print(f"🚀 Starting enhanced operation {self.session_stats['total_operations'] + 1}")
            
            # Launch browser with enhanced navigation
            success = bot.enhanced_navigate(target_url, operation_type)
            
            if success:
                # Perform enhanced operations
                self._execute_enhanced_operations(bot)
                self.session_stats['successful_operations'] += 1
            else:
                self.session_stats['failed_operations'] += 1
                
            self.session_stats['total_operations'] += 1
            
            # Display operation stats if metrics enabled
            if self.config.ENABLE_METRICS:
                stats = bot.get_operation_stats()
                print(f"📊 Operation stats: {stats}")
                
            return success
            
        except Exception as e:
            print(f"❌ Enhanced operation failed: {e}")
            self.session_stats['failed_operations'] += 1
            self.session_stats['total_operations'] += 1
            return False
            
        finally:
            bot.quit()
            self._smart_delay()
            
    def _execute_enhanced_operations(self, bot):
        """Execute enhanced money-making operations"""
        # Enhanced scrolling with pattern variation
        bot.enhanced_scroll()
        
        # TODO: Add your specific revenue operations here
        # Example enhanced operations:
        # bot.enhanced_click(revenue_button, "revenue_button")
        # bot.enhanced_type(form_field, "user_data")
        
        # Additional enhanced scrolling
        bot.enhanced_scroll(scroll_count=random.randint(1, 3))
        
    def _smart_delay(self):
        """Intelligent delay based on success rate and configuration"""
        total_ops = self.session_stats['total_operations']
        if total_ops == 0:
            base_delay = random.randint(30, 60)
        else:
            success_rate = self.session_stats['successful_operations'] / total_ops
            
            if success_rate > 0.8:
                base_delay = random.randint(10, 30)  # Faster for high success
            elif success_rate > 0.5:
                base_delay = random.randint(30, 60)  # Normal pace
            else:
                base_delay = random.randint(60, 120)  # Slower for low success
                
        # Apply pattern variation if enabled
        if hasattr(self, 'pattern_manager') and self.pattern_manager:
            base_delay = self.pattern_manager.apply_timing_variation(base_delay)
            
        print(f"⏰ Next operation in {base_delay} seconds...")
        time.sleep(base_delay)
        
    def get_session_stats(self):
        """Get comprehensive session statistics"""
        duration = time.time() - self.session_stats['start_time']
        total_ops = self.session_stats['total_operations']
        success_rate = (self.session_stats['successful_operations'] / total_ops * 100) if total_ops > 0 else 0
        
        return {
            'duration_seconds': int(duration),
            'total_operations': total_ops,
            'successful_operations': self.session_stats['successful_operations'],
            'failed_operations': self.session_stats['failed_operations'],
            'success_rate_percent': round(success_rate, 1),
            'operations_per_hour': round(total_ops / (duration / 3600), 1) if duration > 0 else 0
        }

def main():
    """Main enhanced operation loop"""
    operator = EnhancedPennyFlowOperator()
    
    print("🔥 ENHANCED PENNYFLOW OPERATOR STARTED 🔥")
    print(f"📝 Configuration: {operator.config.get_operation_settings()}")
    
    try:
        operation_count = 0
        while True:
            success = operator.run_enhanced_operation()
            operation_count += 1
            
            # Print session stats every 10 operations
            if operation_count % 10 == 0:
                stats = operator.get_session_stats()
                print(f"📈 Session progress: {stats}")
                
            if not success:
                print("💤 Waiting before retry...")
                time.sleep(60)
                
    except KeyboardInterrupt:
        print("\n🛑 Enhanced operator stopped by user")
        final_stats = operator.get_session_stats()
        print(f"📊 Final session statistics: {final_stats}")

if __name__ == "__main__":
    main()