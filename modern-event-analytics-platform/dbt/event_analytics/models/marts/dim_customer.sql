select customer_id, customer_name, email, segment, city, country, created_at, updated_at from {{ ref('stg_customers') }}
