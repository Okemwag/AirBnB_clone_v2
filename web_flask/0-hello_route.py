#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Returns string when specified app.route is queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
