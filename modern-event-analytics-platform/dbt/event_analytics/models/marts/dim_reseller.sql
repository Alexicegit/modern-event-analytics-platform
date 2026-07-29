select reseller_id, reseller_name, channel, commission_rate from {{ ref('stg_resellers') }}
