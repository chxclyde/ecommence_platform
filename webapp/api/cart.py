import flask
import webapp
from flask import jsonify, request


# Define the route to retrieve the contents of the user's shopping cart
@webapp.app.route('/api/cart/', methods=['GET'])
def get_cart():
    """
    Description: Retrieves the contents of the user's shopping cart.
    Response: An array of items in the cart, including quantities.
    """
    # Replace this with your logic to retrieve the user's cart contents from the database
    cart_contents = fetch_cart_contents()

    return jsonify(cart_contents)



# Define the route to add an item to the shopping cart
@webapp.app.route('/api/cart/add/', methods=['POST'])
def add_to_cart():
    """
    Description: Adds an item to the shopping cart.
    Request Body: The item ID and the quantity to add.
    Response: Updated contents of the shopping cart.
    """
    # Get item ID and quantity from the request body
    data = request.get_json()
    item_id = data.get("item_id")
    quantity = data.get("quantity")

    # Replace this with your logic to add the item to the user's cart in the database
    add_item_to_cart(item_id, quantity)

    # Retrieve and return the updated cart contents
    cart_contents = fetch_cart_contents()

    return jsonify(cart_contents), 201



# Define the route to remove an item from the shopping cart
@webapp.app.route('/api/cart/remove/', methods=['POST'])
def remove_from_cart():
    """
    Description: Removes an item from the shopping cart.
    Request Body: The item ID and the quantity to remove.
    Response: Updated contents of the shopping cart.
    """
    # Get item ID and quantity from the request body
    data = request.get_json()
    item_id = data.get("item_id")
    quantity = data.get("quantity")

    # Replace this with your logic to remove the item from the user's cart in the database
    remove_item_from_cart(item_id, quantity)

    # Retrieve and return the updated cart contents
    cart_contents = fetch_cart_contents()

    return jsonify(cart_contents), 200

