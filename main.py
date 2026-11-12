from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
import hashlib
import os 
from datetime import timedelta

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'fallback-dev-secret-key')

app.permanent_session_lifetime = timedelta(minutes=15)

raw_password = os.environ.get('SITE_PASSWORD', 'croissanti')
CORRECT_PASSWORD_HASH = hashlib.sha256(raw_password.encode()).hexdigest()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password', '')
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if password_hash == CORRECT_PASSWORD_HASH:
            session.permanent = True
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Incorrect password. Please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    """Home Page"""
    return render_template('index.html')

# (Rest of your routes remain the same...)

@app.route('/research')
@login_required
def research():
    """Research Page"""
    return render_template('research.html')

@app.route('/volunteering')
@login_required
def volunteering():
    """Volunteering Page"""
    return render_template('volunteering.html')

@app.route('/hobbies')
@login_required
def hobbies():
    """Hobbies Main Page"""
    return render_template('hobbies.html')

@app.route('/hobbies/crochet')
@login_required
def hobbies_crochet():
    """Crochet Hobby Page"""
    return render_template('hobbies_crochet.html')

@app.route('/hobbies/languages')
@login_required
def hobbies_languages():
    """Learning Languages Hobby Page"""
    return render_template('hobbies_languages.html')

@app.route('/hobbies/journaling')
@login_required
def hobbies_journaling():
    """Bullet Journaling Hobby Page"""
    return render_template('hobbies_journaling.html')

@app.route('/resume')
@login_required
def resume():
    """Resume Page"""
    return render_template('resume.html')

@app.route('/leadership')
@login_required
def leadership():
    """Leadership Page"""
    return render_template('leadership.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)