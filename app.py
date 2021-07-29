from flask import Flask, render_template, request

import Mileage

app=Flask(__name__)


@app.route("/", methods = ['POST'])
def hello():
    if request.method == "POST":
       Fuel = request.form['Fuel']
       Travel_Distance = Mileage.Mileage_Prediction(Fuel)
       print(Travel_Distance)

    return render_template("index.html")


# @app.route("/sub",methods = ['POST'])
# def submit():
#     #HTML -- .PY
#     if request.method == "POST":
#         name = request.form["username"]

#     #.PY -- HTML

#     return render_template("sub.html", n = name)
    




if __name__=="__main__":
    app.run(debug=True)