from pytube import YouTube
from moviepy.editor import *
import os

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=k9I_fN2fajE&t=919s"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest quality audio stream available
audio_stream = yt.streams.get_audio_only()

# Specify the output directory
output_path = os.path.expanduser("~/Downloads")

# Download the audio
audio_stream.download(output_path=output_path)

# Get the downloaded audio filename
filename = audio_stream.default_filename

# Convert the video file to audio (MP3)
video_path = os.path.join(output_path, filename)
audio_path = os.path.join(output_path, f"{os.path.splitext(filename)[0]}.mp3")

video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

# Remove the original video file
os.remove(video_path)

# Print the path of the downloaded audio
print("Audio downloaded: ", audio_path)

