import os
import subprocess

def convert_video(input_path, output_format, output_dir):
    name, _ = os.path.splitext(os.path.basename(input_path))
    output_filename = f"{name}.{output_format}"
    output_path = os.path.join(output_dir, output_filename)

    try:
        subprocess.run(["ffmpeg", "-y", "-i", input_path, output_path], check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro na conversão: {e}")
