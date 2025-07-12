import random

from flask import Flask

app = Flask(__name__)

RANDOM_NUMBER=random.randint(1,10)

@app.route('/')
def home():
    return "<h1 style=""align:center""> Choose a random number between 1-10 </h1>"

@app.route('/<int:choice>')
def declare(choice):
    if choice==RANDOM_NUMBER:
        return '<h1>Yeah correct Choice</h1> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif choice>RANDOM_NUMBER:
        return '<h1>TOO HIGH</h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    elif choice<RANDOM_NUMBER:
        return '<h1>TOO LOW</h1> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    return None



if __name__ == '__main__':
    app.run(debug=True)
