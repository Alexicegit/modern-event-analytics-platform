"""
Example Airflow DAG for Modern Event Analytics Platform.
This DAG is portfolio-safe and uses BashOperator placeholders for local demonstration.
Replace commands with Snowflake/dbt operators in a production setup.
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='event_analytics_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule='0 2 * * *',
    catchup=False,
    tags=['portfolio', 'snowflake', 'dbt', 'event-analytics'],
) as dag:

    validate_source_files = BashOperator(
        task_id='validate_source_files',
        bash_command='echo Validating source CSV files'
    )

    load_snowflake_raw = BashOperator(
        task_id='load_snowflake_raw',
        bash_command='echo Loading CSV files into Snowflake RAW tables'
    )

    run_dbt_build = BashOperator(
        task_id='run_dbt_build',
        bash_command='cd /opt/airflow/dbt/event_analytics && dbt build --profiles-dir .'
    )

    publish_dashboard_dataset = BashOperator(
        task_id='publish_dashboard_dataset',
        bash_command='echo Power BI dataset is ready for refresh'
    )

    validate_source_files >> load_snowflake_raw >> run_dbt_build >> publish_dashboard_dataset
