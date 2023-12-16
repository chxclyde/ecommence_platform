import flask
import webapp
from flask import jsonify, request


def fetch_cart_contents(user_id):
    try:
        db = webapp.model.get_db()
        cursor = db.execute("""
            SELECT cart_items.item_id, items.name, items.description, items.price, cart_items.quantity
            FROM cart_items
            JOIN items ON cart_items.item_id = items.id
            WHERE cart_items.cart_id = (SELECT id FROM carts WHERE user_id = ?)
        """, (user_id,))
        cart_items = cursor.fetchall()

        # Define a list to store the cart item data
        cart_data = []

        # Format the cart item data as specified in the response
        for cart_item in cart_items:
            cart_item_data = {
                "item_id": cart_item["item_id"],
                "name": cart_item["name"],
                "description": cart_item["description"],
                "price": cart_item["price"],
                "quantity": cart_item["quantity"]
            }
            cart_data.append(cart_item_data)

        return cart_data
    except Exception as e:
        print("Error fetching cart contents:", str(e))
        return []


# Define the route to retrieve the contents of the user's shopping cart
@webapp.app.route('/api/cart', methods=['GET'])
def get_cart():
    """
    Description: Retrieves the contents of the user's shopping cart.
    Response: An array of items in the cart, including quantities.
    """
    # Get the user's cart items from the database
    cart_data = fetch_cart_contents(1)
    return jsonify(cart_data)


# Define the route to add an item to the shopping cart
@webapp.app.route('/api/cart/add/', methods=['POST'])
def add_to_cart():
    """
    Description: Adds an item to the shopping cart.
    Request Body: The item ID and the quantity to add.
    Response: Updated contents of the shopping cart.
    """
    data = request.get_json()
    item_id = data.get("item_id")
    quantity = data.get("quantity")
    user_id = 1
    cart_id = 1
    try:
        db = webapp.model.get_db()
        cursor = db.cursor()
        # Check if the item already exists in the cart
        cursor.execute(
            "SELECT id FROM cart_items WHERE cart_id = ? AND item_id = ?",
            (cart_id, item_id)
        )
        existing_item = cursor.fetchone()

        if existing_item:
            # If the item exists, update the quantity
            cursor.execute(
                "UPDATE cart_items SET quantity = quantity + ? WHERE id = ?",
                (quantity, existing_item["id"])
            )
        else:
            # If the item does not exist, insert a new row
            cursor.execute(
                "INSERT INTO cart_items (cart_id, item_id, quantity) VALUES (?, ?, ?)",
                (cart_id, item_id, quantity)
            )

        db.commit()
    except Exception as e:
        print("Error inserting/updating item in cart:", str(e))
    return fetch_cart_contents(1)


# Define the route to remove an item from the shopping cart
@webapp.app.route('/api/cart/remove/', methods=['POST'])
def remove_from_cart():
    """
    Description: Removes an item from the shopping cart.
    Request Body: The item ID and the quantity to remove.
    Response: Updated contents of the shopping cart.
    """
    try:
        # Get item ID and quantity from the request body
        data = request.get_json()
        item_id = data.get("item_id")
        quantity = data.get("quantity")
        user_id = 1
        cart_id = 1

        # Check if the item is in the cart
        db = webapp.model.get_db()
        cursor = db.execute(
            """
            SELECT id, quantity
            FROM cart_items
            WHERE cart_id = ? AND item_id = ?
            """,
            (cart_id, item_id),
        )
        item_in_cart = cursor.fetchone()

        if item_in_cart:
            # Item is in the cart, decrease the quantity or remove if necessary
            current_quantity = item_in_cart["quantity"]
            new_quantity = current_quantity - quantity

            if new_quantity <= 0:
                # Remove the item from the cart if quantity is zero or negative
                db.execute(
                    """
                    DELETE FROM cart_items
                    WHERE cart_id = ? AND item_id = ?
                    """,
                    (cart_id, item_id),
                )
            else:
                # Update the quantity if it's greater than zero
                db.execute(
                    """
                    UPDATE cart_items
                    SET quantity = ?
                    WHERE cart_id = ? AND item_id = ?
                    """,
                    (new_quantity, cart_id, item_id),
                )
            db.commit()

        # Retrieve and return the updated cart contents
        cart_contents = fetch_cart_contents(user_id)

        return jsonify(cart_contents), 200
    except Exception as e:
        print("Error removing item from cart:", str(e))
        return "Failed to remove item from cart", 500


@webapp.app.route('/api/checkout', methods=['POST'])
def process_checkout():
    """
    Description: Processes the checkout with the items in the cart.
    Request Body: User information and shipping address.
    Response: Confirmation of the order with an order ID.
    """

    # Get user information and shipping address from the request body
    data = request.get_json()
    user_info = data.get("user")
    shipping_address = data.get("shipping_address")
    payment = data.get("payment")
    cart_id = 1

    db = webapp.model.get_db()

    cursor = db.execute("""
        SELECT SUM(items.price * cart_items.quantity) as total_price
        FROM cart_items
        JOIN items ON cart_items.item_id = items.id
        WHERE cart_items.cart_id = 1
    """)
    result = cursor.fetchone()
    total_price = result["total_price"]

    # Insert the order into the orders table
    cursor = db.execute(
        """
        INSERT INTO orders (user_id, total_price, shipping_address, payment_method)
        VALUES (?, ?, ?, ?)
        """,
        (1, total_price, shipping_address, payment)
    )
    order_id = cursor.lastrowid

    # Transfer items from the cart to order_items
    db.execute(
        """
        INSERT INTO order_items (order_id, item_id, quantity)
        SELECT ?, item_id, quantity
        FROM cart_items
        WHERE cart_id = 1
        """,
        (order_id,)
    )
    db.commit()

    # Clear the user's cart after successful checkout (assuming cart_id is 1)
    db = webapp.model.get_db()
    db.execute(
        """
        DELETE FROM cart_items
        WHERE cart_id = 1
        """
    )
    db.commit()

    # Return the order confirmation with the order ID
    response_data = {"order_id": 1}
    return jsonify(response_data), 201
