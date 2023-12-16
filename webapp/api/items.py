import flask
import webapp
from flask import jsonify,request

# Endpoint to retrieve all items
@webapp.app.route('/api/items/', methods=['GET'])
def get_items():
    """
    Description: Retrieves a list of all items in the catalog.
    Response: An array of items, each with a unique ID, name, description, and price.
    """
    db = webapp.model.get_db()
    cursor = db.execute("""
        SELECT items.id, items.name, items.description, items.price
        FROM items
    """)

    items = cursor.fetchall()

    # Define a list to store the item data
    item_list = []

    # Format the item data as specified in the response
    for item in items:
        item_data = {
            "id": item["id"],
            "name": item["name"],
            "description": item["description"],
            "price": item["price"],
        }
        item_list.append(item_data)

    return jsonify(item_list)


#endpoint for adding a new item
@webapp.app.route('/api/items/', methods=['POST'])
def add_item():
    """
    Description: Adds a new item to the catalog (Admin only).
    Request Body: Contains the name, description, and price of the item.
    Response: Details of the added item.
    """
    # Check if the user is an admin (you need to implement authentication)
    if not user_is_admin():
        return "Permission denied", 403

    # Get item data from the request body
    data = request.get_json()

    # Insert the new item into the database
    try:
        db = webapp.model.get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
            (data["name"], data["description"], data["price"])
        )
        item_id = cursor.lastrowid
        cursor.close()

        # Format the added item data
        new_item = {
            "id": item_id,
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
        }

        return jsonify(new_item), 201  # Respond with the added item data and 201 status code

    except Exception as e:
        print("Error adding item:", str(e))
        return "Failed to add item", 500

# Endpoint to delete an item (admin-only)
@webapp.app.route('/api/items/<int:item_id>/', methods=['DELETE'])
def delete_item(item_id):
    """
    Description: Removes an item from the catalog (Admin only).
    Response: A confirmation message indicating successful removal.
    """
    # Check if the user is an admin (you need to implement authentication)
    if not user_is_admin():
        return "Permission denied", 403

    # Delete the item from the database
    try:
        db = webapp.model.get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        db.commit()
        cursor.close()

        return "Item deleted", 204  # Respond with a confirmation message and 204 status code

    except Exception as e:
        print("Error deleting item:", str(e))
        return "Failed to delete item", 500


# Endpoint to update an existing item (admin-only)
@webapp.app.route('/api/items/<int:item_id>/', methods=['PUT'])
def update_item(item_id):
    """
    Description: Updates the details of an existing item (Admin only).
    Request Body: Contains the updated name, description, and/or price.
    Response: Details of the updated item.
    """
    # Check if the user is an admin (you need to implement authentication)
    if not user_is_admin():
        return "Permission denied", 403
    # to be done.

    return



# Function to check if a user is an admin
def user_is_admin():

    return True  # For testing purposes, assume the user is an admin