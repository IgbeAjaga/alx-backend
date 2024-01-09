#!/usr/bin/env python3
"""Force locale with URL parameter"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Render index template with forced locale"""
    locale = request.args.get('locale')
    return render_template('4-index.html', locale=locale)


if __name__ == '__main__':
    app.run()
