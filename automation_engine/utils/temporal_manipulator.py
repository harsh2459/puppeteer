import time
import random
from datetime import datetime, timedelta

class TemporalManipulator:
    def __init__(self, config):
        self.config = config
        self.time_anomalies = []
        
    def create_time_dilation(self, driver, dilation_factor=1.0):
        """Create time dilation effects to confuse timing analysis"""
        scripts = [
            # Override performance timing
            """
            const originalNow = performance.now;
            performance.now = function() {
                return originalNow.call(this) * %f;
            };
            """ % dilation_factor,
            
            # Override Date object
            """
            const originalDate = Date;
            Date = function() {
                if (this instanceof Date) {
                    return new originalDate(originalDate.now() * %f);
                }
                return originalDate();
            };
            Date.now = () => originalDate.now() * %f;
            """ % (dilation_factor, dilation_factor),
            
            # Override setTimeout/setInterval
            """
            const originalSetTimeout = window.setTimeout;
            window.setTimeout = function(callback, delay) {
                return originalSetTimeout(callback, delay * %f);
            };
            
            const originalSetInterval = window.setInterval;
            window.setInterval = function(callback, delay) {
                return originalSetInterval(callback, delay * %f);
            };
            """ % (dilation_factor, dilation_factor)
        ]
        
        for script in scripts:
            try:
                driver.execute_script(script)
            except:
                pass
    
    def generate_historical_footprint(self, days_back=365):
        """Generate believable historical browsing footprint"""
        footprint = []
        base_date = datetime.now() - timedelta(days=days_back)
        
        # Generate daily activity patterns
        for day in range(days_back):
            current_date = base_date + timedelta(days=day)
            daily_visits = random.randint(5, 50)  # 5-50 visits per day
            
            for _ in range(daily_visits):
                visit = {
                    'timestamp': current_date.replace(
                        hour=random.randint(8, 23),
                        minute=random.randint(0, 59)
                    ).isoformat(),
                    'url': self._generate_historical_url(current_date),
                    'duration': random.randint(30, 600),  # 30s to 10min
                    'referrer': self._generate_referrer() if random.random() > 0.3 else None
                }
                footprint.append(visit)
        
        return footprint
    
    def _generate_historical_url(self, date):
        """Generate historically appropriate URLs"""
        # Simulate URL evolution over time
        year = date.year
        domains = [
            'google.com', 'youtube.com', 'facebook.com', 'wikipedia.org',
            'amazon.com', 'reddit.com', 'twitter.com', 'instagram.com'
        ]
        
        # Simulate domain changes over years
        if year < 2010:
            domains = ['google.com', 'yahoo.com', 'msn.com', 'aol.com']
        elif year < 2015:
            domains.extend(['tumblr.com', 'myspace.com', 'blogspot.com'])
        
        return f"https://{random.choice(domains)}"
    
    def manipulate_system_time(self, driver, time_shift_minutes=0):
        """Manipulate system time perception"""
        script = """
        // Override Date constructor
        const timeShift = %d * 60 * 1000; // minutes to milliseconds
        const OriginalDate = window.Date;
        
        window.Date = function(...args) {
            if (args.length === 0) {
                return new OriginalDate(OriginalDate.now() + timeShift);
            }
            return new OriginalDate(...args);
        };
        
        // Copy static methods
        Object.getOwnPropertyNames(OriginalDate).forEach(prop => {
            if (prop !== 'length' && prop !== 'name' && prop !== 'prototype') {
                window.Date[prop] = OriginalDate[prop];
            }
        });
        
        window.Date.now = () => OriginalDate.now() + timeShift;
        window.Date.parse = OriginalDate.parse;
        window.Date.UTC = OriginalDate.UTC;
        """ % time_shift_minutes
        
        driver.execute_script(script)
