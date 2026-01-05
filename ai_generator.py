"""AI Response generation module using Google Gemini API"""

import google.generativeai as genai
from config import GEMINI_MODEL, GENERATION_CONFIG, AI_PROMPT_TEMPLATE

def generate_response(chat_history: str) -> str:
    """
    Generate an AI response based on chat history using Google Gemini.
    
    Args:
        chat_history (str): The full chat history from WhatsApp
        
    Returns:
        str: The AI-generated response text
        
    Raises:
        Exception: If the API call fails
    """
    try:
        # Create prompt from template
        prompt = AI_PROMPT_TEMPLATE.format(chat_history=chat_history)
        
        # Initialize Gemini model
        model = genai.GenerativeModel(GEMINI_MODEL)
        
        # Generate content with specified configuration
        response = model.generate_content(
            prompt,
            generation_config=GENERATION_CONFIG
        )
        
        return response.text.strip()
        
    except Exception as e:
        print(f"Error generating AI response: {str(e)}")
        raise

def validate_response(response_text: str) -> bool:
    """
    Validate the generated response.
    
    Args:
        response_text (str): The response text to validate
        
    Returns:
        bool: True if response is valid, False otherwise
    """
    if not response_text or len(response_text.strip()) == 0:
        return False
    
    if len(response_text) > 500:  # WhatsApp message length limit
        return False
    
    return True
