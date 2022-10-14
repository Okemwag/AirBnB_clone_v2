#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
    Fetches data from FileStorage, creates dynamic HTML page, closes db session
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/<text>')
def render_specific_states_page(text):
    """ Returns HTML page filled with data from FileStorage engine
    """
    states_id = "Not found!"
    objs = storage.all()
    for key, value in objs.items():
        if key.split(".")[1] == text:
            states_id = value
    return render_template('9-states.html', states=None, state=states_id)


@app.route('/states')
def render_cities_states_page():
    """ Returns HTML page filled with data from FileStorage engine
    """
    states_list = []
    objs = storage.all()
    for key, value in objs.items():
        if key.split(".")[0] == "State":
                states_list.append(value)
    return render_template('9-states.html', states=states_list, state=None)


@app.teardown_appcontext
def teardown_db(self):
    """ Closes database session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
