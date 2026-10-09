# Marks Calculator

A simple Flask web app. The user enters a student's name, midterm mark and final mark. The app calculates the total, shows it on the page, and saves every result in a MySQL database.

## Features

- Web form for name, midterm and final marks
- Calculates the total mark
- Saves each result in a MySQL database
- "Saves every result in MySQL (view them with view_db.py)"

## Technologies used

- Python 3
- Flask (backend)
- MySQL (database)
- HTML and CSS (frontend)

## Requirements

- Python 3 installed
- MySQL server installed and running (for example through XAMPP)

## Setup

1. Open a terminal inside the project folder.
2. Install the libraries:
3. Copy `.env.example` to `.env` and enter your MySQL password.```

   pip install -r requirements.txt

```

3. Open `app.py` and set your MySQL username and password in `DB_CONFIG`.
4. Make sure the MySQL server is running.
5. Start the app:

```

python app.py

```

6. Open http://127.0.0.1:5000 in your browser.

The app creates the `students_db` database and the `results` table automatically on the first run. You can also create them manually by running `schema.sql` in MySQL.

## Project structure

```

python_practise/
├── .gitignore
├── app.py # Flask backend and database code
├── schema.sql # SQL commands that create the database and table
├── view_db.py # helper script to print saved records
├── requirements.txt # libraries the project needs
├── README.md # this file
└── templates/
└── index.html # the web page (form, result, table)

```

## How it works

1. The user fills in the form and clicks **Calculate**.
2. Flask reads the form values with `request.form`.
3. The `calculate()` function adds the midterm and final marks.
4. The result is saved in the `results` table.
5. The page shows the result for the submitted marks.

## Author

Maxwel Ochieng Odhiambo
```
