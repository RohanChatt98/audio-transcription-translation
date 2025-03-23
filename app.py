import os
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import logging
import uuid
from S3_client import upload_to_s3
from transcription_client import transcribe_audio,fetch_transcription_text
from llm import analyze_text_with_groq

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# FastAPI App
app = FastAPI()

@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Save file locally
        file_path = f"temp_{uuid.uuid4().hex}.mp3"
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Upload to S3
        s3_uri = upload_to_s3(file_path, file.filename)
        #os.remove(file_path)

        # Start Transcription
        job_name = f"transcription-{uuid.uuid4().hex}"
        transcript_uri = transcribe_audio(s3_uri, job_name)

        # Fetch Transcription Text
        transcript_text = fetch_transcription_text(transcript_uri)

        # Analyze text using Groq (Mistral) with LangChain
        summary, sentiment = analyze_text_with_groq(transcript_text)

        return {
            "transcription": transcript_text,
            "summary": summary,
            "sentiment": sentiment
        }
    except Exception as e:
        logger.error(f"Error processing audio: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing audio")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

