import os
from flask import Flask, render_template, request
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
    lang_code = request.args.get("lang", default=None)
    if lang_code:
        match lang_code:
            case "ru":
                locale = default
            case "en":
                locale = en
            case "he":
                locale = he
            case _:
                locale = default
    else:
        locale = default
    return render_template("index.html", locale=locale, lang=lang_code)
