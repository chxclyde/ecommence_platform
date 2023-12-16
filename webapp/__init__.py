"""webapp package initializer."""
import flask


# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name


# Read settings from config module (webapp/config.py)
app.config.from_object('webapp.config')


# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import webapp.api  # noqa: E402  pylint: disable=wrong-import-position
import webapp.views  # noqa: E402  pylint: disable=wrong-import-position
import webapp.model  # noqa: E402  pylint: disable=wrong-import-position
