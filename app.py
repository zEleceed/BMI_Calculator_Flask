from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        try:
            height = float(request.form["number1"])
            weight = float(request.form["number2"])
            bmi = weight / (height * height)
            result = f"Your BMI is : {bmi:.2f}"
        except ValueError:
            result = "Invalud input."
    else:
        result = None

    return render_template("base.html", result=result)


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password,))
        account = cursor.fetchone()
        if account:
            session["loggedin"] = True
            session["id"] = account["id"]
            session['username'] = account['username']
            msg = "Logged in succesfully !"
            return render_template('index.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
