#!/usr/bin/python3
""" Flask script starts web application
    Listening on 0.0.0.0:5000
    Fetches data from FileStorage, creates dynamic HTML page, closes db session
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def render_states_page():
    """ Returns HTML page filled with data from FileStorage engine
    """
    states_list = []
    objs = storage.all()
    for key, value in objs.items():
        if key.split(".")[0] == "State":
                states_list.append(value)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown_db(self):
    """ Closes database session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
