import time
import random
import uuid
from .bot_engine import PhantomBot
from utils.metrics_collector import MetricsCollector
from utils.pattern_manager import PatternManager

class EnhancedBot(PhantomBot):
    def __init__(self, proxy=None, user_agent=None, config=None):
        super().__init__(proxy, user_agent)
        self.config = config
        self.metrics = MetricsCollector(config) if config.ENABLE_METRICS else None
        self.pattern_manager = PatternManager(config) if config.ENABLE_PATTERN_VARIATION else None
        self.operation_id = str(uuid.uuid4())[:8]
        
    def enhanced_navigate(self, url, operation_type="navigation"):
        """Enhanced navigation with metrics and pattern variation"""
        if self.metrics:
            self.metrics.record_operation_start(self.operation_id, operation_type)
            
        try:
            # Apply pattern-based timing
            base_delay = random.uniform(self.config.MIN_DELAY, self.config.MAX_DELAY)
            if self.pattern_manager:
                base_delay = self.pattern_manager.apply_timing_variation(base_delay)
                
            # Perform navigation
            self.driver.get(url)
            time.sleep(base_delay)
            
            # Record success
            if self.metrics:
                self.metrics.record_operation_end(self.operation_id, success=True, 
                                                details={'url': url, 'delay_used': base_delay})
                
            return True
            
        except Exception as e:
            # Record failure
            if self.metrics:
                self.metrics.record_operation_end(self.operation_id, success=False, 
                                                details={'error': str(e), 'url': url})
            return False
            
    def enhanced_click(self, element, element_description="unknown"):
        """Enhanced click with pattern variation"""
        try:
            # Apply click variation if enabled
            if self.pattern_manager:
                pattern = self.pattern_manager.get_current_pattern()
                variation = pattern['click_variation']
                # Add slight random movement
                self.human_click(element, use_advanced_movement=variation > 0.2)
            else:
                self.human_click(element)
                
            # Record performance metric
            if self.metrics:
                self.metrics.record_performance_metric('clicks_executed', 1)
                
            return True
            
        except Exception as e:
            if self.metrics:
                self.metrics.record_performance_metric('click_errors', 1)
            return False
            
    def enhanced_scroll(self, scroll_count=None):
        """Enhanced scrolling with pattern-based behavior"""
        if self.pattern_manager:
            pattern = self.pattern_manager.get_scroll_pattern()
            count_range = pattern['count']
            distance_range = pattern['distance']
            
            scroll_count = scroll_count or random.randint(*count_range)
            
            for _ in range(scroll_count):
                distance = random.randint(*distance_range)
                self.driver.execute_script(f"window.scrollBy(0, {distance});")
                delay = self.pattern_manager.apply_timing_variation(0.5)
                time.sleep(delay)
        else:
            # Fallback to original behavior
            self.random_scroll()
            
    def get_operation_stats(self):
        """Get statistics for current operation session"""
        if self.metrics:
            return self.metrics.get_performance_stats()
        return {}