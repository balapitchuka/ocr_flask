from flask import Flask, render_template, request
from ocr_core import ocr_core
import os

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']


app = Flask(__name__)


def allowed_file(file_name):
    return '.' in file_name and \
        file_name.rsplit('.', 1)[-1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    print(dir(request))
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']

        if file.filename == '':
            return render_template('upload.html', msg='No file selected')
        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)
            
            return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text, img_scr=UPLOAD_FOLDER+file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == "__main__":
    app.run()