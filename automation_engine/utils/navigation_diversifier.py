import random
import time
import math
from urllib.parse import urlparse, urljoin, urlencode
from selenium.webdriver.common.by import By
from config import settings

class NavigationDiversifier:
    def __init__(self, config):
        self.config = config
        self.navigation_patterns = self._init_navigation_patterns()
        self.current_pattern = 'organic'
        self.navigation_history = []
        self.referrer_chain = []
        self.entropy_source = random.random()
        
    def _init_navigation_patterns(self):
        """Initialize diverse navigation patterns with realistic behaviors"""
        return {
            'organic': {
                'type': 'search_engine',
                'click_accuracy': 0.88,
                'scroll_depth': 0.7,
                'time_on_page': (15, 45),
                'bounce_rate': 0.3,
                'internal_links': 3,
                'reading_behavior': 'comprehensive',
                'scroll_style': 'methodical',
                'exit_strategy': 'natural'
            },
            'social_media': {
                'type': 'social_referral',
                'click_accuracy': 0.82,
                'scroll_depth': 0.9,
                'time_on_page': (8, 25),
                'bounce_rate': 0.5,
                'internal_links': 1,
                'reading_behavior': 'scanning',
                'scroll_style': 'rapid',
                'exit_strategy': 'abrupt'
            },
            'direct': {
                'type': 'direct_traffic',
                'click_accuracy': 0.92,
                'scroll_depth': 0.6,
                'time_on_page': (20, 60),
                'bounce_rate': 0.2,
                'internal_links': 2,
                'reading_behavior': 'focused',
                'scroll_style': 'direct',
                'exit_strategy': 'purposeful'
            },
            'research': {
                'type': 'academic',
                'click_accuracy': 0.95,
                'scroll_depth': 0.95,
                'time_on_page': (45, 120),
                'bounce_rate': 0.1,
                'internal_links': 5,
                'reading_behavior': 'analytical',
                'scroll_style': 'thorough',
                'exit_strategy': 'gradual'
            },
            'shopping': {
                'type': 'ecommerce',
                'click_accuracy': 0.85,
                'scroll_depth': 0.8,
                'time_on_page': (30, 90),
                'bounce_rate': 0.4,
                'internal_links': 4,
                'reading_behavior': 'comparative',
                'scroll_style': 'comparison',
                'exit_strategy': 'considered'
            },
            'news': {
                'type': 'media',
                'click_accuracy': 0.80,
                'scroll_depth': 0.85,
                'time_on_page': (10, 30),
                'bounce_rate': 0.6,
                'internal_links': 6,
                'reading_behavior': 'skimming',
                'scroll_style': 'rapid_scan',
                'exit_strategy': 'quick'
            }
        }
    
    def get_diversified_navigation_plan(self, target_url, pattern_name=None):
        """Create a diversified navigation plan to the target URL"""
        pattern = self._select_navigation_pattern(pattern_name)
        target_domain = urlparse(target_url).netloc
        
        navigation_plan = {
            'target_url': target_url,
            'pattern': pattern,
            'entry_point': self._generate_entry_point(target_domain, pattern),
            'navigation_path': self._generate_navigation_path(target_url, pattern),
            'time_allocations': self._generate_time_allocations(pattern),
            'interaction_sequence': self._generate_interaction_sequence(pattern),
            'exit_strategy': pattern['exit_strategy']
        }
        
        return navigation_plan
    
    def _select_navigation_pattern(self, pattern_name=None):
        """Select appropriate navigation pattern based on context"""
        if pattern_name and pattern_name in self.navigation_patterns:
            return self.navigation_patterns[pattern_name]
        
        # Context-based pattern selection
        current_hour = time.localtime().tm_hour
        patterns = list(self.navigation_patterns.keys())
        weights = [1.0] * len(patterns)
        
        # Time-based weighting
        if 9 <= current_hour <= 17:  # Work hours
            weights[patterns.index('research')] = 1.8
            weights[patterns.index('direct')] = 1.5
        elif 18 <= current_hour <= 22:  # Evening
            weights[patterns.index('social_media')] = 2.0
            weights[patterns.index('shopping')] = 1.7
        else:  # Night
            weights[patterns.index('news')] = 1.6
            weights[patterns.index('organic')] = 1.4
        
        selected_pattern = random.choices(patterns, weights=weights)[0]
        self.current_pattern = selected_pattern
        
        return self.navigation_patterns[selected_pattern]
    
    def _generate_entry_point(self, target_domain, pattern):
        """Generate realistic entry point based on pattern"""
        entry_points = {
            'organic': [
                f"https://www.google.com/search?q={self._generate_search_query(target_domain)}",
                f"https://www.bing.com/search?q={self._generate_search_query(target_domain)}",
                f"https://search.yahoo.com/search?p={self._generate_search_query(target_domain)}"
            ],
            'social_media': [
                "https://www.facebook.com/",
                "https://twitter.com/",
                "https://www.reddit.com/",
                "https://www.linkedin.com/"
            ],
            'direct': [
                f"https://{target_domain}",
                f"https://www.{target_domain}",
                f"https://{target_domain}/home"
            ],
            'research': [
                "https://scholar.google.com/",
                "https://www.wikipedia.org/",
                "https://www.researchgate.net/"
            ],
            'shopping': [
                "https://www.amazon.com/",
                "https://www.ebay.com/",
                "https://www.aliexpress.com/"
            ],
            'news': [
                "https://news.google.com/",
                "https://www.cnn.com/",
                "https://www.bbc.com/news"
            ]
        }
        
        pattern_type = pattern['type']
        if pattern_type in entry_points:
            return random.choice(entry_points[pattern_type])
        
        return f"https://{target_domain}"  # Fallback
    
    def _generate_search_query(self, domain):
        """Generate realistic search queries for organic traffic"""
        domain_keywords = domain.replace('www.', '').split('.')[0]
        
        queries = [
            f"{domain_keywords} official site",
            f"{domain_keywords} login",
            f"what is {domain_keywords}",
            f"{domain_keywords} reviews",
            f"how to use {domain_keywords}",
            f"{domain_keywords} customer service"
        ]
        
        return random.choice(queries).replace(' ', '+')
    
    def _generate_navigation_path(self, target_url, pattern):
        """Generate realistic navigation path to target"""
        target_domain = urlparse(target_url).netloc
        path_steps = []
        
        # Start from entry point
        entry_point = self._generate_entry_point(target_domain, pattern)
        path_steps.append({'url': entry_point, 'type': 'entry', 'duration': random.randint(5, 15)})
        
        # Intermediate steps based on pattern
        intermediate_steps = pattern['internal_links']
        
        for step in range(intermediate_steps):
            step_type = random.choice(['internal_link', 'external_ref', 'search_result'])
            
            if step_type == 'internal_link':
                url = f"https://{target_domain}/{self._generate_internal_path()}"
            elif step_type == 'external_ref':
                url = self._generate_external_referrer()
            else:  # search_result
                url = f"https://www.google.com/search?q={self._generate_related_query(target_domain)}"
            
            path_steps.append({
                'url': url,
                'type': step_type,
                'duration': random.randint(3, 10)
            })
        
        # Final step to target
        path_steps.append({
            'url': target_url,
            'type': 'target',
            'duration': random.randint(pattern['time_on_page'][0], pattern['time_on_page'][1])
        })
        
        return path_steps
    
    def _generate_internal_path(self):
        """Generate realistic internal website paths"""
        paths = [
            'about', 'contact', 'products', 'services', 'blog', 
            'news', 'support', 'faq', 'pricing', 'features'
        ]
        
        subpaths = [
            '', '/team', '/company', '/history', '/mission',
            '/index', '/main', '/home', '/welcome'
        ]
        
        path = random.choice(paths)
        subpath = random.choice(subpaths)
        
        return f"{path}{subpath}"
    
    def _generate_external_referrer(self):
        """Generate realistic external referrer URLs"""
        referrers = [
            'https://www.wikipedia.org/',
            'https://www.youtube.com/',
            'https://www.github.com/',
            'https://stackoverflow.com/',
            'https://www.quora.com/',
            'https://medium.com/',
            'https://www.reddit.com/',
            'https://news.ycombinator.com/'
        ]
        
        return random.choice(referrers)
    
    def _generate_related_query(self, domain):
        """Generate related search queries"""
        domain_keywords = domain.replace('www.', '').split('.')[0]
        
        related_queries = [
            f"alternative to {domain_keywords}",
            f"{domain_keywords} vs competitor",
            f"how {domain_keywords} works",
            f"{domain_keywords} tutorial",
            f"best {domain_keywords} features"
        ]
        
        return random.choice(related_queries).replace(' ', '+')
    
    def _generate_time_allocations(self, pattern):
        """Generate realistic time allocations for navigation"""
        base_times = pattern['time_on_page']
        
        return {
            'entry_page': random.randint(5, 15),
            'intermediate_pages': [random.randint(2, 8) for _ in range(pattern['internal_links'])],
            'target_page': random.randint(base_times[0], base_times[1]),
            'reading_time_variation': random.uniform(0.7, 1.3)
        }
    
    def _generate_interaction_sequence(self, pattern):
        """Generate realistic interaction sequence"""
        sequence = []
        
        # Scroll behavior based on pattern
        scroll_styles = {
            'methodical': ['read_scroll', 'pause', 'read_scroll', 'pause'],
            'rapid': ['quick_scroll', 'scan', 'quick_scroll'],
            'direct': ['scroll_to_content', 'read', 'scroll_to_bottom'],
            'thorough': ['slow_scroll', 'read', 'pause', 'slow_scroll'],
            'comparison': ['scroll_compare', 'pause', 'scroll_compare'],
            'rapid_scan': ['fast_scroll', 'brief_pause', 'fast_scroll']
        }
        
        base_sequence = scroll_styles.get(pattern['scroll_style'], scroll_styles['methodical'])
        
        # Add clicks and other interactions
        click_count = max(1, int(pattern['internal_links'] * random.uniform(0.5, 1.5)))
        
        for i in range(click_count):
            insert_pos = random.randint(1, len(base_sequence) - 1)
            base_sequence.insert(insert_pos, 'click_interaction')
        
        # Add reading behaviors
        reading_behaviors = {
            'comprehensive': ['read_paragraph', 'pause', 'read_paragraph'],
            'scanning': ['scan_content', 'quick_read', 'scan_content'],
            'focused': ['focused_read', 'minimal_scroll', 'focused_read'],
            'analytical': ['detailed_read', 'pause_think', 'detailed_read'],
            'comparative': ['compare_sections', 'pause', 'compare_sections'],
            'skimming': ['skim_headlines', 'brief_read', 'skim_headlines']
        }
        
        reading_sequence = reading_behaviors.get(pattern['reading_behavior'], reading_behaviors['comprehensive'])
        
        # Combine sequences
        combined_sequence = []
        for action in base_sequence:
            if action.startswith('read') or action == 'scan':
                combined_sequence.extend(reading_sequence)
            else:
                combined_sequence.append(action)
        
        return combined_sequence
    
    def execute_diversified_navigation(self, bot, navigation_plan):
        """Execute the diversified navigation plan"""
        try:
            driver = bot.driver
            pattern = navigation_plan['pattern']
            
            # Record navigation start
            navigation_record = {
                'start_time': time.time(),
                'target_url': navigation_plan['target_url'],
                'pattern': self.current_pattern,
                'steps_completed': 0,
                'success': False
            }
            
            # Execute navigation path
            for step in navigation_plan['navigation_path']:
                if self.config.DEBUG_MODE:
                    print(f"🧭 Navigating to: {step['url']}")
                
                # Navigate to step URL
                driver.get(step['url'])
                
                # Simulate realistic behavior on page
                self._simulate_page_behavior(bot, step, pattern)
                
                # Wait appropriate time
                time.sleep(step['duration'])
                
                navigation_record['steps_completed'] += 1
            
            # Final behavior on target page
            self._execute_target_behavior(bot, navigation_plan)
            
            navigation_record.update({
                'end_time': time.time(),
                'success': True,
                'total_duration': time.time() - navigation_record['start_time']
            })
            
            self.navigation_history.append(navigation_record)
            
            if self.config.DEBUG_MODE:
                print(f"✅ Navigation completed: {navigation_plan['target_url']}")
            
            return True
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Navigation failed: {e}")
            
            navigation_record.update({
                'end_time': time.time(),
                'success': False,
                'error': str(e)
            })
            self.navigation_history.append(navigation_record)
            
            return False
    
    def _simulate_page_behavior(self, bot, step, pattern):
        """Simulate realistic behavior on each page"""
        driver = bot.driver
        
        # Scroll based on pattern
        scroll_depth = pattern['scroll_depth']
        if scroll_depth > 0:
            self._execute_scroll_pattern(driver, pattern)
        
        # Simulate reading behavior
        if step['type'] in ['target', 'internal_link']:
            self._simulate_reading_behavior(driver, pattern)
        
        # Random clicks based on pattern accuracy
        if random.random() < pattern['click_accuracy']:
            self._simulate_random_clicks(driver, pattern)
    
    def _execute_scroll_pattern(self, driver, pattern):
        """Execute scroll pattern based on navigation style"""
        scroll_styles = {
            'methodical': self._scroll_methodical,
            'rapid': self._scroll_rapid,
            'direct': self._scroll_direct,
            'thorough': self._scroll_thorough,
            'comparison': self._scroll_comparison,
            'rapid_scan': self._scroll_rapid_scan
        }
        
        scroll_function = scroll_styles.get(pattern['scroll_style'], self._scroll_methodical)
        scroll_function(driver, pattern['scroll_depth'])
    
    def _scroll_methodical(self, driver, depth):
        """Methodical scrolling with pauses"""
        total_scrolls = int(depth * 10)
        for i in range(total_scrolls):
            scroll_amount = random.randint(200, 400)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.3, 0.8))
    
    def _scroll_rapid(self, driver, depth):
        """Rapid scrolling with quick scans"""
        total_scrolls = int(depth * 6)
        for i in range(total_scrolls):
            scroll_amount = random.randint(400, 800)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.1, 0.3))
    
    def _scroll_direct(self, driver, depth):
        """Direct scrolling to content"""
        target_scroll = depth * driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {target_scroll});")
        time.sleep(random.uniform(1, 3))
    
    def _scroll_thorough(self, driver, depth):
        """Thorough scrolling with careful reading"""
        total_scrolls = int(depth * 15)
        for i in range(total_scrolls):
            scroll_amount = random.randint(100, 300)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.5, 1.2))
    
    def _scroll_comparison(self, driver, depth):
        """Comparison scrolling between sections"""
        sections = 4
        for section in range(sections):
            section_scroll = (depth / sections) * driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0, {section_scroll * section});")
            time.sleep(random.uniform(2, 4))
            # Scroll up slightly for comparison
            driver.execute_script("window.scrollBy(0, -100);")
            time.sleep(1)
    
    def _scroll_rapid_scan(self, driver, depth):
        """Rapid scanning scroll pattern"""
        total_scrolls = int(depth * 8)
        for i in range(total_scrolls):
            scroll_amount = random.randint(300, 600)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(random.uniform(0.2, 0.5))
    
    def _simulate_reading_behavior(self, driver, pattern):
        """Simulate realistic reading behavior"""
        reading_time = random.randint(3, 8) * pattern['scroll_depth']
        time.sleep(reading_time)
        
        # Simulate reading movements
        for _ in range(random.randint(2, 5)):
            small_scroll = random.randint(50, 150)
            driver.execute_script(f"window.scrollBy(0, {small_scroll});")
            time.sleep(random.uniform(0.5, 1.5))
    
    def _simulate_random_clicks(self, driver, pattern):
        """Simulate random clicks on page elements"""
        try:
            # Find clickable elements
            clickable_selectors = ['a', 'button', '.btn', '[onclick]', 'input[type="submit"]']
            
            for selector in clickable_selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    # Click a random element based on pattern accuracy
                    if random.random() < pattern['click_accuracy']:
                        element = random.choice(elements)
                        try:
                            element.click()
                            time.sleep(random.uniform(1, 3))
                            driver.back()  # Go back to continue navigation
                            time.sleep(1)
                            break
                        except:
                            continue
        except:
            pass  # Silent fail for click simulation
    
    def _execute_target_behavior(self, bot, navigation_plan):
        """Execute final behavior on target page"""
        driver = bot.driver
        pattern = navigation_plan['pattern']
        
        # Extended behavior on target page
        target_time = navigation_plan['time_allocations']['target_page']
        time_spent = 0
        
        while time_spent < target_time:
            # Scroll through content
            self._execute_scroll_pattern(driver, pattern)
            time_spent += random.randint(5, 15)
            
            # Simulate interactions
            if time_spent < target_time:
                self._simulate_reading_behavior(driver, pattern)
                time_spent += random.randint(3, 8)
    
    def get_navigation_report(self):
        """Get comprehensive navigation diversification report"""
        recent_navigations = self.navigation_history[-5:] if self.navigation_history else []
        
        success_rate = sum(1 for nav in self.navigation_history if nav.get('success', False)) / len(self.navigation_history) if self.navigation_history else 0
        
        return {
            'current_pattern': self.current_pattern,
            'total_navigations': len(self.navigation_history),
            'success_rate': f"{success_rate:.1%}",
            'pattern_usage': self._get_pattern_usage_stats(),
            'recent_navigations': recent_navigations,
            'average_duration': self._get_average_duration()
        }
    
    def _get_pattern_usage_stats(self):
        """Get statistics on pattern usage"""
        pattern_counts = {}
        for nav in self.navigation_history:
            pattern = nav.get('pattern', 'unknown')
            pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        
        return pattern_counts
    
    def _get_average_duration(self):
        """Calculate average navigation duration"""
        successful_navs = [nav for nav in self.navigation_history if nav.get('success', False)]
        if not successful_navs:
            return 0
        
        total_duration = sum(nav.get('total_duration', 0) for nav in successful_navs)
        return total_duration / len(successful_navs)

# Utility function
def create_navigation_diversifier(config=None):
    """Factory function for easy navigation diversifier creation"""
    from config import settings
    config = config or settings.current_config
    return NavigationDiversifier(config)