import React, { useState, useEffect } from "react";


function CartPage() {
    const [cartItems, setCartItems] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);
    const [shippingAddress, setShippingAddress] = useState("");
    const [payment, setPayment] = useState("");
    useEffect(() => {
        // Make an API request to fetch cart items
        fetch('/api/cart')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setCartItems(data);
                calculateTotalPrice(data);
            })
            .catch(error => {
                console.error('Error fetching cart items:', error);
            });
    }, []);

    const calculateTotalPrice = (cartItems) => {
        let total = 0;
        cartItems.forEach(item => {
            total += item.price * item.quantity;
        });
        setTotalPrice(total);
    };

    const handleAddToCart = (itemId, quantityToAdd) => {
        // Make an API request to add an item to the shopping cart
        fetch('/api/cart/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                item_id: itemId,
                quantity: quantityToAdd,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setCartItems(data);
                calculateTotalPrice(data);
            })
            .catch(error => {
                console.error('Error adding item to cart:', error);
            });
    };

    const handleRemoveFromCart = (itemId, quantityToRemove) => {
        // Make an API request to remove an item from the shopping cart
        fetch('/api/cart/remove', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                item_id: itemId,
                quantity: quantityToRemove,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setCartItems(data);
                calculateTotalPrice(data);
            })
            .catch(error => {
                console.error('Error removing item from cart:', error);
            });
    };

    const handleCheckout = () => {
        // Make an API request to process the checkout
        fetch('/api/checkout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                
                user: {
                    name: 'default',
                    email: 'default@example.com',
                },
                shipping_address: shippingAddress,
                payment: payment,
            }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                
                console.log('Order ID:', data.order_id);
                setCartItems([]);
                setPayment("");
                setShippingAddress("");
                setTotalPrice(0);

            })
            .catch(error => {
                console.error('Error processing checkout:', error);
            });
    };

    return (
        <div>
            <h1>Shopping Cart</h1>
            <ul>
                {cartItems.map(item => (
                    <li key={item.item_id}>
                        <h2>{item.name}</h2>
                        <p>{item.description}</p>
                        <p>Price: ${item.price}</p>
                        <p>Quantity: {item.quantity}</p>
                        <button onClick={() => handleAddToCart(item.item_id, 1)}>Add One</button>
                        <button onClick={() => handleRemoveFromCart(item.item_id, 1)}>Remove One</button>
                    </li>
                ))}
            </ul>
            <p>Total Price: ${totalPrice}</p>
            <div>
                <h2>Check out info:</h2>
                <input
                    type="text"
                    placeholder="Payment"
                    value={payment}
                    onChange={e => setPayment( e.target.value )}
                />
                <input
                    type="text"
                    placeholder="Shipping Address"
                    value={shippingAddress}
                    onChange={e => setShippingAddress( e.target.value )}
                />
                <button onClick={handleCheckout}>Checkout</button>
            </div>
            
        </div>
    );
}

export default CartPage;