import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Database configuration
DATABASE_PATH = BASE_DIR / 'echo_muse.db'

# Google Gemini API configuration
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'echo-muse-therapeutic-storytelling-2024')
DEBUG = True

# Therapeutic story generation settings
STORY_GENERATION_CONFIG = {
    'max_tokens': 1000,
    'temperature': 0.7,
    'top_p': 0.9,
    'safety_settings': [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]
}

# Therapeutic techniques and approaches
THERAPEUTIC_TECHNIQUES = {
    'anxiety': {
        'techniques': ['grounding', 'breathing', 'progressive_relaxation'],
        'narrative_style': 'calming and reassuring',
        'themes': ['safety', 'control', 'peace']
    },
    'depression': {
        'techniques': ['cognitive_reframing', 'behavioral_activation', 'self_compassion'],
        'narrative_style': 'hopeful and empowering',
        'themes': ['hope', 'strength', 'connection']
    },
    'stress': {
        'techniques': ['mindfulness', 'time_management', 'boundary_setting'],
        'narrative_style': 'organized and solution-focused',
        'themes': ['balance', 'priorities', 'self-care']
    },
    'grief': {
        'techniques': ['narrative_therapy', 'meaning_making', 'ritual'],
        'narrative_style': 'gentle and honoring',
        'themes': ['memory', 'love', 'healing']
    },
    'anger': {
        'techniques': ['emotion_regulation', 'communication', 'forgiveness'],
        'narrative_style': 'understanding and transformative',
        'themes': ['understanding', 'release', 'growth']
    },
    'loneliness': {
        'techniques': ['connection_building', 'self_relationship', 'community'],
        'narrative_style': 'warm and connecting',
        'themes': ['belonging', 'friendship', 'self-love']
    },
    'fear': {
        'techniques': ['exposure', 'courage_building', 'safety_planning'],
        'narrative_style': 'brave and encouraging',
        'themes': ['courage', 'growth', 'resilience']
    },
    'confusion': {
        'techniques': ['clarity_seeking', 'decision_making', 'values_exploration'],
        'narrative_style': 'clear and guiding',
        'themes': ['wisdom', 'direction', 'purpose']
    }
}

# Ambient sound categories for different emotional states
AMBIENT_SOUNDS = {
    'calming': {
        'sounds': ['ocean_waves', 'rain', 'forest_birds', 'gentle_wind'],
        'description': 'Peaceful nature sounds for relaxation'
    },
    'energizing': {
        'sounds': ['morning_birds', 'flowing_stream', 'light_rain', 'rustling_leaves'],
        'description': 'Uplifting natural sounds for motivation'
    },
    'grounding': {
        'sounds': ['deep_ocean', 'cave_ambience', 'earth_sounds', 'low_frequency_hum'],
        'description': 'Deep, stable sounds for grounding'
    },
    'healing': {
        'sounds': ['tibetan_bowls', 'soft_chimes', 'healing_frequencies', 'gentle_music'],
        'description': 'Therapeutic sounds for emotional healing'
    }
}

# Story prompts and templates
STORY_PROMPTS = {
    'metaphorical': [
        "a garden that grows emotions instead of flowers",
        "a lighthouse keeper who guides lost feelings home",
        "a library where each book contains a different way to heal",
        "a bridge between the land of worry and the island of peace",
        "a craftsperson who weaves strength from broken threads"
    ],
    'journey': [
        "a traveler discovering hidden strengths along a winding path",
        "an explorer mapping the territory of their own resilience",
        "a pilgrim seeking the temple of inner peace",
        "a navigator learning to read the stars of hope",
        "a wanderer finding home within themselves"
    ],
    'transformation': [
        "a caterpillar's patient journey toward becoming a butterfly",
        "a seed that learns to grow in difficult soil",
        "a phoenix discovering the beauty in renewal",
        "a river that carves new channels through solid rock",
        "a storm that clears the air for a rainbow"
    ]
}

# Mood tracking configuration
MOOD_SCALE = {
    1: "Very Low",
    2: "Low", 
    3: "Somewhat Low",
    4: "Below Average",
    5: "Neutral",
    6: "Above Average",
    7: "Somewhat High",
    8: "High",
    9: "Very High",
    10: "Excellent"
}

# Application metadata
APP_INFO = {
    'name': 'Echo-Muse',
    'version': '1.0.0',
    'description': 'AI-Powered Therapeutic Storytelling Companion',
    'author': 'Echo-Muse Development Team',
    'license': 'MIT',
    'repository': 'https://github.com/your-username/echo-muse'
}