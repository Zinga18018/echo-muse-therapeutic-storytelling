/**
 * Echo-Muse: AI-Powered Therapeutic Storytelling Companion
 * Frontend JavaScript for interactive functionality
 */

// Global variables
let currentAudio = null;
let isGenerating = false;
let sessionData = {
    sessions: [],
    currentSession: null
};

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    loadProgressData();
    setupEventListeners();
});

/**
 * Initialize the application
 */
function initializeApp() {
    // Set default values
    const userName = document.getElementById('user-name');
    if (userName && !userName.value) {
        userName.value = 'friend';
    }
    
    // Initialize mood sliders
    updateMoodDisplay('mood-before', 5);
    updateMoodDisplay('mood-after', 5);
    
    // Show home section by default
    showSection('home');
    
    console.log('🎭 Echo-Muse initialized successfully');
}

/**
 * Setup event listeners for interactive elements
 */
function setupEventListeners() {
    // Mood slider listeners
    const moodBefore = document.getElementById('mood-before');
    const moodAfter = document.getElementById('mood-after');
    
    if (moodBefore) {
        moodBefore.addEventListener('input', function() {
            updateMoodDisplay('mood-before', this.value);
        });
    }
    
    if (moodAfter) {
        moodAfter.addEventListener('input', function() {
            updateMoodDisplay('mood-after', this.value);
            if (sessionData.currentSession) {
                sessionData.currentSession.mood_after = parseInt(this.value);
            }
        });
    }
    
    // Form validation
    const userInput = document.getElementById('user-input');
    if (userInput) {
        userInput.addEventListener('input', function() {
            validateForm();
        });
    }
}

/**
 * Update mood display based on slider value
 */
function updateMoodDisplay(sliderId, value) {
    const slider = document.getElementById(sliderId);
    if (!slider) return;
    
    const moodTexts = {
        1: '😔 Very Low',
        2: '😞 Low', 
        3: '😐 Below Average',
        4: '😕 Somewhat Low',
        5: '😐 Neutral',
        6: '🙂 Above Average',
        7: '😊 Good',
        8: '😄 Very Good',
        9: '😁 Great',
        10: '🤩 Excellent'
    };
    
    // Update slider background color
    const percentage = ((value - 1) / 9) * 100;
    slider.style.background = `linear-gradient(to right, #ef4444 0%, #f59e0b 50%, #10b981 100%)`;
    
    // Find and update mood display text
    const container = slider.closest('.mood-slider');
    if (container) {
        let display = container.querySelector('.mood-display');
        if (!display) {
            display = document.createElement('div');
            display.className = 'mood-display';
            container.appendChild(display);
        }
        display.textContent = moodTexts[value] || `Mood: ${value}/10`;
    }
}

/**
 * Validate form before submission
 */
function validateForm() {
    const userInput = document.getElementById('user-input');
    const generateBtn = document.getElementById('generate-btn');
    
    if (userInput && generateBtn) {
        const isValid = userInput.value.trim().length > 10;
        generateBtn.disabled = !isValid || isGenerating;
        
        if (!isValid && userInput.value.length > 0) {
            userInput.style.borderColor = '#ef4444';
        } else {
            userInput.style.borderColor = '';
        }
    }
}

/**
 * Generate therapeutic story
 */
