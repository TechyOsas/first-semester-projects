-- SQL queries for retrieving insights


--------BASIC QUERIES---------

--RETRIEVE ALL CUSTOMERS
SELECT *
FROM customers;

--RERIEVE ALL PRODUCTS
SELECT *
FROM products;

--FILTER PRODUCTS BY CATEGORY(Kitchen)
SELECT *
FROM products
WHERE category = 'Kitchen';

--LIST RECENT ORDERS BY DATE
SELECT *
FROM orders
ORDER BY order_date DESC;



--------AGGREGATION---------

--COUNT THE NUMBER OF TOTAL ORDERS
SELECT 
    COUNT(*)
FROM orders;

--CALCULATE REVENUE PER PRODUCT (PRICE * QUANITY) USING SUM()
SELECT
	o.product_id,
	SUM(p.price * o.quantity) AS revenue_per_product
FROM orders AS o
LEFT JOIN products AS p
ON o.product_id = p.product_id
GROUP BY o.product_id
ORDER BY o.product_id ASC;


--FIND AVERAGE PRODUCT PRICE
SELECT
	ROUND(AVG(price),2) AS average_product_price
FROM products;




--------JOINS---------

--USE INNER JOIN TO GET DETAILED ORDER INFO (WITH CUSTOMER AND PRODUCT DETAILS)
SELECT
	o.order_id,
	o.customer_id,
	o.product_id,
	o.quantity,
	o.order_date,
	c.name,
	c.email,
	c.join_date,
	p.product_name,
	p.category,
	p.price
FROM orders AS o
INNER JOIN customers AS c
ON o.customer_id = c.customer_id
INNER JOIN products AS p
ON o.product_id = p.product_id;

--USE LEFT JOIN TO LIST ALL CUSTOMERS AND INCLUDE THEIR ORDERS (IF ANY)
SELECT
	c.customer_id,
	c.name,
	o.order_id,
	o.product_id,
	o.quantity,
	o.order_date
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;

--USE LEFT JOIN TO SHOW PRODUCTS EVEN IF THEY HAVEN'T BEEN ORDERED
SELECT
	p.product_id,
	p.product_name,
	p.category,
	p.price,
	o.order_id,
	o.order_date
FROM products AS p
LEFT JOIN orders AS o
ON p.product_id = o.product_id;
