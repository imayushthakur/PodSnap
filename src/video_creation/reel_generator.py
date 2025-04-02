# src/video_creation/reel_generator.py
from moviepy.editor import AudioFileClip, ImageClip, TextClip, CompositeVideoClip, concatenate_videoclips

def create_reel(podcast_path, highlights, images, output_path, duration):
    """
    Create a video reel from podcast highlights and images.
    
    Args:
        podcast_path (str): Path to the podcast audio file
        highlights (List[str]): List of podcast highlights
        images (List[Tuple[str, str]]): List of (highlight, image_path) pairs
        output_path (str): Path to save the output video
        duration (int): Target duration of the reel in seconds
    """
    # Load the podcast audio
    podcast_audio = AudioFileClip(str(podcast_path))
    
    # Calculate clip duration
    clip_duration = duration / len(images)
    
    # Create video clips for each highlight-image pair
    video_clips = []
    
    for highlight, image_path in images:
        # Create image clip and resize for vertical format (9:16)
        image_clip = ImageClip(image_path).resize(width=1080, height=1920)
        image_clip = image_clip.set_duration(clip_duration)
        
        # Create text clip with the highlight
        text_clip = TextClip(
            txt=highlight,
            fontsize=40,
            font="Arial",
            color="white",
            bg_color="black",
            method="caption",
            size=(900, None)
        ).set_position(("center", "center")).set_duration(clip_duration)
        
        # Extract audio segment
        audio_start = random.uniform(0, max(0, podcast_audio.duration - clip_duration))
        clip_audio = podcast_audio.subclip(audio_start, audio_start + clip_duration)
        
        # Combine image and text with audio
        composite = CompositeVideoClip([image_clip, text_clip]).set_audio(clip_audio)
        video_clips.append(composite)
    
    # Concatenate all clips with crossfades
    final_clip = concatenate_videoclips(video_clips, method="compose")
    
    # Write the final video file
    final_clip.write_videofile(
        str(output_path),
        codec="libx264",
        audio_codec="aac",
        fps=30
    )
