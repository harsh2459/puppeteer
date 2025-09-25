import asyncio
import random
import time
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from config import settings

class QuantumBotnetManager:
    def __init__(self, config):
        self.config = config
        self.active_bots: Dict[str, dict] = {}
        self.bot_groups: Dict[str, List[str]] = {}
        self.task_queue = asyncio.Queue()
        self.results_queue = asyncio.Queue()
        self.coordination_engine = CoordinationEngine(config)
        self.entropy_source = random.random()
        self.performance_metrics = {
            'total_operations': 0,
            'successful_operations': 0,
            'failed_operations': 0,
            'average_response_time': 0.0,
            'bot_uptime': {}
        }
        
    async def initialize_botnet(self, bot_count: int, group_strategy: str = "balanced"):
        """Initialize the botnet with specified number of bots"""
        try:
            if self.config.DEBUG_MODE:
                print(f"🚀 Initializing botnet with {bot_count} bots...")
            
            # Create bot groups based on strategy
            groups = self._create_bot_groups(bot_count, group_strategy)
            
            # Initialize bots asynchronously
            initialization_tasks = []
            for group_name, group_size in groups.items():
                for i in range(group_size):
                    bot_id = f"{group_name}_bot_{i+1}"
                    task = asyncio.create_task(self._initialize_single_bot(bot_id, group_name))
                    initialization_tasks.append(task)
            
            # Wait for all bots to initialize
            results = await asyncio.gather(*initialization_tasks, return_exceptions=True)
            
            successful_inits = sum(1 for r in results if r is True)
            
            if self.config.DEBUG_MODE:
                print(f"✅ Botnet initialized: {successful_inits}/{bot_count} bots ready")
            
            return successful_inits
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Botnet initialization failed: {e}")
            return 0
    
    def _create_bot_groups(self, total_bots: int, strategy: str) -> Dict[str, int]:
        """Create bot groups based on distribution strategy"""
        group_strategies = {
            "balanced": {
                "organic_traffic": 0.4,
                "social_media": 0.3,
                "research": 0.2,
                "shopping": 0.1
            },
            "stealth_focused": {
                "organic_traffic": 0.6,
                "research": 0.3,
                "social_media": 0.1
            },
            "aggressive": {
                "social_media": 0.5,
                "shopping": 0.3,
                "organic_traffic": 0.2
            }
        }
        
        strategy_weights = group_strategies.get(strategy, group_strategies["balanced"])
        groups = {}
        
        for group_name, weight in strategy_weights.items():
            group_size = max(1, int(total_bots * weight))
            groups[group_name] = group_size
        
        # Distribute remaining bots
        allocated_bots = sum(groups.values())
        remaining_bots = total_bots - allocated_bots
        
        if remaining_bots > 0:
            # Add to largest group
            largest_group = max(groups.items(), key=lambda x: x[1])
            groups[largest_group[0]] += remaining_bots
        
        return groups
    
    async def _initialize_single_bot(self, bot_id: str, group_name: str) -> bool:
        """Initialize a single bot instance"""
        try:
            # Create bot configuration
            bot_config = {
                'bot_id': bot_id,
                'group': group_name,
                'persona_type': self._select_persona_for_group(group_name),
                'geographic_context': self._select_geographic_context(),
                'behavioral_profile': self._generate_behavioral_profile(group_name),
                'technical_settings': self._generate_technical_settings(),
                'initialization_time': time.time(),
                'last_activity': time.time(),
                'status': 'initializing'
            }
            
            # Simulate bot initialization (in real implementation, this would create actual bot instances)
            await asyncio.sleep(random.uniform(1, 3))  # Simulate initialization time
            
            # Add to active bots
            self.active_bots[bot_id] = bot_config
            self.bot_groups.setdefault(group_name, []).append(bot_id)
            
            # Initialize performance tracking
            self.performance_metrics['bot_uptime'][bot_id] = {
                'start_time': time.time(),
                'last_checkin': time.time(),
                'total_uptime': 0
            }
            
            if self.config.DEBUG_MODE:
                print(f"🤖 Bot initialized: {bot_id}")
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Bot {bot_id} initialization failed: {e}")
            return False
    
    def _select_persona_for_group(self, group_name: str) -> str:
        """Select appropriate persona for bot group"""
        group_personas = {
            "organic_traffic": ["professional", "student", "retiree"],
            "social_media": ["student", "creative", "entrepreneur"],
            "research": ["professional", "entrepreneur", "student"],
            "shopping": ["professional", "retiree", "creative"]
        }
        
        return random.choice(group_personas.get(group_name, ["professional"]))
    
    def _select_geographic_context(self) -> Dict:
        """Select geographic context for bot"""
        regions = [
            {
                'country': 'US',
                'timezone': 'America/New_York',
                'locale': 'en_US'
            },
            {
                'country': 'GB',
                'timezone': 'Europe/London',
                'locale': 'en_GB'
            },
            {
                'country': 'DE',
                'timezone': 'Europe/Berlin',
                'locale': 'de_DE'
            },
            {
                'country': 'JP',
                'timezone': 'Asia/Tokyo',
                'locale': 'ja_JP'
            }
        ]
        
        return random.choice(regions)
    
    def _generate_behavioral_profile(self, group_name: str) -> Dict:
        """Generate behavioral profile for bot"""
        base_profiles = {
            "organic_traffic": {
                "browsing_speed": "moderate",
                "click_accuracy": 0.9,
                "session_length": (20, 60),
                "exploration_level": "balanced"
            },
            "social_media": {
                "browsing_speed": "fast",
                "click_accuracy": 0.8,
                "session_length": (10, 30),
                "exploration_level": "high"
            },
            "research": {
                "browsing_speed": "slow",
                "click_accuracy": 0.95,
                "session_length": (30, 90),
                "exploration_level": "focused"
            },
            "shopping": {
                "browsing_speed": "variable",
                "click_accuracy": 0.85,
                "session_length": (15, 45),
                "exploration_level": "comparative"
            }
        }
        
        return base_profiles.get(group_name, base_profiles["organic_traffic"])
    
    def _generate_technical_settings(self) -> Dict:
        """Generate technical settings for bot"""
        return {
            "browser_type": random.choice(["chrome", "firefox", "safari"]),
            "device_type": random.choice(["desktop", "laptop", "tablet"]),
            "network_speed": random.choice(["fast", "medium", "slow"]),
            "javascript_enabled": True,
            "cookies_enabled": random.random() < 0.8,
            "images_enabled": True
        }
    
    async def distribute_task(self, task: Dict, distribution_strategy: str = "round_robin") -> List:
        """Distribute task to botnet based on strategy"""
        try:
            task_id = hashlib.md5(json.dumps(task).encode()).hexdigest()[:8]
            task['task_id'] = task_id
            task['distribution_strategy'] = distribution_strategy
            
            if self.config.DEBUG_MODE:
                print(f"📋 Distributing task {task_id} to botnet...")
            
            # Select bots based on strategy
            selected_bots = self._select_bots_for_task(task, distribution_strategy)
            
            if not selected_bots:
                if self.config.DEBUG_MODE:
                    print("❌ No suitable bots available for task")
                return []
            
            # Execute task on selected bots
            execution_tasks = []
            for bot_id in selected_bots:
                execution_task = asyncio.create_task(
                    self._execute_task_on_bot(bot_id, task)
                )
                execution_tasks.append(execution_task)
            
            # Wait for results
            results = await asyncio.gather(*execution_tasks, return_exceptions=True)
            
            # Process results
            successful_results = []
            for result in results:
                if isinstance(result, dict) and result.get('success'):
                    successful_results.append(result)
                    self.performance_metrics['successful_operations'] += 1
                else:
                    self.performance_metrics['failed_operations'] += 1
            
            self.performance_metrics['total_operations'] += len(selected_bots)
            
            if self.config.DEBUG_MODE:
                print(f"✅ Task {task_id} completed: {len(successful_results)}/{len(selected_bots)} successful")
            
            return successful_results
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Task distribution failed: {e}")
            return []
    
    def _select_bots_for_task(self, task: Dict, strategy: str) -> List[str]:
        """Select appropriate bots for task execution"""
        available_bots = list(self.active_bots.keys())
        
        if not available_bots:
            return []
        
        task_requirements = task.get('requirements', {})
        required_group = task_requirements.get('bot_group')
        required_geography = task_requirements.get('geography')
        
        # Filter bots based on requirements
        filtered_bots = available_bots
        
        if required_group:
            filtered_bots = [b for b in filtered_bots if self.active_bots[b]['group'] == required_group]
        
        if required_geography:
            filtered_bots = [b for b in filtered_bots if 
                           self.active_bots[b]['geographic_context']['country'] == required_geography]
        
        if not filtered_bots:
            filtered_bots = available_bots  # Fallback to all bots
        
        # Apply selection strategy
        if strategy == "round_robin":
            return self._round_robin_selection(filtered_bots, task.get('bot_count', 1))
        elif strategy == "random":
            return self._random_selection(filtered_bots, task.get('bot_count', 1))
        elif strategy == "performance_based":
            return self._performance_based_selection(filtered_bots, task.get('bot_count', 1))
        else:
            return self._round_robin_selection(filtered_bots, task.get('bot_count', 1))
    
    def _round_robin_selection(self, bots: List[str], count: int) -> List[str]:
        """Round-robin bot selection"""
        if not hasattr(self, '_round_robin_index'):
            self._round_robin_index = 0
        
        selected = []
        for _ in range(min(count, len(bots))):
            selected.append(bots[self._round_robin_index % len(bots)])
            self._round_robin_index += 1
        
        return selected
    
    def _random_selection(self, bots: List[str], count: int) -> List[str]:
        """Random bot selection"""
        return random.sample(bots, min(count, len(bots)))
    
    def _performance_based_selection(self, bots: List[str], count: int) -> List[str]:
        """Performance-based bot selection"""
        # Sort bots by performance (simplified - in real implementation, use actual metrics)
        sorted_bots = sorted(bots, key=lambda b: self._calculate_bot_performance(b), reverse=True)
        return sorted_bots[:min(count, len(sorted_bots))]
    
    def _calculate_bot_performance(self, bot_id: str) -> float:
        """Calculate bot performance score"""
        bot_data = self.performance_metrics['bot_uptime'].get(bot_id, {})
        uptime = bot_data.get('total_uptime', 0)
        last_checkin = bot_data.get('last_checkin', 0)
        
        # Simple performance calculation (can be enhanced)
        uptime_score = min(1.0, uptime / 3600)  # Normalize to 1 hour
        recency_score = 1.0 if (time.time() - last_checkin) < 300 else 0.5  # 5 minutes threshold
        
        return (uptime_score + recency_score) / 2
    
    async def _execute_task_on_bot(self, bot_id: str, task: Dict) -> Dict:
        """Execute task on a specific bot"""
        try:
            start_time = time.time()
            
            # Update bot activity
            self.active_bots[bot_id]['last_activity'] = time.time()
            self.performance_metrics['bot_uptime'][bot_id]['last_checkin'] = time.time()
            
            # Simulate task execution (in real implementation, this would execute actual bot commands)
            execution_time = random.uniform(2, 10)  # Simulate variable execution time
            await asyncio.sleep(execution_time)
            
            # Simulate success/failure
            success_rate = task.get('success_rate', 0.9)
            success = random.random() < success_rate
            
            result = {
                'bot_id': bot_id,
                'task_id': task['task_id'],
                'success': success,
                'execution_time': time.time() - start_time,
                'result_data': self._generate_task_result(bot_id, task, success),
                'timestamp': time.time()
            }
            
            # Update performance metrics
            self._update_performance_metrics(bot_id, result)
            
            return result
            
        except Exception as e:
            return {
                'bot_id': bot_id,
                'task_id': task.get('task_id', 'unknown'),
                'success': False,
                'error': str(e),
                'timestamp': time.time()
            }
    
    def _generate_task_result(self, bot_id: str, task: Dict, success: bool) -> Dict:
        """Generate realistic task result data"""
        bot_info = self.active_bots[bot_id]
        
        if success:
            return {
                'status': 'completed',
                'data_captured': random.randint(1, 100),
                'pages_visited': random.randint(1, 5),
                'execution_quality': random.uniform(0.7, 1.0),
                'bot_signature': hashlib.md5(bot_id.encode()).hexdigest()[:8]
            }
        else:
            return {
                'status': 'failed',
                'error_type': random.choice(['timeout', 'captcha', 'network_error', 'element_not_found']),
                'retry_suggested': random.random() < 0.7,
                'failure_context': f"Bot {bot_id} encountered an issue"
            }
    
    def _update_performance_metrics(self, bot_id: str, result: Dict):
        """Update performance metrics based on task result"""
        # Update bot uptime
        current_time = time.time()
        bot_uptime = self.performance_metrics['bot_uptime'][bot_id]
        bot_uptime['total_uptime'] = current_time - bot_uptime['start_time']
        
        # Update average response time
        execution_time = result.get('execution_time', 0)
        total_ops = self.performance_metrics['total_operations']
        current_avg = self.performance_metrics['average_response_time']
        
        if total_ops > 0:
            new_avg = (current_avg * (total_ops - 1) + execution_time) / total_ops
            self.performance_metrics['average_response_time'] = new_avg
    
    async def monitor_botnet_health(self):
        """Continuous botnet health monitoring"""
        while True:
            try:
                current_time = time.time()
                inactive_threshold = 300  # 5 minutes
                
                # Check for inactive bots
                inactive_bots = []
                for bot_id, bot_data in self.active_bots.items():
                    last_activity = bot_data.get('last_activity', 0)
                    if current_time - last_activity > inactive_threshold:
                        inactive_bots.append(bot_id)
                        bot_data['status'] = 'inactive'
                
                # Attempt to reactivate inactive bots
                for bot_id in inactive_bots:
                    if random.random() < 0.3:  # 30% chance of successful reactivation
                        await self._reactivate_bot(bot_id)
                
                # Update performance metrics
                self._update_global_metrics()
                
                if self.config.DEBUG_MODE and inactive_bots:
                    print(f"⚠️ {len(inactive_bots)} bots marked as inactive")
                
                await asyncio.sleep(60)  # Check every minute
                
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"❌ Health monitoring error: {e}")
                await asyncio.sleep(30)
    
    async def _reactivate_bot(self, bot_id: str) -> bool:
        """Attempt to reactivate an inactive bot"""
        try:
            if self.config.DEBUG_MODE:
                print(f"🔄 Attempting to reactivate bot: {bot_id}")
            
            # Simulate reactivation process
            await asyncio.sleep(random.uniform(2, 5))
            
            # 80% chance of successful reactivation
            success = random.random() < 0.8
            
            if success:
                self.active_bots[bot_id]['status'] = 'active'
                self.active_bots[bot_id]['last_activity'] = time.time()
                self.performance_metrics['bot_uptime'][bot_id]['last_checkin'] = time.time()
            
            return success
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Bot reactivation failed: {e}")
            return False
    
    def _update_global_metrics(self):
        """Update global botnet performance metrics"""
        active_bots = sum(1 for b in self.active_bots.values() if b.get('status') == 'active')
        total_bots = len(self.active_bots)
        
        # Calculate success rate
        total_ops = self.performance_metrics['total_operations']
        successful_ops = self.performance_metrics['successful_operations']
        success_rate = successful_ops / total_ops if total_ops > 0 else 0
        
        self.performance_metrics.update({
            'active_bots': active_bots,
            'total_bots': total_bots,
            'success_rate': success_rate,
            'last_health_check': time.time()
        })
    
    def get_botnet_report(self) -> Dict:
        """Get comprehensive botnet status report"""
        group_stats = {}
        for group_name, bots in self.bot_groups.items():
            active_bots = sum(1 for b in bots if self.active_bots.get(b, {}).get('status') == 'active')
            group_stats[group_name] = {
                'total_bots': len(bots),
                'active_bots': active_bots,
                'utilization_rate': active_bots / len(bots) if bots else 0
            }
        
        return {
            'performance_metrics': self.performance_metrics,
            'group_statistics': group_stats,
            'total_groups': len(self.bot_groups),
            'botnet_health': self._calculate_botnet_health(),
            'coordination_status': self.coordination_engine.get_status()
        }
    
    def _calculate_botnet_health(self) -> float:
        """Calculate overall botnet health score"""
        active_bots = self.performance_metrics.get('active_bots', 0)
        total_bots = self.performance_metrics.get('total_bots', 1)
        success_rate = self.performance_metrics.get('success_rate', 0)
        
        availability_score = active_bots / total_bots
        performance_score = success_rate
        
        return (availability_score + performance_score) / 2
    
    async def graceful_shutdown(self):
        """Perform graceful shutdown of the botnet"""
        if self.config.DEBUG_MODE:
            print("🛑 Initiating graceful botnet shutdown...")
        
        # Signal all bots to shutdown
        shutdown_tasks = []
        for bot_id in self.active_bots.keys():
            task = asyncio.create_task(self._shutdown_bot(bot_id))
            shutdown_tasks.append(task)
        
        # Wait for shutdowns to complete
        await asyncio.gather(*shutdown_tasks, return_exceptions=True)
        
        if self.config.DEBUG_MODE:
            print("✅ Botnet shutdown completed")

class CoordinationEngine:
    """Advanced coordination engine for botnet management"""
    
    def __init__(self, config):
        self.config = config
        self.coordination_strategies = self._init_strategies()
        self.communication_log = []
    
    def _init_strategies(self):
        """Initialize coordination strategies"""
        return {
            'swarm_intelligence': {
                'description': 'Distributed decision making',
                'complexity': 'high',
                'stealth_level': 'high'
            },
            'centralized_control': {
                'description': 'Central command structure',
                'complexity': 'medium',
                'stealth_level': 'medium'
            },
            'hybrid_approach': {
                'description': 'Balanced centralized/distributed',
                'complexity': 'high',
                'stealth_level': 'high'
            }
        }
    
    def get_status(self):
        """Get coordination engine status"""
        return {
            'active_strategy': 'hybrid_approach',
            'communication_volume': len(self.communication_log),
            'coordination_efficiency': random.uniform(0.7, 0.95)
        }

# Utility function
def create_botnet_manager(config=None):
    """Factory function for easy botnet manager creation"""
    from config import settings
    config = config or settings.current_config
    return QuantumBotnetManager(config)