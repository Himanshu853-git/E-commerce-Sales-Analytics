use e_commerce;
CREATE TABLE sales (
    order_id VARCHAR(20),
    customer_id VARCHAR(20),
    product_id VARCHAR(20),

    order_date DATE,
    order_time TIME,
    delivery_date DATE,

    quantity INT,

    unit_price DECIMAL(12,2),
    order_value DECIMAL(12,2),
    shipping_cost DECIMAL(12,2),

    coupon_code VARCHAR(50),
    coupon_discount DECIMAL(12,2),

    total_amount DECIMAL(12,2),

    payment_mode VARCHAR(50),
    order_status VARCHAR(50),

    rating VARCHAR(20),
    review_text TEXT,

    city VARCHAR(100),
    state VARCHAR(100),

    customer_age INT,
    customer_age_group VARCHAR(20)
);