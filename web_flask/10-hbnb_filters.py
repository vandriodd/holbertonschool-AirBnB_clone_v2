#!/usr/bin/python3
"""
  10-hbnb_filters module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenities import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(e):
    """ Closes the storage connection """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb():
    """ Displays hbnb filters template """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
