import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GETTY_API_KEY = os.getenv("GETTY_API_KEY")
GETTY_API_SECRET = os.getenv("GETTY_API_SECRET")

# Whisper Configuration
WHISPER_MODEL = "medium"  # Options: tiny, base, small, medium, large
WHISPER_LANGUAGE = "en"   # Default language, can be auto-detected

# GPT Configuration
GPT_MODEL = "gpt-3.5-turbo"  # Or "gpt-4" if available
HIGHLIGHT_COUNT = 5

# CLIP Configuration
CLIP_MODEL = "ViT-B/32"  # Options: ViT-B/32, ViT-B/16, ViT-L/14

# Video Configuration
DEFAULT_REEL_DURATION = 60  # seconds
HIGHLIGHT_DURATION = 10  # seconds per highlight
FONT = "Arial"
FONT_SIZE = 40
FONT_COLOR = "white"
