from flask import Flask
from flask import render_template, request

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the first line of flask code. Hope you remember this."

# @app.route("/nigger")
# def niggers():
#     return "This is a page for niggers"

@app.route("/index", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name'] # derived from the id of the input type.. in our case it is "name"
        return f"Name of the person is {name}"
    return render_template("form.html")


@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name'] # derived from the id of the input type.. in our case it is "name"
        return f"Name of the person is {name}"
    return render_template("form.html")



    
if __name__ == "__main__":
    app.run(debug = True) #debug = true is used so tht we dont hav to restart the app everytime some changes are made. only needs to be saved.
    
    

