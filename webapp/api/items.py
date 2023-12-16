import flask
import webapp
from flask import jsonify

# Endpoint to retrieve all items
@webapp.app.route('/api/items/', methods=['GET'])
def get_items():
    """
    Description: Retrieves a list of all items in the catalog.
    Response: An array of items, each with a unique ID, name, description, and price.
    """
    db = webapp.model.get_db()
    cursor = db.execute("""
        SELECT items.id, items.name, items.description, items.price, catalog_items.quantity
        FROM items
        LEFT JOIN catalog_items ON items.id = catalog_items.item_id
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
            "quantity": item["quantity"]
        }
        item_list.append(item_data)

    return jsonify(item_list)

# Endpoint to add a new item (admin-only)
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
    new_item = {
        "id": len(catalog) + 1,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"]
    }
    catalog.append(new_item)
    return jsonify(new_item), 201

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

    # Find the item with the specified item_id
    item = next((item for item in catalog if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404

    # Update item details from the request body
    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["description"] = data.get("description", item["description"])
    item["price"] = data.get("price", item["price"])
    return jsonify(item)

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

    # Find and remove the item with the specified item_id
    item = next((item for item in catalog if item["id"] == item_id), None)
    if item is None:
        return "Item not found", 404

    catalog.remove(item)
    return "Item deleted", 204

# Function to check if a user is an admin (you need to implement this)
def user_is_admin():

    return True  # For testing purposes, assume the user is an admin