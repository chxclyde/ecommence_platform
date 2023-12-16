import flask
import webapp


@webapp.app.route('/api/services/')
def get_index():
    """Get index page."""
    context = {
        "comments": "/api/v1/comments/",
        "likes": "/api/v1/likes/",
        "posts": "/api/v1/posts/",
        "url": "/api/v1/"
    }
    connection = webapp.model.get_db()
    print(connection)
    return flask.jsonify(**context)
