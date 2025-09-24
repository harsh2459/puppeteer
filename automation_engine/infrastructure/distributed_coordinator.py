import threading
import time
import json
from datetime import datetime
from queue import Queue, PriorityQueue

class DistributedCoordinator:
    def __init__(self, config):
        self.config = config
        self.operation_queue = PriorityQueue()
        self.active_operations = {}
        self.completed_operations = {}
        self.node_assignments = {}
        self.coordination_lock = threading.Lock()
        self.operation_counter = 0
        
        # Initialize load balancer
        from infrastructure.load_balancer import QuantumLoadBalancer
        self.load_balancer = QuantumLoadBalancer(config)
        
        # Initialize resource manager
        from infrastructure.resource_manager import QuantumResourceManager
        self.resource_manager = QuantumResourceManager(config)
        
        # Start coordination threads
        self._start_coordination_system()
    
    def _start_coordination_system(self):
        """Start distributed coordination system"""
        self.coordination_thread = threading.Thread(target=self._coordination_loop)
        self.coordination_thread.daemon = True
        self.coordination_thread.start()
        
        self.health_check_thread = threading.Thread(target=self._health_check_loop)
        self.health_check_thread.daemon = True
        self.health_check_thread.start()
        
        print("🔧 Distributed coordination system started")
    
    def submit_operation(self, operation_type, target_url, priority=5, geographic_preference=None):
        """Submit operation to distributed system"""
        operation_id = f"op_{self.operation_counter}_{int(time.time())}"
        self.operation_counter += 1
        
        operation_data = {
            'id': operation_id,
            'type': operation_type,
            'target_url': target_url,
            'priority': priority,
            'geographic_preference': geographic_preference,
            'submission_time': datetime.now().isoformat(),
            'status': 'queued'
        }
        
        # Add to priority queue (lower number = higher priority)
        self.operation_queue.put((priority, operation_data))
        
        with self.coordination_lock:
            self.active_operations[operation_id] = operation_data
        
        print(f"📥 Operation submitted: {operation_id} (priority: {priority})")
        return operation_id
    
    def _coordination_loop(self):
        """Main coordination loop for distributing operations"""
        while True:
            try:
                if not self.operation_queue.empty():
                    # Get highest priority operation
                    priority, operation_data = self.operation_queue.get_nowait()
                    operation_id = operation_data['id']
                    
                    # Find optimal node
                    optimal_node = self.load_balancer.get_optimal_node(
                        operation_data['type'],
                        operation_data['geographic_preference']
                    )
                    
                    if optimal_node:
                        # Assign operation to node
                        self._assign_operation_to_node(operation_id, optimal_node, operation_data)
                    else:
                        # No available nodes, re-queue with lower priority
                        operation_data['priority'] += 1
                        if operation_data['priority'] <= 10:  # Max priority level
                            self.operation_queue.put((operation_data['priority'], operation_data))
                            print(f"🔁 Re-queued {operation_id} with priority {operation_data['priority']}")
                        else:
                            print(f"❌ Operation {operation_id} failed - no available nodes")
                
                time.sleep(0.1)  # Small delay to prevent busy waiting
                
            except Exception as e:
                print(f"⚠️ Coordination loop error: {e}")
                time.sleep(1)
    
    def _assign_operation_to_node(self, operation_id, node_id, operation_data):
        """Assign operation to specific node"""
        with self.coordination_lock:
            self.node_assignments[operation_id] = {
                'node_id': node_id,
                'assignment_time': datetime.now().isoformat(),
                'status': 'assigned'
            }
            
            operation_data['status'] = 'assigned'
            operation_data['assigned_node'] = node_id
            operation_data['assignment_time'] = datetime.now().isoformat()
        
        print(f"🔀 Operation {operation_id} assigned to node {node_id}")
        
        # In real implementation, this would send operation to node
        # For now, simulate execution
        self._simulate_operation_execution(operation_id, node_id, operation_data)
    
    def _simulate_operation_execution(self, operation_id, node_id, operation_data):
        """Simulate operation execution (replace with actual node communication)"""
        def execute_operation():
            try:
                start_time = time.time()
                
                # Simulate operation execution time
                execution_time = random.uniform(5, 15)
                time.sleep(execution_time)
                
                # Simulate success/failure
                success = random.random() > 0.1  # 90% success rate
                
                response_time = time.time() - start_time
                
                # Update load balancer stats
                self.load_balancer.update_performance_stats(node_id, success, response_time)
                
                # Mark operation as completed
                with self.coordination_lock:
                    operation_data['status'] = 'completed' if success else 'failed'
                    operation_data['completion_time'] = datetime.now().isoformat()
                    operation_data['execution_time'] = response_time
                    operation_data['success'] = success
                    
                    self.completed_operations[operation_id] = operation_data
                    if operation_id in self.active_operations:
                        del self.active_operations[operation_id]
                    
                    # Release node
                    self.load_balancer.release_node(node_id)
                
                status_icon = "✅" if success else "❌"
                print(f"{status_icon} Operation {operation_id} completed on node {node_id} "
                      f"({response_time:.1f}s, success: {success})")
                
            except Exception as e:
                print(f"❌ Operation {operation_id} failed with error: {e}")
                
                with self.coordination_lock:
                    operation_data['status'] = 'failed'
                    operation_data['error'] = str(e)
                    self.completed_operations[operation_id] = operation_data
                    if operation_id in self.active_operations:
                        del self.active_operations[operation_id]
                    
                    self.load_balancer.release_node(node_id)
        
        # Execute in separate thread
        execution_thread = threading.Thread(target=execute_operation)
        execution_thread.daemon = True
        execution_thread.start()
    
    def _health_check_loop(self):
        """Health check loop for distributed system"""
        while True:
            try:
                self.load_balancer.run_health_checks()
                time.sleep(60)  # Run health checks every minute
            except Exception as e:
                print(f"⚠️ Health check loop error: {e}")
                time.sleep(30)
    
    def get_system_status(self):
        """Get comprehensive system status"""
        with self.coordination_lock:
            queued_operations = self.operation_queue.qsize()
            active_operations = len(self.active_operations)
            completed_operations = len(self.completed_operations)
            
            node_status = {}
            for node_id, node_data in self.load_balancer.node_pool.items():
                node_status[node_id] = {
                    'status': node_data['status'],
                    'load': node_data['current_load'],
                    'capacity': node_data['capacity'],
                    'region': node_data['region']
                }
        
        return {
            'timestamp': datetime.now().isoformat(),
            'queued_operations': queued_operations,
            'active_operations': active_operations,
            'completed_operations': completed_operations,
            'node_status': node_status,
            'system_health': self._calculate_system_health()
        }
    
    def _calculate_system_health(self):
        """Calculate overall system health"""
        healthy_nodes = sum(
            1 for node_data in self.load_balancer.node_pool.values()
            if node_data['status'] == 'healthy'
        )
        total_nodes = len(self.load_balancer.node_pool)
        
        if total_nodes == 0:
            return "unknown"
        
        health_ratio = healthy_nodes / total_nodes
        
        if health_ratio >= 0.8:
            return "healthy"
        elif health_ratio >= 0.5:
            return "degraded"
        else:
            return "unhealthy"