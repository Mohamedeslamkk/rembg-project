from flask import Flask, request, jsonify
from rembg import remove
from io import BytesIO

app = Flask(name)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    input_image = request.files['image'].read()
    output_image = remove(input_image)
    return jsonify({'output': output_image.hex()})

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
