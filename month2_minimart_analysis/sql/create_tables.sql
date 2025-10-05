-- SQL script to create necessary tables


--CREATE THE CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    join_date DATE NOT NULL,
    CONSTRAINT pk_customers PRIMARY KEY (customer_id)
);


--CREATE THE PRODUCTS TABLE
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    price DECIMAL NOT NULL,
    CONSTRAINT pk_products PRIMARY KEY (product_id)
);


--CREATE THE ORDERS TABLE
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    CONSTRAINT pk_orders PRIMARY KEY (order_id),
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT fk_orders_product FOREIGN KEY (product_id) REFERENCES products(product_id)
);