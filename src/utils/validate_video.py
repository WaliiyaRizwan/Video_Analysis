import os

# Function to validate if the file has a video extension
def VideoValidation(file_name: str) -> bool:
    video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".wmv"} 
    _, file_extension = os.path.splitext(file_name)
    return file_extension.lower() in video_extensions
