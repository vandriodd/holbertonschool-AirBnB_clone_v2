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


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_state():
    """ Displays state by id or states """
    states = storage.all(State).values()

    if id is None:
        all_states = states.values()
    else:
        key = f"State.{id}"
        all_states = [states[key]] if key in states else []
    return render_template('9-states.html', states=all_states,
                           len=len(all_states))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
