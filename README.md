# WhatsApp Auto Reply Bot

🤖 An intelligent WhatsApp chatbot that automatically generates context-aware replies using Google Gemini AI with Python automation.

## Features

✨ **AI-Powered Responses**: Uses Google Gemini API to generate natural, context-aware replies

📱 **WhatsApp Integration**: Directly interacts with WhatsApp Desktop using PyAutoGUI

🎙️ **Bilingual Support**: Generates responses in Hindi+English with optional sarcasm

📋 **Smart Chat Parsing**: Extracts sender information and avoids replying to own messages

🔧 **Modular Architecture**: Clean separation of concerns with focused modules

## Project Structure

```
WhatsApp-Auto-Reply-Bot/
├── config.py           # Configuration & API setup
├── chat_parser.py      # Chat history parsing logic
├── ai_generator.py     # Gemini API response generation
├── input_handler.py    # PyAutoGUI automation
├── main.py             # Main orchestration loop
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Module Descriptions

### `config.py`
Centralized configuration including:
- User settings (name, max replies, delays)
- Screen coordinates for WhatsApp elements
- Gemini API configuration
- Prompt templates

### `chat_parser.py`
Handles WhatsApp chat format parsing:
- Extracts last message sender
- Validates if reply should be sent
- Parses timestamped messages

### `ai_generator.py`
Manages AI response generation:
- Calls Gemini API with chat context
- Validates response length and content
- Error handling for API failures

### `input_handler.py`
Automates WhatsApp interactions:
- Selects and copies chat history
- Focuses WhatsApp window
- Pastes and sends messages via GUI automation

### `main.py`
Main entry point that:
- Orchestrates all modules
- Implements the reply loop
- Handles keyboard interrupts
- Logs bot activity

## Installation

1. Clone the repository:
```bash
git clone https://github.com/askaks19/WhatsApp-Auto-Reply-Bot.git
cd WhatsApp-Auto-Reply-Bot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

### 1. Get Gemini API Key
- Visit [Google AI Studio](https://aistudio.google.com)
- Create a new API key
- Keep it secure

### 2. Set Environment Variable

**Linux/macOS:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

### 3. Configure `config.py`
Adjust the screen coordinates for your display:
- `WHATSAPP_WINDOW_CLICK`: Click position to focus WhatsApp
- `CHAT_START_POS` & `CHAT_END_POS`: Chat selection area
- `INPUT_BOX` & `SEND_BUTTON`: Message input coordinates
- `MY_NAME`: Your WhatsApp display name

## Usage

1. Open WhatsApp Desktop (make sure it's active)
2. Run the bot:
```bash
python main.py
```

3. The bot will:
   - Wait for incoming messages
   - Generate AI responses
   - Send replies automatically
   - Stop after `MAX_REPLIES` (configurable)

## How It Works

```
┌─────────────────────────────────────┐
│ 1. Copy Chat History from WhatsApp  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 2. Parse Last Sender from Chat      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 3. Check if Reply is Needed         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 4. Generate AI Response via Gemini  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 5. Validate & Send Message          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ 6. Wait & Repeat Loop               │
└─────────────────────────────────────┘
```

## Configuration Options

Edit `config.py` to customize:

```python
MY_NAME = "your name"          # Your WhatsApp display name
MAX_REPLIES = 10               # Maximum replies before stopping
REPLY_DELAY = 10               # Seconds between reply checks
GEMINI_MODEL = "gemini-1.5-flash"  # AI model to use
```

## Customization

### Change AI Personality
Edit the `AI_PROMPT_TEMPLATE` in `config.py`:
```python
AI_PROMPT_TEMPLATE = """You are texting like [YOUR_NAME], 
replying briefly and [TONE] in [LANGUAGES].
Analyze the chat history...
"""
```

### Adjust Screen Coordinates
Find your screen coordinates and update in `config.py`

### Modify Reply Logic
Edit `chat_parser.py` to customize when replies are sent

## Limitations

⚠️ **Important Considerations:**
- Requires WhatsApp Desktop (not web-based)
- Screen coordinates are display-specific
- API calls consume Gemini quota
- PyAutoGUI may be unstable on some systems
- Bot cannot access encrypted messages

## Security Notes

🔐 **Keep API Key Safe:**
- Never hardcode API keys in source
- Use environment variables only
- Don't share keys in public repos
- Rotate keys regularly

## Future Enhancements

🚀 Planned features:
- Conversation memory & context
- Custom command triggers
- Multi-user support
- Offline response generation
- Web interface for configuration
- Conversation logging

## Troubleshooting

**Bot not detecting messages?**
- Verify screen coordinates in `config.py`
- Ensure WhatsApp window is active
- Check message format matches parser expectations

**API errors?**
- Verify GEMINI_API_KEY is set
- Check API quota usage
- Ensure internet connection

**PyAutoGUI issues?**
- Check for conflicting keyboard shortcuts
- Run with administrator privileges on Windows

## License

MIT License - Feel free to use and modify

## Author

**Ayush Kumar Singh**  
B.Tech Computer Science (AI) - MIT Bengaluru

## Disclaimer

This project is for educational purposes. Use responsibly and respect WhatsApp's Terms of Service. Automated messaging may violate ToS or spam regulations in your jurisdiction.
