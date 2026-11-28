use e_commerce;

CREATE TABLE customers (
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    gender VARCHAR(10),
    age INTEGER,
    age_group VARCHAR(20),
    date_of_birth DATE,
    email VARCHAR(150),
    phone VARCHAR(20),
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),
    registration_date DATE,
    customer_tier VARCHAR(20),
    total_orders INTEGER,
    total_spent NUMERIC(12,2)
);
