select distinct sale_date as date_day, extract(year from sale_date) as year, extract(month from sale_date) as month, extract(quarter from sale_date) as quarter from {{ ref('stg_ticket_sales') }}
