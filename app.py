from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_restful import Resource
# Local imports
from config import app, db, api
from models import *


class CheckSession(Resource):
    """this allows a user to stay logged in to the site even after refresh
    since the user_id will not be removed from the session until a request is
    made to /logout"""

    def get(self):
        user = User.query.filter(User.id == session.get("user_id")).first()
        if not user:
            return make_response({"error": "Unauthorized: you must be logged in to make that request"}, 401)
        else:
            return make_response(user.to_dict(), 200)


api.add_resource(CheckSession, '/check_session', endpoint='check_session')


class Signup(Resource):
    def post(self):
        if request.is_json:
            json = request.get_json()
        else:
            json = request.form
        try:
            user = User(
                username=json['username'],
                name=json['name'],
            )
            user.password_hash = json['password']
            db.session.add(user)
            db.session.commit()
            # allow user to sign in right after signing up
            session["user_id"] = user.id

            return make_response(user.to_dict(), 201)
        except Exception as e:
            return make_response({'errors': str(e)}, 422)


api.add_resource(Signup, '/signup', endpoint='signup')


class Login(Resource):
    def post(self):
        try:
            if request.is_json:
                json = request.get_json()
                print("Received JSON data:", json)
            else:
                json = request.form.to_dict()
                print("Received JSON data:", json)
            username = json.get('username')
            password = json.get("password")
            print("Username:", username)
            print("Password:", password)
            user = User.query.filter(User.username == username).first()
            print("User:", user)
            if not user:
                response_body = {"error": "User not found"}
                status = 404
            else:
                if user.authenticate(password):
                    session['user_id'] = user.id
                    return redirect(url_for('bmi_calc'))
                    # response_body = user.to_dict()
                    # status = 200
                else:
                    response_body = {'error': 'Invalid username or password'}
                    status = 401
            return make_response(response_body, status)

        except Exception as e:
           return make_response({'errors': str(e)}, 422)


api.add_resource(Login, '/login', endpoint='login')


class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {}, 204


api.add_resource(Logout, '/logout', endpoint='logout')


@app.route("/", methods=["GET", "POST"])
def bmi_calc():
    if request.method == "POST":
        try:
            height = float(request.form["number1"])
            weight = float(request.form["number2"])
            bmi = weight / (height * height)
            result = f"Your BMI is : {bmi:.2f}"
        except ValueError:
            result = "Invalid input."
    else:
        result = None

    return render_template("base.html", result=result)


@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route("/signup", methods=["GET"])
def signup_page():
    return render_template("signup.html")


@app.route("/logout", methods=["GET"])
def logout_page():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
