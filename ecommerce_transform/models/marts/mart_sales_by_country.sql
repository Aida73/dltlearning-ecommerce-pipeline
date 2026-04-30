SELECT
    country,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS revenue,
    AVG(total_amount) AS avg_order_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM {{ ref('stg_orders') }}
GROUP BY country
ORDER BY revenue DESC
