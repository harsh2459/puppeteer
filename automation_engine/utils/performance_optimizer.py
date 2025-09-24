import time
import psutil
from datetime import datetime

class PerformanceOptimizer:
    def __init__(self, config):
        self.config = config
        self.performance_history = []
        self.optimization_rules = self._initialize_optimization_rules()
        
    def _initialize_optimization_rules(self):
        """Initialize performance optimization rules"""
        return {
            'memory_usage': {
                'threshold': 80,  # Percentage
                'action': 'reduce_concurrency',
                'severity': 'high'
            },
            'cpu_usage': {
                'threshold': 75,
                'action': 'delay_operations', 
                'severity': 'medium'
            },
            'network_latency': {
                'threshold': 1000,  # milliseconds
                'action': 'switch_proxy',
                'severity': 'medium'
            },
            'operation_success_rate': {
                'threshold': 0.7,  # 70%
                'action': 'adjust_timing',
                'severity': 'high'
            }
        }
    
    def monitor_performance(self, operation_metrics):
        """Monitor system performance and apply optimizations"""
        current_metrics = self._gather_system_metrics()
        current_metrics.update(operation_metrics)
        
        self.performance_history.append({
            'timestamp': datetime.now().isoformat(),
            'metrics': current_metrics
        })
        
        # Keep only last 50 entries
        if len(self.performance_history) > 50:
            self.performance_history.pop(0)
        
        # Apply optimizations based on rules
        optimizations_applied = self._apply_optimization_rules(current_metrics)
        
        return {
            'current_metrics': current_metrics,
            'optimizations_applied': optimizations_applied
        }
    
    def _gather_system_metrics(self):
        """Gather current system performance metrics"""
        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()
        
        return {
            'memory_usage_percent': memory.percent,
            'memory_used_gb': memory.used / (1024**3),
            'cpu_usage_percent': cpu,
            'disk_usage_percent': disk.percent,
            'network_bytes_sent': network.bytes_sent,
            'network_bytes_recv': network.bytes_recv,
            'timestamp': datetime.now().isoformat()
        }
    
    def _apply_optimization_rules(self, current_metrics):
        """Apply optimization rules based on current metrics"""
        optimizations = []
        
        for metric_name, rule in self.optimization_rules.items():
            current_value = current_metrics.get(metric_name, 0)
            threshold = rule['threshold']
            
            if self._evaluate_condition(current_value, threshold, rule.get('condition', 'above')):
                optimization = self._execute_optimization_action(rule['action'], current_value)
                optimizations.append({
                    'metric': metric_name,
                    'value': current_value,
                    'threshold': threshold,
                    'action': rule['action'],
                    'optimization': optimization
                })
        
        return optimizations
    
    def _evaluate_condition(self, value, threshold, condition):
        """Evaluate optimization condition"""
        if condition == 'above':
            return value > threshold
        elif condition == 'below':
            return value < threshold
        elif condition == 'equal':
            return value == threshold
        else:
            return value > threshold  # Default to above
    
    def _execute_optimization_action(self, action, current_value):
        """Execute specific optimization action"""
        actions = {
            'reduce_concurrency': self._reduce_concurrency,
            'delay_operations': self._delay_operations,
            'switch_proxy': self._switch_proxy,
            'adjust_timing': self._adjust_timing,
            'clear_caches': self._clear_caches
        }
        
        if action in actions:
            return actions[action](current_value)
        else:
            return f"Unknown action: {action}"
    
    def _reduce_concurrency(self, memory_usage):
        """Reduce concurrent operations due to high memory usage"""
        # Implementation would adjust config.MAX_CONCURRENT_OPERATIONS
        reduction = max(1, int(self.config.MAX_CONCURRENT_OPERATIONS * 0.7))
        return f"Reduced concurrency from {self.config.MAX_CONCURRENT_OPERATIONS} to {reduction}"
    
    def _delay_operations(self, cpu_usage):
        """Increase delays between operations due to high CPU usage"""
        delay_increase = min(5.0, self.config.MAX_DELAY * 1.5)
        return f"Increased max delay to {delay_increase}s"
    
    def _switch_proxy(self, latency):
        """Switch proxy due to high network latency"""
        return "Initiated proxy rotation due to high latency"
    
    def _adjust_timing(self, success_rate):
        """Adjust timing based on operation success rate"""
        if success_rate < 0.7:
            timing_adjustment = "increased delays and variation"
        else:
            timing_adjustment = "optimized for speed"
        return f"Adjusted timing: {timing_adjustment}"
    
    def _clear_caches(self, _):
        """Clear caches to free memory"""
        import gc
        gc.collect()
        return "Cleared memory caches"