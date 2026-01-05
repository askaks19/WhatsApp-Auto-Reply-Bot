"""Chat history parser module for extracting sender information from WhatsApp exports"""

def get_last_sender(chat_text: str):
    """
    Extract sender from the last chat line in WhatsApp format.
    WhatsApp exported line format: [time, date] Name: message
    
    Args:
        chat_text (str): The full chat history as a string
        
    Returns:
        str: Name of the last sender, or None if not found
    """
    lines = [line.strip() for line in chat_text.strip().split('\n') if line.strip()]
    
    if not lines:
        return None
    
    last_line = lines[-1]
    
    # WhatsApp exported line format: [time, date] Name: message
    if "]" in last_line and ":" in last_line:
        try:
            after_bracket = last_line.split("]", 1)[1].strip()  # "Name: message"
            sender = after_bracket.split(":", 1)[0].strip()  # "Name"
            return sender
        except Exception:
            return None
    
    return None

def should_reply(last_sender: str, my_name: str) -> bool:
    """
    Determine if we should reply based on who sent the last message.
    Skip if the last message is from ourselves.
    
    Args:
        last_sender (str): Name of the last sender
        my_name (str): Our WhatsApp name
        
    Returns:
        bool: True if we should reply, False if sender is us or no sender
    """
    if not last_sender:
        return False
    
    if last_sender.strip().lower() == my_name.strip().lower():
        return False
    
    return True
