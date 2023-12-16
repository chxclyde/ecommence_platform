# 1. Item Catalog Endpoints
## GET /api/items

Description: Retrieves a list of all items in the catalog. \
Response: An array of items, each with a unique ID, name, description, and price.\
## POST /api/items (Admin only)

Description: Adds a new item to the catalog. \
Request Body: Contains the name, description, and price of the item. \
Response: Details of the added item. 
## PUT /api/items/{itemId} (Admin only)

Description: Updates the details of an existing item. \
Request Body: Contains the updated name, description, and/or price. \
Response: Details of the updated item.
## DELETE /api/items/{itemId} (Admin only)

Description: Removes an item from the catalog.\
Response: A confirmation message indicating successful removal.
# 2. Shopping Cart Endpoints
## GET /api/cart

Description: Retrieves the contents of the user's shopping cart. \
Response: An array of items in the cart, including quantities.
## POST /api/cart/add

Description: Adds an item to the shopping cart.\
Request Body: The item ID and the quantity to add.\
Response: Updated contents of the shopping cart.
## POST /api/cart/remove

Description: Removes an item from the shopping cart.\
Request Body: The item ID and the quantity to remove.\
Response: Updated contents of the shopping cart.
# 3. Checkout Endpoint
## POST /api/checkout
Description: Processes the checkout with the items in the cart. \
Request Body: User information and shipping address.\
Response: Confirmation of the order with an order ID.