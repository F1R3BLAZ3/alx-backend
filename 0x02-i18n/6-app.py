#!/usr/bin/env python3

"""
Basic Flask app with a single route, Babel integration, language selection,
and user login emulation.
"""

from flask import Flask, render_template, g, request
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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> Optional[dict]:
    """
    Retrieve user information based on user ID.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Execute before all other functions and set logged-in user information.
    """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best-matching language for the user.
    """
    # Check if the 'locale' parameter is present in the request
    # and is a supported locale
    if 'locale' in request.args and request.args['locale'] in app.config[
            'LANGUAGES']:
        return request.args['locale']

    # Check if the user is logged in and their preferred locale is supported
    if hasattr(g, 'user') and g.user and g.user.get('locale') in app.config[
            'LANGUAGES']:
        return g.user.get('locale')

    # Check the request header for preferred language
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Resort to the default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    """
    Render the index.html template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
