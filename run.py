import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about1") # що сюди введемо те і буде відображатися в кінці url адреси
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

    # Ми ніколи не повинні мати «debug=True» у робочій програмі
    # або коли ми подаємо наші проекти на оцінку.
    # Це дуже важливо, тому що debug=True може дозволити запуск довільного коду, і, очевидно, це недолік безпеки.
    # Ви повинні мати лише debug=True під час тестування програми в режимі розробки, але змініть його на debug=False перед тим, як надсилати свій проект.
