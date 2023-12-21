# example run:
airflow run <dag_id> <task_id> <start_date>
airflow run etl_pipeline download_file 2020-01-10

airflow list_dags