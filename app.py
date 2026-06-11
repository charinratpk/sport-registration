from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        
        name = request.form["name"]
        nickname = request.form["nickname"]
        classroom = request.form["classroom"]
        level = request.form["level"]
        gender = request.form["gender"]
        sport = request.form["sport"]

        register_time = datetime.now().strftime(
            "%D/%m/%Y %H:%M:%S"
        )

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO registrations
            (name,nickname,classroom,level,gender,sport,register_time)

            VALUES
            (?,?,?,?,?,?,?)
            """,
            (name, 
             nickname, 
             classroom, 
             level, 
             gender, 
             sport, 
             register_time
            )
        )

        conn.commit()
        conn.close()

    return render_template("index.html")

@app.route("/list")
def show_list():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT  id, 
            name, 
            nickname, 
            classroom, 
            level, 
            gender, 
            sport, 
            register_time
    FROM registrations
    """)

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "list.html",
        students=students
    )

if __name__ == "__main__":
    app.run(debug=True)