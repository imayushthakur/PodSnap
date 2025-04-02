
import requests
from src.config import GETTY_API_KEY, GETTY_API_SECRET

def fetch_images_from_getty(queries):
    """Fetch images from Getty Images API for the given queries."""
    # Get authentication token
    token = get_getty_auth_token()
    
    all_images = []
    headers = {
        "Api-Key": GETTY_API_KEY,
        "Authorization": f"Bearer {token}"
    }
    
    for query in queries:
        params = {
            "phrase": query,
            "fields": "id,title,preview,display_sizes",
            "page_size": 3,
            "sort_order": "best_match"
        }
        
        response = requests.get(
            "https://api.gettyimages.com/v3/search/images",
            headers=headers,
            params=params
        )
        
        if response.status_code == 200:
            data = response.json()
            for item in data.get("images", []):
                image_url = item["display_sizes"][0]["uri"]
                image_data = {
                    "url": image_url,
                    "source": "getty",
                    "query": query,
                    "title": item.get("title", ""),
                    "local_path": download_image(image_url)
                }
                all_images.append(image_data)
    
    return all_images
