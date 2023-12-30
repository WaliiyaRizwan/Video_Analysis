# FastAPI Video Analysis

This project is a FastAPI application that allows users to upload video files, extract audio, transcribe it using OpenAI's Whisper model, and analyze the transcriptions for the presence of specified "bad words." The project provides a REST API for handling video uploads and analyzing the audio.

## Features

- **Video Upload:** Upload one or more video files for analysis.
- **Audio Extraction:** Extract audio from the uploaded videos.
- **Transcription:** Transcribe the extracted audio using OpenAI's Whisper model.
- **Bad Word Analysis:** Count occurrences of specified "bad words" in the transcriptions.
- **Error Handling:** Proper error handling for file validation, transcription, and other potential errors.

## Requirements

- Python 3.7 or later
- FastAPI
- MoviePy
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-video-analysis.git
   cd fastapi-video-analysis
