# 📊 CSV Explorer Web App

A web-based application built using Python, Flask, MySQL, Pandas, HTML, CSS, and Jinja2 that allows users to upload and explore CSV files easily.

---

## 🚀 Project Overview

CSV Explorer Web App enables users to:

- Upload CSV files  
- Preview dataset  
- Analyze data (rows, columns, missing values, duplicates)  
- Search, filter, and sort data  
- Store upload history in MySQL  
- Delete records from history  

---

## ✨ Features

- Upload CSV file  
- Preview first 5 rows of dataset  
- Total rows & columns count  
- Column names display  
- Missing values detection  
- Duplicate rows detection  
- Search functionality  
- Sort data by column (asc/desc)  
- Store upload history in MySQL  
- Delete history records with confirmation  
- Clean and responsive UI  

---

## 🛠️ Tech Stack

- Backend: Python, Flask  
- Database: MySQL  
- Data Processing: Pandas  
- Frontend: HTML, CSS, Jinja2  
- Tools: VS Code  

---

## 📂 Project Structure

csv-explorer-web-app/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── history.html
│
├── static/
│   └── css/
│       └── style.css
│
├── venv/
└── README.md

---

## 🗃️ Database Setup

Run the following SQL in MySQL:

CREATE DATABASE csv_explorer_db;

USE csv_explorer_db;

CREATE TABLE upload_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    total_rows INT,
    total_columns INT,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

## ⚙️ Installation & Setup

1. Clone the repository
git clone <your-repo-link>
cd csv-explorer-web-app

2. Create virtual environment
python -m venv venv

3. Activate virtual environment (Windows)
venv\Scripts\activate

4. Install dependencies
pip install flask pandas mysql-connector-python

5. Update database credentials
Open app.py and update:
password="your_mysql_password"

6. Run the application
python app.py

7. Open in browser
http://127.0.0.1:5000

---

## 🎯 How It Works

1. User uploads CSV file  
2. Flask processes file using pandas  
3. Data insights are generated  
4. Results displayed on UI  
5. Upload history stored in MySQL  
6. User can delete records  

---

## 💡 Future Improvements

- Pagination for large datasets  
- Download filtered CSV  
- Charts & visualization  
- User authentication  

---

## 👩‍💻 Author

Sanika Patil