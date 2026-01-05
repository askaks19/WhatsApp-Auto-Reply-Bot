"""Input handling module for clipboard and GUI interaction via PyAutoGUI"""

import pyautogui
import pyperclip
import time
from config import WHATSAPP_WINDOW_CLICK, CHAT_START_POS, CHAT_END_POS, INPUT_BOX, SEND_BUTTON

def focus_whatsapp_window():
    """
    Focus the WhatsApp window by clicking on a specific coordinate.
    """
    pyautogui.click(WHATSAPP_WINDOW_CLICK[0], WHATSAPP_WINDOW_CLICK[1])
    time.sleep(0.5)

def copy_chat_history():
    """
    Select and copy the chat history from WhatsApp.
    
    Returns:
        str: The copied chat history as a string
    """
    # Move to start position
    pyautogui.moveTo(CHAT_START_POS[0], CHAT_START_POS[1])
    time.sleep(0.2)
    
    # Click and drag to select
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.moveTo(CHAT_END_POS[0], CHAT_END_POS[1], duration=1.0)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)
    
    # Copy to clipboard
    pyautogui.hotkey('ctrl', 'c')
    
    # Unselect
    pyautogui.click(CHAT_START_POS[0], CHAT_START_POS[1])
    time.sleep(1)
    
    # Get text from clipboard
    chat_history = pyperclip.paste()
    return chat_history

def send_message(message_text: str):
    """
    Send a message to WhatsApp by pasting and clicking send.
    
    Args:
        message_text (str): The message to send
    """
    # Copy message to clipboard
    pyperclip.copy(message_text)
    time.sleep(0.5)
    
    # Click input box
    pyautogui.click(INPUT_BOX[0], INPUT_BOX[1])
    time.sleep(0.3)
    
    # Paste message
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    
    # Click send button
    pyautogui.click(SEND_BUTTON[0], SEND_BUTTON[1])
    time.sleep(0.5)
