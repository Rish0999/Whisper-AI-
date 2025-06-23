# Whisper AI Transcription App

Welcome to the Whisper AI Transcription App. This application allows you to transcribe audio files into text using OpenAI's Whisper model.
This project was made by Rishit Mohan, Rhea Bhatia and Arin Pramod Singla.
---

## Features

- Supports MP3 and WAV files
- Converts audio to 16kHz mono for Whisper compatibility
- Displays the transcribed text
- Allows download of the transcript as `.srt`

---

## Required Libraries

- `streamlit` – for the web interface
- `whisper` – OpenAI's transcription model
- `librosa` – for audio processing
- `torch` – for tensor conversion
- `numpy` – array operations
- `tempfile` – to save temporary audio files

---

## Sample Workflow

1. User uploads an audio file (MP3/WAV)
2. File is validated and saved temporarily
3. Librosa loads the audio at 16kHz mono
4. Audio converted to a Torch tensor
5. Whisper transcribes the audio
6. Text is displayed and available for download

---

## Example

**Uploaded File:** `example.wav`  
**Transcription Output:**  
`"This is a sample transcription of the audio content."`

---

*Thank you for using the Whisper AI Transcription App!*
