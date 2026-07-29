select organizer_id, organizer_name, organizer_type, country, created_at, updated_at from {{ source('raw', 'ORGANIZERS_RAW') }}
