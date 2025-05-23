from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/game/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/game/icons/<path:filename>')
def serve_icons(filename):
    return send_from_directory('static/icons', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)