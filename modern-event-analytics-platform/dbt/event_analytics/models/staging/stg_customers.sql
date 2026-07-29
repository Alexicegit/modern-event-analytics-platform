select customer_id, customer_name, email, segment, city, country, created_at, updated_at from {{ source('raw', 'CUSTOMERS_RAW') }}
