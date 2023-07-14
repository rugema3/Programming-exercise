import youtube_dl

def my_progress_callback(progress):
    if progress['status'] == 'downloading':
        total_size = progress['total_bytes']
        downloaded_bytes = progress['downloaded_bytes']
        percent = (downloaded_bytes / total_size) * 100
        print(f"Downloaded: {percent:.2f}%")

url = input("Enter the YouTube video URL: ")

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'progress_hooks': [my_progress_callback],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

