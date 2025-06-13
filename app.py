#!/usr/bin/env python3
"""
Echo-Muse: AI-Powered Therapeutic Storytelling Companion
Main Flask application for generating personalized healing stories with adaptive soundscapes.
"""

import os
import json
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import random
import uuid

# Configure the Gemini API
API_KEY = "AIzaSyAuEJ3qq-qMfK-LFnx0bWfWtc6iYH9mymI"
genai.configure(api_key=API_KEY)

app = Flask(__name__)
app.secret_key = 'echo-muse-therapeutic-storytelling-2024'

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

class TherapeuticStoryGenerator:
    """Core class for generating therapeutic stories and analyzing emotional states."""
    
    def __init__(self):
        self.therapeutic_techniques = {
            'anxiety': 'grounding and mindfulness techniques',
            'depression': 'cognitive behavioral therapy and hope-building',
            'trauma': 'narrative therapy and empowerment themes',
            'stress': 'relaxation and coping strategies',
            'grief': 'acceptance and healing journey themes',
            'self_esteem': 'self-compassion and strength recognition'
        }
        
        self.story_archetypes = [
            'The Hero\'s Journey of Healing',
            'The Wise Guide Within',
            'The Garden of Growth',
            'The Bridge to Tomorrow',
            'The Light in the Forest',
            'The Ocean of Calm',
            'The Phoenix Rising',
            'The Sacred Mountain Path',
            'The Healing Waters',
            'The Butterfly Transformation',
            'The Ancient Tree of Wisdom',
            'The Starlit Journey Home',
            'The Desert Oasis Discovery',
            'The Crystal Cave of Clarity',
            'The Rainbow After the Storm',
            'The Gentle River of Time'
        ]
        
        self.story_settings = [
            'enchanted forest with glowing fireflies',
            'peaceful mountain meadow at sunrise',
            'serene lakeside with gentle waves',
            'mystical garden with blooming flowers',
            'quiet beach with soft sand dunes',
            'ancient library filled with wisdom',
            'cozy cabin by a crackling fireplace',
            'floating island in the clouds',
            'underground crystal cavern',
            'bamboo grove with singing birds',
            'lighthouse on a cliff overlooking the sea',
            'secret waterfall hidden in the jungle'
        ]
        
        self.healing_metaphors = [
            'flowing water that cleanses and renews',
            'growing plants that reach toward the light',
            'gentle winds that carry away worries',
            'warm sunlight that heals and energizes',
            'solid earth that grounds and supports',
            'dancing flames that transform and purify',
            'twinkling stars that guide the way',
            'soft rain that nourishes growth',
            'ocean waves that ebb and flow naturally',
            'mountain peaks that offer perspective'
        ]
    
    def analyze_emotional_state(self, user_input):
        """Analyze user input to determine emotional state and therapeutic needs."""
        prompt = f"""
        As a compassionate AI therapist, analyze the following user input and provide insights:
        
        User Input: "{user_input}"
        
        Please provide a JSON response with:
        1. primary_emotion: The main emotion detected (anxiety, depression, trauma, stress, grief, self_esteem, or neutral)
        2. intensity: Scale of 1-10 for emotional intensity
        3. key_themes: List of 3-5 key emotional themes or concerns
        4. therapeutic_focus: Recommended therapeutic approach
        5. story_tone: Suggested tone for the healing story (gentle, empowering, hopeful, calming, etc.)
        
        Respond only with valid JSON.
        """
        
        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)
        except Exception as e:
            # Fallback analysis
            return {
                'primary_emotion': 'neutral',
                'intensity': 5,
                'key_themes': ['self-reflection', 'growth', 'healing'],
                'therapeutic_focus': 'general wellness',
                'story_tone': 'gentle'
            }
    
    def generate_therapeutic_story(self, emotional_analysis, user_name="friend"):
        """Generate a personalized therapeutic story based on emotional analysis."""
        archetype = random.choice(self.story_archetypes)
        setting = random.choice(self.story_settings)
        metaphor = random.choice(self.healing_metaphors)
        technique = self.therapeutic_techniques.get(emotional_analysis['primary_emotion'], 'mindfulness and self-compassion')
        
        # Add variety with different story elements
        story_elements = {
            'time_of_day': random.choice(['dawn', 'morning', 'afternoon', 'sunset', 'twilight', 'night']),
            'weather': random.choice(['gentle breeze', 'warm sunshine', 'soft rain', 'clear skies', 'misty air']),
            'companion': random.choice(['wise owl', 'gentle deer', 'flowing stream', 'ancient tree', 'guiding star', 'inner voice']),
            'discovery': random.choice(['hidden path', 'secret garden', 'magical spring', 'glowing crystal', 'ancient wisdom', 'inner strength'])
        }
        
        prompt = f"""
        Create a unique therapeutic healing story with these specifications:
        
        Story Archetype: {archetype}
        Setting: {setting}
        Central Metaphor: {metaphor}
        Time of Day: {story_elements['time_of_day']}
        Weather/Atmosphere: {story_elements['weather']}
        Companion/Guide: {story_elements['companion']}
        Key Discovery: {story_elements['discovery']}
        
        Emotional Context:
        - Primary Emotion: {emotional_analysis['primary_emotion']}
        - Intensity: {emotional_analysis['intensity']}/10
        - Key Themes: {', '.join(emotional_analysis['key_themes'])}
        - Therapeutic Approach: {technique}
        - Story Tone: {emotional_analysis['story_tone']}
        - User Name: {user_name}
        
        Guidelines:
        - Create a 800-1200 word therapeutic story
        - Weave the central metaphor throughout the narrative
        - Include rich sensory details specific to the setting
        - Incorporate the companion/guide naturally
        - Build toward the key discovery as a moment of insight
        - Use practical coping strategies within the story context
        - End with hope, empowerment, and actionable wisdom
        - Use second person ("you") for personal connection
        - Make each story feel completely unique and fresh
        
        The story should transport the reader to this specific world while addressing their emotional needs.
        """
        
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return self.get_fallback_story(emotional_analysis['story_tone'], setting, metaphor)
    
    def get_fallback_story(self, tone="gentle", setting="peaceful forest", metaphor="flowing water"):
        """Provide varied fallback stories if AI generation fails."""
        fallback_stories = [
            f"""
            You find yourself in a {setting}, where the atmosphere feels {tone} and welcoming. The world around you seems to pulse with the rhythm of {metaphor}, reminding you of your own inner strength.
            
            As you explore this sacred space, you notice how everything here exists in perfect harmony. The elements around you whisper ancient wisdom about resilience, growth, and the power of transformation that lives within you.
            
            You pause to truly feel this moment, understanding that like {metaphor}, you have the ability to adapt, flow, and find your way through any challenge. This realization fills you with a profound sense of peace and confidence.
            
            Take a deep breath and carry this wisdom with you. You are stronger than you know, more resilient than you imagine, and worthy of all the healing and joy that life has to offer.
            """,
            f"""
            In this {setting}, you discover a place where time moves differently, where healing happens naturally, and where the essence of {metaphor} teaches you about your own capacity for renewal.
            
            The gentle energy of this space invites you to release what no longer serves you. You feel lighter with each breath, more connected to your authentic self, and increasingly aware of the infinite possibilities that await you.
            
            Like {metaphor}, you are constantly evolving, constantly growing, constantly becoming more of who you're meant to be. This journey of transformation is not just possible—it's already happening within you.
            
            Trust in your process, honor your journey, and know that every step forward is a victory worth celebrating.
            """,
            f"""
            You arrive at a {setting} that feels like a sanctuary created just for you. Here, surrounded by the gentle presence of {metaphor}, you find the space to simply be—without judgment, without pressure, without the need to be anything other than exactly who you are.
            
            In this moment of pure acceptance, you begin to see yourself through eyes of compassion. You recognize the courage it takes to face each day, the strength you've shown in difficult times, and the beautiful heart that continues to hope and love despite everything.
            
            The wisdom of {metaphor} reminds you that healing is not about becoming perfect—it's about becoming whole. And you are already on that path, already worthy of love and belonging, already enough.
            
            Carry this truth with you always: you are a miracle in motion, a story still being written, a light that cannot be dimmed.
            """
        ]
        
        return random.choice(fallback_stories)

