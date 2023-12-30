# FastAPI Video Analysis

This project is a FastAPI application that allows users to upload video files, extract audio, transcribe it using OpenAI's Whisper model, and analyze the transcriptions for the presence of specified "bad words." The project provides a REST API for handling video uploads and analyzing the audio.

## Features

- **Video Upload:** Upload one or more video files for analysis.
- **Audio Extraction:** Extract audio from the uploaded videos.
- **Transcription:** Transcribe the extracted audio using OpenAI's Whisper model.
- **Bad Word Analysis:** Count occurrences of specified "bad words" in the transcriptions.
- **Error Handling:** Proper error handling for file validation, transcription, and other potential errors.

## Requirements

- Python 3.10 or later
- FastAPI
- MoviePy
- Requests
- git+https://github.com/openai/whisper.git 
- ffmpeg

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WaliiyaRizwan/Exercise-FASTAPI.git

## Working 
1. ### Run the App:
   This command runs the application using the Python script server.py. After running the server, you can access the video uploading API at the specified URL.
   ```bash
   python server.py

   http://127.0.0.1:5001/api/video/bad-word-count/
   
2. ### Video Uploading and Validation:
   This code snippet handles the uploading and validation of video files. It iterates through the uploaded files, checks if they have valid video extensions, and saves them temporarily.
   ### Upload
   ```
   for file in files:
        try:
            # Validate that the uploaded file has a video extension
            if not VideoValidation(file.filename):
                raise HTTPException(status_code=400, detail=f"Invalid file type. Please upload a video file. ({file.filename})")

            # Save the video file temporarily
            video_path = file.filename
            with open(video_path, "wb") as buffer:
                buffer.write(file.file.read())
   ```
   ### Validation
   ```
   def VideoValidation(file_name: str) -> bool:
       video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".wmv"} 
       _, file_extension = os.path.splitext(file_name)
       return file_extension.lower() in video_extensions
   ```

3. ### Audio Extraction:
   This function extracts audio from a video file using the MoviePy library. It takes the path of the input video and the desired output path for the audio file.
   ```
   def extract_audio(video_path: str, output_path: str):
       video_clip = VideoFileClip(video_path)
       audio_clip = video_clip.audio
       audio_clip.write_audiofile(output_path)
       video_clip.close()
       return output_path
   ```
    
4. ### Transcription:
   This code segment uses the Whisper model to transcribe the text from an audio file. 
   ```
   model = whisper.load_model("base", device=DEVICE)

   def extract_text(audio_file):
       result = model.transcribe(audio_file)
       return result["text"]
   ```
5. ### Bad Word Analysis:
   Here, a list of "bad words" is defined, and a dictionary is created to count the occurrences of these words in a given text. Adjust the list of bad words as needed for your specific use case.
   ```
   # Save the bad words file
       bad_words_path = os.path.join(UPLOADS_DIR, bad_words_file.filename)
       with open(bad_words_path, "wb") as buffer:
           buffer.write(bad_words_file.file.read())

       bad_words = load_bad_words(bad_words_path)

       bad_word_counts = {word: text.lower().count(word) for word in bad_words}
   ```

## Response:
I tested the route in postman on a short funny clip of "Mind your Language". Here is how the response looks like:

```
   [
    {
        "message": "Audio analyzed successfully for videoplayback.mp4.",
        "audio_file_path": "videoplayback.mp3",
        "transcript": " and ask you to identify them and we'll see how well you do, alright? Who should we start with, Ellie? Yes please. What is this? Apple! Yeah. Loverly, you're not supposed to eat it. I'm more sorry, I only had a small bite. You're as well finished now. Sully, what is this? It is orange. Orange. All rings. That's better. You really must work at those arsehs. It's like very hard. Tri-sing round the ragged rock, the ragged rascal of rock. Lown the luggled block, the luggled block. Yes, you're going to have to keep practicing. Anna, what is this? Paper bag. Yes. Yes, but what's inside it? Well no, I cannot see inside. It's flour, you know, flour is. Yeah, but you're there to vending. No, no, it's not that kind of flour. This is flour to make pastry and bread. Ah, vice-male. It is. Gemilla? What is this? Garde. So I'm sure you're right, but what is it in English? I don't know. Have you never heard of a carrot? Garde. Yes, carrot. Oh, ha! Horace and Garde. No, no, no, Gemilla, that's horse and cart. This is a carrot. Who can tell me what these are? Fish fingers. Good. No, excuse please. No, they don't say it. What do I even say? You were going to say something about fish not having fingers? Yes, please. They were don't know. Mark. Tomaco. Good. Tarot. Potato. Potato. Ah, so. Juan. Giovanni. I like my juice. Good. One cow juice. No. Milk. Ah, see, really. You know where we catch milk from, Fond? Cisignola. Debic, Mond. Quiet, please, we get milk from cows. See, Baka. Cow. Run, Gitch. Cornflakes? No, oats. Oh, that is oats. My friend, who I am working with, every morning he's telling me, last night he's having his oats. He's telling me he's writing down very much. No, I'm sure he does. Who can tell me what this is? Baka. Good. Baka, come from. And a milkman. Baka does not come from the milk. Every week I buy the bacon from the milkman. Peek. Peek. Peek. You are polypig. You are a pig. You Italian. Ravioli. Ah, shut your plates up and eat your doughnuts. I don't like how they do. Juan, what Giovanni was trying to say is that Baka comes from a pig. Sora. No, can anyone tell me what we call a pig after it has been killed? Yes, please. It is a dead pig. Please. No, Ravioli, you know that's pork. Right. What is this? Anybody? Pinoch meat. Yes. Well, actually it's a tin of dog meat. Or blyme. I was putting dogs in tins to it. I think I've heard enough. They are better than they were. They could hardly be worse.",
        "bad_word_counts": {
            "tomaco": 1,
            "tarot": 1,
            "tell": 5,
            "ask": 1,
            "bite": 1,
            "orange": 2,
            "carrot": 3
        }
    }
]

```
