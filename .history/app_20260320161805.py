from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    # Read CSV using pandas
    df = pd.read_csv(file)

    # Take first 5 rows as preview
    preview = df.head().to_html()

    return preview

if __name__ == "__main__":
    app.run(debug=True)