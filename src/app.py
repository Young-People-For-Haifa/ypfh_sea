import os
from flask import Flask, render_template, request, session, g
from src.locales import ru, en, he
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.static_folder = "./static"
app.secret_key = os.environ.get("SECRET_KEY")


def _get_locale(lang_code: str):
    match lang_code:
        case "ru":
            return ru
        case "en":
            return en
        case "he":
            return he
        case _:
            return ru


@app.before_request
def get_locale_from_session():
    if "lang" in session:
        lang_code = session.get("lang")
        g.locale = _get_locale(lang_code)
        g.lang = lang_code


@app.route("/")
def home():
    locale = g.get("locale", None)
    lang = g.get("lang", None)
    selected_lang = request.args.get("lang", default=None)
    if locale and lang and not selected_lang:
        return render_template("index.html", locale=locale, lang=lang)
    elif selected_lang:
        selected_locale = _get_locale(selected_lang)
        session["lang"] = selected_lang
        return render_template("index.html", locale=selected_locale, lang=selected_lang)
    else:
        return render_template("index.html", locale=ru, lang="ru")
