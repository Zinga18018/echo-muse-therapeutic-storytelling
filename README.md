# 🎭 Echo-Muse: AI-Powered Therapeutic Storytelling Companion

*Personalized healing through the power of AI-generated stories and ambient soundscapes*

![Echo-Muse Main Interface](sc/{5BCD52CE-60F3-430D-87A5-EEA95B171106}.png)

## 🌟 Overview

Echo-Muse is an innovative therapeutic storytelling application that combines the power of AI-generated narratives with carefully crafted ambient soundscapes to create a personalized healing experience. Built with Flask and powered by Google's Gemini AI, this application offers users a unique approach to emotional wellness through interactive storytelling.

## ✨ Key Features

### 🎨 Personalized Story Generation
- **AI-Powered Narratives**: Utilizes Google Gemini Pro to create unique, therapeutic stories tailored to individual emotional states
- **Therapeutic Techniques Integration**: Incorporates evidence-based approaches including:
  - Cognitive Behavioral Therapy (CBT) themes
  - Mindfulness and grounding techniques
  - Narrative therapy principles
  - Self-compassion and empowerment themes

### 🎵 Adaptive Ambient Soundscapes
- **8 Unique Soundscape Types**:
  - 🌲 **Forest Dawn**: Grounding bird songs and nature awakening (174Hz, 285Hz, 396Hz)
  - 🌊 **Ocean Waves**: Calming rhythmic wave patterns (256Hz, 384Hz, 432Hz)
  - 🏔️ **Mountain Wind**: Energizing mountain breezes and echoes (341Hz, 512Hz, 639Hz)
  - 🌸 **Garden Bloom**: Healing garden ambiance with soft breezes (285Hz, 528Hz, 741Hz)
  - 💎 **Crystal Cave**: Mystical crystal harmonics (432Hz, 528Hz, 639Hz)
  - 🌧️ **Rain Meditation**: Peaceful rain on leaves (174Hz, 396Hz, 528Hz)
  - 🔥 **Fireplace Warmth**: Comforting crackling fireplace (256Hz, 341Hz, 432Hz)
  - ⭐ **Starlight Journey**: Transcendent cosmic harmonies (528Hz, 639Hz, 741Hz)

### 🎼 Advanced Audio Technology
- **Harmonious Frequencies**: Uses musical intervals and Solfeggio frequencies for optimal therapeutic effect
- **Web Audio API Integration**: Real-time audio generation with sine wave oscillators and gentle filtering
- **Intelligent Soundscape Matching**: Automatically recommends ambient sounds based on story content

### 📊 Progress Tracking & Session Management
- **Mood Monitoring**: Before and after session mood tracking (1-10 scale)
- **Session History**: Complete record of all therapeutic sessions with timestamps
- **Story Sharing**: Easy sharing functionality for meaningful narratives
- **Session Persistence**: Save and revisit important therapeutic moments

## 🖥️ User Interface

### Welcome & Input Interface
![User Input Interface](sc/{AE1F577F-85A4-4663-8F7D-71C9AF314774}.png)

The clean, intuitive interface features:
- **Personalized Greeting**: Customizable name input for a personal touch
- **Mood Assessment Slider**: Visual mood rating system (1-10) with emoji indicators
- **Thought Sharing Area**: Safe space to express current feelings and concerns
- **Story Generation Button**: One-click access to personalized therapeutic content

### Story Experience & Audio Controls
![Story Display and Audio Controls](sc/{E33260B6-0E49-4936-A88A-3677A150E848}.png)

The immersive story experience includes:
- **Beautiful Story Display**: Optimized typography for comfortable reading
- **Integrated Audio Controls**: Play/pause ambient soundscapes that complement your story
- **Session Management**: Save and revisit meaningful stories
- **Progress Updates**: Post-story mood assessment to track emotional improvement

## 🛠️ Technology Stack

### Backend Architecture
- **Python Flask Framework**: Robust web application foundation
- **Google Gemini AI Integration**: Advanced natural language processing for story generation
- **SQLite Database**: Lightweight session and progress data storage
- **Therapeutic Story Generator Class**: Specialized AI prompt engineering for healing narratives
- **Ambient Sound Generator Class**: Intelligent soundscape recommendation system

### Frontend Technology
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox
- **Web Audio API**: Real-time audio synthesis and processing
- **Vanilla JavaScript**: Progressive enhancement for accessibility
- **Local Storage Integration**: Client-side session persistence

### Audio Engineering
- **Harmonic Frequency Selection**: Carefully chosen frequencies based on:
  - Musical theory (perfect fifths, octaves, major triads)
  - Solfeggio frequencies (174Hz, 285Hz, 396Hz, 432Hz, 528Hz, 639Hz, 741Hz)
  - Therapeutic sound research
- **Dynamic Audio Generation**: Real-time oscillator creation with frequency modulation

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Google Generative AI library
- Modern web browser with Web Audio API support

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd echo-muse
   ```

2. **Install dependencies**:
   ```bash
   pip install flask google-generativeai
   ```

3. **Configure API Key**:
   - Obtain a Google Gemini API key
   - Update the `API_KEY` variable in `app.py`

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open your browser to `http://localhost:5000`
   - Begin your therapeutic storytelling journey

