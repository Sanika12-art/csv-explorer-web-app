from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Global variable to store data
df_global = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global df_global

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    df = pd.read_csv(file)
    df_global = df

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

    <form action='/search' method='post'>
        <input type='text' name='keyword' placeholder='Search...'>
        <button type='submit'>Search</button>
    </form>
    <br>

    {preview}
    """

@app.route("/search", methods=["POST"])
def search():
    global df_global

    keyword = request.form["keyword"]

    # Filter rows containing keyword
    filtered_df = df_global[df_global.astype(str).apply(lambda row: row.str.contains(keyword, case=False).any(), axis=1)]

    return filtered_df.to_html()

if __name__ == "__main__":
    app.run(debug=True)