import time
import random
import math
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

class TemporalManipulator:
    def __init__(self, config):
        self.config = config
        self.time_anomalies = []
        self.reference_time = time.time()
        self.time_dilation_factor = 1.0
        self.historical_offset = 0
        self.quantum_entropy = random.random()
        
    def create_time_dilation(self, driver, dilation_factor=None):
        """Create time dilation effects to confuse timing analysis"""
        if dilation_factor is None:
            dilation_factor = random.uniform(0.95, 1.05)  # Small natural variations
        
        self.time_dilation_factor = dilation_factor
        
        scripts = [
            # Override performance timing with quantum variations
            f"""
            // Quantum performance timing override
            const originalNow = performance.now;
            let timeOffset = 0;
            let lastCall = Date.now();
            
            performance.now = function() {{
                const realTime = originalNow.call(this);
                // Add quantum-level variations that are consistent per session
                timeOffset += (Math.random() - 0.5) * 0.2 * {dilation_factor};
                const adjustedTime = realTime * {dilation_factor} + timeOffset;
                lastCall = Date.now();
                return Math.max(0, adjustedTime);
            }};
            """,
            
            # Override Date object with temporal manipulation
            f"""
            // Temporal Date manipulation
            const timeDilation = {dilation_factor};
            const timeSkew = {random.randint(-1000, 1000)}; // Small random skew
            
            const OriginalDate = window.Date;
            const originalDateNow = OriginalDate.now;
            
            window.Date = function(...args) {{
                if (args.length === 0) {{
                    const realTime = originalDateNow();
                    return new OriginalDate(realTime * timeDilation + timeSkew);
                }}
                return new OriginalDate(...args);
            }};
            
            // Copy static methods with temporal adjustments
            Object.getOwnPropertyNames(OriginalDate).forEach(prop => {{
                if (!['length', 'name', 'prototype', 'now'].includes(prop)) {{
                    window.Date[prop] = OriginalDate[prop];
                }}
            }});
            
            window.Date.now = () => originalDateNow() * timeDilation + timeSkew;
            window.Date.parse = OriginalDate.parse;
            window.Date.UTC = OriginalDate.UTC;
            """,
            
            # Override timers with temporal consistency
            f"""
            // Temporal timer manipulation
            const timerDilation = {dilation_factor};
            
            const originalSetTimeout = window.setTimeout;
            const originalSetInterval = window.setInterval;
            
            window.setTimeout = function(callback, delay, ...args) {{
                const dilatedDelay = delay * timerDilation;
                return originalSetTimeout(callback, dilatedDelay, ...args);
            }};
            
            window.setInterval = function(callback, delay, ...args) {{
                const dilatedDelay = delay * timerDilation;
                return originalSetInterval(callback, dilatedDelay, ...args);
            }};
            
            // Override requestAnimationFrame for smooth animations
            const originalRAF = window.requestAnimationFrame;
            window.requestAnimationFrame = function(callback) {{
                return originalRAF(function(timestamp) {{
                    const dilatedTimestamp = timestamp * timerDilation;
                    callback(dilatedTimestamp);
                }});
            }};
            """,
            
            # Manipulate timing APIs for advanced detection evasion
            """
            // Timing API manipulation
            if (window.performance && performance.timing) {
                const originalTiming = { ...performance.timing };
                
                // Add small random variations to timing data
                Object.keys(originalTiming).forEach(key => {
                    if (originalTiming[key] > 0) {
                        const variation = (Math.random() - 0.5) * 10; // ±5ms variation
                        performance.timing[key] = originalTiming[key] + variation;
                    }
                });
            }
            """,
            
            # Manipulate navigation timing
            f"""
            // Navigation timing manipulation
            if (performance.getEntriesByType) {{
                const originalGetEntries = performance.getEntriesByType;
                performance.getEntriesByType = function(type) {{
                    const entries = originalGetEntries.call(this, type);
                    if (type === 'navigation') {{
                        return entries.map(entry => {{
                            const newEntry = {{ ...entry }};
                            // Apply consistent temporal distortion
                            Object.keys(newEntry).forEach(key => {{
                                if (typeof newEntry[key] === 'number' && newEntry[key] > 0) {{
                                    const variation = (Math.random() - 0.5) * 15 * {dilation_factor};
                                    newEntry[key] = Math.max(0, newEntry[key] + variation);
                                }}
                            }});
                            return newEntry;
                        }});
                    }}
                    return entries;
                }};
            }}
            """
        ]
        
        for i, script in enumerate(scripts):
            try:
                driver.execute_script(script)
                if self.config.DEBUG_MODE:
                    print(f"⏰ Time dilation script {i+1} injected")
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Time script {i+1} failed: {e}")
    
    def generate_historical_footprint(self, days_back=365, activity_level='medium'):
        """Generate believable historical browsing footprint"""
        footprint = []
        base_date = datetime.now() - timedelta(days=days_back)
        
        # Activity level adjustments
        activity_multipliers = {
            'low': (3, 15),
            'medium': (10, 40),
            'high': (25, 80),
            'extreme': (50, 150)
        }
        
        min_visits, max_visits = activity_multipliers.get(activity_level, (10, 40))
        
        # Generate daily activity patterns with weekly cycles
        for day in range(days_back):
            current_date = base_date + timedelta(days=day)
            
            # Weekend vs weekday patterns
            is_weekend = current_date.weekday() >= 5
            if is_weekend:
                daily_visits = random.randint(min_visits, max_visits)
            else:
                daily_visits = random.randint(min_visits * 2, max_visits * 2)
            
            # Seasonal variations (more activity in winter)
            month = current_date.month
            if month in [11, 12, 1]:  # Winter months
                daily_visits = int(daily_visits * 1.3)
            elif month in [6, 7, 8]:  # Summer months
                daily_visits = int(daily_visits * 0.8)
            
            for visit_num in range(daily_visits):
                visit_time = current_date.replace(
                    hour=random.randint(6, 23),  # More activity during waking hours
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )
                
                # Visit duration follows power law distribution (most visits short)
                duration = max(30, int(random.paretovariate(1.5) * 60))
                
                footprint.append({
                    'timestamp': visit_time.isoformat(),
                    'url': self._generate_historical_url(visit_time),
                    'duration': duration,
                    'referrer': self._generate_referrer(visit_time) if random.random() > 0.4 else None,
                    'user_agent': self._generate_historical_user_agent(visit_time),
                    'activity_type': random.choice(['browsing', 'search', 'social', 'shopping', 'research'])
                })
        
        # Sort by timestamp
        footprint.sort(key=lambda x: x['timestamp'])
        
        return footprint
    
    def _generate_historical_url(self, timestamp):
        """Generate historically appropriate URLs"""
        year = timestamp.year
        
        # Domain evolution over time
        if year < 2010:
            domains = ['google.com', 'yahoo.com', 'msn.com', 'aol.com', 'myspace.com']
            paths = ['/', '/search', '/mail', '/news']
        elif year < 2015:
            domains = ['google.com', 'facebook.com', 'youtube.com', 'wikipedia.org', 'blogspot.com']
            paths = ['/', '/home', '/watch', '/wiki', '/search']
        else:
            domains = ['google.com', 'youtube.com', 'facebook.com', 'amazon.com', 'reddit.com', 'twitter.com']
            paths = ['/', '/home', '/watch', '/product', '/r/', '/hashtag/']
        
        domain = random.choice(domains)
        path = random.choice(paths)
        
        # Add query parameters for search-like URLs
        if random.random() < 0.3 and 'search' in path:
            queries = ['q=weather', 'q=news', 'q=recipes', 'q=sports', 'q=movies']
            return f"https://{domain}{path}?{random.choice(queries)}"
        
        return f"https://{domain}{path}"
    
    def _generate_referrer(self, timestamp):
        """Generate realistic referrers"""
        year = timestamp.year
        
        if year < 2015:
            referrers = [
                'https://www.google.com/',
                'https://search.yahoo.com/',
                'https://www.bing.com/',
                None  # Direct traffic
            ]
        else:
            referrers = [
                'https://www.google.com/',
                'https://www.facebook.com/',
                'https://twitter.com/',
                'https://www.reddit.com/',
                'https://mail.google.com/',
                None  # Direct traffic
            ]
        
        return random.choice(referrers)
    
    def _generate_historical_user_agent(self, timestamp):
        """Generate historically accurate user agents"""
        year = timestamp.year
        
        if year < 2010:
            return "Mozilla/5.0 (Windows NT 5.1; rv:10.0) Gecko/20100101 Firefox/10.0"
        elif year < 2015:
            return "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36"
        elif year < 2020:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        else:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    def manipulate_system_time(self, driver, time_shift_minutes=0, consistency='high'):
        """Manipulate system time perception with consistency levels"""
        if consistency == 'high':
            jitter = random.randint(-30, 30)  # Small jitter
        elif consistency == 'medium':
            jitter = random.randint(-120, 120)  # Medium jitter
        else:  # low
            jitter = random.randint(-300, 300)  # Large jitter
        
        total_shift_seconds = (time_shift_minutes * 60) + jitter
        
        script = f"""
        // Advanced system time manipulation
        const timeShift = {total_shift_seconds} * 1000; // Convert to milliseconds
        const consistencyLevel = '{consistency}';
        
        const OriginalDate = window.Date;
        let timeManipulationActive = true;
        
        // Create a new Date constructor with time manipulation
        window.Date = function(...args) {{
            if (!timeManipulationActive) {{
                return new OriginalDate(...args);
            }}
            
            if (args.length === 0) {{
                const realTime = OriginalDate.now();
                let adjustedTime = realTime + timeShift;
                
                // Add consistency-based jitter
                if (consistencyLevel === 'medium') {{
                    adjustedTime += (Math.random() - 0.5) * 60000; // ±30 seconds
                }} else if (consistencyLevel === 'low') {{
                    adjustedTime += (Math.random() - 0.5) * 300000; // ±2.5 minutes
                }}
                
                return new OriginalDate(adjustedTime);
            }}
            return new OriginalDate(...args);
        }};
        
        // Copy all static properties
        Object.getOwnPropertyNames(OriginalDate).forEach(prop => {{
            if (!['length', 'name', 'prototype'].includes(prop)) {{
                window.Date[prop] = OriginalDate[prop];
            }}
        }});
        
        // Override now() method
        window.Date.now = function() {{
            if (!timeManipulationActive) {{
                return OriginalDate.now();
            }}
            
            let adjustedTime = OriginalDate.now() + timeShift;
            
            if (consistencyLevel === 'medium') {{
                adjustedTime += (Math.random() - 0.5) * 60000;
            }} else if (consistencyLevel === 'low') {{
                adjustedTime += (Math.random() - 0.5) * 300000;
            }}
            
            return adjustedTime;
        }};
        
        // Add method to disable time manipulation
        window.disableTimeManipulation = function() {{
            timeManipulationActive = false;
        }};
        
        // Add method to enable time manipulation
        window.enableTimeManipulation = function() {{
            timeManipulationActive = true;
        }};
        
        console.log('Time manipulation active: shift =', timeShift, 'ms, consistency =', consistencyLevel);
        """
        
        try:
            driver.execute_script(script)
            if self.config.DEBUG_MODE:
                print(f"⏰ System time manipulated: {time_shift_minutes} minutes shift")
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"⚠️ Time manipulation failed: {e}")
    
    def create_temporal_anomalies(self, driver, anomaly_type='subtle'):
        """Create temporal anomalies to confuse forensic analysis"""
        anomalies = {
            'subtle': [
                # Small, hard-to-detect anomalies
                "performance.timeOrigin += 100;",
                "performance.timing.navigationStart += 50;"
            ],
            'moderate': [
                # More noticeable but still plausible
                "performance.timeOrigin += 500;",
                "performance.timing.navigationStart += 200;",
                "Date.prototype.getTime = function() { return originalGetTime.call(this) + 1000; };"
            ],
            'aggressive': [
                # Significant temporal distortions
                "performance.timeOrigin += 5000;",
                "performance.timing = null;",
                "delete performance.timing;"
            ]
        }
        
        scripts = anomalies.get(anomaly_type, anomalies['subtle'])
        
        for script in scripts:
            try:
                driver.execute_script(script)
                self.time_anomalies.append({
                    'timestamp': time.time(),
                    'anomaly': script,
                    'type': anomaly_type
                })
            except Exception as e:
                if self.config.DEBUG_MODE:
                    print(f"⚠️ Temporal anomaly failed: {e}")
    
    def simulate_time_based_behavior(self, driver, behavior_profile):
        """Simulate time-based human behavior patterns"""
        current_hour = datetime.now().hour
        
        if behavior_profile == 'morning_person':
            if 5 <= current_hour <= 10:
                # Peak morning activity
                self._simulate_alert_behavior(driver)
            elif 22 <= current_hour <= 24 or 0 <= current_hour <= 4:
                # Late night sluggishness
                self._simulate_tired_behavior(driver)
                
        elif behavior_profile == 'night_owl':
            if 22 <= current_hour <= 24 or 0 <= current_hour <= 2:
                # Peak night activity
                self._simulate_alert_behavior(driver)
            elif 6 <= current_hour <= 9:
                # Morning sluggishness
                self._simulate_tired_behavior(driver)
                
        elif behavior_profile == 'office_worker':
            if 9 <= current_hour <= 17:
                # Work hours - focused but busy
                self._simulate_focused_behavior(driver)
            else:
                # Off hours - casual
                self._simulate_casual_behavior(driver)
    
    def _simulate_alert_behavior(self, driver):
        """Simulate alert, focused behavior"""
        scripts = [
            "window.scrollTo(0, window.scrollY + 200);",
            "setTimeout(() => window.scrollTo(0, window.scrollY - 100), 500);"
        ]
        for script in scripts:
            try:
                driver.execute_script(script)
                time.sleep(0.2)
            except:
                pass
    
    def _simulate_tired_behavior(self, driver):
        """Simulate tired, sluggish behavior"""
        time.sleep(random.uniform(1, 3))  # Longer delays
    
    def _simulate_focused_behavior(self, driver):
        """Simulate focused work behavior"""
        scripts = [
            "window.scrollTo(0, document.body.scrollHeight * 0.3);",
            "setTimeout(() => window.scrollTo(0, document.body.scrollHeight * 0.7), 1000);"
        ]
        for script in scripts:
            try:
                driver.execute_script(script)
                time.sleep(0.5)
            except:
                pass
    
    def _simulate_casual_behavior(self, driver):
        """Simulate casual browsing behavior"""
        scripts = [
            "window.scrollTo(0, Math.random() * document.body.scrollHeight);"
        ]
        for script in scripts:
            try:
                driver.execute_script(script)
                time.sleep(random.uniform(0.5, 2))
            except:
                pass
    
    def get_temporal_report(self):
        """Get comprehensive temporal manipulation report"""
        return {
            'time_dilation_factor': self.time_dilation_factor,
            'historical_offset_seconds': self.historical_offset,
            'quantum_entropy': self.quantum_entropy,
            'anomalies_created': len(self.time_anomalies),
            'reference_time': self.reference_time,
            'current_system_time': time.time(),
            'anomaly_types': list(set(anom['type'] for anom in self.time_anomalies))
        }

# Utility function for easy integration
def create_temporal_manipulator(config=None):
    """Factory function for easy temporal manipulator creation"""
    from config import settings
    config = config or settings.current_config
    return TemporalManipulator(config)