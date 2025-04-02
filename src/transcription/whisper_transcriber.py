
import whisper
import torch
from src.config import WHISPER_MODEL, WHISPER_LANGUAGE

def transcribe_podcast(file_path):
    """
    Transcribe podcast using OpenAI Whisper.
    
    Args:
        file_path (str or Path): Path to the podcast audio file
        
    Returns:
        str: Transcribed text
    """
    # Load the Whisper model
    model = whisper.load_model(WHISPER_MODEL)
    
    # Perform transcription
    result = model.transcribe(
        str(file_path),
        language=WHISPER_LANGUAGE if WHISPER_LANGUAGE != "auto" else None,
        fp16=torch.cuda.is_available()
    )
    
    return result["text"]
