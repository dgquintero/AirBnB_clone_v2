#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from models import storage
from models import *
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
