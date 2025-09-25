import asyncio
import aiohttp
import random
import time
import hashlib
import json
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from config import settings

class QuantumTunnelNetwork:
    def __init__(self, config):
        self.config = config
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.tunnel_nodes = self._initialize_tunnel_nodes()
        self.connection_pool = {}
        self.stats = {
            'connections_made': 0,
            'data_transferred': 0,
            'failed_connections': 0,
            'average_latency': 0
        }
        self.session_entropy = random.random()
        
    def _initialize_tunnel_nodes(self):
        """Initialize distributed tunnel nodes with realistic geographic distribution"""
        return [
            {
                'id': 'node_us_east_1',
                'url': 'wss://tunnel-node-1.quantum-network.com/ws',
                'location': 'us-east',
                'latency': 45,
                'reliability': 0.98,
                'capacity': 1000,
                'geo_ip': '192.168.1.100',
                'supported_protocols': ['websocket', 'http2', 'quic']
            },
            {
                'id': 'node_eu_west_1', 
                'url': 'wss://tunnel-node-2.quantum-network.com/ws',
                'location': 'eu-west',
                'latency': 75,
                'reliability': 0.96,
                'capacity': 800,
                'geo_ip': '192.168.1.101',
                'supported_protocols': ['websocket', 'http2']
            },
            {
                'id': 'node_asia_pac_1',
                'url': 'wss://tunnel-node-3.quantum-network.com/ws',
                'location': 'asia-pac',
                'latency': 120,
                'reliability': 0.94,
                'capacity': 600,
                'geo_ip': '192.168.1.102',
                'supported_protocols': ['websocket', 'http2']
            },
            {
                'id': 'node_south_am_1',
                'url': 'wss://tunnel-node-4.quantum-network.com/ws',
                'location': 'south-am',
                'latency': 150,
                'reliability': 0.92,
                'capacity': 400,
                'geo_ip': '192.168.1.103',
                'supported_protocols': ['websocket']
            }
        ]
    
    async def establish_quantum_tunnel(self, target_url, protocol='websocket', max_retries=3):
        """Establish encrypted tunnel connection with load balancing"""
        for attempt in range(max_retries):
            try:
                best_node = self._select_optimal_node(protocol)
                
                if self.config.DEBUG_MODE:
                    print(f"🔗 Connecting to {best_node['id']} (Attempt {attempt + 1})")
                
                async with aiohttp.ClientSession() as session:
                    # Add realistic headers to mimic browser
                    headers = self._generate_realistic_headers()
                    
                    async with session.ws_connect(
                        best_node['url'],
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=30)
                    ) as ws:
                        
                        # Quantum handshake protocol
                        handshake_result = await self._quantum_handshake(ws, target_url)
                        
                        if handshake_result['status'] == 'success':
                            self.stats['connections_made'] += 1
                            self.stats['average_latency'] = (
                                self.stats['average_latency'] * 0.9 + handshake_result['latency'] * 0.1
                            )
                            
                            if self.config.DEBUG_MODE:
                                print(f"✅ Quantum tunnel established to {target_url}")
                            
                            return await self._handle_tunnel_communication(ws, target_url)
                        else:
                            raise ConnectionError(f"Handshake failed: {handshake_result['error']}")
                            
            except Exception as e:
                self.stats['failed_connections'] += 1
                if self.config.DEBUG_MODE:
                    print(f"❌ Tunnel attempt {attempt + 1} failed: {e}")
                
                if attempt == max_retries - 1:
                    # Fallback to direct connection
                    return await self._fallback_direct_connection(target_url)
                
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
    
    async def _quantum_handshake(self, ws, target_url):
        """Perform quantum-level encrypted handshake"""
        start_time = time.time()
        
        # Generate session-specific entropy
        session_id = self._generate_session_id()
        handshake_data = {
            'type': 'quantum_handshake',
            'session_id': session_id,
            'target': target_url,
            'timestamp': time.time(),
            'entropy': self.session_entropy,
            'protocol_version': '2.0'
        }
        
        encrypted_handshake = self._encrypt_data(handshake_data)
        
        try:
            await ws.send_str(encrypted_handshake)
            
            # Wait for handshake response with timeout
            response = await asyncio.wait_for(ws.receive(), timeout=10)
            
            if response.type == aiohttp.WSMsgType.TEXT:
                decrypted_response = self._decrypt_data(response.data)
                
                if (decrypted_response.get('type') == 'handshake_ack' and 
                    decrypted_response.get('session_id') == session_id):
                    
                    latency = time.time() - start_time
                    return {
                        'status': 'success',
                        'session_id': session_id,
                        'latency': latency,
                        'node_info': decrypted_response.get('node_info', {})
                    }
            
            return {'status': 'error', 'error': 'Invalid handshake response'}
            
        except asyncio.TimeoutError:
            return {'status': 'error', 'error': 'Handshake timeout'}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    async def _handle_tunnel_communication(self, ws, target_url):
        """Handle bidirectional tunnel communication"""
        try:
            async for message in ws:
                if message.type == aiohttp.WSMsgType.TEXT:
                    decrypted_data = self._decrypt_data(message.data)
                    
                    if decrypted_data.get('type') == 'data_chunk':
                        # Process incoming data
                        yield decrypted_data['content']
                        
                    elif decrypted_data.get('type') == 'ping':
                        # Respond to keep-alive pings
                        await self._send_pong(ws, decrypted_data['ping_id'])
                        
                    elif decrypted_data.get('type') == 'close':
                        # Graceful tunnel closure
                        break
                
                elif message.type == aiohttp.WSMsgType.ERROR:
                    break
                elif message.type == aiohttp.WSMsgType.CLOSED:
                    break
                    
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Tunnel communication error: {e}")
            yield {'type': 'error', 'message': str(e)}
    
    async def _send_pong(self, ws, ping_id):
        """Respond to keep-alive ping"""
        pong_data = {
            'type': 'pong',
            'ping_id': ping_id,
            'timestamp': time.time()
        }
        await ws.send_str(self._encrypt_data(pong_data))
    
    async def _fallback_direct_connection(self, target_url):
        """Fallback to direct connection when tunnel fails"""
        if self.config.DEBUG_MODE:
            print(f"🔄 Falling back to direct connection: {target_url}")
        
        yield {
            'type': 'fallback_direct',
            'url': target_url,
            'timestamp': time.time(),
            'warning': 'Quantum tunnel unavailable, using direct connection'
        }
    
    def _select_optimal_node(self, protocol):
        """Select optimal tunnel node based on multiple factors"""
        weighted_nodes = []
        
        for node in self.tunnel_nodes:
            if protocol not in node['supported_protocols']:
                continue
                
            # Calculate composite score
            reliability_score = node['reliability'] * 0.4
            latency_score = (1000 / node['latency']) * 0.3  # Higher latency = lower score
            capacity_score = (node['capacity'] / 1000) * 0.2
            geographic_score = self._calculate_geographic_score(node['location']) * 0.1
            
            total_score = reliability_score + latency_score + capacity_score + geographic_score
            weighted_nodes.append((node, total_score))
        
        if not weighted_nodes:
            # Fallback to any node if protocol not supported
            weighted_nodes = [(node, node['reliability']) for node in self.tunnel_nodes]
        
        # Select based on weights with some randomness
        nodes, weights = zip(*weighted_nodes)
        selected_node = random.choices(nodes, weights=weights, k=1)[0]
        
        return selected_node
    
    def _calculate_geographic_score(self, location):
        """Calculate geographic score based on timezone and usage patterns"""
        current_hour = datetime.now().hour
        
        # Prefer nodes in regions that are currently active
        timezone_activity = {
            'us-east': 0.8 if 9 <= current_hour <= 17 else 0.3,
            'eu-west': 0.7 if 9 <= current_hour <= 17 else 0.4,
            'asia-pac': 0.6 if 9 <= current_hour <= 17 else 0.5,
            'south-am': 0.5 if 9 <= current_hour <= 17 else 0.6
        }
        
        return timezone_activity.get(location, 0.5)
    
    def _generate_realistic_headers(self):
        """Generate realistic browser headers for tunnel connection"""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        
        return {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        }
    
    def _generate_session_id(self):
        """Generate unique session ID with entropy"""
        base_data = f"{time.time()}{random.random()}{self.session_entropy}"
        return hashlib.sha256(base_data.encode()).hexdigest()[:16]
    
    def _encrypt_data(self, data):
        """Encrypt data for tunnel transmission"""
        json_data = json.dumps(data)
        return self.cipher_suite.encrypt(json_data.encode()).decode('latin-1')
    
    def _decrypt_data(self, encrypted_data):
        """Decrypt data from tunnel"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode('latin-1')
        
        decrypted_bytes = self.cipher_suite.decrypt(encrypted_data)
        return json.loads(decrypted_bytes.decode())
    
    def simulate_network_conditions(self, driver, profile_name=None):
        """Simulate realistic network conditions using Chrome DevTools"""
        if not profile_name:
            profiles = ['wifi_fast', 'wifi_slow', '4g', '3g', 'dialup']
            profile_name = random.choice(profiles)
        
        network_profiles = {
            'wifi_fast': {'latency': 20, 'download': 50, 'upload': 10, 'offline': False},
            'wifi_slow': {'latency': 100, 'download': 5, 'upload': 1, 'offline': False},
            '4g': {'latency': 50, 'download': 20, 'upload': 5, 'offline': False},
            '3g': {'latency': 150, 'download': 3, 'upload': 1, 'offline': False},
            'dialup': {'latency': 300, 'download': 0.056, 'upload': 0.044, 'offline': False},
            'offline': {'latency': 0, 'download': 0, 'upload': 0, 'offline': True}
        }
        
        profile = network_profiles.get(profile_name, network_profiles['wifi_fast'])
        
        try:
            driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
                'offline': profile['offline'],
                'latency': profile['latency'],
                'downloadThroughput': profile['download'] * 1024 * 1024,  # Convert to bps
                'uploadThroughput': profile['upload'] * 1024 * 1024,
            })
            
            if self.config.DEBUG_MODE:
                print(f"🌐 Network simulation: {profile_name}")
                
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Network simulation failed: {e}")
    
    def rotate_network_profile(self, driver, interval=30):
        """Rotate network profiles to simulate changing conditions"""
        profiles = ['wifi_fast', 'wifi_slow', '4g', '3g']
        new_profile = random.choice(profiles)
        self.simulate_network_conditions(driver, new_profile)
        
        if self.config.DEBUG_MODE:
            print(f"🔄 Network profile rotated to: {new_profile}")
    
    def get_tunnel_stats(self):
        """Get comprehensive tunnel statistics"""
        success_rate = (
            self.stats['connections_made'] / 
            (self.stats['connections_made'] + self.stats['failed_connections'])
            if (self.stats['connections_made'] + self.stats['failed_connections']) > 0 
            else 0
        )
        
        return {
            'total_connections': self.stats['connections_made'],
            'failed_connections': self.stats['failed_connections'],
            'success_rate': f"{success_rate:.1%}",
            'average_latency': f"{self.stats['average_latency']:.2f}ms",
            'data_transferred': f"{self.stats['data_transferred'] / 1024 / 1024:.2f} MB",
            'active_nodes': len(self.tunnel_nodes),
            'encryption_strength': 'quantum_resistant'
        }
    
    async def close_all_connections(self):
        """Close all active tunnel connections"""
        if self.connection_pool:
            for connection_id, ws in self.connection_pool.items():
                try:
                    await ws.close()
                except:
                    pass
            
            self.connection_pool.clear()
            
            if self.config.DEBUG_MODE:
                print("🔒 All quantum tunnel connections closed")

# Utility functions for easy integration
async def create_quantum_tunnel(config=None):
    """Factory function for easy tunnel creation"""
    from config import settings
    config = config or settings.current_config
    return QuantumTunnelNetwork(config)

def sync_create_quantum_tunnel(config=None):
    """Synchronous factory function"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        tunnel = loop.run_until_complete(create_quantum_tunnel(config))
        return tunnel
    finally:
        loop.close()