async function generateStory() {
    if (isGenerating) return;
    
    const userInput = document.getElementById('user-input');
    const userName = document.getElementById('user-name');
    const moodBefore = document.getElementById('mood-before');
    const generateBtn = document.getElementById('generate-btn');
    
    if (!userInput || !userInput.value.trim()) {
        alert('Please share what\'s on your mind before generating a story.');
        return;
    }
    
    if (userInput.value.trim().length < 10) {
        alert('Please share a bit more about what you\'re experiencing (at least 10 characters).');
        return;
    }
    
    isGenerating = true;
    
    // Update button state
    const btnText = generateBtn.querySelector('.btn-text');
    const btnLoading = generateBtn.querySelector('.btn-loading');
    
    btnText.style.display = 'none';
    btnLoading.style.display = 'inline';
    generateBtn.disabled = true;
    
    try {
        // Create session data
        sessionData.currentSession = {
            timestamp: new Date().toISOString(),
            user_input: userInput.value.trim(),
            user_name: userName.value.trim() || 'friend',
            mood_before: parseInt(moodBefore.value),
            mood_after: null
        };
        
        // Send request to backend
        const response = await fetch('/generate_story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_input: sessionData.currentSession.user_input,
                user_name: sessionData.currentSession.user_name,
                mood_before: sessionData.currentSession.mood_before
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        // Display the story
        displayStory(data.story, data.ambient_sound);
        
        // Store session data
        sessionData.currentSession.story = data.story;
        sessionData.currentSession.ambient_sound = data.ambient_sound;
        
    } catch (error) {
        console.error('Error generating story:', error);
        alert('Sorry, there was an error generating your story. Please try again.');
    } finally {
        // Reset button state
        isGenerating = false;
        btnText.style.display = 'inline';
        btnLoading.style.display = 'none';
        generateBtn.disabled = false;
    }
}

/**
 * Display the generated story
 */
function displayStory(story, ambientSound) {
    const storySection = document.getElementById('story-section');
    const storyContent = document.getElementById('story-content');
    
    if (!storySection || !storyContent) return;
    
    // Format and display story
    storyContent.innerHTML = formatStoryText(story);
    
    // Show story section with animation
    storySection.style.display = 'block';
    storySection.scrollIntoView({ behavior: 'smooth' });
    
    // Setup ambient sound
    if (ambientSound) {
        setupAmbientSound(ambientSound);
    }
    
    // Reset mood after slider
    const moodAfter = document.getElementById('mood-after');
    if (moodAfter) {
        moodAfter.value = 5;
        updateMoodDisplay('mood-after', 5);
    }
}

/**
 * Format story text with proper paragraphs and styling
 */
function formatStoryText(story) {
    if (!story) return '';
    
    // Split into paragraphs and format
    const paragraphs = story.split('\n\n').filter(p => p.trim());
    
    return paragraphs.map(paragraph => {
        const trimmed = paragraph.trim();
        if (trimmed.startsWith('**') && trimmed.endsWith('**')) {
            // Handle bold headers
            return `<h4>${trimmed.slice(2, -2)}</h4>`;
        } else {
            // Regular paragraph
            return `<p>${trimmed}</p>`;
        }
    }).join('');
}

/**
 * Setup ambient sound for the story with enhanced variety
 */
function setupAmbientSound(soundscapeData) {
    const audioElement = document.getElementById('ambient-audio');
    const playButton = document.getElementById('play-audio');
    
    if (!audioElement || !playButton) return;
    
    // Handle both old string format and new object format
    let soundscape;
    if (typeof soundscapeData === 'string') {
        // Fallback for old format
        soundscape = {
            type: soundscapeData,
            description: `${soundscapeData} ambient sounds`,
            frequencies: [220, 330, 440, 550],
            patterns: ['gentle', 'flowing']
        };
    } else {
        soundscape = soundscapeData;
    }
    
    // Generate a dynamic soundscape using Web Audio API
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Store enhanced soundscape data
    audioElement.audioContext = audioContext;
    audioElement.soundscape = soundscape;
    audioElement.frequencies = soundscape.frequencies;
    audioElement.patterns = soundscape.patterns;
    
    // Update play button with descriptive text
    playButton.innerHTML = `🎵 Play ${soundscape.description}`;
    
    console.log(`🎵 Enhanced ambient sound setup:`, soundscape);
}

/**
 * Toggle ambient audio playback
 */
function toggleAudio() {
    const audioElement = document.getElementById('ambient-audio');
    const playButton = document.getElementById('play-audio');
    
    if (!audioElement || !playButton) return;
    
    // Check if audio is currently playing
    if (!audioElement.isPlaying) {
        startAmbientAudio(audioElement, playButton);
    } else {
        stopAmbientAudio(audioElement, playButton);
    }
}

/**
 * Start playing enhanced ambient audio using Web Audio API
 */
function startAmbientAudio(audioElement, playButton) {
    try {
        const audioContext = audioElement.audioContext;
        const soundscape = audioElement.soundscape || {};
        const frequencies = audioElement.frequencies || [220, 330, 440];
        const patterns = audioElement.patterns || ['gentle'];
        
        if (!audioContext) {
            throw new Error('Audio context not available');
        }
        
        // Resume audio context if suspended (required by some browsers)
        if (audioContext.state === 'suspended') {
            audioContext.resume();
        }
        
        // Create harmonious oscillators with careful tuning
        const oscillators = [];
        const gainNodes = [];
        const filterNodes = [];
        
        // Use only the first 2-3 frequencies to avoid chaos
        const selectedFreqs = frequencies.slice(0, 3);
        
        selectedFreqs.forEach((freq, index) => {
            // Create oscillator with consistent wave type
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            const filterNode = audioContext.createBiquadFilter();
            
            // Use sine waves for clean, pleasant tones
            oscillator.type = 'sine';
            
            // Set exact frequency without random variations
            oscillator.frequency.setValueAtTime(freq, audioContext.currentTime);
            
            // Configure gentle low-pass filter for warmth
            filterNode.type = 'lowpass';
            filterNode.frequency.setValueAtTime(1200, audioContext.currentTime);
            filterNode.Q.setValueAtTime(0.5, audioContext.currentTime);
            
            // Set gentle, consistent volume
            const baseVolume = 0.08 / selectedFreqs.length;
            let finalVolume = baseVolume;
            
            // Adjust volume based on frequency (lower frequencies slightly louder)
            if (freq < 300) {
                finalVolume *= 1.2;
            } else if (freq > 500) {
                finalVolume *= 0.8;
            }
            
            // Apply pattern-based volume adjustments
            if (patterns.includes('gentle') || patterns.includes('soft')) {
                finalVolume *= 0.6;
            } else if (patterns.includes('deep') || patterns.includes('grounding')) {
                finalVolume *= 0.8;
            }
            
            gainNode.gain.setValueAtTime(finalVolume, audioContext.currentTime);
            
            // Add very subtle, slow volume modulation for organic feel
            if (patterns.includes('flowing') || patterns.includes('rhythmic')) {
                const modulationRate = 0.3 + (index * 0.1); // Slower, more gentle
                
                // Create very gentle volume oscillation
                const startTime = audioContext.currentTime;
                const modulationGain = audioContext.createGain();
                const lfo = audioContext.createOscillator();
                
                lfo.frequency.setValueAtTime(modulationRate, startTime);
                lfo.type = 'sine';
                
                modulationGain.gain.setValueAtTime(finalVolume * 0.1, startTime); // Very subtle modulation
                
                lfo.connect(modulationGain);
                modulationGain.connect(gainNode.gain);
                
                lfo.start(startTime);
                
                // Store LFO for cleanup
                if (!audioElement.lfos) audioElement.lfos = [];
                audioElement.lfos.push(lfo);
            }
            
            // Connect nodes: oscillator -> filter -> gain -> destination
            oscillator.connect(filterNode);
            filterNode.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            // Start oscillator
            oscillator.start();
            
            oscillators.push(oscillator);
            gainNodes.push(gainNode);
            filterNodes.push(filterNode);
        });
        
        // Store oscillators for cleanup
        audioElement.oscillators = oscillators;
        audioElement.gainNodes = gainNodes;
        audioElement.filterNodes = filterNodes;
        audioElement.isPlaying = true;
        
        // Update button
        playButton.innerHTML = playButton.innerHTML.replace('Play', 'Pause');
        playButton.style.background = 'linear-gradient(135deg, #10b981, #059669)';
        
        console.log('🎵 Harmonious ambient audio started:', soundscape.description);
        
    } catch (error) {
        console.log('Audio play failed:', error);
        // Fallback: show a visual indication
        playButton.innerHTML = '🎵 Ambient Sounds Active (Visual Mode)';
        playButton.style.background = 'linear-gradient(135deg, #6366f1, #8b5cf6)';
        audioElement.isPlaying = true;
    }
}

/**
 * Stop playing ambient audio and clean up resources
 */
function stopAmbientAudio(audioElement, playButton) {
    try {
        // Stop all oscillators
        if (audioElement.oscillators) {
            audioElement.oscillators.forEach(oscillator => {
                try {
                    oscillator.stop();
                } catch (e) {
                    // Oscillator might already be stopped
                }
            });
        }
        
        // Stop all LFO oscillators
        if (audioElement.lfos) {
            audioElement.lfos.forEach(lfo => {
                try {
                    lfo.stop();
                } catch (e) {
                    // LFO might already be stopped
                }
            });
        }
        
        // Clean up all audio nodes
        audioElement.oscillators = null;
        audioElement.gainNodes = null;
        audioElement.filterNodes = null;
        audioElement.lfos = null;
        audioElement.isPlaying = false;
        
        // Update button
        playButton.innerHTML = playButton.innerHTML.replace('Pause', 'Play').replace('Active (Visual Mode)', 'Play');
        playButton.style.background = '';
        
        console.log('🎵 Harmonious ambient audio stopped');
        
    } catch (error) {
        console.log('Error stopping audio:', error);
        // Force reset
        audioElement.isPlaying = false;
        playButton.innerHTML = playButton.innerHTML.replace('Pause', 'Play').replace('Active (Visual Mode)', 'Play');
        playButton.style.background = '';
    }
}

/**
 * Share/save the current story
 */
function shareStory() {
    if (!sessionData.currentSession) {
        alert('No story to save!');
        return;
    }
    
    // Save session data
    saveSession();
    
    // Show confirmation
    alert('Your healing story has been saved to your progress! 💜');
}

/**
 * Save current session to progress
 */
async function saveSession() {
    if (!sessionData.currentSession) return;
    
    try {
        const response = await fetch('/update_mood', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                mood_before: sessionData.currentSession.mood_before,
                mood_after: sessionData.currentSession.mood_after || 5,
                user_input: sessionData.currentSession.user_input,
                story: sessionData.currentSession.story
            })
        });
        
        if (response.ok) {
            // Add to local session data
            sessionData.sessions.unshift(sessionData.currentSession);
            updateProgressDisplay();
        }
    } catch (error) {
        console.error('Error saving session:', error);
    }
}

