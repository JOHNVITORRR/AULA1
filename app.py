from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

