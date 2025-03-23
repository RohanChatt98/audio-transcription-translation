# import os
# import logging
# from fastapi import HTTPException
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain.schema import HumanMessage

# # Load environment variables
# load_dotenv()

# # Groq API Configuration
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()

# # Initialize ChatGroq (LangChain wrapper for Groq)
# llm = ChatGroq(
#     groq_api_key=GROQ_API_KEY,
#     model_name="Llama-3.1-8b-Instant"
# )

# # Function to parse Groq response
# def parse_groq_response(response_text):
#     try:
#         lines = response_text.split("\n")
#         summary = lines[0].strip() if lines else "No summary available"
#         sentiment = lines[1].strip() if len(lines) > 1 else "Sentiment not detected"
#         return summary, sentiment
#     except Exception as e:
#         logger.error(f"Error parsing Groq response: {str(e)}")
#         return "No summary available", "Sentiment not detected"

# # Function to analyze text using LangChain + ChatGroq (Gemma-9b-It)
# def analyze_text_with_groq(text):
#     # prompt = f"""
#     # Given the following customer conversation:

#     # {text}

#     # 1. Summarize the conversation in a short paragraph.
#     # 2. Provide a sentiment analysis (Positive, Negative, or Neutral).
#     # """
#     prompt = f"""
#     Here is the transcription of the conversation: 
#     {transcription}

#     Please generate a **summary** of this transcription and classify the **sentiment** into 'Positive', 'Negative', or 'Neutral'. 
#     Provide the output in this format:

#     Summary: [summary]
#     Sentiment: [sentiment]
#     """


#     try:
#         response = llm.invoke([HumanMessage(content=prompt)])
#         result = response.content
#         summary, sentiment = parse_groq_response(result)
#         return summary, sentiment
#     except Exception as e:
#         logger.error(f"Error calling Groq LLM: {str(e)}")
#         raise HTTPException(status_code=500, detail="Error processing text with Groq")
    

import os
import logging
from fastapi import HTTPException
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize ChatGroq (LangChain wrapper for Groq) with Llama 3.2 3B-preview model
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="Llama-3.2-3B-preview"
)

# Function to parse Groq response (for both summary and translation)
def parse_groq_response(response_text):
    try:
        # Assuming the model gives us a single line for translation and one for summary
        lines = response_text.strip().split("\n")
        
        # If there are two lines: first is translation, second is summary
        if len(lines) == 2:
            translated_text = lines[0].strip()
            summary = lines[1].strip()
        else:
            translated_text = "No translation available"
            summary = "No summary available"

        return translated_text, summary
    except Exception as e:
        logger.error(f"Error parsing Groq response: {str(e)}")
        return "No translation available", "No summary available"

# Function to analyze text, translate to Hindi, and summarize it in English using Groq
def analyze_text_with_groq(text):
    prompt = f"""
    Here is the transcription of the conversation: 
    {text}

    Please do the following:
    1. Translate the conversation to Hindi.
    2. Summarize the conversation in a short paragraph in English.

    Please provide the output in the following format:
    Translation: [translated_text]
    Summary: [summary]
    """

    try:
        # Request translation and summarization from Llama 3.2 3B-preview model
        response = llm.invoke([HumanMessage(content=prompt)])
        result = response.content
        
        # Parse and return translated text and summary
        translated_text, summary = parse_groq_response(result)
        
        return translated_text, summary

    except Exception as e:
        logger.error(f"Error calling Groq LLM: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing text with Groq")
