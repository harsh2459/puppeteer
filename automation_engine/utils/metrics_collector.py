import time
import json
import threading
from datetime import datetime
from collections import deque

class MetricsCollector:
    def __init__(self, config):
        self.config = config
        self.operation_metrics = deque(maxlen=1000)  # Keep last 1000 operations
        self.performance_data = {}
        self.lock = threading.Lock()
        
    def record_operation_start(self, operation_id, operation_type):
        """Record operation start time and details"""
        with self.lock:
            self.operation_metrics.append({
                'id': operation_id,
                'type': operation_type,
                'start_time': time.time(),
                'end_time': None,
                'success': None,
                'details': {}
            })
            
    def record_operation_end(self, operation_id, success=True, details=None):
        """Record operation completion and results"""
        with self.lock:
            for op in self.operation_metrics:
                if op['id'] == operation_id:
                    op['end_time'] = time.time()
                    op['success'] = success
                    op['details'] = details or {}
                    break
                    
    def record_performance_metric(self, metric_name, value):
        """Record performance-related metrics"""
        with self.lock:
            if metric_name not in self.performance_data:
                self.performance_data[metric_name] = deque(maxlen=100)
            self.performance_data[metric_name].append({
                'timestamp': datetime.now().isoformat(),
                'value': value
            })
            
    def get_success_rate(self, operation_type=None, window_size=100):
        """Calculate success rate for recent operations"""
        with self.lock:
            relevant_ops = [op for op in self.operation_metrics 
                          if op['end_time'] is not None and
                          (operation_type is None or op['type'] == operation_type)]
            
            if not relevant_ops:
                return 0.0
                
            recent_ops = relevant_ops[-window_size:]
            successful = sum(1 for op in recent_ops if op['success'])
            return successful / len(recent_ops)
            
    def get_performance_stats(self):
        """Get comprehensive performance statistics"""
        with self.lock:
            completed_ops = [op for op in self.operation_metrics if op['end_time'] is not None]
            
            if not completed_ops:
                return {}
                
            durations = [op['end_time'] - op['start_time'] for op in completed_ops]
            recent_ops = completed_ops[-50:]  # Last 50 operations
            
            return {
                'total_operations': len(completed_ops),
                'success_rate': self.get_success_rate(),
                'avg_duration': sum(durations) / len(durations),
                'recent_success_rate': self.get_success_rate(window_size=50),
                'performance_metrics': {k: len(v) for k, v in self.performance_data.items()}
            }
            
    def save_metrics(self):
        """Save metrics to file for analysis"""
        if not self.config.ENABLE_METRICS:
            return
            
        filename = f"{self.config.DATA_PATH}metrics_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        data = {
            'timestamp': datetime.now().isoformat(),
            'operations': list(self.operation_metrics),
            'performance': dict(self.performance_data)
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Could not save metrics: {e}")