from flask import Flask, render_template
from src.locale import ru

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", locale=ru)


app.run(debug=True)
