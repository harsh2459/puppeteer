import random
import json
import os
from pathlib import Path

class AdaptiveBehavior:
    def __init__(self):
        self.behavior_log = []
        self.load_behavior_data()
        
    def load_behavior_data(self):
        behavior_file = Path("logs/behavior_data.json")
        if behavior_file.exists():
            with open(behavior_file, 'r') as f:
                self.behavior_log = json.load(f)
                
    def save_behavior_data(self):
        with open("logs/behavior_data.json", 'w') as f:
            json.dump(self.behavior_log, f, indent=4)
            
    def get_optimized_delay(self, success_rate):
        if success_rate > 0.8:
            return random.uniform(0.5, 1.5)
        elif success_rate > 0.5:
            return random.uniform(1.0, 3.0)
        else:
            return random.uniform(2.0, 5.0)
            
    def record_operation(self, success, duration, actions_count):
        self.behavior_log.append({
            "success": success,
            "duration": duration,
            "actions_count": actions_count,
            "timestamp": time.time()
        })
        self.save_behavior_data()