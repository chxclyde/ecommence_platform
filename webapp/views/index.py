import flask
from flask import redirect, url_for
import webapp


@webapp.app.route('/')
def show_index():
    """Show the index page."""
    
    context = {"logname": "test"}
    return flask.render_template("userindex.html", **context)

@webapp.app.route('/admin/')
def show_adminindex():
    """Show the admin index page."""
    context = {}
    return flask.render_template("adminindex.html", **context)

@webapp.app.route('/cart/')
def show_cart_page():
    """Show the cart page."""
    context = {}
    return flask.render_template("cart.html", **context)

