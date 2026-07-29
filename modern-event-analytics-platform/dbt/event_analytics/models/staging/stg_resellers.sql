select reseller_id, reseller_name, channel, commission_rate, created_at, updated_at from {{ source('raw', 'RESELLERS_RAW') }}
