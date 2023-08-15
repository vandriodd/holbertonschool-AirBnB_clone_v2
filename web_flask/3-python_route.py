#!/usr/bin/python3
"""
  3-python_route module
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_display():
    """Route handler that display a greeting message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_display():
    """Route handler that display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    """Route handler that display 'C' followed by text variable"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    """Route handler that display 'Python' followed by given text or default"""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
