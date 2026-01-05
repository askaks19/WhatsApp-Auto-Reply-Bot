"""WhatsApp Auto Reply Bot - Main Entry Point

This script orchestrates the WhatsApp chatbot by combining all modules:
- config: Configuration and API setup
- chat_parser: Chat history parsing
- ai_generator: AI response generation
- input_handler: PyAutoGUI and clipboard operations
"""

import time
from config import MY_NAME, MAX_REPLIES, REPLY_DELAY, setup_gemini_api
from chat_parser import get_last_sender, should_reply
from ai_generator import generate_response, validate_response
from input_handler import focus_whatsapp_window, copy_chat_history, send_message

def main_loop(max_replies=MAX_REPLIES):
    """
    Main bot loop that continuously reads chat, generates responses, and sends them.
    
    Args:
        max_replies (int): Maximum number of replies before stopping
    """
    print("🤖 WhatsApp Auto Reply Bot Starting...")
    print(f"👤 User Name: {MY_NAME}")
    print(f"📨 Max Replies: {max_replies}")
    
    # Setup Gemini API
    try:
        setup_gemini_api()
        print("✅ Gemini API initialized successfully")
    except ValueError as e:
        print(f"❌ Failed to initialize Gemini API: {e}")
        return
    
    # Focus WhatsApp window
    focus_whatsapp_window()
    print("✅ WhatsApp window focused")
    time.sleep(2)
    
    replies_sent = 0
    
    try:
        while replies_sent < max_replies:
            print(f"\n[Attempt {replies_sent + 1}/{max_replies}] Fetching chat history...")
            
            # Copy chat history from WhatsApp
            chat_history = copy_chat_history()
            print(f"📝 Chat history retrieved ({len(chat_history)} characters)")
            
            # Extract last sender
            last_sender = get_last_sender(chat_history)
            print(f"👤 Last sender: {last_sender}")
            
            # Check if we should reply
            if not should_reply(last_sender, MY_NAME):
                print("⏭️ Skipping reply (last message is from us or invalid)")
                time.sleep(REPLY_DELAY)
                continue
            
            # Generate AI response
            print("🧠 Generating AI response...")
            try:
                response_text = generate_response(chat_history)
                print(f"💬 AI Response: {response_text}")
                
                # Validate response
                if not validate_response(response_text):
                    print("❌ Response validation failed")
                    time.sleep(REPLY_DELAY)
                    continue
                
                # Send message
                print("📤 Sending message...")
                send_message(response_text)
                
                replies_sent += 1
                print(f"✅ Reply {replies_sent} sent successfully")
                
            except Exception as e:
                print(f"❌ Error generating response: {str(e)}")
                time.sleep(REPLY_DELAY)
                continue
            
            # Wait before next reply
            print(f"⏳ Waiting {REPLY_DELAY} seconds before next check...")
            time.sleep(REPLY_DELAY)
        
        print(f"\n🔴 Max replies ({max_replies}) reached. Bot stopping.")
        
    except KeyboardInterrupt:
        print("\n⚠️ Bot interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main_loop()
