import random
import json
import os
from datetime import datetime, timedelta

class SyntheticIdentityFactory:
    def __init__(self):
        self.identities_generated = 0
        self.demographics = self._load_demographic_data()
        
    def create_quantum_identity(self, age_group="adult", location="US", interests=None):
        identity = {
            "id": f"quantum_id_{self.identities_generated}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "demographics": self._generate_demographics(age_group, location),
            "digital_footprint": self._generate_quantum_digital_footprint(interests),
            "technical_profile": self._generate_quantum_technical_profile(),
            "behavioral_patterns": self._generate_quantum_behavioral_patterns(age_group),
            "quantum_fingerprint": self._generate_quantum_fingerprint(),
            "creation_timestamp": datetime.now().isoformat()
        }
        
        self.identities_generated += 1
        self._save_identity(identity)
        return identity
    
    def _generate_quantum_fingerprint(self):
        return {
            "canvas_hash": self._generate_canvas_noise(),
            "webgl_hash": self._randomize_webgl_rendering(),
            "audio_context_hash": self._modify_audio_fingerprint(),
            "timezone_offset": random.randint(-720, 720),
            "font_metrics": self._vary_font_rendering(),
            "hardware_concurrency": random.choice([4, 8, 12, 16]),
            "device_memory": random.choice([4, 8, 16, 32]),
            "screen_depth": random.choice([24, 30, 32]),
            "pixel_ratio": round(random.uniform(1.0, 3.0), 2)
        }
    
    def _generate_quantum_technical_profile(self):
        return {
            "timezone": random.choice(["America/New_York", "Europe/London", "Asia/Tokyo", "Australia/Sydney"]),
            "screen_resolutions": [
                f"{random.choice([1920, 1366, 1536, 1440])}x{random.choice([1080, 768, 864, 900])}",
                f"{random.choice([375, 414, 360])}x{random.choice([812, 896, 800])}"
            ],
            "browser_plugins": random.randint(3, 12),
            "font_fingerprint": self._generate_quantum_font_list(),
            "language_preferences": ["en-US", "en"] + (["es", "fr"] if random.random() > 0.8 else []),
            "accept_languages": "en-US,en;q=0.9" + (",es;q=0.8,fr;q=0.7" if random.random() > 0.8 else ""),
            "hardware_concurrency": random.choice([4, 8, 12, 16]),
            "device_memory": random.choice([4, 8, 16, 32]),
            "webgl_vendor": random.choice(["Google Inc. (Intel)", "NVIDIA Corporation", "AMD", "Apple Inc."]),
            "webgl_renderer": random.choice([
                "ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0)",
                "NVIDIA GeForce RTX 4080/PCIe/SSE2",
                "Apple M2 Pro"
            ])
        }
    
    def _generate_quantum_font_list(self):
        font_sets = {
            "windows": ["Arial", "Times New Roman", "Calibri", "Verdana", "Tahoma", "Segoe UI"],
            "mac": ["Helvetica Neue", "San Francisco", "Times New Roman", "Arial", "Lucida Grande"],
            "linux": ["DejaVu Sans", "Liberation Sans", "Times New Roman", "Arial", "Ubuntu"]
        }
        
        os_type = random.choice(["windows", "mac", "linux"])
        base_fonts = font_sets[os_type]
        
        additional_fonts = random.sample([
            "Courier New", "Georgia", "Palatino", "Garamond", "Book Antiqua",
            "Comic Sans MS", "Impact", "Trebuchet MS"
        ], random.randint(3, 8))
        
        return base_fonts + additional_fonts
    
    def _generate_quantum_behavioral_patterns(self, age_group):
        patterns = {
            "teen": {"click_speed": "fast", "scroll_behavior": "rapid", "attention_span": "short"},
            "young_adult": {"click_speed": "moderate", "scroll_behavior": "balanced", "attention_span": "medium"},
            "adult": {"click_speed": "deliberate", "scroll_behavior": "methodical", "attention_span": "long"},
            "senior": {"click_speed": "slow", "scroll_behavior": "cautious", "attention_span": "variable"}
        }
        
        base_pattern = patterns.get(age_group, patterns["adult"])
        base_pattern.update({
            "mouse_tremor_variance": random.uniform(0.1, 0.5),
            "typing_rhythm_patterns": self._generate_typing_dna(),
            "scroll_velocity_profile": self._create_scroll_signature(),
            "attention_span_fluctuation": random.uniform(0.7, 1.3)
        })
        
        return base_pattern
    
    def _generate_typing_dna(self):
        return {
            "base_speed": random.uniform(0.08, 0.15),
            "error_rate": random.uniform(0.01, 0.03),
            "thinking_pause_frequency": random.uniform(0.03, 0.07),
            "backspace_pattern": random.choice(["immediate", "delayed", "burst"])
        }
    
    def _generate_canvas_noise(self):
        return f"canvas_{random.randint(1000000000, 9999999999)}"
    
    def _randomize_webgl_rendering(self):
        return f"webgl_{random.randint(1000000000, 9999999999)}"
    
    def _modify_audio_fingerprint(self):
        return f"audio_{random.randint(1000000000, 9999999999)}"
    
    def _vary_font_rendering(self):
        return f"fonts_{random.randint(1000000000, 9999999999)}"
    
    def _create_scroll_signature(self):
        return {
            "primary_style": random.choice(["continuous", "bounce", "random"]),
            "scroll_speed": random.uniform(0.5, 2.0),
            "scroll_direction_bias": random.uniform(0.3, 0.7),
            "scroll_pause_pattern": random.choice(["even", "clustered", "random"])
        }

# Keep existing methods, update create_advanced_identity to use quantum
def create_advanced_identity(self, age_group="adult", location="US", interests=None):
    return self.create_quantum_identity(age_group, location, interests)