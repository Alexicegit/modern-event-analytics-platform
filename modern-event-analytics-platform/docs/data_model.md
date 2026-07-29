# Data Model

## Fact Table
- fact_ticket_sales

## Dimensions
- dim_customer
- dim_event
- dim_reseller
- dim_date

## Grain
`fact_ticket_sales` has one row per paid ticket sale transaction.

## Business Keys
- sale_id
- event_id
- customer_id
- reseller_id
