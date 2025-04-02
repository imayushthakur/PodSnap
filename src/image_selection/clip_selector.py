
import torch
import clip
from PIL import Image

def select_best_images(highlight_images):
    """
    Select the best image for each highlight using CLIP.
    
    Args:
        highlight_images: List of tuples (highlight_text, list_of_image_dicts)
        
    Returns:
        List of tuples (highlight_text, image_path)
    """
    # Load CLIP model
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    
    selected_pairs = []
    
    for highlight_text, images in highlight_images:
        # Preprocess the highlight text
        text = clip.tokenize([highlight_text]).to(device)
        
        best_score = -1
        best_image_path = None
        
        for img_data in images:
            # Load and preprocess image
            image = preprocess(Image.open(img_data["local_path"])).unsqueeze(0).to(device)
            
            # Calculate similarity score
            with torch.no_grad():
                image_features = model.encode_image(image)
                text_features = model.encode_text(text)
                
                # Normalize features
                image_features /= image_features.norm(dim=-1, keepdim=True)
                text_features /= text_features.norm(dim=-1, keepdim=True)
                
                # Calculate similarity
                similarity = (100.0 * image_features @ text_features.T).item()
            
            if similarity > best_score:
                best_score = similarity
                best_image_path = img_data["local_path"]
        
        if best_image_path:
            selected_pairs.append((highlight_text, best_image_path))
    
    return selected_pairs
