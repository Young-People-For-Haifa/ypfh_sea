import logging
import os
from flask import Flask, render_template, request, session
from flask_babel import Babel
from src.locale import Config, default, en, he


def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.static_folder = "./static"
app.secret_key = os.environ.get("SECRET_KEY")
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def home():
    locale = get_locale()
    if locale == "ru":
        lang_code = "ru"
    elif locale == "en":
        lang_code = "en"
    else:
        lang_code = "he"
    return render_template("index.html", locale=default, lang=lang_code)


app.run(debug=True)
