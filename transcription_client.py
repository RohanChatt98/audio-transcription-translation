import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to transcribe audio using OpenAI Whisper
def transcribe_audio(file_path: str):
    """Transcribes audio to text using OpenAI Whisper."""
    try:
        with open(file_path, "rb") as audio_file:
            response =  openai.audio.transcriptions.create(
                model="whisper-1", file=audio_file, language="en"
            )
        return response["text"]
    except Exception as e:
        raise Exception(f"Error transcribing audio: {str(e)}")
