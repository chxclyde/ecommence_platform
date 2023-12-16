
INSERT INTO users (name, email, password_hash, is_admin) 
VALUES ('Default User', 'user@example.com', 'hashed_password', 0);


INSERT INTO carts (user_id) 
VALUES (1);


INSERT INTO items (name, description, price) 
VALUES 
('Item One', 'Description for item one', 19.99),
('Item Two', 'Description for item two', 29.99),
('Item Three', 'Description for item three', 39.99),
('Item Four', 'Description for item four', 49.99),
('Item Five', 'Description for item five', 59.99),
('Item Six', 'Description for item six', 69.99),
('Item Seven', 'Description for item seven', 79.99),
('Item Eight', 'Description for item eight', 89.99),
('Item Nine', 'Description for item nine', 99.99),
('Item Ten', 'Description for item ten', 109.99);