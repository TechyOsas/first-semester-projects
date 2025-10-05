-- SQL script to insert sample data


--INSERTING DATA INTO THE CUSTOMERS TABLE
INSERT INTO customers (customer_id, name, email, join_date)
VALUES
    (1, 'Sarah Johnson', 'sarah.johnson@gmail.com', '2025-01-15'),
    (2, 'Michael Chen', 'michael.chen@gmail.com', '2025-02-03'),
    (3, 'Emily Rodriguez', 'emily.rodriguez@gmail.com', '2025-02-20'),
    (4, 'David Thompson', 'david.thompson@gmail.com', '205-03-10'),
    (5, 'Jessica Williams', 'jessica.w@gmail.com', '2025-03-25'),
    (6, 'Robert Kim', 'robert.kim@gmail.com', '2025-04-05'),
    (7, 'Amanda Parker', 'amanda.parker@gmail.com', '2025-04-18'),
    (8, 'James Wilson', 'james.wilson@gmail.com', '2025-05-01'),
    (9, 'Lisa Anderson', 'lisa.anderson@gmail.com', '2025-05-12'),
    (10, 'Daniel Brown', 'daniel.brown@gmail.com', '2025-05-30'),
    (11, 'Maria Garcia', 'maria.garcia@gmail.com', '2025-06-08'),
    (12, 'Kevin Davis', 'kevin.davis@gmail.com', '2025-06-22'),
    (13, 'Jennifer Lee', 'jennifer.lee@gmail.com', '2025-07-05'),
    (14, 'Thomas Martin', 'thomas.martin@gmail.com', '2025-07-19'),
    (15, 'Nicole Taylor', 'nicole.taylor@gmail.com', '2025-08-02');


--INSERTING DATA INTO THE PRODUCTS TABLE
INSERT INTO products (product_id, product_name, category, price)
VALUES
    (101, 'Wireless Bluetooth Headphones', 'Electronics', 89.99),
    (102, 'Stainless Steel Water Bottle', 'Kitchen', 24.99),
    (103, 'Organic Cotton T-Shirt', 'Clothing', 29.99),
    (104, 'Python Programming Book', 'Books', 45.50),
    (105, 'Yoga Mat Premium', 'Fitness', 39.99),
    (106, 'Smartphone Case', 'Electronics', 19.99),
    (107, 'Ceramic Coffee Mug Set', 'Kitchen', 34.99),
    (108, 'Running Shoes', 'Clothing', 119.99),
    (109, 'Data Science Handbook', 'Books', 55.00),
    (110, 'Dumbbell Set 20lbs', 'Fitness', 49.99),
    (111, 'Portable Charger 10000mAh', 'Electronics', 29.99),
    (112, 'Non-Stick Cooking Pan', 'Kitchen', 42.99),
    (113, 'Winter Jacket', 'Clothing', 149.99),
    (114, 'Web Development Guide', 'Books', 38.75),
    (115, 'Resistance Bands Set', 'Fitness', 22.99);


--INSERTING DATA INTO THE ORDERS TABLE
INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date)
VALUES
    (1001, 1, 101, 1, '2025-09-01'),
    (1002, 2, 104, 2, '2025-09-02'),
    (1003, 3, 103, 1, '2025-09-02'),
    (1004, 4, 108, 1, '2025-09-03'),
    (1005, 5, 107, 1, '2025-09-04'),
    (1006, 1, 102, 3, '2025-09-05'),
    (1007, 6, 105, 1, '2025-09-05'),
    (1008, 7, 106, 2, '2025-09-06'),
    (1009, 8, 109, 1, '2025-09-07'),
    (1010, 9, 110, 1, '2025-09-08'),
    (1011, 10, 111, 1, '2025-09-09'),
    (1012, 2, 112, 1, '2025-09-10'),
    (1013, 11, 113, 1, '2025-09-11'),
    (1014, 12, 114, 1, '2025-09-12'),
    (1015, 13, 115, 2, '2025-09-13');