class AmbientSoundGenerator:
    """Generate diverse ambient soundscape recommendations based on story content."""
    
    def __init__(self):
        self.soundscape_types = {
            'forest_dawn': {
                'type': 'grounding',
                'description': 'Forest awakening with bird songs',
                'frequencies': [220, 330, 440],  # A3, E4, A4 - perfect harmony
                'patterns': ['gentle', 'natural', 'organic']
            },
            'ocean_waves': {
                'type': 'calming',
                'description': 'Rhythmic ocean waves',
                'frequencies': [110, 220, 330],  # A2, A3, E4 - octaves and fifth
                'patterns': ['flowing', 'rhythmic', 'deep']
            },
            'mountain_wind': {
                'type': 'energizing',
                'description': 'Mountain winds and distant echoes',
                'frequencies': [261.63, 329.63, 392],  # C4, E4, G4 - major triad
                'patterns': ['airy', 'expansive', 'uplifting']
            },
            'garden_bloom': {
                'type': 'healing',
                'description': 'Gentle garden with soft breezes',
                'frequencies': [256, 320, 384],  # C4, E4, G4 (rounded) - gentle harmony
                'patterns': ['nurturing', 'soft', 'harmonious']
            },
            'crystal_cave': {
                'type': 'mystical',
                'description': 'Resonant crystal harmonics',
                'frequencies': [432, 540, 648],  # A4 (432Hz tuning), C#5, E5
                'patterns': ['crystalline', 'pure', 'ethereal']
            },
            'rain_meditation': {
                'type': 'peaceful',
                'description': 'Gentle rain on leaves',
                'frequencies': [174, 285, 396],  # Solfeggio frequencies - healing tones
                'patterns': ['soothing', 'consistent', 'meditative']
            },
            'fireplace_warmth': {
                'type': 'comforting',
                'description': 'Crackling fireplace warmth',
                'frequencies': [146.83, 220, 293.66],  # D3, A3, D4 - warm octaves
                'patterns': ['warm', 'crackling', 'cozy']
            },
            'starlight_journey': {
                'type': 'transcendent',
                'description': 'Cosmic harmonies and stellar winds',
                'frequencies': [528, 639, 741],  # Solfeggio frequencies - transformation
                'patterns': ['cosmic', 'expansive', 'infinite']
            }
        }
        
        self.keyword_mapping = {
            'forest': ['forest_dawn', 'rain_meditation'],
            'ocean': ['ocean_waves'],
            'mountain': ['mountain_wind'],
            'garden': ['garden_bloom'],
            'crystal': ['crystal_cave'],
            'rain': ['rain_meditation'],
            'fire': ['fireplace_warmth'],
            'star': ['starlight_journey'],
            'cave': ['crystal_cave'],
            'water': ['ocean_waves', 'rain_meditation'],
            'wind': ['mountain_wind'],
            'tree': ['forest_dawn'],
            'flower': ['garden_bloom']
        }
    
    def recommend_soundscape(self, story_content, emotional_tone):
        """Recommend appropriate ambient sound type based on story content and emotion."""
        story_lower = story_content.lower()
        
        # Find matching soundscapes based on story keywords
        matching_soundscapes = []
        for keyword, soundscapes in self.keyword_mapping.items():
            if keyword in story_lower:
                matching_soundscapes.extend(soundscapes)
        
        # If we found matches, randomly select one
        if matching_soundscapes:
            selected = random.choice(matching_soundscapes)
            return self.soundscape_types[selected]
        
        # Fallback based on emotional tone
        emotion_fallbacks = {
            'anxiety': 'rain_meditation',
            'depression': 'mountain_wind',
            'stress': 'ocean_waves',
            'grief': 'garden_bloom',
            'gentle': 'forest_dawn',
            'calming': 'ocean_waves',
            'energizing': 'mountain_wind',
            'healing': 'garden_bloom'
        }
        
        fallback_key = emotion_fallbacks.get(emotional_tone, 'forest_dawn')
        return self.soundscape_types[fallback_key]

