import React, { useState, useEffect } from "react";


function UserIndexPage() {
    const [items, setItems] = useState([]);
  
    useEffect(() => {
      // Make an API request to fetch catalog items
      fetch('/api/items') // Update with your API endpoint
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          setItems(data);
        })
        .catch(error => {
          console.error('Error fetching items:', error);
        });
    }, []);
  
    const handleAddToCart = itemId => {
      // Make a POST request to add an item to the shopping cart
      fetch('/api/cart/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ item_id: itemId, quantity: 1 }), // You can adjust quantity as needed
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to add item to cart');
          }
          // Handle the response if needed
        })
        .catch(error => {
          console.error('Error adding item to cart:', error);
        });
    };
  
    return (
      <div>
        <h1>Item Catalog</h1>
        <ul>
          {items.map(item => (
            <li key={item.id}>
              <h2>{item.name}</h2>
              <p>{item.description}</p>
              <p>Price: ${item.price}</p>
              <button onClick={() => handleAddToCart(item.id)}>Add to Cart</button>
            </li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default UserIndexPage;