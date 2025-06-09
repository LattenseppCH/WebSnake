from flask import Flask, send_from_directory, render_template, request
from flask import Flask, request, jsonify, render_template, make_response, redirect
import requests

app = Flask(__name__, static_folder='static')


def submit_highscore(username, score_easy, score_hard):
    url = 'http://flask_auth:5000/api/highscore'
    data = {
        'username': username,
        'score_easy': score_easy,
        'score_hard': score_hard
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("High scores submitted successfully!")
        else:
            print("Failed to submit high scores:", response.json())
    except requests.RequestException as e:
        print("Error submitting high scores:", e)


@app.route('/')
def index():
    token = request.cookies.get('auth')
    username = 'Guest'

    if token:
        try:
            res = requests.get('http://flask_auth:5000/api/resolve-token', params={'token': token}, timeout=2)
            if res.ok:
                username = res.json().get('username', 'Guest')
        except requests.RequestException:
            pass  # Auth-Server nicht erreichbar

    return render_template('index.html', username=username)

@app.route('/icons/<path:filename>')
def serve_icons(filename):
    return send_from_directory('static/icons', filename)

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
