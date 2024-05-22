from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        try:
            height = float(request.form["number1"])
            weight = float(request.form["number2"])
            bmi =  weight / (height*height)
            result = f"Your BMI is : {bmi:.2f}"
        except ValueError:
            result = "Invalud input."
    else:
        result = None

    return render_template("base.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