# Initialize components
story_generator = TherapeuticStoryGenerator()
sound_generator = AmbientSoundGenerator()

# Database setup
def init_db():
    """Initialize the SQLite database for user sessions and progress tracking."""
    conn = sqlite3.connect('echo_muse.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            user_name TEXT,
            timestamp DATETIME,
            emotional_state TEXT,
            story_content TEXT,
            soundscape TEXT,
            mood_before INTEGER,
            mood_after INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Main page of the application."""
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    """Generate a therapeutic story based on user input."""
    try:
        data = request.json
        user_input = data.get('user_input', '')
        user_name = data.get('user_name', 'friend')
        mood_before = data.get('mood_before', 5)
        
        # Analyze emotional state
        emotional_analysis = story_generator.analyze_emotional_state(user_input)
        
        # Generate therapeutic story
        story = story_generator.generate_therapeutic_story(emotional_analysis, user_name)
        
        # Recommend soundscape
        soundscape = sound_generator.recommend_soundscape(story, emotional_analysis['story_tone'])
        
        # Create session ID
        session_id = str(uuid.uuid4())
        
        # Store session data
        conn = sqlite3.connect('echo_muse.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sessions (id, user_name, timestamp, emotional_state, story_content, soundscape, mood_before)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (session_id, user_name, datetime.now(), json.dumps(emotional_analysis), story, json.dumps(soundscape), mood_before))
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'story': story,
            'emotional_analysis': emotional_analysis,
            'ambient_sound': soundscape
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/update_mood', methods=['POST'])
def update_mood():
    """Update the user's mood after experiencing the story."""
    try:
        data = request.json
        session_id = data.get('session_id')
        mood_after = data.get('mood_after')
        
        conn = sqlite3.connect('echo_muse.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE sessions SET mood_after = ? WHERE id = ?', (mood_after, session_id))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/progress')
def progress():
    """Show user's progress and session history."""
    try:
        conn = sqlite3.connect('echo_muse.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT timestamp, mood_before, mood_after, emotional_state
            FROM sessions 
            WHERE mood_after IS NOT NULL
            ORDER BY timestamp DESC
            LIMIT 10
        ''')
        sessions = cursor.fetchall()
        conn.close()
        
        return render_template('progress.html', sessions=sessions)
        
    except Exception as e:
        return f"Error loading progress: {str(e)}"

if __name__ == '__main__':
    init_db()
    print("🎭 Echo-Muse: AI-Powered Therapeutic Storytelling Companion")
    print("🌟 Starting the healing journey...")
    app.run(debug=True, host='0.0.0.0', port=5000)