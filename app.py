from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()   # reads your password and settings from the .env file

app = Flask(__name__)

# Connection settings come from the .env file
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "students_db"),
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    # Step 1: connect to the MySQL server only (no database name yet)
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor.close()
    conn.close()

    # Step 2: connect to the database and create the table
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            midterm INT,
            final INT,
            total INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def calculate(midterm, final):
    return midterm + final

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    result = None

    if request.method == "POST":
        name = request.form["name"]
        midterm = int(request.form["midterm"])
        final = int(request.form["final"])
        result = calculate(midterm, final)

        # Save to the database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO results (name, midterm, final, total) VALUES (%s, %s, %s, %s)",
            (name, midterm, final, result)
        )
        conn.commit()
        cursor.close()
        conn.close()

    return render_template("index.html", name=name, result=result)
if __name__ == "__main__":
    init_db()
    app.run(debug=True)