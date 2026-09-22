from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Create database and table
def create_database():
    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT NOT NULL,
            department TEXT NOT NULL,
            subject TEXT NOT NULL,
            rating INTEGER NOT NULL,
            comments TEXT
        )
    """)

    conn.commit()
    conn.close()


create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    roll_number = request.form["roll_number"]
    department = request.form["department"]
    subject = request.form["subject"]
    rating = request.form["rating"]
    comments = request.form["comments"]

    conn = sqlite3.connect("feedback.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback
        (name, roll_number, department, subject, rating, comments)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        roll_number,
        department,
        subject,
        rating,
        comments
    ))

    conn.commit()
    conn.close()

    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)