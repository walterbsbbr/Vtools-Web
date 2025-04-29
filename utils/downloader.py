import os
import yt_dlp

class DownloadError(Exception):
    pass

def sanitize_filename(title):
    """Corta o nome se for muito longo"""
    if len(title) > 100:
        return title[:100]
    return title

def download_video(url, output_dir):
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title).100s.%(ext)s'),  # Limita o nome a 100 caracteres
        'format': 'bestvideo+bestaudio/best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except yt_dlp.utils.DownloadError as e:
        raise DownloadError(f"Erro no download: {str(e)}")
