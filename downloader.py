import yt_dlp
import os

def download(url: str) -> str:
    opts = {'format': (
                "bv*[height<=720][ext=mp4]+ba[ext=m4a]/"
                "b[height<=720][ext=mp4]/"
                "bv*[height<=720]+ba/"
                "b[height<=720]"
            ),
            'outtmpl': "%(id)s.%(ext)s",
            'merge-output-format': "mp4"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info["requested_downloads"][0]["filepath"]
            
