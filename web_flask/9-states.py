#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from models import storage
from models import *
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def display_states(state_id=None):
    states = storage.all("State")
    if state_id is not None:
            state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
