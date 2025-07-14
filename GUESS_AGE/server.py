from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def first_page():
    return 'Yo! Yo! Give a name to the URL.. Like localhost/NAME'


@app.route("/<name>")
def home(name):
    data_gender=requests.get(f"https://api.genderize.io?name={name}")
    data_age=requests.get(f"https://api.agify.io?name={name}")
    gender=data_gender.json()["gender"]
    age=data_age.json()["age"]
    return render_template("index.html",name=name,gender=gender,age=age)

if __name__=="__main__":
    app.run(debug=True)