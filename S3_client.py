import os
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

def upload_to_s3(file_path, s3_key):
    """Uploads an audio file to S3."""
    s3_client.upload_file(file_path, S3_BUCKET, s3_key)
    return f"s3://{S3_BUCKET}/{s3_key}"

def download_from_s3(s3_key, local_path):
    """Downloads an audio file from S3."""
    s3_client.download_file(S3_BUCKET, s3_key, local_path)
    return local_path
