import os
import sys
from yt_dlp import YoutubeDL
from shutil import get_terminal_size

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLkhsntAjSDdIQ2t7t6hcE1P3NcGM7_j-y"
OUTPUT_FOLDER = "downloads_mp3"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def clear_line():
    sys.stdout.write('\r' + ' ' * get_terminal_size().columns + '\r')
    sys.stdout.flush()

def human_speed(speed_bytes):
    if not speed_bytes:
        return ""
    return f"{speed_bytes / 1024 / 1024:.2f} MB/s" if speed_bytes > 1024 * 1024 else f"{speed_bytes / 1024:.1f} KB/s"

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        downloaded = d.get('_downloaded_bytes_str', '').strip()
        total = d.get('_total_bytes_str', '').strip()
        speed = human_speed(d.get('_speed'))
        filename = os.path.basename(d.get('filename', ''))

        clear_line()
        print(f"[Downloading] -> 🎵 {filename} {downloaded}/{total} ({percent}) {speed}", end="\r")

    elif d['status'] == 'finished':
        filename = os.path.basename(d.get('filename', ''))
        size = round(os.path.getsize(d['filename']) / (1024 * 1024), 2)
        clear_line()
        print(f"[Downloaded] -> 🎵 {filename} {size}MB")

def get_playlist_info(url):
    ydl_opts = {'quiet': True, 'extract_flat': True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title'), info.get('entries', [])

def download_audio(title, url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"\n⚠️ Error downloading {title}: {e}")

if __name__ == "__main__":
    print("📥 Fetching playlist info...")
    playlist_title, entries = get_playlist_info(PLAYLIST_URL)
    print(f"\n📂 Playlist: {playlist_title}")
    print(f"🎬 Total videos: {len(entries)}\n")

    for entry in entries:
        title = entry.get('title', 'Unknown Title')
        url = entry.get('url')
        if url:
            download_audio(title, url, OUTPUT_FOLDER)
        else:
            print(f"⚠️ Skipping invalid entry: {title}")

    print(f"\n✅ Done! MP3s saved in: {OUTPUT_FOLDER}")
