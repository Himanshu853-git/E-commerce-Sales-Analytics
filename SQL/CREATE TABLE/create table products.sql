use e_commerce;
CREATE TABLE products (
    product_id VARCHAR(20),
    product_name VARCHAR(150),
    category VARCHAR(50),
    brand VARCHAR(50),
    original_price NUMERIC(12,2),
    discount_percent INTEGER,
    discount_amount NUMERIC(12,2),
    selling_price NUMERIC(12,2),
    stock_quantity INTEGER,
    weight_kg NUMERIC(5,2),
    avg_rating NUMERIC(3,2),
    total_reviews INTEGER
);