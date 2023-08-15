#!/usr/bin/python3
"""
  5-number_template module
"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_display(n):
    """Route handler that displays if given arg is a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display HTML template if given arg is a number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)