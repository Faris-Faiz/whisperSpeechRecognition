import streamlit as st
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import sounddevice as sd
import numpy as np
import threading
import queue
import time  # Add this import statement

# Load the Whisper model
@st.cache_resource
def load_model():
    processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")
    return processor, model

processor, model = load_model()

# Function to record audio
def record_audio(duration, sample_rate, q):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    q.put(recording)

# Function to transcribe audio
def transcribe_audio(audio, sample_rate):
    try:
        input_features = processor(audio, sampling_rate=sample_rate, return_tensors="pt").input_features
        
        # Force English language output
        forced_decoder_ids = processor.get_decoder_prompt_ids(language="en", task="transcribe")
        
        predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription[0]
    except Exception as e:
        st.error(f"Error during transcription: {str(e)}")
        return None

# Streamlit UI
st.title("Speech Recognition App")

st.write("Click the button below to start recording your voice:")

if st.button("🎤 Record"):
    duration = 5  # Recording duration in seconds
    sample_rate = 16000  # Sample rate for Whisper model

    # Create a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Use a queue to get the recording from the thread
    q = queue.Queue()

    # Start recording in a separate thread
    recording_thread = threading.Thread(target=record_audio, args=(duration, sample_rate, q))
    recording_thread.start()

    # Update progress bar
    for i in range(duration):
        status_text.text(f"Recording: {i+1} seconds...")
        progress_bar.progress((i + 1) / duration)
        time.sleep(1)

    recording_thread.join()
    status_text.text("Processing audio...")

    # Get the recording from the queue
    audio = q.get().flatten()

    # Transcribe the audio
    transcription = transcribe_audio(audio, sample_rate)

    if transcription:
        st.success("Transcription complete!")
        st.write("Transcribed text:")
        st.write(transcription)
    else:
        st.error("Transcription failed. Please try again.")

st.write("---")
st.write("This app uses the Whisper model from Hugging Face to transcribe English speech to text.")
st.write("Make sure you have a working microphone connected to your device.")