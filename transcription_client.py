import os
import boto3
import uuid
from datetime import datetime, timezone
from fastapi import HTTPException
import requests
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# AWS Configuration
AWS_REGION = os.getenv("AWS_REGION")
job_name = f"transcription-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:8]}"
TRANSCRIBE_CLIENT = boto3.client("transcribe", region_name=AWS_REGION)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Function to transcribe audio using AWS Transcribe
def transcribe_audio(s3_uri, job_name):
    try:
        TRANSCRIBE_CLIENT.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={"MediaFileUri": s3_uri},
            MediaFormat="wav",
            LanguageCode="en-US"
        )

        while True:
            response = TRANSCRIBE_CLIENT.get_transcription_job(TranscriptionJobName=job_name)
            status = response["TranscriptionJob"]["TranscriptionJobStatus"]
            if status in ["COMPLETED", "FAILED"]:
                break

        if status == "FAILED":
            raise HTTPException(status_code=500, detail="Transcription job failed")

        transcript_uri = response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
        return transcript_uri
    except Exception as e:
        logger.error(f"Error in transcription: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to transcribe audio")

# Function to fetch transcription text
def fetch_transcription_text(transcript_uri):
    response = requests.get(transcript_uri)
    transcript_json = response.json()
    return transcript_json["results"]["transcripts"][0]["transcript"]

