import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")
print("1. Total revenue per category")
query = """
SELECT
    p.category,
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS total_revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category;
"""
result = pd.read_sql_query(query, conn)
print(result)
print("\n2. Top 10 customers by total order value")
query2 = """
SELECT
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS total_order_value
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_order_value DESC
LIMIT 10;"""
result2 = pd.read_sql_query(query2, conn)
print(result2)


print("\n3. Month-wise order count for the last 12 months")
query3 = """
SELECT
strftime('%Y-%m', order_date) AS month,
COUNT(order_id) AS total_orders
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month DESC
LIMIT 12;"""
result3 = pd.read_sql_query(query3, conn)
print(result3)

print("\n4. Customers who placed orders but never had any item delivered")

query4 = """
SELECT
c.customer_id,
c.customer_name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(
    CASE
    WHEN o.status = 'DELIVERED' THEN 1
    ELSE 0
    END
) = 0;"""
result4 = pd.read_sql_query(query4, conn)
print(result4)

print("\n5. Products that were ordered but had more returns than purchases")
query5 = """
SELECT
p.product_id,
p.product_name,
SUM(oi.quantity) AS total_purchased,
SUM(CASE WHEN o.status='RETURNED' THEN oi.quantity ELSE 0 END) AS total_returned
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
JOIN orders o
ON oi.order_id=o.order_id
GROUP BY p.product_id,p.product_name
HAVING total_returned > total_purchased;
"""
result5 = pd.read_sql_query(query5, conn)
print(result5)


print("\n6. Return rate per category")
query6 = """
SELECT
p.category,
SUM(CASE WHEN o.status='RETURNED' THEN oi.quantity ELSE 0 END) AS returned_items,
SUM(oi.quantity) AS total_items,
ROUND(
SUM(CASE WHEN o.status='RETURNED' THEN oi.quantity ELSE 0 END)*100.0/SUM(oi.quantity),
2
) AS return_rate_percentage
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
JOIN orders o
ON oi.order_id=o.order_id
GROUP BY p.category;
"""
result6 = pd.read_sql_query(query6, conn)
print(result6)

print("\n7. Running total of revenue per region")
query7 = """
WITH daily_sales AS (
SELECT
o.region_code,
DATE(o.order_date) AS order_date,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS daily_revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY o.region_code,DATE(o.order_date))
SELECT
region_code,
order_date,
daily_revenue,
SUM(daily_revenue) OVER(
PARTITION BY region_code
ORDER BY order_date
) AS running_total
FROM daily_sales
ORDER BY region_code,order_date;
"""
result7 = pd.read_sql_query(query7, conn)
print(result7)


print("\n8. Rank products by revenue within each category")
query8 = """
WITH product_revenue AS (
SELECT
p.category,
p.product_name,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS total_revenue
FROM products p
JOIN order_items oi
ON p.product_id=oi.product_id
GROUP BY p.category,p.product_name)
SELECT
category,
product_name,
total_revenue,
DENSE_RANK() OVER(
PARTITION BY category
ORDER BY total_revenue DESC
) AS rank_in_category
FROM product_revenue
ORDER BY category,rank_in_category;
"""
result8 = pd.read_sql_query(query8, conn)
print(result8)


print("\n9. Customer order gap analysis")
query9 = """
WITH customer_orders AS (
SELECT
customer_id,
DATE(order_date) AS order_date,
LAG(DATE(order_date)) OVER(
PARTITION BY customer_id
ORDER BY DATE(order_date)
) AS previous_order_date
FROM orders),
order_gaps AS (
SELECT
customer_id,
order_date,
previous_order_date,
JULIANDAY(order_date)-JULIANDAY(previous_order_date) AS days_gap
FROM customer_orders)
SELECT
customer_id,
order_date,
previous_order_date,
days_gap,
CASE
WHEN AVG(days_gap) OVER(PARTITION BY customer_id)>30 THEN 'At Risk'
ELSE 'Active'
END AS customer_status
FROM order_gaps
ORDER BY customer_id,order_date;
"""
result9 = pd.read_sql_query(query9, conn)
print(result9)

print("\n10. Monthly customer revenue categories")
query10 = """
WITH monthly_revenue AS (
SELECT
o.customer_id,
strftime('%Y-%m',o.order_date) AS month,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS monthly_revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY o.customer_id,strftime('%Y-%m',o.order_date)),
customer_category AS (
SELECT
customer_id,
month,
monthly_revenue,
CASE
WHEN monthly_revenue>10000 THEN 'High'
WHEN monthly_revenue>=5000 THEN 'Medium'
ELSE 'Low'
END AS revenue_category
FROM monthly_revenue)
SELECT
month,
revenue_category,
COUNT(customer_id) AS customer_count
FROM customer_category
GROUP BY month,revenue_category
ORDER BY month,revenue_category;"""
result10 = pd.read_sql_query(query10, conn)
print(result10)


print("\n11. Customer segmentation using NTILE")
query11 = """
WITH customer_value AS (
SELECT
c.customer_id,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS total_value
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY c.customer_id)
SELECT
customer_id,
total_value,
quartile,
CASE
WHEN quartile=1 THEN 'Platinum'
WHEN quartile=2 THEN 'Gold'
WHEN quartile=3 THEN 'Silver'
ELSE 'Bronze'
END AS quartile_label
FROM(SELECT
customer_id,
total_value,
NTILE(4) OVER(ORDER BY total_value DESC) AS quartile
FROM customer_value)
ORDER BY total_value DESC;"""
result11 = pd.read_sql_query(query11, conn)
print(result11)


