import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from gtts import gTTS
import io

# --- Functions ---

def transcribe_audio(audio_bytes):
    """Converts audio bytes to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    
    try:
        with sr.AudioFile(audio_file) as source:
            # Read the audio data from the file
            audio_data = recognizer.record(source)
            # Transcribe using Google's free API
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Could not request results from the speech recognition service."
    except Exception as e:
        return f"An error occurred: {e}"

def get_bot_response(user_text):
    """
    Generates a text response from the bot. 
    You can replace this logic with an API call to Gemini, OpenAI, Claude, etc.
    """
    # Simple keyword-based mock bot for demonstration
    user_text_lower = user_text.lower()
    
    if "hello" in user_text_lower or "hi" in user_text_lower:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_text_lower:
        return "I am just a computer program, but I'm functioning perfectly. Thank you for asking!"
    elif "weather" in user_text_lower:
        return "I can't check the live weather yet, but I hope it's sunny wherever you are."
    elif "sorry" in user_text_lower:
        return "Please try speaking a bit closer to the microphone."
    else:
        return f"I heard you say: '{user_text}'. I am a simple bot right now, so I don't have a specific answer for that."

def text_to_speech(text):
    """Converts text back to audio using Google Text-to-Speech (gTTS)."""
    tts = gTTS(text=text, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    return audio_fp.getvalue()

# --- Streamlit UI ---

st.set_page_config(page_title="Voice Bot", page_icon="🎤")
st.title("🎤 Cloud-Ready Voice Bot")
st.write("Click the microphone to speak. The bot will transcribe your voice, reply, and speak back to you!")

# Client-side audio recorder widget
audio_bytes = audio_recorder(
    text="Click to record", 
    recording_color="#e81e1e", 
    neutral_color="#6aa36f"
)

if audio_bytes:
    # Play back the user's recording
    st.write("**You recorded:**")
    st.audio(audio_bytes, format="audio/wav")

    # Step 1: Transcribe
    with st.spinner("Transcribing..."):
        user_text = transcribe_audio(audio_bytes)
    
    st.success("Transcription Complete")
    st.write(f"🗣️ **You:** {user_text}")

    # Step 2: Get Bot Response
    with st.spinner("Bot is thinking..."):
        bot_response = get_bot_response(user_text)
    
    st.write(f"🤖 **Bot:** {bot_response}")

    # Step 3: Speak Response
    with st.spinner("Generating audio response..."):
        bot_audio_bytes = text_to_speech(bot_response)
        st.audio(bot_audio_bytes, format="audio/mp3", autoplay=True)
