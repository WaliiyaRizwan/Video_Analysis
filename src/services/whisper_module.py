import whisper
import torch 
from tempfile import NamedTemporaryFile

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)

def TextExtraction(audio_file):
    result = model.transcribe(audio_file)
    return result["text"]