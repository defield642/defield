import os
from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_path):
    """Extract audio from a video file and save it as an MP3."""
    try:
        video_clip = VideoFileClip(/home/defield/Videos/video music/Post_Malone_-_Motley_Crew__Official_Video_(360p).mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(/home/defield/Music, codec='mp3')
        audio_clip.close()
        video_clip.close()
        print(f"Successfully extracted audio to {}")/home/defield/Music
    except Exception as e:
        print(f"Failed to extract audio from {/home/defield/Videos/video music/Post_Malone_-_Motley_Crew__Official_Video_(360p).mp4}: {e}")

def process_videos(video_folder, output_folder):
    """Process multiple video files in a folder and save their audio as MP3."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for video_file in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_file)
        if os.path.isfile(video_path) and video_file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
            output_path = os.path.join(output_folder, os.path.splitext(video_file)[0] + '.mp3')
            extract_audio(video_path, output_path)

if __name__ == "__main__":
    video_folder = 'path/to/your/video/folder'  # Change to your video folder path
    output_folder = 'path/to/your/output/folder'  # Change to your output folder path
    
    process_videos(video_folder, output_folder)
