import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LangChain with Groq Llama3
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="Llama-3.2-3B-preview"
)


# Function to translate text to Hindi using LangChain and Groq's Llama3
def translate_to_hindi(text: str):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Translate the following text to Hindi: {text}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    translation = chain.run(text)
    return translation
