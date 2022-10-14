#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
"""
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


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
