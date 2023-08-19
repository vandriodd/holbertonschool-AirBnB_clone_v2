#!/usr/bin/python3
"""
  9-states module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(e):
    """ Closes the storage connection """
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """ Displays a list of states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """ Displays a state by id and its cities"""
    state = storage.all(State).get(f"State.{id}")
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
