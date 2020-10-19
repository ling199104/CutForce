#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from apis.templates.__init__ import app
from flask import Response, request, redirect, url_for
from os.path import exists
from apis.models.FFmpegConcatenation import *


DOWNLOAD_FOLDER = './apis/static/video/'


# request downloading video
@app.route("/download", methods=["POST"])
def request_download():
    # Get timestamp from json
    request_data = request.get_json()
    # Check if json data is right.
    if request_data['message'] == 'video':
        file_path: str = request_data['filename']
        clip_data: dict = request_data['data']
        # Processing video format
        split_audio(clip_data)
        # Redirect to the following url after video processing is done
        return redirect(url_for('download/{}'.format(file_path)), code=302)
    else:
        return "400 Bad request"  # Debug-only


# Application/octet-stream
@app.route("/download/<file_path>", methods=["GET"])
def download_file(file_path, chunk_size):
    def generate():
        if not exists(file_path):
            return "File not found."
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    return Response(generate(), content_type="application/octet-stream")
