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