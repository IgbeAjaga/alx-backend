#!/usr/bin/env python3
"""Display the current time"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    user_locale = request.args.get('locale')
    if user_locale in Config.LANGUAGES:
        return user_locale
    elif g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    g.user = None
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        g.user = users[int(user_id)]

@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone')
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE

@app.route('/')
def index():
    if g.user:
        username = g.user['name']
    else:
        username = None
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime('%b %d, %Y, %I:%M:%S %p')  # Format time
    return render_template('8-index.html', username=username, current_time=current_time)

if __name__ == '__main__':
    app.run()