/**
 * Reset form for new story
 */
function resetForm() {
    // Clear form
    const userInput = document.getElementById('user-input');
    const moodBefore = document.getElementById('mood-before');
    const storySection = document.getElementById('story-section');
    
    if (userInput) userInput.value = '';
    if (moodBefore) {
        moodBefore.value = 5;
        updateMoodDisplay('mood-before', 5);
    }
    
    // Hide story section
    if (storySection) {
        storySection.style.display = 'none';
    }
    
    // Stop audio
    const audioElement = document.getElementById('ambient-audio');
    const playButton = document.getElementById('play-audio');
    if (audioElement && audioElement.isPlaying) {
        stopAmbientAudio(audioElement, playButton);
    }
    
    // Reset button states
    if (playButton) {
        playButton.innerHTML = '🎵 Play Ambient Sounds';
        playButton.style.background = '';
    }
    
    // Clear current session
    sessionData.currentSession = null;
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

/**
 * Show specific section (navigation)
 */
function showSection(sectionName) {
    // Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
        section.style.display = 'none';
    });
    
    // Show target section
    const targetSection = document.getElementById(sectionName);
    if (targetSection) {
        targetSection.classList.add('active');
        targetSection.style.display = 'block';
    }
    
    // Update navigation
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
    });
    
    // Find and activate current nav link
    const currentNavLink = Array.from(navLinks).find(link => 
        link.onclick && link.onclick.toString().includes(sectionName)
    );
    if (currentNavLink) {
        currentNavLink.classList.add('active');
    }
    
    // Load progress data if showing progress section
    if (sectionName === 'progress') {
        loadProgressData();
    }
}

