import threading
import psutil
import time
from queue import Queue
from datetime import datetime
import json

class QuantumResourceManager:
    def __init__(self, config):
        self.config = config
        self.connection_pool = Queue()
        self.memory_usage_log = []
        self.performance_metrics = {}
        self.lock = threading.Lock()
        self.optimization_thread = None
        self.running = False
        
        # Initialize connection pool
        self._initialize_connection_pool()
        
    def _initialize_connection_pool(self):
        """Initialize connection pool based on system resources"""
        max_connections = min(
            self.config.MAX_CONCURRENT_OPERATIONS,
            psutil.cpu_count() * 2,  # Conservative scaling
            int(psutil.virtual_memory().available / (512 * 1024 * 1024))  # 512MB per connection
        )
        
        for i in range(max_connections):
            self.connection_pool.put({
                'id': f'conn_{i}',
                'status': 'available',
                'last_used': datetime.now(),
                'usage_count': 0
            })
            
        print(f"🔧 Connection pool initialized with {max_connections} connections")
    
    def acquire_connection(self, timeout=30):
        """Acquire a connection from the pool with timeout"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                if not self.connection_pool.empty():
                    conn = self.connection_pool.get_nowait()
                    conn['status'] = 'active'
                    conn['last_used'] = datetime.now()
                    conn['usage_count'] += 1
                    
                    # Monitor memory usage
                    self._log_memory_usage()
                    return conn
                    
            except:
                pass
                
            time.sleep(0.1)
            
        raise Exception("❌ Connection acquisition timeout")
    
    def release_connection(self, connection):
        """Release connection back to pool"""
        connection['status'] = 'available'
        self.connection_pool.put(connection)
        
        # Cleanup memory if needed
        self._optimize_memory_usage()
    
    def _log_memory_usage(self):
        """Log current memory usage for optimization"""
        memory_info = psutil.virtual_memory()
        self.memory_usage_log.append({
            'timestamp': datetime.now().isoformat(),
            'used_gb': memory_info.used / (1024**3),
            'available_gb': memory_info.available / (1024**3),
            'percent': memory_info.percent,
            'active_connections': self.connection_pool.qsize()
        })
        
        # Keep only last 100 entries
        if len(self.memory_usage_log) > 100:
            self.memory_usage_log.pop(0)
    
    def _optimize_memory_usage(self):
        """Optimize memory usage based on current load"""
        if len(self.memory_usage_log) < 5:
            return
            
        recent_usage = self.memory_usage_log[-5:]
        avg_usage = sum(entry['percent'] for entry in recent_usage) / 5
        
        if avg_usage > 85:  # High memory usage
            self._reduce_memory_footprint()
        elif avg_usage < 30:  # Low memory usage
            self._expand_capacity()
    
    def _reduce_memory_footprint(self):
        """Reduce memory footprint when usage is high"""
        print("🔄 Reducing memory footprint...")
        # Implement memory cleanup strategies
        import gc
        gc.collect()
        
    def _expand_capacity(self):
        """Expand capacity when usage is low"""
        current_size = self.connection_pool.qsize()
        max_allowed = min(50, psutil.cpu_count() * 3)  # Conservative limit
        
        if current_size < max_allowed:
            new_conn = {
                'id': f'conn_exp_{current_size}',
                'status': 'available',
                'last_used': datetime.now(),
                'usage_count': 0
            }
            self.connection_pool.put(new_conn)
            print(f"📈 Expanded connection pool to {current_size + 1}")
    
    def get_performance_metrics(self):
        """Get comprehensive performance metrics"""
        memory_info = psutil.virtual_memory()
        cpu_percent = psutil.cpu_percent(interval=1)
        
        return {
            'timestamp': datetime.now().isoformat(),
            'memory_used_gb': round(memory_info.used / (1024**3), 2),
            'memory_available_gb': round(memory_info.available / (1024**3), 2),
            'memory_percent': memory_info.percent,
            'cpu_percent': cpu_percent,
            'active_connections': self.config.MAX_CONCURRENT_OPERATIONS - self.connection_pool.qsize(),
            'available_connections': self.connection_pool.qsize(),
            'connection_utilization': f"{((self.config.MAX_CONCURRENT_OPERATIONS - self.connection_pool.qsize()) / self.config.MAX_CONCURRENT_OPERATIONS * 100):.1f}%"
        }
    
    def start_optimization_loop(self):
        """Start background optimization thread"""
        self.running = True
        self.optimization_thread = threading.Thread(target=self._optimization_loop)
        self.optimization_thread.daemon = True
        self.optimization_thread.start()
        print("🔧 Resource optimization loop started")
    
    def stop_optimization_loop(self):
        """Stop optimization thread"""
        self.running = False
        if self.optimization_thread:
            self.optimization_thread.join()
        print("🔧 Resource optimization loop stopped")
    
    def _optimization_loop(self):
        """Background optimization loop"""
        while self.running:
            try:
                self._log_memory_usage()
                self._optimize_memory_usage()
                
                # Clean up old metrics
                current_time = time.time()
                self.performance_metrics = {
                    k: v for k, v in self.performance_metrics.items() 
                    if current_time - v['timestamp'] < 300  # Keep 5 minutes
                }
                
            except Exception as e:
                print(f"⚠️ Optimization loop error: {e}")
                
            time.sleep(10)  # Run every 10 seconds

class ConnectionPool:
    """Advanced connection pooling with health checks"""
    def __init__(self, max_size=20):
        self.max_size = max_size
        self.active_connections = {}
        self.available_connections = Queue()
        self.connection_counter = 0
        self.health_check_interval = 60  # seconds
        
    def get_connection(self, bot_config):
        """Get a healthy connection"""
        # Try to get available connection first
        if not self.available_connections.empty():
            conn_id = self.available_connections.get()
            if self._is_connection_healthy(conn_id):
                return self.active_connections[conn_id]
        
        # Create new connection if under limit
        if len(self.active_connections) < self.max_size:
            return self._create_new_connection(bot_config)
        
        # Wait for available connection
        return self._wait_for_connection()
    
    def _create_new_connection(self, bot_config):
        """Create new bot connection"""
        from core.bot_engine import QuantumBot
        
        conn_id = f"conn_{self.connection_counter}"
        self.connection_counter += 1
        
        bot = QuantumBot(
            proxy=bot_config.get('proxy'),
            user_agent=bot_config.get('user_agent'),
            use_quantum_stealth=True
        )
        
        self.active_connections[conn_id] = {
            'bot': bot,
            'created_at': datetime.now(),
            'last_used': datetime.now(),
            'usage_count': 0,
            'status': 'active'
        }
        
        return self.active_connections[conn_id]
    
    def _is_connection_healthy(self, conn_id):
        """Check if connection is still healthy"""
        conn = self.active_connections.get(conn_id)
        if not conn:
            return False
            
        # Check if browser session is still valid
        try:
            conn['bot'].driver.current_url
            return True
        except:
            # Connection is dead, clean up
            self._cleanup_connection(conn_id)
            return False
    
    def _cleanup_connection(self, conn_id):
        """Clean up dead connection"""
        if conn_id in self.active_connections:
            try:
                self.active_connections[conn_id]['bot'].quit()
            except:
                pass
            del self.active_connections[conn_id]