
import openai
from typing import List

def generate_image_queries(highlights: List[str], queries_per_highlight: int = 3) -> List[List[str]]:
    """
    Generate effective image search queries for each highlight.
    
    Args:
        highlights (List[str]): List of podcast highlights
        queries_per_highlight (int): Number of different queries to generate per highlight
        
    Returns:
        List[List[str]]: List of query lists for each highlight
    """
    all_queries = []
    
    for highlight in highlights:
        prompt = f"""
        Generate {queries_per_highlight} different search queries that would find 
        relevant and visually interesting images to accompany this podcast quote:
        
        "{highlight}"
        
        Format the output as a JSON array of strings.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You create effective visual search queries for videos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        # Parse JSON response
        import json
        queries = json.loads(response.choices[0].message.content)
        all_queries.append(queries)
    
    return all_queries
