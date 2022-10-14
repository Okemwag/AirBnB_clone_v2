#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
"""
from flask import Flask, escape, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/number_odd_or_even/<int:n>')
def render_num_odd_even(n):
    """ Returns HTML page only if n is int when app.route queried,
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_template/<int:n>')
def render_num(n):
    """ Returns HTML page only if n is int when app.route queried,
    """
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>')
def display_int(n):
    """ Returns string confirming if n is int when app.route queried,
    """
    return '%d is a number' % n


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def display_python(text):
    """ Returns string with text variable when app.route queried,
        Default text value: "is cool"
    """
    return 'Python %s' % escape(text.replace("_", " "))


@app.route('/c/<text>')
def display_c(text):
    """ Returns string with text variable when app.route queried
    """
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/hbnb')
def display_hbnb():
    """ Returns string when specified app.route queried
    """
    return 'HBNB'


@app.route('/')
def display_hello():
    """ Returns string when specified app.route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
