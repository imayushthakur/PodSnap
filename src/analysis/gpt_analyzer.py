
import openai
from typing import List
import json
from src.config import OPENAI_API_KEY, GPT_MODEL, HIGHLIGHT_COUNT

# Configure OpenAI API
openai.api_key = OPENAI_API_KEY

def extract_highlights(transcript: str, count: int = HIGHLIGHT_COUNT) -> List[str]:
    """
    Extract the most interesting highlights from the podcast transcript using GPT-3.
    
    Args:
        transcript (str): The podcast transcript
        count (int): Number of highlights to extract
        
    Returns:
        List[str]: List of highlight quotes/segments
    """
    prompt = f"""
    Below is a transcript from a podcast. Extract exactly {count} of the most interesting, 
    insightful, or surprising quotes or segments that would make viewers want to listen 
    to the full podcast. Each highlight should be concise but impactful.
    
    Transcript:
    {transcript[:12000]}
    
    Highlights (JSON array):
    """
    
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "You are a professional video editor who selects engaging clips from podcasts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=count * 100,
        temperature=0.7
    )
    
    # Extract JSON array from response
    content = response.choices[0].message.content.strip()
    highlights = json.loads(content)
    
    return highlights[:count]