## 📁 Project Structure

```
echo-muse/
├── app.py                 # Main Flask application
├── static/
│   ├── css/
│   │   └── style.css     # Application styling
│   └── js/
│       └── app.js        # Frontend JavaScript
├── templates/
│   └── index.html        # Main HTML template
├── sc/                   # Screenshots for documentation
│   ├── {5BCD52CE...}.png # Main interface screenshot
│   ├── {AE1F577F...}.png # User input screenshot
│   └── {E33260B6...}.png # Story display screenshot
├── sessions.db           # SQLite database (auto-created)
└── README.md            # This documentation
```

## 🎯 Therapeutic Approach

Echo-Muse employs evidence-based therapeutic techniques:

- **Narrative Therapy**: Helps users reframe their experiences through storytelling
- **Cognitive Behavioral Therapy**: Incorporates positive thought patterns and coping strategies
- **Mindfulness Integration**: Combines stories with ambient sounds for present-moment awareness
- **Bibliotherapy**: Uses therapeutic reading as a healing modality
- **Sound Therapy**: Leverages specific frequencies known to promote relaxation and healing

## 🌈 Use Cases

- **Daily Stress Relief**: Quick therapeutic stories for everyday challenges
- **Anxiety Management**: Grounding narratives with calming soundscapes
- **Sleep Preparation**: Peaceful stories with gentle ambient sounds
- **Emotional Processing**: Safe space to explore feelings through guided narratives
- **Mindfulness Practice**: Combining storytelling with meditative audio experiences
- **Creative Inspiration**: Unique stories that spark imagination and hope

## 💫 How to Use Echo-Muse

### Getting Started

1. **Enter Your Name**: Personalize your experience with a custom greeting
2. **Share Your Feelings**: Describe what's on your mind in the text area - be as detailed or brief as you'd like
3. **Rate Your Current Mood**: Use the mood slider to indicate how you're feeling (1-10 scale)
4. **Generate Your Story**: Click "Crafting your story..." and let Echo-Muse create a personalized therapeutic narrative
5. **Experience the Journey**: Read your story while ambient sounds create a calming atmosphere
6. **Track Your Progress**: Rate your mood after the session to see your emotional improvement

### Advanced Features

- **Audio Controls**: Toggle ambient soundscapes on/off during story reading
- **Session Saving**: Save meaningful stories for future reference
- **Story Sharing**: Share inspiring narratives with others (anonymously)
- **Progress Tracking**: View your emotional journey over time in the Progress section

## 🔒 Privacy & Safety

- **Local Data Storage**: All personal information stays on your device
- **No Personal Data Transmission**: Stories are generated without storing personal details
- **Session Anonymization**: User sessions are stored with anonymous identifiers
- **Therapeutic Disclaimer**: This tool is designed for wellness support, not as a replacement for professional mental health care

## 🔮 Future Enhancements

- **Voice Narration**: AI-generated voice reading of stories
- **Binaural Beats**: Advanced audio therapy integration
- **Guided Meditation**: Interactive meditation sessions
- **Community Features**: Anonymous story sharing (with consent)
- **Therapist Integration**: Tools for mental health professionals
- **Mobile App**: Native iOS and Android applications
- **Multi-language Support**: Therapeutic stories in multiple languages

## 🤝 Contributing

We welcome contributions to make Echo-Muse even more effective as a therapeutic tool. Please consider:

- **Therapeutic Expertise**: Mental health professionals' insights
- **Audio Engineering**: Sound therapy and frequency research
- **Accessibility**: Making the tool available to all users
- **Localization**: Translating therapeutic content
- **User Experience**: Interface and interaction improvements

## 📄 License

This project is created for therapeutic and educational purposes. Please ensure any use aligns with ethical guidelines for mental health applications.

## 🙏 Acknowledgments

- **Google Gemini AI**: For powerful natural language generation
- **Web Audio API**: For enabling real-time audio synthesis
- **Therapeutic Community**: For research and insights into healing through storytelling
- **Open Source Community**: For the tools and libraries that make this possible

---

*"In every story lies the seed of healing, and in every sound, the echo of peace."*

**Echo-Muse** - Where technology meets therapy, and stories become medicine. 🎭✨

## ⚠️ Important Disclaimer

**Echo-Muse is a complementary tool for emotional well-being and is not a substitute for professional mental health care.** If you're experiencing severe depression, anxiety, or other mental health concerns, please consult with a qualified mental health professional.

**Crisis Resources:**
- National Suicide Prevention Lifeline: 988
- Crisis Text Line: Text HOME to 741741
- International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the language model that powers our storytelling
- **The therapeutic community** for decades of research into healing through narrative
- **Open source contributors** who make projects like this possible
- **Beta testers** who helped refine the user experience

## 📞 Support

Need help or have questions?

- **Documentation**: Check our [Wiki](https://github.com/your-username/echo-muse/wiki)
- **Issues**: Report bugs or request features in our [Issue Tracker](https://github.com/your-username/echo-muse/issues)
- **Discussions**: Join conversations in our [Discussions](https://github.com/your-username/echo-muse/discussions)

---

*"In every story, there is a seed of healing. In every narrative, a path to wholeness."*

**Created with 💜 for healing and hope.**