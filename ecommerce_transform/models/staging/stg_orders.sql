-- Nettoyage de base
SELECT
    order_id,
    customer_id,
    product,
    quantity,
    unit_price,
    quantity * unit_price AS total_amount,
    country,
    status,
    CAST(created_at AS TIMESTAMP) AS created_at
FROM {{ source('raw_ecommerce', 'orders') }}
WHERE status != 'cancelled'
