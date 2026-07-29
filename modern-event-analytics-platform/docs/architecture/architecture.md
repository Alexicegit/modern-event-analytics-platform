# Architecture

```text
Synthetic CSV Data
    ↓
Airflow DAG
    ↓
Snowflake RAW Schema
    ↓
dbt STAGING Models
    ↓
dbt MART Models
    ↓
Power BI Dashboard
```

## Layers
- RAW: Loaded source-aligned CSV data
- STAGING: Clean renamed and typed models
- MART: Star schema facts and dimensions

## Reliability Patterns
- Audit columns
- File history design placeholder
- dbt tests
- Incremental model design placeholder
- Reconciliation query placeholders
