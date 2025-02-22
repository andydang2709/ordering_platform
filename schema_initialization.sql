CREATE SCHEMA IF NOT EXISTS ordering_app;

USE ordering_app;

-- DROP TABLE IF EXISTS customers;
-- DROP TABLE IF EXISTS transactions;
-- DROP TABLE IF EXISTS menu;

CREATE TABLE customers (
    user_id VARCHAR(100) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    favorites JSON, #each value in here would link to transactions table, a value of transaction_id
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

### This part will be moved to a dedicated app afterwards on the menu management side ###
INSERT INTO customers VALUES
("andydang", SHA2('abc123', 256), "Andy Dang", '[1]', '2024-09-17');

INSERT INTO menu VALUES
("drink_base_01","Vietnamese Coffee", 1.25),
("dairy_01","Whole Milk", 0.75),
("syrup_01","Vanilla Syrup",0.25),
("sweet_00", "0% Sweetness Level", 0.00),
("ice_50","50% Ice Level", 0.00)
;

INSERT INTO transactions (user_id, food_id, sales_revenue) VALUES 
    ("andydang", '["base_01", "dairy_01", "syrup_01", "sweetness_00", "ice_50"]', 5.02),
    ("andydang", '["food_01", "sweetness_50", "no_nuts"]', 7.50);
    
select * from transactions;