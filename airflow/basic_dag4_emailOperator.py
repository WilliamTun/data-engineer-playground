from airflow.models import DAG
from airflow.operators.email_operator import EmailOperator
from datetime import datetime

default_arguments = {
    'owner': 'will',
    'email': 'will@gmail.com',
    'start_date': datetime(20, 1, 20)
}

etl_dag = DAG(
    dag_id="etl_pipeline",
    default_args=default_arguments
)

email_task = EmailOperator(
    task_id="email someone",
    to="friend@gmail.com",
    subject="zouk",
    html_content="Attached is the schedule",
    files="zouk_schedule.xlsx"
    dag=etl_dag
)