select event_id, event_name, category, organizer_id, event_city, event_country, event_date, capacity, base_ticket_price, created_at, updated_at from {{ source('raw', 'EVENTS_RAW') }}
