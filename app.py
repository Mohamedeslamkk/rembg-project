from flask import Flask, request, jsonify
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    file = request.files['image']
    img = Image.open(file.stream)
    output = remove(img)
    img_byte_arr = io.BytesIO()
    output.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, attachment_filename='output.png')

if __name__ == "__main__":
    app.run()