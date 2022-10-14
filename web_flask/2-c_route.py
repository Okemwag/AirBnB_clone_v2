#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
"""
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/c/<text>')
def display_c(text):
    """ Returns string with text variable when specified app.route is queried
    """
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/')
def display_hello():
    """ Returns string when specified app.route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """ Returns string when specified app.route is queried
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
