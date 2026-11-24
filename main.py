import hashlib
import hmac
import os
import secrets
import time
from datetime import timedelta, datetime
from functools import wraps

from flask import Flask, abort, make_response, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
secret_key = os.environ.get('FLASK_SECRET_KEY')
site_password = os.environ.get('SITE_PASSWORD')
site_password_hash = os.environ.get('SITE_PASSWORD_HASH') or os.environ.get('PASSWORD_HASH')
if not secret_key or not (site_password or site_password_hash):
    raise RuntimeError('Set FLASK_SECRET_KEY and either SITE_PASSWORD_HASH, PASSWORD_HASH, or SITE_PASSWORD in environment variables.')

app.secret_key = secret_key
SESSION_SECONDS = 30 * 60
app.permanent_session_lifetime = timedelta(seconds=SESSION_SECONDS)
app.config.update(
    SESSION_COOKIE_SECURE=os.environ.get('FLASK_LOCAL_HTTP') != '1',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_REFRESH_EACH_REQUEST=False,
    MAX_CONTENT_LENGTH=1024 * 1024,
)


def password_matches(candidate):
    if site_password_hash:
        return check_password_hash(site_password_hash, candidate)
    return hmac.compare_digest(
        hashlib.sha256(candidate.encode('utf-8')).digest(),
        hashlib.sha256(site_password.encode('utf-8')).digest(),
    )


def is_authenticated():
    expires_at = session.get('expires_at')
    return bool(session.get('authenticated') and isinstance(expires_at, (int, float)) and time.time() < expires_at)


@app.before_request
def expire_login():
    if session.get('authenticated') and not is_authenticated():
        session.clear()


@app.after_request
def security_headers(response):
    response.headers['Cache-Control'] = 'no-store, private'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['X-Frame-Options'] = 'DENY'
    return response


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated():
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.context_processor
def auth_context():
    return {'session_expiration_ms': int(session.get('expires_at', 0) * 1000) if is_authenticated() else 0, 'current_year': datetime.now().year}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_authenticated():
        return redirect(url_for('index'))
    if request.method == 'POST':
        password = request.form.get('password', '')
        if password_matches(password):
            session.clear()
            session.permanent = True
            session['authenticated'] = True
            session['expires_at'] = int(time.time()) + SESSION_SECONDS
            session['csrf_token'] = secrets.token_urlsafe(32)
            return redirect(url_for('index'))
        return make_response(render_template('login.html', error='Incorrect password. Please try again.'), 401)
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    token = request.form.get('csrf_token', '')
    if not hmac.compare_digest(token, session.get('csrf_token', '')):
        abort(403)
    session.clear()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/research')
@login_required
def research():
    return render_template('research.html')


@app.route('/volunteering')
@login_required
def volunteering():
    return render_template('volunteering.html')


@app.route('/hobbies')
@login_required
def hobbies():
    return render_template('hobbies.html')


@app.route('/hobbies/crochet')
@login_required
def hobbies_crochet():
    # Existing project upload did not include a crochet template.
    return redirect(url_for('hobbies') + '#crochet')


@app.route('/hobbies/languages')
@login_required
def hobbies_languages():
    return redirect(url_for('hobbies') + '#languages')


@app.route('/hobbies/journaling')
@login_required
def hobbies_journaling():
    return redirect(url_for('hobbies') + '#journaling')


@app.route('/resume')
@login_required
def resume():
    return render_template('resume.html')


@app.route('/leadership')
@login_required
def leadership():
    return render_template('leadership.html')


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8000)
