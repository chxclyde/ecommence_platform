import React, { useState, useEffect } from "react";


export default function AdminIndexPage() {
    const [items, setItems] = useState([]);
    const [newItem, setNewItem] = useState({ name: '', description: '', price: '' });

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

    const handleAddItem = () => {
        // Make a POST request to add a new item
        fetch('/api/items', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to add item');
                }
                return response.json();
            })
            .then(data => {
                // Refresh the item list after successfully adding an item
                setItems([...items, data]);
                setNewItem({ name: '', description: '', price: 0 });
            })
            .catch(error => {
                console.error('Error adding item:', error);
            });
    };

    const handleDeleteItem = itemId => {
        // Make a DELETE request to remove an item
        fetch(`/api/items/${itemId}`, {
            method: 'DELETE',
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to delete item');
                }
                // Remove the deleted item from the item list
                setItems(items.filter(item => item.id !== itemId));
            })
            .catch(error => {
                console.error('Error deleting item:', error);
            });
    };

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <div>
                <h2>Add New Item</h2>
                <input
                    type="text"
                    placeholder="Name"
                    value={newItem.name}
                    onChange={e => setNewItem({ ...newItem, name: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={newItem.description}
                    onChange={e => setNewItem({ ...newItem, description: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="price"
                    value={newItem.price}
                    onChange={e => setNewItem({ ...newItem, price: e.target.value })}
                />
                
                <button onClick={handleAddItem}>Add Item</button>
            </div>
            <h2>Item Catalog</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>
                        <h3>{item.name}</h3>
                        <p>{item.description}</p>
                        <p>Price: ${item.price}</p>
                        <button onClick={() => handleDeleteItem(item.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}