/**
 * Load progress data from backend
 */
async function loadProgressData() {
    try {
        const response = await fetch('/progress');
        if (response.ok) {
            // Progress page exists, we can redirect there
            // For now, just update local display
            updateProgressDisplay();
        }
    } catch (error) {
        console.error('Error loading progress:', error);
        updateProgressDisplay();
    }
}

/**
 * Update progress display with current data
 */
function updateProgressDisplay() {
    const totalSessions = document.getElementById('total-sessions');
    const avgImprovement = document.getElementById('avg-improvement');
    const currentStreak = document.getElementById('current-streak');
    
    if (totalSessions) {
        totalSessions.textContent = sessionData.sessions.length;
    }
    
    if (avgImprovement && sessionData.sessions.length > 0) {
        const improvements = sessionData.sessions
            .filter(s => s.mood_after && s.mood_before)
            .map(s => s.mood_after - s.mood_before);
        
        if (improvements.length > 0) {
            const avg = improvements.reduce((a, b) => a + b, 0) / improvements.length;
            avgImprovement.textContent = avg > 0 ? `+${avg.toFixed(1)}` : avg.toFixed(1);
        }
    }
    
    if (currentStreak) {
        // Simple streak calculation (consecutive days with sessions)
        currentStreak.textContent = calculateStreak();
    }
}

/**
 * Calculate current streak of consecutive days with sessions
 */
function calculateStreak() {
    if (sessionData.sessions.length === 0) return 0;
    
    const today = new Date();
    const sessions = sessionData.sessions.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
    
    let streak = 0;
    let currentDate = new Date(today);
    
    for (const session of sessions) {
        const sessionDate = new Date(session.timestamp);
        const daysDiff = Math.floor((currentDate - sessionDate) / (1000 * 60 * 60 * 24));
        
        if (daysDiff === streak) {
            streak++;
            currentDate.setDate(currentDate.getDate() - 1);
        } else if (daysDiff > streak) {
            break;
        }
    }
    
    return streak;
}

// Export functions for global access
window.generateStory = generateStory;
window.toggleAudio = toggleAudio;
window.shareStory = shareStory;
window.resetForm = resetForm;
window.showSection = showSection;

console.log('🎭 Echo-Muse JavaScript loaded successfully');