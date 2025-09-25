import random
import time
import hashlib
import json
from datetime import datetime, timedelta
from faker import Faker
from config import settings

class SyntheticIdentityFactory:
    def __init__(self, config):
        self.config = config
        self.faker = Faker()
        self.identity_templates = self._init_identity_templates()
        self.generated_identities = []
        self.entropy_source = random.random()
        
    def _init_identity_templates(self):
        """Initialize identity templates for different personas"""
        return {
            'professional': {
                'age_range': (25, 55),
                'education_levels': ['bachelors', 'masters', 'phd'],
                'industries': ['technology', 'finance', 'healthcare', 'education', 'legal'],
                'income_range': (50000, 150000),
                'interests': ['professional_development', 'technology', 'finance', 'travel'],
                'behavior_traits': ['punctual', 'organized', 'goal_oriented']
            },
            'student': {
                'age_range': (18, 25),
                'education_levels': ['high_school', 'bachelors'],
                'industries': ['education', 'retail', 'hospitality'],
                'income_range': (10000, 30000),
                'interests': ['gaming', 'social_media', 'music', 'sports'],
                'behavior_traits': ['curious', 'social', 'tech_savvy']
            },
            'retiree': {
                'age_range': (65, 85),
                'education_levels': ['high_school', 'bachelors', 'masters'],
                'industries': ['retired', 'volunteer', 'part_time'],
                'income_range': (30000, 80000),
                'interests': ['gardening', 'reading', 'travel', 'family'],
                'behavior_traits': ['patient', 'traditional', 'community_focused']
            },
            'entrepreneur': {
                'age_range': (30, 50),
                'education_levels': ['bachelors', 'masters', 'self_taught'],
                'industries': ['startup', 'technology', 'consulting', 'ecommerce'],
                'income_range': (80000, 300000),
                'interests': ['innovation', 'business', 'technology', 'networking'],
                'behavior_traits': ['risk_taking', 'innovative', 'driven']
            },
            'creative': {
                'age_range': (20, 45),
                'education_levels': ['bachelors', 'self_taught', 'art_school'],
                'industries': ['arts', 'design', 'media', 'entertainment'],
                'income_range': (30000, 90000),
                'interests': ['art', 'design', 'music', 'film', 'writing'],
                'behavior_traits': ['expressive', 'innovative', 'non_conformist']
            }
        }
    
    def create_quantum_identity(self, persona_type=None, geographic_context=None):
        """Create a comprehensive synthetic identity with quantum-level uniqueness"""
        try:
            # Select or randomize persona type
            if not persona_type or persona_type not in self.identity_templates:
                persona_type = random.choice(list(self.identity_templates.keys()))
            
            template = self.identity_templates[persona_type]
            geographic_context = geographic_context or self._select_geographic_context()
            
            # Generate identity components
            basic_info = self._generate_basic_info(template, geographic_context)
            digital_footprint = self._generate_digital_footprint(basic_info)
            technical_profile = self._generate_technical_profile()
            behavioral_profile = self._generate_behavioral_profile(template)
            quantum_fingerprint = self._generate_quantum_fingerprint()
            
            # Assemble complete identity
            identity = {
                'id': self._generate_identity_hash(basic_info),
                'persona_type': persona_type,
                'basic_info': basic_info,
                'digital_footprint': digital_footprint,
                'technical_profile': technical_profile,
                'behavioral_profile': behavioral_profile,
                'quantum_fingerprint': quantum_fingerprint,
                'creation_timestamp': time.time(),
                'entropy_source': self.entropy_source,
                'consistency_seed': random.random()
            }
            
            # Store identity
            self.generated_identities.append(identity)
            
            if self.config.DEBUG_MODE:
                print(f"🆔 Synthetic identity created: {basic_info['first_name']} {basic_info['last_name']} ({persona_type})")
            
            return identity
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Identity creation failed: {e}")
            return self._create_fallback_identity()
    
    def _select_geographic_context(self):
        """Select realistic geographic context for identity"""
        regions = {
            'north_america': {
                'countries': ['US', 'CA'],
                'timezones': ['America/New_York', 'America/Chicago', 'America/Los_Angeles', 'America/Denver'],
                'locales': ['en_US', 'en_CA']
            },
            'europe': {
                'countries': ['GB', 'DE', 'FR', 'IT', 'ES', 'NL'],
                'timezones': ['Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Rome'],
                'locales': ['en_GB', 'de_DE', 'fr_FR', 'it_IT', 'es_ES']
            },
            'asia_pacific': {
                'countries': ['JP', 'KR', 'CN', 'AU', 'SG'],
                'timezones': ['Asia/Tokyo', 'Asia/Seoul', 'Asia/Shanghai', 'Australia/Sydney'],
                'locales': ['ja_JP', 'ko_KR', 'zh_CN', 'en_AU']
            }
        }
        
        region = random.choice(list(regions.keys()))
        return regions[region]
    
    def _generate_basic_info(self, template, geographic_context):
        """Generate basic personal information"""
        # Set appropriate locale
        locale = random.choice(geographic_context['locales'])
        self.faker = Faker(locale)
        
        age = random.randint(template['age_range'][0], template['age_range'][1])
        birth_year = datetime.now().year - age
        
        basic_info = {
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
            'age': age,
            'birth_year': birth_year,
            'gender': random.choice(['male', 'female', 'non_binary']),
            'location': {
                'country': random.choice(geographic_context['countries']),
                'city': self.faker.city(),
                'timezone': random.choice(geographic_context['timezones']),
                'locale': locale
            },
            'education': {
                'level': random.choice(template['education_levels']),
                'field': self._generate_education_field(template),
                'institution': self.faker.company() if random.random() > 0.3 else 'University'
            },
            'occupation': {
                'industry': random.choice(template['industries']),
                'title': self._generate_occupation_title(template),
                'income': random.randint(template['income_range'][0], template['income_range'][1])
            }
        }
        
        return basic_info
    
    def _generate_education_field(self, template):
        """Generate education field based on persona type"""
        field_mapping = {
            'professional': ['Computer Science', 'Business', 'Engineering', 'Medicine', 'Law'],
            'student': ['Computer Science', 'Business', 'Arts', 'Sciences', 'Engineering'],
            'retiree': ['Business', 'Education', 'Engineering', 'Liberal Arts'],
            'entrepreneur': ['Business', 'Computer Science', 'Engineering', 'Economics'],
            'creative': ['Fine Arts', 'Design', 'Film', 'Music', 'Journalism']
        }
        
        return random.choice(field_mapping.get(template, field_mapping['professional']))
    
    def _generate_occupation_title(self, template):
        """Generate occupation title based on persona type"""
        title_mapping = {
            'professional': ['Manager', 'Director', 'Analyst', 'Consultant', 'Engineer'],
            'student': ['Student', 'Intern', 'Part-time Worker', 'Research Assistant'],
            'retiree': ['Retired', 'Consultant', 'Volunteer', 'Part-time'],
            'entrepreneur': ['Founder', 'CEO', 'Entrepreneur', 'Business Owner'],
            'creative': ['Designer', 'Artist', 'Writer', 'Photographer', 'Creative Director']
        }
        
        return random.choice(title_mapping.get(template, title_mapping['professional']))
    
    def _generate_digital_footprint(self, basic_info):
        """Generate digital footprint and online presence"""
        username_base = f"{basic_info['first_name'].lower()}{basic_info['last_name'].lower()}"
        
        digital_footprint = {
            'email_addresses': [
                f"{username_base}{random.randint(1, 99)}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}",
                f"{username_base}.work@{random.choice(['company.com', 'business.com'])}"
            ],
            'usernames': [
                username_base,
                f"{basic_info['first_name'][0]}{basic_info['last_name'].lower()}",
                f"{basic_info['first_name'].lower()}_{random.randint(100, 999)}"
            ],
            'social_media': {
                'platforms': random.sample(['facebook', 'twitter', 'linkedin', 'instagram', 'reddit'], 3),
                'activity_level': random.choice(['active', 'moderate', 'minimal']),
                'join_date': self.faker.date_between(start_date='-10y', end_date='-1y')
            },
            'online_behavior': {
                'browsing_hours': random.randint(5, 40),
                'primary_device': random.choice(['desktop', 'laptop', 'mobile']),
                'preferred_browser': random.choice(['chrome', 'firefox', 'safari', 'edge'])
            }
        }
        
        return digital_footprint
    
    def _generate_technical_profile(self):
        """Generate technical capabilities and preferences"""
        technical_profile = {
            'device_preferences': {
                'os': random.choice(['windows', 'macos', 'linux', 'chromeos']),
                'device_type': random.choice(['desktop', 'laptop', 'tablet']),
                'screen_resolution': random.choice(['1920x1080', '2560x1440', '1366x768', '3840x2160']),
                'browser_plugins': random.sample(['adblock', 'grammarly', 'darkreader', 'passwordmanager'], 2)
            },
            'network_characteristics': {
                'connection_type': random.choice(['wifi', 'ethernet', '4g', '5g']),
                'average_speed': random.randint(10, 1000),
                'vpn_usage': random.random() < 0.3  # 30% use VPN
            },
            'privacy_settings': {
                'cookies_accepted': random.random() < 0.8,  # 80% accept cookies
                'tracking_allowed': random.random() < 0.6,  # 60% allow tracking
                'ad_personalization': random.random() < 0.7  # 70% allow ad personalization
            }
        }
        
        return technical_profile
    
    def _generate_behavioral_profile(self, template):
        """Generate behavioral patterns and preferences"""
        behavioral_profile = {
            'browsing_patterns': {
                'peak_hours': random.sample(range(6, 24), 4),  # 4 random hours of activity
                'session_length': random.randint(10, 120),  # minutes
                'sites_per_session': random.randint(3, 15)
            },
            'content_preferences': {
                'categories': random.sample(['news', 'entertainment', 'technology', 'sports', 'shopping'], 3),
                'engagement_level': random.choice(['passive', 'active', 'interactive']),
                'sharing_behavior': random.choice(['frequent', 'occasional', 'rare'])
            },
            'purchasing_behavior': {
                'online_shopping_frequency': random.choice(['weekly', 'monthly', 'occasional']),
                'average_spend': random.randint(50, 500),
                'preferred_payment': random.choice(['credit_card', 'paypal', 'bank_transfer'])
            },
            'personality_traits': template['behavior_traits'] + random.sample([
                'cautious', 'adventurous', 'analytical', 'emotional', 'practical'
            ], 2)
        }
        
        return behavioral_profile
    
    def _generate_quantum_fingerprint(self):
        """Generate quantum-level unique fingerprint for identity"""
        base_data = f"{time.time()}{random.random()}{self.entropy_source}"
        identity_hash = hashlib.sha256(base_data.encode()).hexdigest()
        
        quantum_fingerprint = {
            'identity_hash': identity_hash,
            'behavioral_entropy': random.random(),
            'interaction_pattern': self._generate_interaction_pattern(),
            'temporal_signature': self._generate_temporal_signature(),
            'cognitive_biases': self._generate_cognitive_biases()
        }
        
        return quantum_fingerprint
    
    def _generate_interaction_pattern(self):
        """Generate unique interaction patterns"""
        patterns = {
            'click_accuracy': random.uniform(0.7, 0.98),
            'scroll_speed': random.uniform(0.5, 1.5),
            'typing_speed': random.uniform(0.08, 0.25),
            'decision_making_time': random.uniform(0.5, 3.0),
            'error_correction_style': random.choice(['immediate', 'delayed', 'batch'])
        }
        
        return patterns
    
    def _generate_temporal_signature(self):
        """Generate temporal behavior signature"""
        return {
            'activity_peaks': sorted(random.sample(range(0, 24), 3)),  # 3 peak activity hours
            'weekly_pattern': random.choice(['weekday_heavy', 'weekend_heavy', 'balanced']),
            'seasonal_variation': random.uniform(0.1, 0.9),
            'response_latency': random.uniform(0.1, 2.0)
        }
    
    def _generate_cognitive_biases(self):
        """Generate cognitive biases and decision-making patterns"""
        biases = {
            'risk_aversion': random.uniform(0.1, 0.9),
            'attention_span': random.uniform(0.3, 1.2),
            'learning_speed': random.uniform(0.5, 1.5),
            'pattern_recognition': random.uniform(0.4, 1.1),
            'impulse_control': random.uniform(0.2, 0.95)
        }
        
        return biases
    
    def _generate_identity_hash(self, basic_info):
        """Generate unique hash for identity"""
        base_string = f"{basic_info['first_name']}{basic_info['last_name']}{basic_info['age']}{time.time()}"
        return hashlib.md5(base_string.encode()).hexdigest()[:12]
    
    def _create_fallback_identity(self):
        """Create fallback identity in case of errors"""
        return {
            'id': 'fallback_' + str(int(time.time())),
            'persona_type': 'professional',
            'basic_info': {
                'first_name': 'John',
                'last_name': 'Doe',
                'age': 35,
                'location': {'country': 'US', 'timezone': 'America/New_York'}
            },
            'digital_footprint': {'email_addresses': ['johndoe@example.com']},
            'technical_profile': {},
            'behavioral_profile': {},
            'quantum_fingerprint': {},
            'creation_timestamp': time.time()
        }
    
    def evolve_identity(self, original_identity, evolution_factor=0.1):
        """Evolve an existing identity with slight variations"""
        try:
            new_identity = original_identity.copy()
            
            # Apply evolutionary changes
            if random.random() < evolution_factor:
                # Slight name variation
                if random.random() < 0.3:
                    new_identity['basic_info']['first_name'] = self.faker.first_name()
            
            if random.random() < evolution_factor:
                # Age progression
                new_identity['basic_info']['age'] += random.randint(1, 3)
            
            if random.random() < evolution_factor:
                # Location change
                new_identity['basic_info']['location']['city'] = self.faker.city()
            
            # Update digital footprint
            new_identity['digital_footprint']['email_addresses'].append(
                f"new{random.randint(100, 999)}@{random.choice(['gmail.com', 'outlook.com'])}"
            )
            
            # Evolve behavioral patterns
            for key in new_identity['behavioral_profile']['browsing_patterns']:
                if isinstance(new_identity['behavioral_profile']['browsing_patterns'][key], (int, float)):
                    variation = random.uniform(0.9, 1.1)
                    new_identity['behavioral_profile']['browsing_patterns'][key] = int(
                        new_identity['behavioral_profile']['browsing_patterns'][key] * variation
                    )
            
            new_identity['evolution_count'] = original_identity.get('evolution_count', 0) + 1
            new_identity['parent_identity'] = original_identity['id']
            new_identity['creation_timestamp'] = time.time()
            
            self.generated_identities.append(new_identity)
            
            return new_identity
            
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Identity evolution failed: {e}")
            return original_identity
    
    def get_identity_report(self):
        """Get comprehensive identity generation report"""
        recent_identities = self.generated_identities[-5:] if self.generated_identities else []
        
        # Calculate statistics
        persona_counts = {}
        country_counts = {}
        
        for identity in self.generated_identities:
            persona = identity.get('persona_type', 'unknown')
            country = identity.get('basic_info', {}).get('location', {}).get('country', 'unknown')
            
            persona_counts[persona] = persona_counts.get(persona, 0) + 1
            country_counts[country] = country_counts.get(country, 0) + 1
        
        return {
            'total_identities': len(self.generated_identities),
            'persona_distribution': persona_counts,
            'geographic_distribution': country_counts,
            'recent_identities': recent_identities,
            'available_templates': list(self.identity_templates.keys())
        }
    
    def save_identity_library(self, filepath=None):
        """Save generated identities to file"""
        if not filepath:
            filepath = f"identity_library_{int(time.time())}.json"
        
        try:
            with open(filepath, 'w') as f:
                json.dump({
                    'identities': self.generated_identities,
                    'metadata': {
                        'total_count': len(self.generated_identities),
                        'generation_timestamp': time.time(),
                        'entropy_source': self.entropy_source
                    }
                }, f, indent=2, default=str)
            
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Identity library save failed: {e}")
            return False
    
    def load_identity_library(self, filepath):
        """Load identities from file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.generated_identities = data.get('identities', [])
            return True
        except Exception as e:
            if self.config.DEBUG_MODE:
                print(f"❌ Identity library load failed: {e}")
            return False

# Utility function
def create_identity_factory(config=None):
    """Factory function for easy identity factory creation"""
    from config import settings
    config = config or settings.current_config
    return SyntheticIdentityFactory(config)