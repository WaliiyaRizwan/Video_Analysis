from pydantic import BaseModel
from fastapi import UploadFile, File


class AudioExtractionResponse(BaseModel):
    message: str
    audio_file_path: str


class VideoUpload(BaseModel):
    files: list[UploadFile] = File(...)
