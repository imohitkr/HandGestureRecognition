from flask import Flask, render_template, Response, make_response, send_file
import json
import process_video
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

app = Flask(__name__ + "- Hand Gesture Recognition", static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(process_video.frame_process(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/asl')
def asl():
    return render_template('asl.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/live-data_video')
def live_data_video():
    """ echo video predictions as JSON"""
    f = open('tmp/video_prediction.json')
    data = json.load(f)
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response



if __name__ == '__main__':
    app.run(debug=False)
