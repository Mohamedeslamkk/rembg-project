from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

@app.route('/remove_bg', methods=['POST'])
def remove_background():
    file = request.files['file']
    if not file:
        return 'No file provided.', 400
    input_img = file.read()
    output_img = remove(input_img)
    byte_io = io.BytesIO()
    byte_io.write(output_img)
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')

if __name__ == '__main__':
    app.run()
