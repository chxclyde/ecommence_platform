
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

INSERT INTO catalog_items (item_id, quantity)
VALUES 
(1, 50), -- Item One
(2, 30), -- Item Two
(3, 20), -- Item Three
(4, 50), -- Item Four
(5, 30), -- Item Five
(6, 20), -- Item Six
(7, 50), -- Item Seven
(8, 30), -- Item Eight
(9, 20), -- Item Nine
(10, 50); -- Item Ten