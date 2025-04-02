# src/main.py
import argparse
from pathlib import Path

from src.transcription.whisper_transcriber import transcribe_podcast
from src.analysis.gpt_analyzer import extract_highlights
from src.image_search.query_generator import generate_image_queries
from src.image_search.serp_fetcher import fetch_images_from_google
from src.image_search.getty_fetcher import fetch_images_from_getty
from src.image_selection.clip_selector import select_best_images
from src.video_creation.reel_generator import create_reel

def main():
    parser = argparse.ArgumentParser(description="Generate video reels from podcasts using AI")
    parser.add_argument("--podcast", required=True, help="Path to the podcast audio file")
    parser.add_argument("--output", required=True, help="Path for the output reel video")
    parser.add_argument("--highlights", type=int, default=5, help="Number of highlights to extract")
    parser.add_argument("--duration", type=int, default=60, help="Target duration of the reel in seconds")
    args = parser.parse_args()
    
    # Step 1: Transcribe podcast
    transcript = transcribe_podcast(args.podcast)
    
    # Step 2: Extract highlights
    highlights = extract_highlights(transcript, count=args.highlights)
    
    # Step 3: Generate image search queries
    image_queries = generate_image_queries(highlights)
    
    # Step 4: Fetch images
    all_images = []
    for i, (highlight, queries) in enumerate(zip(highlights, image_queries)):
        # Get images from Google and Getty
        google_images = fetch_images_from_google(queries)
        getty_images = fetch_images_from_getty(queries)
        
        # Combine images from both sources
        highlight_images = google_images + getty_images
        if highlight_images:
            all_images.append((highlight, highlight_images))
    
    # Step 5: Select the best image for each highlight using CLIP
    selected_images = select_best_images(all_images)
    
    # Step 6: Create the video reel
    create_reel(
        podcast_path=args.podcast,
        highlights=highlights,
        images=selected_images,
        output_path=args.output,
        duration=args.duration
    )
    
    print(f"Reel generated successfully and saved to: {args.output}")

if __name__ == "__main__":
    main()
