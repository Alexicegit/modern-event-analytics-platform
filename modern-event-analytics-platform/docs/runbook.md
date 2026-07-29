# Operational Runbook

## Daily Run
1. Validate source files
2. Load source files into Snowflake RAW tables
3. Run dbt build
4. Validate dbt tests
5. Refresh Power BI dataset

## Common Failure Scenarios
- Missing source file
- Invalid schema
- Duplicate business key
- Referential integrity failure
- Snowflake connection failure

## Recovery
- Fix source file or mapping issue
- Re-run failed task from Airflow
- Validate dbt test results
- Refresh dashboard dataset
