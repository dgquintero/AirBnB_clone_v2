#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from models import storage
from models import *
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
