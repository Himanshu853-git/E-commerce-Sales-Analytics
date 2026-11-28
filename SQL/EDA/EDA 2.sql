use e_commerce;

-- TOTAL REVENUE-- 

select
round(sum(total_amount),2) as total_revenue
from ecommerce_master;

-- TOTAL ORDERS-- 

select
count(distinct order_id)
from ecommerce_master;

-- UNIQUE CUSTOMER-- 

select
count(distinct customer_id)
from ecommerce_master;

-- AVERAGE ORDER VALUE-- 

select
round(avg (total_amount),2)
from ecommerce_master;

-- ORDER STATUS ANALYSIS-- 

select
order_status,
count(*) as orders
from ecommerce_master
group by order_status
order by orders desc;

-- PAYMENT MODE ANALYSIS-- 

SELECT
payment_mode,
count(*) as orders
from ecommerce_master
group by payment_mode
order by orders desc;

-- REVENUE BY CATEGORY-- 

select
category,
round(sum(total_amount),2) as revenue
from ecommerce_master
group by category
order by revenue desc;

-- REVENUE BY BRAND-- 

select
brand,
round(sum(total_amount),2) as revenue
from ecommerce_master
group by brand
order by revenue desc
limit 20;

-- REVENUE BY STATE-- 

select
state,
round(sum(total_amount),2) as revenue
from ecommerce_master
group by state
order by revenue desc;


-- MONTHLY REVENUE TREND-- 

select
date_format(order_date, '%Y-%m') as month,
round(sum(total_amount), 2) as revenue
from ecommerce_master
group by DATE_FORMAT(order_date, '%Y-%m')
order by month;

-- TOP PRODUCTS-- 

select
product_name,
round(sum(total_amount),2) as revenue
from ecommerce_master
group by product_name
order by revenue desc
limit 10;

-- TOP CUSTOMERS-- 

select
customer_name,
round(sum(total_amount),2) as spending
from ecommerce_master
group by customer_name
order by spending desc
limit 10;








