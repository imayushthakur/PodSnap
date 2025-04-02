
from googleapiclient.discovery import build
from src.config import GOOGLE_API_KEY, GOOGLE_CSE_ID

def fetch_images_from_google(queries):
    """Fetch images from Google Search API for the given queries."""
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    
    all_images = []
    for query in queries:
        result = service.cse().list(
            q=query,
            cx=GOOGLE_CSE_ID,
            searchType="image",
            num=3,
            imgSize="large",
            safe="active",
        ).execute()
        
        if "items" in result:
            for item in result["items"]:
                image_data = {
                    "url": item["link"],
                    "source": "google",
                    "query": query,
                    "title": item.get("title", ""),
                    "local_path": download_image(item["link"])
                }
                all_images.append(image_data)
    
    return all_images
