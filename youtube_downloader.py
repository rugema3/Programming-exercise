import time
from pytube import YouTube
from tqdm import tqdm

# Set the save path
SAVE_PATH = "E:/"

# Enter the YouTube video URL
link = input("Enter the YouTube video URL: ")

try:
    # Create a YouTube object
    yt = YouTube(link)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Set the filename
    filename = "pytube_video"

    # Calculate the approximate file size
    file_size_mb = stream.filesize / (1024 * 1024)

    # Calculate the estimated download time based on the download speed
    download_time_seconds = file_size_mb / (3.59 / 8)  # Assuming download speed of 3.59 Mbps

    print("Starting download...")
    start_time = time.time()

    # Download the video
    stream.download(output_path=SAVE_PATH, filename=filename, skip_existing=False, on_progress_callback=lambda stream, chunk, bytes_remaining: progress_callback(file_size_mb, bytes_remaining))

    end_time = time.time()
    download_duration_seconds = end_time - start_time

    # Calculate the actual download speed
    actual_download_speed = file_size_mb / (download_duration_seconds / 8)

    print("\nVideo downloaded successfully!")
    print(f"Download Speed: {actual_download_speed:.2f} Mbps")

except Exception as e:
    print("Error:", str(e))


def progress_callback(file_size_mb, bytes_remaining):
    downloaded_mb = (file_size_mb * 1024) - (bytes_remaining / (1024 * 1024))
    progress = downloaded_mb / file_size_mb * 100
    print(f"\rProgress: {progress:.2f}% ", end="")

