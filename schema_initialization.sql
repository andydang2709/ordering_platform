CREATE SCHEMA IF NOT EXISTS ordering_app;

USE ordering_app;

CREATE TABLE customers (
    user_id VARCHAR(100) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    favorites JSON, #each value in here would link to transactions table
    last_visit DATE
);

CREATE TABLE transactions (
	transaction_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id VARCHAR(100) NOT NULL,
    food_id	JSON, # each component in food_id would link to menu table
    sales_revenue DECIMAL(10,2),
	FOREIGN KEY (user_id) REFERENCES customers(user_id) ON DELETE CASCADE
);

CREATE TABLE menu (
	component_id VARCHAR(50) PRIMARY KEY,
    component_name VARCHAR(100) NOT NULL,
    price DECIMAL(5,2)
);

