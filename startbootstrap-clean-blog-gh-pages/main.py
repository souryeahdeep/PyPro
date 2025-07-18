from flask import Flask,render_template
import requests
'''
A Blog Project
'''

app=Flask(__name__)
response=requests.get("https://api.npoint.io/ad8c79fb8795a8535d1c")
blogs = response.json()

@app.route("/")
def home():
    return render_template("index.html",blogs=blogs)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")   

@app.route('/posts/<int:id>')
def posts(id):
    print(id)
    return render_template("post.html",blog=blogs[id-1])



if __name__=='__main__':
    app.run(debug=True)
