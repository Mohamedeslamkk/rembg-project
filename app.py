from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'لم يتم توفير صورة'}, 400
    
    # قراءة الصورة المُرسلة
    input_image = request.files['image'].read()
    
    # معالجة الصورة لإزالة الخلفية
    output_image = remove(input_image)
    
    # تحويل النتيجة إلى تدفق بايتات
    output_image_io = BytesIO(output_image)
    output_image_io.seek(0)
    
    # إرسال الصورة الناتجة كملف
    return send_file(output_image_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
