import whisper
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)


def extract_text(audio_file):
    result = model.transcribe(audio_file)
    return result["text"]
