import os
import shutil
import uvicorn
from fastapi import FastAPI, File, UploadFile
from S3_client import upload_to_s3, download_from_s3
from transcription_client import transcribe_audio
from llm import translate_to_hindi

app = FastAPI()

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    """Handles audio transcription & translation."""
    
    # Save uploaded file locally
    local_file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(local_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Upload file to S3
    s3_key = f"audio/{file.filename}"
    s3_uri = upload_to_s3(local_file_path, s3_key)

    # Download file back (needed for Whisper)
    downloaded_path = os.path.join(UPLOAD_FOLDER, f"downloaded_{file.filename}")
    download_from_s3(s3_key, downloaded_path)

    # Transcribe audio using OpenAI Whisper
    transcription = transcribe_audio(downloaded_path)

    # Translate transcription to Hindi using LangChain and Groq's Llama3
    translation = translate_to_hindi(transcription)

    return {
        "transcription": transcription,
        "translation": translation
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)