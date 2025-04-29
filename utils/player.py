import os

ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'avi', 'wmv', 'mov', 'flv', 'ogg', 'mpeg', 'gp3', 'webm'}

def allowed_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return ext in ALLOWED_EXTENSIONS

def list_videos(directory):
    """Lista os vídeos válidos no diretório."""
    return [f for f in os.listdir(directory) if allowed_file(f)]
