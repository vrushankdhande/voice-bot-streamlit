# 🎤 Cloud-Ready Voice Bot using Streamlit

An interactive **AI Voice Bot** built with **Python + Streamlit** that allows users to:

- 🎙️ Record voice directly from the browser  
- 🧠 Convert speech to text using Google Speech Recognition  
- 🤖 Generate chatbot responses  
- 🔊 Convert bot replies back into speech using Google Text-to-Speech (gTTS)  

This project demonstrates the complete workflow of a **Speech-to-Text → AI Response → Text-to-Speech** pipeline in a simple and cloud-ready web application.

---

# 🚀 Features

✅ Browser-based voice recording  
✅ Real-time speech transcription  
✅ AI chatbot response generation  
✅ Text-to-speech audio playback  
✅ Streamlit-powered interactive UI  
✅ Easy deployment on cloud platforms  

---

# 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **SpeechRecognition**
- **gTTS (Google Text-to-Speech)**
- **audio-recorder-streamlit**

---

# 📂 Project Workflow

```text
User Voice Input
        ↓
Audio Recorder (Browser)
        ↓
Speech-to-Text Conversion
        ↓
Bot Response Generation
        ↓
Text-to-Speech Conversion
        ↓
Audio Response Playback
```

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/vrushankdhande/voice-bot-streamlit.git

cd voice-bot-streamlit
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit
pip install SpeechRecognition
pip install gtts
pip install audio-recorder-streamlit
```

---

# ▶️ Run the Application

```bash
streamlit run voice_bot.py
```

---

# 🎯 How It Works

## 🎙️ Audio Recording
The application records audio directly from the browser using:

```python
audio_recorder_streamlit
```

---

## 🧠 Speech Recognition
The recorded audio is converted into text using:

```python
speech_recognition
```

Google's free speech recognition API is used for transcription.

---

## 🤖 Bot Response
A simple keyword-based chatbot generates responses.

Example:

```python
if "hello" in user_text_lower:
    return "Hello there! How can I help you today?"
```

This logic can easily be replaced with:

- OpenAI GPT
- Gemini AI
- Claude AI
- LangChain
- RAG pipelines

---

## 🔊 Text-to-Speech
Bot responses are converted back into speech using:

```python
gTTS
```

The generated MP3 audio is then played in Streamlit.

---

# 📸 Output Preview

### User Interaction Flow

```text
🎤 User Speaks
↓
📝 Speech Transcribed
↓
🤖 Bot Generates Reply
↓
🔊 Voice Response Played
```

---

# 🌐 Cloud Deployment

This project is cloud-ready and can be deployed on:

- Streamlit Cloud
- Render
- Railway
- Hugging Face Spaces
- AWS / GCP / Azure

---

# 🔮 Future Improvements

- Integrate OpenAI/Gemini APIs
- Add multilingual support
- Real-time streaming transcription
- Memory-enabled conversations
- Voice selection options
- RAG-based chatbot
- Emotion-aware responses

---

# 📊 Use Cases

- AI Voice Assistants
- Customer Support Bots
- Accessibility Applications
- Voice-enabled AI Agents
- Educational Chatbots
- Smart Automation Systems

---

# 💡 Key Learning Outcomes

This project demonstrates:

- Speech-to-Text Systems
- Audio Processing
- Conversational AI
- Streamlit App Development
- Text-to-Speech Synthesis
- End-to-End AI Workflow Integration

---

# 🧑‍💻 Author

**Vrushank Dhande**  
Data Science | Machine Learning | AI Automation | Python Developer

---

# 🔖 LinkedIn Post Caption

🚀 Built a Cloud-Ready AI Voice Bot using Python & Streamlit 🎤🤖

This project can:
✅ Record voice from browser  
✅ Convert speech to text  
✅ Generate chatbot responses  
✅ Convert responses back into speech  

Tech Stack:
Python | Streamlit | SpeechRecognition | gTTS

A simple yet powerful example of an end-to-end Voice AI pipeline.

#Python #AI #MachineLearning #Streamlit #VoiceBot #SpeechRecognition #GenerativeAI #DataScience #Automation #OpenAI
