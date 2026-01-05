"""Configuration and API setup for WhatsApp Auto Reply Bot"""

import google.generativeai as genai
import os

# User Configuration
MY_NAME = "ayush singh"  # Your WhatsApp name
MAX_REPLIES = 10  # Maximum replies before stopping
REPLY_DELAY = 10  # Seconds to wait between replies

# Screen Coordinates (adjust for your screen resolution)
WHATSAPP_WINDOW_CLICK = (478, 1043)
CHAT_START_POS = (725, 135)
CHAT_END_POS = (1840, 923)
INPUT_BOX = (1597, 980)
SEND_BUTTON = (1862, 968)

# Gemini API Configuration
def setup_gemini_api(api_key=None):
    """Initialize Gemini API with provided or environment API key"""
    if api_key is None:
        api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not provided or set in environment")
    
    genai.configure(api_key=api_key)
    return genai

# Gemini Model Configuration
GEMINI_MODEL = "gemini-1.5-flash"
GENERATION_CONFIG = {
    "temperature": 0.7,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40,
}

# Prompt Template
AI_PROMPT_TEMPLATE = """You are texting like Ayush, replying briefly and sarcastically sometimes in Hindi+English.
Analyze the chat history and write the next message that Ayush would realistically send, don't use sarcasm a lot.
ONLY reply with the text message (no quotes, no extra words).

Chat:
{chat_history}"""