print("\n12. Year-over-Year revenue comparison")
query12 = """
WITH monthly_revenue AS (
SELECT
strftime('%Y',o.order_date) AS year,
strftime('%m',o.order_date) AS month,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
GROUP BY strftime('%Y',o.order_date),strftime('%m',o.order_date))
SELECT
m1.year,
m1.month,
m1.revenue,
m2.revenue AS prev_year_revenue,
CASE
WHEN m2.revenue IS NULL OR m2.revenue=0 THEN NULL
ELSE ROUND(((m1.revenue-m2.revenue)*100.0)/m2.revenue,2)
END AS yoy_growth_percent
FROM monthly_revenue m1
LEFT JOIN monthly_revenue m2
ON m1.month=m2.month
AND CAST(m1.year AS INTEGER)=CAST(m2.year AS INTEGER)+1
ORDER BY m1.year,m1.month;"""
result12 = pd.read_sql_query(query12, conn)
print(result12)

print("\n13. First and last purchased category for each customer")
query13 = """
WITH customer_categories AS (
SELECT
o.customer_id,
o.order_date,
p.category,
FIRST_VALUE(p.category) OVER(
PARTITION BY o.customer_id
ORDER BY DATE(o.order_date)
) AS first_category,
FIRST_VALUE(p.category) OVER(
PARTITION BY o.customer_id
ORDER BY DATE(o.order_date) DESC
) AS last_category
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
JOIN products p
ON oi.product_id=p.product_id
WHERE o.customer_id IS NOT NULL)
SELECT DISTINCT
customer_id,
first_category,
last_category,
CASE
WHEN first_category=last_category THEN 'No'
ELSE 'Yes'
END AS category_shift
FROM customer_categories
ORDER BY customer_id;"""
result13 = pd.read_sql_query(query13, conn)
print(result13)


print("\n14. Cumulative distribution of customer revenue")
query14 = """
WITH customer_revenue AS (
SELECT
o.customer_id,
SUM(oi.quantity*oi.unit_price*(1-oi.discount_percent/100.0)) AS revenue
FROM orders o
JOIN order_items oi
ON o.order_id=oi.order_id
WHERE o.customer_id IS NOT NULL
GROUP BY o.customer_id)
SELECT
customer_id,
revenue,
SUM(revenue) OVER(
ORDER BY revenue DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue,
ROUND(
SUM(revenue) OVER(
ORDER BY revenue DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)*100.0/SUM(revenue) OVER(),2
) AS cumulative_percent
FROM customer_revenue
ORDER BY revenue DESC;"""
result14 = pd.read_sql_query(query14, conn)
print(result14)


print("\n15. Cohort analysis")
query15 = """
WITH cohort AS (
SELECT
customer_id,
strftime('%Y-%m',registration_date) AS cohort_month
FROM customers),
customer_orders AS (
SELECT
c.customer_id,
c.cohort_month,
((CAST(strftime('%Y',o.order_date) AS INTEGER)-CAST(strftime('%Y',c.cohort_month||'-01') AS INTEGER))*12+
(CAST(strftime('%m',o.order_date) AS INTEGER)-CAST(strftime('%m',c.cohort_month||'-01') AS INTEGER))) AS month_number
FROM cohort c
JOIN orders o
ON c.customer_id=o.customer_id),
cohort_size AS (
SELECT
cohort_month,
COUNT(DISTINCT customer_id) AS cohort_size
FROM cohort
GROUP BY cohort_month)
SELECT
co.cohort_month,
COUNT(DISTINCT CASE WHEN month_number=0 THEN co.customer_id END) AS month_0,
COUNT(DISTINCT CASE WHEN month_number=1 THEN co.customer_id END) AS month_1,
COUNT(DISTINCT CASE WHEN month_number=2 THEN co.customer_id END) AS month_2,
COUNT(DISTINCT CASE WHEN month_number=3 THEN co.customer_id END) AS month_3,
ROUND(COUNT(DISTINCT CASE WHEN month_number=0 THEN co.customer_id END)*100.0/cs.cohort_size,2) AS retention_month_0,
ROUND(COUNT(DISTINCT CASE WHEN month_number=1 THEN co.customer_id END)*100.0/cs.cohort_size,2) AS retention_month_1,
ROUND(COUNT(DISTINCT CASE WHEN month_number=2 THEN co.customer_id END)*100.0/cs.cohort_size,2) AS retention_month_2,
ROUND(COUNT(DISTINCT CASE WHEN month_number=3 THEN co.customer_id END)*100.0/cs.cohort_size,2) AS retention_month_3
FROM customer_orders co
JOIN cohort_size cs
ON co.cohort_month=cs.cohort_month
GROUP BY co.cohort_month,cs.cohort_size
ORDER BY co.cohort_month;"""
result15 = pd.read_sql_query(query15, conn)
print(result15)


print("\n16. Products frequently bought together")
query16 = """
SELECT
p1.product_name AS product_a,
p2.product_name AS product_b,
COUNT(*) AS times_bought_together
FROM order_items oi1
JOIN order_items oi2
ON oi1.order_id=oi2.order_id
AND oi1.product_id<oi2.product_id
JOIN products p1
ON oi1.product_id=p1.product_id
JOIN products p2
ON oi2.product_id=p2.product_id
GROUP BY
p1.product_name,
p2.product_name
ORDER BY
times_bought_together DESC,
product_a,
product_b;"""
result16=pd.read_sql_query(query16,conn)
print(result16)