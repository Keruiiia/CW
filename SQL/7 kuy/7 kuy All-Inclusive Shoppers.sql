/*
Let's consider a situation where we have three tables:

users table:

Columns: id, name
Primary key: id
products table:

Columns: id, product_name
Primary key: id
orders table:

Columns: id, user_id, product_id
Primary key: id
Foreign keys: user_id references users(id), product_id references products(id)

In this kata, we need to find out the names and IDs of all users who ordered every
available product at least once. The result should be ordered by user_id in descending order. */

SELECT u.id as user_id, u.name as name
	FROM orders o
	JOIN users u ON o.user_id = u.id
GROUP BY u.id, u.name
HAVING COUNT(DISTINCT o.product_id) = (SELECT COUNT(*) FROM products)
ORDER BY u.id DESC;