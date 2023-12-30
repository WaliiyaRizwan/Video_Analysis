from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from src.utils.validate_video import VideoValidation
from src.utils.audio_extraction import extract_audio
from src.services.whisper_module import extract_text
from src.utils.load_words import load_bad_words
import os

app = router = APIRouter(prefix="/video")

# Specify the directory to store uploaded files
UPLOADS_DIR = "uploads"

# Create the directory if it doesn't exist
os.makedirs(UPLOADS_DIR, exist_ok=True)

# Endpoint for multiple video file uploads
@app.post("/bad-word-count/")
async def upload_videos(files: list[UploadFile] = File(...), bad_words_file: UploadFile = File(...)):
    # Save the bad words file
    bad_words_path = os.path.join(UPLOADS_DIR, bad_words_file.filename)
    with open(bad_words_path, "wb") as buffer:
        buffer.write(bad_words_file.file.read())

    bad_words = load_bad_words(bad_words_path)
    
    result = []

    for file in files:
        try:
            # Validate that the uploaded file has a video extension
            if not VideoValidation(file.filename):
                raise HTTPException(status_code=400, detail=f"Invalid file type. Please upload a video file. ({file.filename})")

            # Save the video file temporarily
            video_path = file.filename
            with open(video_path, "wb") as buffer:
                buffer.write(file.file.read())

            # Set the output audio file path
            audio_name = video_path.split(".")[0]
            audio_path = f"{audio_name}.mp3"

            # Extract audio from the video
            path = extract_audio(video_path, audio_path)

            text = extract_text(audio_path)

            # Count occurrences of bad words in the transcription
            bad_word_counts = {word: text.lower().count(word) for word in bad_words}

            result.append({
                "message": f"Audio analyzed successfully for {file.filename}.",
                "audio_file_path": audio_path,
                "transcript": text,
                "bad_word_counts": bad_word_counts
            })

        except HTTPException as e:
            # Handle FastAPI HTTPExceptions
            result.append({
                "message": f"Error analyzing {file.filename}: {e.detail}",
                "audio_file_path": None,
                "transcript": None,
                "bad_word_counts": None
            })

        except Exception as e:
            # Handle other exceptions
            result.append({
                "message": f"Unexpected error analyzing {file.filename}: {str(e)}",
                "audio_file_path": None,
                "transcript": None,
                "bad_word_counts": None
            })
        finally:
            if os.path.exists(video_path):
                os.remove(video_path)
            if os.path.exists(audio_path):
                os.remove(audio_path)

    return result
