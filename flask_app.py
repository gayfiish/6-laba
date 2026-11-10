from pathlib import Path
from uuid import uuid4
from flask import Flask, render_template, request

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

UPLOAD_FOLDER = Path(__file__).resolve().parent / "uploads"
ALLOWED_EXTENSIONS = {".txt", ".pdf", ".png", ".jpg", ".jpeg"}


@app.route("/", methods=["GET", "POST"])
def index():
    greeting = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if name:
            greeting = f"Привет, {name}!"

    return render_template("index.html", greeting=greeting)


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")

    if not file or not file.filename:
        message = "Выберите файл."
    else:
        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            message = "Недопустимый формат файла."
        else:
            UPLOAD_FOLDER.mkdir(exist_ok=True)

            filename = f"{uuid4().hex}{extension}"
            file.save(UPLOAD_FOLDER / filename)

            message = f"Файл {file.filename} успешно загружен!"

    return render_template("index.html", upload_message=message)


if __name__ == "__main__":
    app.run(debug=True)