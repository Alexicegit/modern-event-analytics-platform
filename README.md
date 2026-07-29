# Modern Event Analytics Platform

Confidentiality-safe end-to-end Senior Data Engineering portfolio project using synthetic event ticketing data.

## Business Problem
Event businesses need trusted analytics for ticket sales, revenue, customer segments, event performance, and reseller performance. This project builds a complete modern data platform from raw data generation to analytics-ready marts and BI dashboard design.

## Technology Stack
- Python for synthetic data generation
- Apache Airflow for orchestration
- Snowflake for cloud data warehousing
- dbt for analytics engineering and transformations
- Power BI for executive dashboards
- GitHub for portfolio documentation and version control

## Architecture
```text
Synthetic Source Data / CSV
        ↓
Python Data Generation
        ↓
Airflow Orchestration
        ↓
Snowflake RAW Layer
        ↓
dbt STAGING Layer
        ↓
dbt MART Layer
        ↓
Power BI Executive Dashboard
```

## Repository Structure
```text
data/raw/                  Synthetic CSV source data
scripts/                   Python data generation script
snowflake/sql/             Snowflake database, schema, stage, and table scripts
dbt/event_analytics/       dbt project with staging and mart models
airflow/dags/              Example Airflow DAG
powerbi/                   Dashboard build guide
docs/                      Architecture, data model, runbook, Toptal showcase notes
.github/workflows/         Example CI workflow for dbt checks
```

## Core Data Model
- `dim_event`
- `dim_customer`
- `dim_reseller`
- `dim_date`
- `fact_ticket_sales`

## Business KPIs
- Total Revenue
- Tickets Sold
- Average Order Value
- Revenue by Event Category
- Top Events by Revenue
- Customer Segment Contribution
- Reseller Sales Contribution

## How to Showcase on Toptal
Use this as your featured project. Mention it as a portfolio implementation, not as a real client project.

**Suggested title:** Modern Event Analytics Platform | Snowflake, dbt, Airflow, Power BI

## Confidentiality Notice
This project uses fully synthetic data and generic business concepts. It does not include confidential client data, employer-specific assets, production credentials, or internal system details.
