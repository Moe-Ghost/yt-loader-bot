import yt_dlp

def download(url: str) -> str:
    opts = {'format': "bv*[height<=720]+ba/b",
            'outtmpl': "%(id)s.%(ext)s",
            'merge-output-format': "mp4"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return info["requested_downloads"][0]["filepath"]