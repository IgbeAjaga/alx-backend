#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from jinja2 import escape

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.args.get('locale') \
        or g.user.locale \
        or request.accept_languages.best_match(app.config['LANGUAGES']) \
        or app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    g.user = get_user(request.args.get('login_as'))

def get_user(user_id):
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    return users.get(int(user_id))

@app.route('/')
def index():
    if g.user:
        welcome_message = _('You are logged in as %(username)s.', username=escape(g.user['name']))
    else:
        welcome_message = _('You are not logged in.')
    return render_template('3-index.html', welcome_message=welcome_message)

if __name__ == '__main__':
    app.run()
