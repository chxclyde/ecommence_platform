import flask
import webapp


@webapp.app.route('/api/services/')
def get_service():
    """service."""
    context = {
        "Item Catalog Endpoints": "/api/items",
        "Shopping Cart Endpoints": "/api/cart",
        "Checkout Endpoint": "/api/checkout"
    }

    return flask.jsonify(**context)
