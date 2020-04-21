#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return 'C {}'.format(escape(text.replace("_", " ")))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text ='is cool'):
    return 'Python {}'.format(escape(text.replace("_", " ")))

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
