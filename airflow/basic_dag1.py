from airflow.models import DAG


etl_dag = DAG(
    dag_id="etl_pipeline",
    default_args={"start_date":"2020-01-08"}
)

# example:
# airflow run <dag_id> <task_id> <start_date>
# aurflow run etl_pipeline download_file 2020-01-10