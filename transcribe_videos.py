# Import necessary libraries
import whisper
import moviepy.editor as mp
import os
import glob
from tqdm import tqdm

def transcribe_video(video_file, model, output_folder):
    
    try:
        # Extract base name from video file path
        base_name = os.path.basename(video_file).rsplit('.', 1)[0]

        # Create output text file name
        txt_file_name = os.path.join(output_folder, f"{base_name}_text.txt")
        
        # Load video file
        video = mp.VideoFileClip(video_file)

        # Extract audio from video
        audio = video.audio

        # Create temporary audio file path
        audio_file = os.path.join(output_folder, f"temp_audio_{base_name}.wav")

        # Write audio to file
        audio.write_audiofile(audio_file, verbose=False, logger=None)
        
        # Transcribe audio using Whisper model
        result = model.transcribe(audio_file)
        
        # Write transcription to text file
        with open(txt_file_name, 'w', encoding='utf-8') as txt_file:
            txt_file.write(result["text"])
        
        print(f"Transcription saved to: {txt_file_name}")
        
    except Exception as e:
        # Print error message if processing fails
        print(f"Error processing {video_file}: {str(e)}")
    
    finally:
        # Clean up resources
        if 'audio' in locals():
            audio.close()
        if 'video' in locals():
            video.close()
        if os.path.exists(audio_file):
            os.remove(audio_file)

def main():

    # Set input and output folder paths
    source_folder = 'speech'
    output_folder = 'text'

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load Whisper model
    model = whisper.load_model("large")

    # Get list of all MP4 files in source folder
    video_files = glob.glob(os.path.join(source_folder, '*.mp4'))

    # Process each video file with a progress bar
    for video_file in tqdm(video_files, desc="Processing videos"):
        transcribe_video(video_file, model, output_folder)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()