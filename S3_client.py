import os
import boto3
from dotenv import load_dotenv
import logging
from fastapi import HTTPException

# Load environment variables
load_dotenv()
# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")

S3_CLIENT = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_REGION)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Function to upload audio to S3
def upload_to_s3(file_path, file_name):
    try:
        S3_CLIENT.upload_file(file_path, S3_BUCKET, file_name)
        s3_uri = f"s3://{S3_BUCKET}/{file_name}"
        return s3_uri
    except Exception as e:
        logger.error(f"Error uploading to S3: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to upload file to S3")
