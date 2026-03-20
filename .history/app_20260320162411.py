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

    df = pd.read_csv(file)

    total_rows = len(df)
    total_columns = len(df.columns)
    column_names = list(df.columns)
    missing_values = df.isnull().sum().to_dict()
    duplicate_rows = int(df.duplicated().sum())

    preview = df.head().to_html()

    return f"""
    Total Rows: {total_rows}<br>
    Total Columns: {total_columns}<br>
    Column Names: {column_names}<br>
    Missing Values: {missing_values}<br>
    Duplicate Rows: {duplicate_rows}<br><br>
    {preview}
    """

if __name__ == "__main__":
    app.run(debug=True)