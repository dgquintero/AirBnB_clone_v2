#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from models import storage
from models import *
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, 
                           amenities=amenities)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
