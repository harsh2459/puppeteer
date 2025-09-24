import random
import time
from datetime import datetime
from threading import Lock
import requests

class QuantumLoadBalancer:
    def __init__(self, config):
        self.config = config
        self.node_pool = {}
        self.geo_distribution = {}
        self.traffic_patterns = {}
        self.lock = Lock()
        self.performance_stats = {}
        
        self._initialize_geo_distribution()
        self._initialize_traffic_patterns()
    
    def _initialize_geo_distribution(self):
        """Initialize geographic distribution patterns"""
        self.geo_distribution = {
            "north_america": {
                "weight": 0.4,
                "proxies": ["us", "ca"],
                "timezone_offset": [-5, -8],
                "languages": ["en-US", "en-CA"]
            },
            "europe": {
                "weight": 0.3,
                "proxies": ["uk", "de", "fr", "nl"],
                "timezone_offset": [0, 2],
                "languages": ["en-GB", "de-DE", "fr-FR"]
            },
            "asia": {
                "weight": 0.2,
                "proxies": ["jp", "sg", "kr"],
                "timezone_offset": [8, 9],
                "languages": ["ja-JP", "ko-KR", "zh-CN"]
            },
            "other": {
                "weight": 0.1,
                "proxies": ["au", "br"],
                "timezone_offset": [10, -3],
                "languages": ["en-AU", "pt-BR"]
            }
        }
    
    def _initialize_traffic_patterns(self):
        """Initialize realistic traffic patterns"""
        self.traffic_patterns = {
            "business_hours": {
                "description": "High activity during business hours",
                "peak_start": 9,  # 9 AM
                "peak_end": 17,   # 5 PM
                "base_requests_per_hour": 50,
                "peak_multiplier": 3.0
            },
            "evening_surge": {
                "description": "Evening usage surge",
                "peak_start": 18,  # 6 PM
                "peak_end": 22,    # 10 PM
                "base_requests_per_hour": 30,
                "peak_multiplier": 2.5
            },
            "weekend": {
                "description": "Weekend browsing patterns",
                "peak_start": 10,  # 10 AM
                "peak_end": 20,    # 8 PM
                "base_requests_per_hour": 40,
                "peak_multiplier": 2.0
            },
            "steady": {
                "description": "Steady low-volume traffic",
                "base_requests_per_hour": 20,
                "peak_multiplier": 1.2
            }
        }
    
    def register_node(self, node_id, node_capacity, geographic_region, performance_metrics=None):
        """Register a new node in the load balancer"""
        with self.lock:
            self.node_pool[node_id] = {
                'capacity': node_capacity,
                'region': geographic_region,
                'current_load': 0,
                'performance_metrics': performance_metrics or {},
                'last_health_check': datetime.now(),
                'status': 'healthy'
            }
            
            print(f"🔧 Node registered: {node_id} in {geographic_region}")
    
    def get_optimal_node(self, operation_type="standard", geographic_preference=None):
        """Get optimal node based on load and geography"""
        with self.lock:
            available_nodes = [
                node_id for node_id, node_data in self.node_pool.items()
                if node_data['status'] == 'healthy' 
                and node_data['current_load'] < node_data['capacity'] * 0.8  # 80% capacity threshold
            ]
            
            if not available_nodes:
                return None
            
            # Filter by geographic preference if specified
            if geographic_preference:
                preferred_nodes = [
                    node_id for node_id in available_nodes
                    if self.node_pool[node_id]['region'] == geographic_preference
                ]
                if preferred_nodes:
                    available_nodes = preferred_nodes
            
            # Select node based on load balancing algorithm
            if operation_type == "high_priority":
                # Choose least loaded node
                selected_node = min(available_nodes, 
                                  key=lambda x: self.node_pool[x]['current_load'])
            else:
                # Weighted random selection based on capacity
                weights = [
                    self.node_pool[node_id]['capacity'] - self.node_pool[node_id]['current_load']
                    for node_id in available_nodes
                ]
                selected_node = random.choices(available_nodes, weights=weights)[0]
            
            # Update load
            self.node_pool[selected_node]['current_load'] += 1
            
            return selected_node
    
    def release_node(self, node_id):
        """Release node after operation completion"""
        with self.lock:
            if node_id in self.node_pool:
                self.node_pool[node_id]['current_load'] = max(
                    0, self.node_pool[node_id]['current_load'] - 1
                )
    
    def get_geographic_distribution(self, target_region=None):
        """Get geographic distribution for traffic normalization"""
        if target_region:
            return self.geo_distribution.get(target_region, self.geo_distribution["north_america"])
        
        # Weighted random selection based on distribution weights
        regions = list(self.geo_distribution.keys())
        weights = [self.geo_distribution[region]["weight"] for region in regions]
        selected_region = random.choices(regions, weights=weights)[0]
        
        return self.geo_distribution[selected_region]
    
    def get_traffic_pattern(self, pattern_name=None):
        """Get traffic pattern for request timing"""
        if not pattern_name:
            # Auto-select based on current time
            current_hour = datetime.now().hour
            weekday = datetime.now().weekday() < 5  # Monday-Friday
            
            if weekday and 9 <= current_hour <= 17:
                pattern_name = "business_hours"
            elif 18 <= current_hour <= 22:
                pattern_name = "evening_surge"
            elif not weekday:
                pattern_name = "weekend"
            else:
                pattern_name = "steady"
        
        return self.traffic_patterns.get(pattern_name, self.traffic_patterns["steady"])
    
    def calculate_request_delay(self, pattern_name=None):
        """Calculate delay between requests based on traffic pattern"""
        pattern = self.get_traffic_pattern(pattern_name)
        
        base_delay = 3600 / pattern["base_requests_per_hour"]  # seconds between requests
        
        # Apply peak multiplier if in peak hours
        current_hour = datetime.now().hour
        if pattern.get('peak_start') and pattern.get('peak_end'):
            if pattern['peak_start'] <= current_hour <= pattern['peak_end']:
                base_delay /= pattern['peak_multiplier']
        
        # Add some randomness
        jitter = random.uniform(0.8, 1.2)
        final_delay = base_delay * jitter
        
        return max(1, final_delay)  # Minimum 1 second delay
    
    def update_performance_stats(self, node_id, operation_success, response_time):
        """Update performance statistics for nodes"""
        with self.lock:
            if node_id not in self.performance_stats:
                self.performance_stats[node_id] = {
                    'total_operations': 0,
                    'successful_operations': 0,
                    'total_response_time': 0,
                    'response_time_samples': []
                }
            
            stats = self.performance_stats[node_id]
            stats['total_operations'] += 1
            if operation_success:
                stats['successful_operations'] += 1
            stats['total_response_time'] += response_time
            stats['response_time_samples'].append(response_time)
            
            # Keep only last 100 samples
            if len(stats['response_time_samples']) > 100:
                stats['response_time_samples'].pop(0)
    
    def get_node_health(self, node_id):
        """Get health status of a node"""
        with self.lock:
            if node_id not in self.node_pool:
                return "unknown"
            
            node_data = self.node_pool[node_id]
            success_rate = 0
            
            if node_id in self.performance_stats:
                stats = self.performance_stats[node_id]
                if stats['total_operations'] > 0:
                    success_rate = stats['successful_operations'] / stats['total_operations']
            
            # Determine health based on success rate and load
            if success_rate < 0.7:
                return "unhealthy"
            elif node_data['current_load'] > node_data['capacity'] * 0.9:
                return "overloaded"
            else:
                return "healthy"
    
    def run_health_checks(self):
        """Run health checks on all nodes"""
        with self.lock:
            for node_id in list(self.node_pool.keys()):
                health_status = self.get_node_health(node_id)
                self.node_pool[node_id]['status'] = health_status
                self.node_pool[node_id]['last_health_check'] = datetime.now()
                
                if health_status != "healthy":
                    print(f"⚠️ Node {node_id} status: {health_status}")