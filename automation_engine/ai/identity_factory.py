import random
import json
import os
from datetime import datetime, timedelta
from config import settings

class SyntheticIdentityFactory:
    def __init__(self):
        self.identities_generated = 0
        self.demographics = self._load_demographic_data()
        
    def create_advanced_identity(self, age_group="adult", location="US", interests=None):
        """Create advanced synthetic identity with full digital footprint"""
        identity = {
            "id": f"identity_{self.identities_generated}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "demographics": self._generate_demographics(age_group, location),
            "digital_footprint": self._generate_complete_digital_footprint(interests),
            "technical_profile": self._generate_advanced_technical_profile(),
            "behavioral_patterns": self._generate_behavioral_patterns(age_group),
            "temporal_data": self._generate_temporal_consistency(),
            "creation_timestamp": datetime.now().isoformat()
        }
        
        self.identities_generated += 1
        self._save_identity(identity)
        return identity
    
    def create_basic_identity(self):
        """Quick identity for immediate use"""
        return self.create_advanced_identity()
    
    def _generate_complete_digital_footprint(self, interests):
        """Generate comprehensive digital history"""
        footprint = {
            "browsing_history": self._generate_browsing_history(365),  # 1 year history
            "social_media_presence": self._generate_social_presence(),
            "search_patterns": self._generate_search_queries(interests),
            "purchase_behavior": self._generate_purchase_history(),
            "content_preferences": self._generate_content_preferences(interests),
            "online_habits": self._generate_online_habits()
        }
        return footprint
    
    def _generate_browsing_history(self, days_back=365):
        """Generate 1 year of believable browsing history"""
        history = []
        start_date = datetime.now() - timedelta(days=days_back)
        
        # Popular sites with realistic visit patterns
        sites = {
            "google.com": {"daily_visits": 3, "session_duration": (2, 10)},
            "youtube.com": {"daily_visits": 2, "session_duration": (10, 45)},
            "facebook.com": {"daily_visits": 1, "session_duration": (5, 20)},
            "amazon.com": {"daily_visits": 0.3, "session_duration": (5, 30)},
            "wikipedia.org": {"daily_visits": 0.2, "session_duration": (3, 15)}
        }
        
        current_date = start_date
        while current_date <= datetime.now():
            for site, pattern in sites.items():
                # Probabilistic visit generation
                if random.random() < pattern["daily_visits"]:
                    visit = {
                        "date": current_date.strftime("%Y-%m-%d"),
                        "time": f"{random.randint(8, 23)}:{random.randint(0, 59):02d}",
                        "site": site,
                        "duration_minutes": random.randint(*pattern["session_duration"]),
                        "actions": random.randint(3, 15)
                    }
                    history.append(visit)
            
            current_date += timedelta(days=1)
        
        return history
    
    def _generate_social_presence(self):
        """Generate social media presence data"""
        platforms = ["facebook", "twitter", "instagram", "linkedin", "reddit"]
        presence = {}
        
        for platform in platforms:
            if random.random() > 0.3:  # 70% chance of having account
                account_age_days = random.randint(180, 2000)  # 6 months to 5 years
                join_date = (datetime.now() - timedelta(days=account_age_days)).strftime("%Y-%m-%d")
                
                presence[platform] = {
                    "has_account": True,
                    "join_date": join_date,
                    "activity_level": random.choice(["low", "medium", "high"]),
                    "friends_followers": random.randint(50, 5000),
                    "post_frequency": f"{random.randint(1, 30)} per month"
                }
            else:
                presence[platform] = {"has_account": False}
        
        return presence
    
    def _generate_search_queries(self, interests):
        """Generate realistic search query history"""
        interest_keywords = {
            "technology": ["python programming", "new smartphones", "AI news", "gaming PC builds"],
            "sports": ["NBA scores", "football transfers", "Olympics news", "fitness tips"],
            "entertainment": ["new movies", "Netflix series", "music releases", "celebrity news"],
            "news": ["world news", "local events", "weather forecast", "stock market"]
        }
        
        queries = []
        base_interests = interests or ["technology", "news"]
        
        for _ in range(random.randint(200, 800)):  # 200-800 search queries
            interest = random.choice(base_interests)
            keyword = random.choice(interest_keywords.get(interest, ["general search"]))
            variation = random.choice(["", " 2024", " review", " how to", " best"])
            
            queries.append(f"{keyword}{variation}")
        
        return queries[:100]  # Return last 100 queries
    
    def _generate_advanced_technical_profile(self):
        """Generate advanced technical fingerprint"""
        return {
            "timezone": random.choice(["America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]),
            "screen_resolutions": [
                random.choice(["1920x1080", "1366x768", "1536x864", "1440x900"]),
                random.choice(["375x812", "414x896", "360x800"])  # Mobile secondary
            ],
            "browser_plugins": random.randint(3, 12),
            "font_fingerprint": self._generate_font_list(),
            "language_preferences": ["en-US", "en"] + (["es", "fr"] if random.random() > 0.8 else []),
            "accept_languages": "en-US,en;q=0.9,es;q=0.8,fr;q=0.7",
            "hardware_concurrency": random.choice([4, 8, 12, 16]),
            "device_memory": random.choice([4, 8, 16, 32])
        }
    
    def _generate_font_list(self):
        """Generate realistic font list based on OS"""
        windows_fonts = ["Arial", "Times New Roman", "Calibri", "Verdana", "Tahoma"]
        mac_fonts = ["Helvetica Neue", "San Francisco", "Times New Roman", "Arial"]
        linux_fonts = ["DejaVu Sans", "Liberation Sans", "Times New Roman", "Arial"]
        
        font_sets = [windows_fonts, mac_fonts, linux_fonts]
        base_fonts = random.choice(font_sets)
        
        # Add some random additional fonts
        additional_fonts = random.sample([
            "Courier New", "Georgia", "Palatino", "Garamond", "Book Antiqua"
        ], random.randint(2, 5))
        
        return base_fonts + additional_fonts
    
    def _generate_behavioral_patterns(self, age_group):
        """Generate age-appropriate behavioral patterns"""
        patterns = {
            "teen": {
                "click_speed": "fast",
                "scroll_behavior": "rapid",
                "attention_span": "short",
                "multitasking": "high"
            },
            "young_adult": {
                "click_speed": "moderate", 
                "scroll_behavior": "balanced",
                "attention_span": "medium",
                "multitasking": "medium"
            },
            "adult": {
                "click_speed": "deliberate",
                "scroll_behavior": "methodical", 
                "attention_span": "long",
                "multitasking": "low"
            },
            "senior": {
                "click_speed": "slow",
                "scroll_behavior": "cautious",
                "attention_span": "variable",
                "multitasking": "very_low"
            }
        }
        
        return patterns.get(age_group, patterns["adult"])
    
    def _generate_temporal_consistency(self):
        """Generate temporal patterns for consistency"""
        return {
            "typical_start_time": f"{random.randint(8, 10)}:00",
            "typical_end_time": f"{random.randint(22, 24)}:00",
            "peak_activity_hours": [9, 10, 14, 15, 20, 21],
            "weekend_activity_multiplier": random.uniform(1.2, 2.0),
            "timezone_consistency": random.choice(["strict", "moderate", "flexible"])
        }
    
    def _save_identity(self, identity):
        """Save identity to file for persistence"""
        identity_dir = settings.IDENTITY_PROFILES_PATH
        os.makedirs(identity_dir, exist_ok=True)
        
        filename = f"{identity['id']}.json"
        filepath = os.path.join(identity_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(identity, f, indent=2)
    
    def load_identity(self, identity_id):
        """Load previously created identity"""
        filepath = os.path.join(settings.IDENTITY_PROFILES_PATH, f"{identity_id}.json")
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def _load_demographic_data(self):
        """Load demographic distributions"""
        return {
            "US": {"age_groups": {"teen": 0.18, "young_adult": 0.27, "adult": 0.38, "senior": 0.17}},
            "EU": {"age_groups": {"teen": 0.15, "young_adult": 0.23, "adult": 0.42, "senior": 0.20}},
            "ASIA": {"age_groups": {"teen": 0.20, "young_adult": 0.30, "adult": 0.36, "senior": 0.14}}
        }