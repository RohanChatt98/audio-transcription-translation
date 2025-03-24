
# Audio Transcription and Summarization

This project provides an API that allows users to upload audio files, transcribe them into text using OpenAI Whisper, and get summarized version of the transcriptions in hindi. The backend is built using FastAPI, and OpenAI's API is used for transcription and analysis.

## Features

- **Audio Transcription:** Transcribe audio files to text using OpenAI Whisper API.
- **Summarization:** After transcription, the text can be processed for summarization(implemented with a separate service, e.g., Llama 3.2).
- **Real-time Processing:** Upload audio files to be transcribed and processed immediately.
- **Easy to Integrate:** This API can be easily integrated with other systems to transcribe and analyze audio interactions.

## Requirements

- Python 3.10 or higher
- `FastAPI` for the backend API
- `openai` Python package for OpenAI API access
- `dotenv` for managing environment variables
- `uvicorn` for running the FastAPI server

## Installation

### Step 1: Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
```

### Step 3: Activate the virtual environment

- For Windows:
    ```bash
    venv\Scripts\activate
    ```

- For MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Set up your OpenAI API Key

1. Create a `.env` file in the root of the project directory.
2. Add your OpenAI API key as follows:

```bash
OPENAI_API_KEY=your_openai_api_key
```

You can get your OpenAI API key from the [OpenAI API platform](https://platform.openai.com/account/api-keys).

## Usage

### Starting the Server

After installing the dependencies and setting up the environment variables, you can start the FastAPI server:

```bash
uvicorn app:app --reload
```

This will start the server on `http://127.0.0.1:8000`.

### API Endpoints

1. **POST /transcribe**
   - Upload an audio file (e.g., MP3, WAV) to be transcribed.
   - **Request Body:**
     - `file`: The audio file to transcribe (multipart/form-data).
   - **Response:**
     - Returns the transcribed text in JSON format.

Example Request:
```bash
curl -X 'POST'   'http://127.0.0.1:8000/transcribe'   -F 'file=@path_to_your_audio_file.mp3'
```

Example Response:
```json
{
  "transcription": "This is the transcribed text of the audio file."
}
```

## Contributing

We welcome contributions to improve this project. You can contribute by:

- Forking the repository.
- Creating a new branch (`git checkout -b feature-xyz`).
- Making your changes and committing them (`git commit -am 'Add feature xyz'`).
- Pushing your changes (`git push origin feature-xyz`).
- Creating a pull request.

## License

This project is licensed under the Apache License Version 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing Whisper API .
- Groq for providing Llama-3.2-3B-preview 
- FastAPI for building the backend API.
- Uvicorn for fast and efficient ASGI server.

For any further issues, feel free to open an issue in the GitHub repository.
