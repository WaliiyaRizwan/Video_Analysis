from pydantic import BaseModel
from moviepy.editor import VideoFileClip


# Function to extract audio from a video file
def extract_audio(video_path: str, output_path: str):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    video_clip.close()
    return output_path