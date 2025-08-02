from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')
    format_type = data.get('format', 'mp4')
    quality = data.get('quality', 'best')

    if not url:
        return jsonify({'error': 'URL no proporcionada'}), 400

    # añadir la calidad al nombre del archivo para evitar sobrescritura
    common_opts = {
        'outtmpl': f'{DOWNLOAD_DIR}/%(title)s_{quality}.%(ext)s',
        'prefer_ffmpeg': True,
        'noplaylist': True,
        'ignoreerrors': True
    }

    if format_type == 'mp3':
        ydl_opts = {
            **common_opts,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': ['-vn'],
        }
    else:
        format_map = {
            'best': 'bestvideo+bestaudio/best',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            '240p': 'bestvideo[height<=240]+bestaudio/best'
        }

        ydl_opts = {
            **common_opts,
            'format': format_map.get(quality, 'bestvideo+bestaudio/best'),
            'merge_output_format': 'mp4',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            # ajusta la extensión según el formato
            if format_type == 'mp3':
                filename = os.path.splitext(filename)[0] + '.mp3'
            elif not filename.endswith('.mp4'):
                filename = os.path.splitext(filename)[0] + '.mp4'

            basename = os.path.basename(filename)
            return jsonify({'success': True, 'filename': basename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/file/<filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)