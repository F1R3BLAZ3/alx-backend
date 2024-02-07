#!/usr/bin/env python3

"""
Basic Flask app with a single route, Babel integration, and language selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best-matching language for the user.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render the index.html template.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
