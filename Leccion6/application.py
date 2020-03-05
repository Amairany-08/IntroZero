from flask import Flask, render_template, request, session
import random
from datetime import timedelta
app = Flask(__name__)

#Ejercicio1
"""
@app.route("/")
def index():
    return "Hello, World!"
"""
#Ejercicio 2
"""
@app.route("/")
def index():
    return "Hello, World!"
@app.route("/david")
def david():
    return "Hello, David!"
"""
#Ejercicio 3
"""
@app.route("/")
def index():
    return "Hello, World!"
@app.route("/david")
def david():
    return "Hello, David!"
@app.route("/maria")
def maria():
    return "Hello, Maria!"
"""
#Ejercicio 4
"""
@app.route("/")
def index():
    return "Hello, World!"
@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!
"""
#Ejercicio 5
"""
@app.route("/")
def index():
    return render_template("index.html")

"""
#Ejercicio 6
"""
@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)
"""
#Ejercicio 7
"""
@app.route("/")
def index():
    headline = "Hola k ase XDXD!"
    return render_template("index.html", headline=headline)
@app.route("/bye")
def bye():
    headline = "GoodBye!"
    return render_template("index.html", headline=headline)
"""
#Ejercio 8
"""
@app.route("/")
def index():
    headline = random.choice(["Hello, world!","Hi there!", "Good morning!"])
    return render_template("index.html", headline=headline)
"""
#Ejercicio 9
"""
@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = (now.month == 1) and (now.day == 1)
    new_year = True
    return render_template("index.html", new_year=new_year)
"""
#Ejercicio 10
"""
@app.route("/")
def index():
    names =["Alice","Bob","Charlie"]
    return render_template("index.html", names=names)
"""
#Ejercicio 11
"""
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/more")
def more():
    return render_template("more.html")
"""
#Ejercicio 12
"""
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html",name=name)

"""
#Ejercicio 13
"""
@app.route("/hello", methods=["POST","GET"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)
"""
#Ejercicio 14
"""
app.secret_key="whatever"
app.permanent_session_lifetime=timedelta(minutes=1)
@app.route("/", methods=["GET","POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        session.permanent = True
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("index.html",notes=session["notes"])
"""