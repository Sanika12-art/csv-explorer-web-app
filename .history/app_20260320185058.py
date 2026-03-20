from flask import Flask, render_template, request
import pandas as pd
import mysql.connector

app = Flask(__name__)

df_global = None

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sanika123",
        database="csv_explorer_db"
    )
    return connection

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

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO upload_history (file_name, total_rows, total_columns)
        VALUES (%s, %s, %s)
        """
        values = (file.filename, total_rows, total_columns)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    except Exception as e:
        return f"Database Error: {e}"

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

    <form action='/sort' method='post'>
        <input type='text' name='column' placeholder='Column name'>
        <select name='order'>
            <option value='asc'>Ascending</option>
            <option value='desc'>Descending</option>
        </select>
        <button type='submit'>Sort</button>
    </form>
    <br>

    <a href='/history'>View Upload History</a>
    <br><br>

    {preview}
    """

@app.route("/search", methods=["POST"])
def search():
    global df_global

    keyword = request.form["keyword"]

    filtered_df = df_global[
        df_global.astype(str).apply(
            lambda row: row.str.contains(keyword, case=False).any(), axis=1
        )
    ]

    return filtered_df.to_html()

@app.route("/sort", methods=["POST"])
def sort():
    global df_global

    column = request.form["column"]
    order = request.form["order"]

    if order == "asc":
        sorted_df = df_global.sort_values(by=column, ascending=True)
    else:
        sorted_df = df_global.sort_values(by=column, ascending=False)

    return sorted_df.to_html()

@app.route("/history")
def history():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM upload_history")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)