# E-Commerce Platform

## Getting Started

To run the E-Commerce Platform locally, follow these steps:

1. Create a virtual environment and activate it:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. Install project dependencies from requirements.txt:

    ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database and run the app:
    ```bash
   ./bin/dbinit create
   ./bin/run
   ```
Due to time limitations, most of tests are done through postman and UI. I didn't come out with pytest.

http://localhost:7000/ for user page.\
http://localhost:7000/admin/ for admin page.


# API documentation:
see API_documentation.md

# Requirements
- [✔️] Item Catalog: Create a catalog of items that includes at least 10 different items, each
with a unique name, description, and price.

- [✔️] Shopping Cart: Implement a shopping cart that allows users to add items from the item
catalog. The shopping cart should keep track of the quantity of each item.
- [✔️] Add/Remove Items: Users should be able to add items to and remove items from the
shopping cart.
- [✔️] Checkout Process: Implement a checkout process that includes user information,
shipping address, and payment method (just mock the actual payment).
- [🕒] Admin: Implement an admin system to manage the catalog, including adding/removing
items, changing price etc..
- [✔️] API: Implement a RESTful API that allows users to interact with the shopping cart and
checkout process. The API should support operations to add an item, remove an item,
get the total cost, and checkout.
- [✔️] Frontend: Implement a user-friendly interface that allows users to interact with the
shopping cart, item catalog, and checkout process.
- [🕒] Unit Tests: Write unit tests to verify the functionality of your application.

