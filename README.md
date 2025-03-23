
# Audio Transcription & Summarization API

This project leverages the power of AWS Transcribe for real-time transcription, Groq for language models, and FastAPI to create a fast and scalable web application. The system listens for audio files, processes them to generate transcriptions, summarizes the transcribed text, and translates the summary into Hindi, all through a simple API.

## Features

- **Audio Transcription**: Automatically transcribes audio files to text using AWS Transcribe.
- **Summarization**: Generates a concise summary of the transcription.
- **Translation**: Translates the summary into Hindi for multilingual support.
- **Real-time Processing**: Processes audio files in real-time, providing rapid feedback.
- **FastAPI Backend**: Provides a high-performance API layer for integration with other systems.

## Architecture Overview

1. **AWS Transcribe**: Used to transcribe audio files into text.
2. **Groq API**: Utilizes advanced language models to process the transcriptions for summarization and translation.
3. **FastAPI**: A fast and efficient Python web framework used for creating the API endpoints.
4. **S3 Bucket**: Used to store and retrieve audio files for processing.
5. **Logging and Error Handling**: Built-in logging and error handling ensure smooth operation and troubleshooting.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

1. **Python 3.10+**: Ensure Python 3.10 or later is installed.
2. **AWS Account**: You need an AWS account with access to Transcribe and S3.
3. **Groq API Key**: Obtain a Groq API key to use their language models for summarization and translation.

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/RohanChatt98/audio-transcription-summary.git
cd audio-transcription-summary
```

### Step 2: Set Up the Environment

1. Create a `.env` file in the root directory and add your AWS and Groq API keys:

```
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=us-east-1
S3_BUCKET=your-s3-bucket-name
GROQ_API_KEY=your-groq-api-key
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Run the FastAPI application locally using `uvicorn`:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Step 4: Test the API

To test the API, send a `POST` request to `/upload_audio/` with an audio file. You can use tools like `curl` or Postman.

#### Example using `curl`:

```bash
curl -X 'POST'   'http://127.0.0.1:8000/upload_audio/'   -H 'accept: application/json'   -H 'Content-Type: multipart/form-data'   -F 'file=@path_to_audio_file.wav;type=audio/wav'
```

### Step 5: Get the Response

After uploading the audio file, the API will return a JSON response with the transcription, summary, and translation.

```json
{
  "transcription": "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot cross bun.",
  "summary": "Translation:",
  "sentiment": "तले हुए स्वाद का गंध पुराने पीले बियर का ही होता है। उसे गर्मी से उबरने में ही इसका स्वाद आता है। ठंडी डीप से स्वास्थ्य और जोश को रोका जा सकता है। स्वादिष्ट नमक की टमाटर अच्छा है हाम से। टैकोस अल पास्तोर मेरे पसंदीदा हैं। एक ताज़ा खाना होट क्रॉस बन बहुत स्वादिष्ट है।"
}
```

## API Endpoints

### `POST /upload_audio/`

Uploads an audio file and returns its transcription, summary, and translation.

#### Request Body:
- **file**: The audio file in `.wav` format.

#### Response:
- **transcription**: The transcribed text of the audio.
- **summary**: The summary of the transcribed text.
- **sentiment**: The translation of the summary into Hindi.

---

## Development and Contributions

Feel free to fork this project and submit pull requests. Here are some areas where you could contribute:

- Add support for more file formats (e.g., MP3, OGG).
- Improve error handling for file uploads.
- Integrate additional LLMs for better summarization.

### Running Tests

To run tests (if any), use:

```bash
pytest
```

### Code Style

Please follow **PEP8** standards and add docstrings for new functions.

## License

This project is licensed under the Apache Licence version 2.0.

---

## Contact

For any questions or suggestions, feel free to reach out to:

- **Your Name**: [Rohan Chatterjee]
- **Email id**: [rohan.chattrji@gmail.com]
