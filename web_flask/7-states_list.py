#!/usr/bin/python3
"""
  7-states_list module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_connection(e):
    """ Closes the storage connection """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ Displays a list of states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
