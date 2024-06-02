from flask import Flask, render_template, request, make_response, session
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

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
