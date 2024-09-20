# Video Transcription with Whisper AI 🎥📝

This project leverages OpenAI's Whisper model to deliver high-quality transcription of audio from video files.

## Prerequisites

- Python 3.7 or higher
- FFmpeg (required for audio extraction)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/video-transcription.git
cd video-transcription
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Install FFmpeg:
- On macOS (using Homebrew): `brew install ffmpeg`
- On Ubuntu or Debian: `sudo apt-get install ffmpeg`
- On Windows: Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add to PATH

## Usage

1. Place your MP4 video files in a folder named `speech` in the project directory.

2. Run the script:

```python
python transcribe_videos.py
```

3. Transcribed text files will be saved in a folder named `text`.