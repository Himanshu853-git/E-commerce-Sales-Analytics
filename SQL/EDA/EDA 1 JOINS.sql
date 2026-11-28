USE e_commerce;

CREATE OR REPLACE VIEW ecommerce_master AS
SELECT
    s.*,
    c.customer_name,
    c.gender,
    c.age,
    c.age_group,
    c.customer_tier,
    c.registration_date,
    p.product_name,
    p.category,
    p.brand,
    p.discount_percent,
    p.stock_quantity,
    p.avg_rating
FROM sales s
LEFT JOIN customers c
ON s.customer_id = c.customer_id
LEFT JOIN products p
ON s.product_id = p.product_id;