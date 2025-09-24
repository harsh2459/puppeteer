import random
import time
from urllib.parse import urlparse, urlunparse

class NavigationDiversifier:
    def __init__(self, config):
        self.config = config
        self.navigation_patterns = self._initialize_patterns()
        
    def _initialize_patterns(self):
        """Initialize diverse navigation patterns"""
        return {
            "direct": {
                "description": "Direct navigation to target",
                "steps": ["target"],
                "delay_between": (1, 3)
            },
            "search_engine": {
                "description": "Simulate search engine referral",
                "steps": ["search_engine", "search_results", "target"],
                "delay_between": (2, 5)
            },
            "social_media": {
                "description": "Simulate social media referral", 
                "steps": ["social_media", "target"],
                "delay_between": (1, 4)
            },
            "news_aggregator": {
                "description": "Simulate news site referral",
                "steps": ["news_site", "target"], 
                "delay_between": (3, 6)
            }
        }
    
    def get_diversified_navigation_plan(self, target_url, pattern_name=None):
        """Generate diversified navigation plan"""
        pattern = self.navigation_patterns.get(
            pattern_name or random.choice(list(self.navigation_patterns.keys()))
        )
        
        navigation_plan = []
        current_url = target_url
        
        for step in pattern["steps"]:
            if step == "target":
                nav_step = {
                    "type": "target",
                    "url": target_url,
                    "description": "Final destination"
                }
            elif step == "search_engine":
                nav_step = self._generate_search_engine_step(target_url)
            elif step == "social_media":
                nav_step = self._generate_social_media_step(target_url)
            elif step == "news_site":
                nav_step = self._generate_news_site_step(target_url)
            elif step == "search_results":
                nav_step = self._generate_search_results_step(target_url)
            else:
                continue
                
            navigation_plan.append(nav_step)
        
        return {
            "pattern": pattern_name,
            "steps": navigation_plan,
            "delays": pattern["delay_between"]
        }
    
    def _generate_search_engine_step(self, target_url):
        """Generate search engine referral step"""
        domain = urlparse(target_url).netloc
        search_queries = [
            f"site:{domain}",
            f"{domain} review",
            f"visit {domain}",
            f"{domain} official site"
        ]
        
        return {
            "type": "search_engine",
            "url": f"https://www.google.com/search?q={random.choice(search_queries)}",
            "description": "Search engine referral",
            "actions": ["search", "click_result"]
        }
    
    def _generate_social_media_step(self, target_url):
        """Generate social media referral step"""
        social_platforms = [
            {"name": "twitter", "url": "https://twitter.com/home"},
            {"name": "facebook", "url": "https://www.facebook.com/"},
            {"name": "reddit", "url": "https://www.reddit.com/"},
            {"name": "linkedin", "url": "https://www.linkedin.com/feed/"}
        ]
        
        platform = random.choice(social_platforms)
        return {
            "type": "social_media",
            "url": platform["url"],
            "description": f"Social media visit ({platform['name']})",
            "actions": ["scroll", "click_link"]
        }
    
    def _generate_news_site_step(self, target_url):
        """Generate news site referral step"""
        news_sites = [
            "https://www.bbc.com/news",
            "https://www.cnn.com",
            "https://www.reuters.com",
            "https://apnews.com"
        ]
        
        return {
            "type": "news_site",
            "url": random.choice(news_sites),
            "description": "News site visit",
            "actions": ["read_article", "click_link"]
        }
    
    def _generate_search_results_step(self, target_url):
        """Generate search results page step"""
        return {
            "type": "search_results",
            "url": "https://www.google.com/search?q=related+results",
            "description": "Search results page",
            "actions": ["scroll_results", "click_result"]
        }
    
    def execute_diversified_navigation(self, bot, navigation_plan):
        """Execute the diversified navigation plan"""
        for i, step in enumerate(navigation_plan["steps"]):
            print(f"🧭 Navigation step {i+1}: {step['description']}")
            
            # Navigate to step URL
            bot.driver.get(step["url"])
            
            # Perform step-specific actions
            self._perform_step_actions(bot, step)
            
            # Delay between steps
            if i < len(navigation_plan["steps"]) - 1:
                delay = random.uniform(*navigation_plan["delays"])
                time.sleep(delay)
    
    def _perform_step_actions(self, bot, step):
        """Perform actions specific to each navigation step"""
        actions = step.get("actions", [])
        
        for action in actions:
            if action == "scroll":
                bot.quantum_scroll()
            elif action == "search":
                # Simulate search behavior
                time.sleep(random.uniform(1, 3))
            elif action == "click_result":
                # Simulate clicking a search result
                time.sleep(random.uniform(0.5, 2))
            elif action == "read_article":
                # Simulate reading behavior
                for _ in range(random.randint(2, 5)):
                    bot.quantum_scroll()
                    time.sleep(random.uniform(1, 3))
            elif action == "click_link":
                time.sleep(random.uniform(0.5, 1.5))