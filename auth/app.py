from flask import Flask, request, redirect, render_template, make_response
from datetime import datetime
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    data = request.form
    if User.query.filter_by(username=data['username']).first():
        return "User existiert schon", 409

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # POST: Login-Verarbeitung
    data = request.form
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return "Falsche Daten", 403

    user.generate_token()
    user.last_logon = datetime.utcnow()
    db.session.commit()

    resp = make_response(redirect('/game'))
    resp.set_cookie('auth', user.auth_token, httponly=True, max_age=3600)
    return resp


@app.route('/check')
def check():
    token = request.cookies.get('auth')
    if User.query.filter_by(auth_token=token).first():
        return jsonify({'status': 'ok'}), 200
    return jsonify({'status': 'unauthorized'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
