import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()   # reads your password and settings from the .env file

# Connect to the same database your Flask app uses
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "students_db"),
)
cursor = conn.cursor()

# Get every saved record
cursor.execute("SELECT id, name, midterm, final, total FROM results")
rows = cursor.fetchall()

# Print them
if rows:
    print("ID | Name | Midterm | Final | Total")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
else:
    print("No records saved yet.")

cursor.close()
conn.close()