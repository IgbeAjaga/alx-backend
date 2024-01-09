#!/usr/bin/env python3
"""5-app.py - Mocking user login system"""

from flask import Flask, render_template, request, g
from typing import Dict, Union
import flask_babel
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Return user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set the user"""
    g.user = get_user()


@app.route('/')
def index():
    """Render index template"""
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
