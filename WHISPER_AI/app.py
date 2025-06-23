import streamlit as st
import whisper
import librosa
import torch
import numpy as np
import tempfile

#  Whisper model
model = whisper.load_model("base")  # "tiny", "small", etc.

def transcribe(audio_file):
    file_extension = audio_file.name.split('.')[-1].lower()
    if file_extension not in ("mp3", "wav"):
        st.error("Unsupported audio format. Please upload MP3 or WAV files.")
        return None

    # Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:
        tmp.write(audio_file.read())
        temp_path = tmp.name

    # Load and process audio using librosa
    y, sr = librosa.load(temp_path, sr=16000, mono=True)  # Whisper expects 16kHz mono
    audio = torch.from_numpy(y).float()

    # Run Whisper's transcription
    result = model.transcribe(audio)
    return result["text"]

# Create download link
def download_link(text):
    filename = "transcript.srt"
    st.session_state.download_link = f"{text}"
    st.session_state.download_filename = filename
    return filename

# Streamlit App Logic
def main():
    st.title("Whisper AI Transcription App")

    uploaded_file = st.file_uploader("Upload MP3 or WAV file", type=["mp3", "wav"])

    if uploaded_file is not None:
        with st.spinner("Transcribing..."):
            transcript = transcribe(uploaded_file)

            if transcript:
                st.success("Transcription complete!")
                st.write(transcript)

                download_filename = download_link(transcript)
                st.download_button(
                    label="Download Transcript",
                    data=st.session_state.download_link,
                    file_name=download_filename
                )

if __name__ == "__main__":
    main()
