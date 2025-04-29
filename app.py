from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
import os

from utils.converter import convert_video
from utils.downloader import download_video
from utils.player import allowed_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CONVERTED_FOLDER = "converted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        file = request.files['video']
        output_format = request.form['format'].lower()

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(input_path)

            try:
                output_path = convert_video(input_path, output_format, CONVERTED_FOLDER)
                return send_file(output_path, as_attachment=True)
            except Exception as e:
                return f"Erro durante a conversão: {e}", 500
        else:
            return "Formato de vídeo não suportado", 400

    return render_template('convert.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']

        try:
            filename = download_video(url, UPLOAD_FOLDER)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return f"Erro ao baixar vídeo: {e}", 500

    return render_template('download.html')

@app.route('/player', methods=['GET', 'POST'])
def player():
    if request.method == 'POST':
        file = request.files['video']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            return redirect(url_for('player', file=filename))
        else:
            return "Formato de vídeo não suportado", 400

    filename = request.args.get('file')
    return render_template('player.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
