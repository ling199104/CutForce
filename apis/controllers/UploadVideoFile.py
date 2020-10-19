#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from os.path import join
from flask import request, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from apis.templates.__init__ import app


UPLOAD_FOLDER = './apis/static/temps'
ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'avi', 'mov'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16GB


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(
                {
                    "success": "True",
                    "message": "Upload successful",
                    "data": (url_for('uploaded_file', filename=filename))
                }
            )
    else:
        return jsonify(
            {
                "success": "False",
                "message": "Upload failed"
            }
        )


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
