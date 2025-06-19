# 🎵 YouTube Playlist MP3 Downloader

A Python script to download all songs in a YouTube playlist as MP3 files using `yt-dlp` and `ffmpeg`.

---

## 📦 Features

* ✅ Download YouTube playlist as MP3
* ✅ Automatic audio extraction and conversion using `ffmpeg`
* ✅ Clean console output with real-time progress, download speed, and file size
* ✅ Playlist title and total video count shown
* ✅ Files saved into `downloads_mp3` directory

---

## 🔧 Requirements

* Python 3.8 or above
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
* [`ffmpeg`](https://ffmpeg.org/)

### Install requirements:

```bash
pip install yt-dlp
```

**Install `ffmpeg`:**

* macOS: `brew install ffmpeg`
* Ubuntu/Debian: `sudo apt install ffmpeg`
* Windows (with Chocolatey): `choco install ffmpeg`

---

## 🚀 How to Use

1. Clone or download this repository.
2. Open `youtube_mp3_downloader.py` and set your playlist URL:

```python
PLAYLIST_URL = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

3. Run the script:

```bash
python3 main.py
```

4. MP3 files will be saved in the `downloads_mp3/` folder.

---

## 📂 Folder Structure

```
main.py   # Main script
downloads_mp3/              # Folder where MP3s are saved
```

---

## 📜 Output Example

```text
📅 Fetching playlist info...

📂 Playlist: My Favorite Songs
🎮 Total videos: 12

[Downloading] -> 🎵 Song Title.webm 2.10MiB/4.00MiB (52.5%) 700.3 KB/s
[Downloaded] -> 🎵 Song Title.webm 3.88MB
...
✅ Done! MP3s saved in: downloads_mp3
```

---

## 🧐 Notes

* Only audio is downloaded (no video).
* Audio is converted to `.mp3` using `ffmpeg`.
* If you receive rate-limit or network errors, try a different network or VPN.

---

## 🛠 Customization

To change the audio quality:

```python
'preferredquality': '192'  # Can be set to '320' for highest quality
```

To change the output folder:

```python
OUTPUT_FOLDER = "my_music_folder"
```

---

## 🪯 Troubleshooting

* **ffmpeg not found** → Make sure it's installed and in your system PATH.
* **Playlist not fetching** → Confirm it’s public and accessible.
* **HTTP 403/400 errors** → Retry later or use a VPN.

---

## 🤝 Contributing

Feel free to fork, enhance or raise issues.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Credits

* Python 3
* Built using [yt\_dlp](https://github.com/yt-dlp/yt-dlp)
* Terminal output styled manually
* Special thanks to **ChatGPT-4o** for assistance in scripting and logic design ✨

