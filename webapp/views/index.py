import flask
from flask import redirect, url_for
import webapp


@webapp.app.route('/')
def show_index():
    """Show the index page."""
    
    context = {"logname": "test"}
    return flask.render_template("index.html", **context)
