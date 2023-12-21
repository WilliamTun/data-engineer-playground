from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
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

def printme(message):
    print(f"python says {message}!")

python_task = PythonOperator(
    task_id="saying hello",
    python_callable=printme,
    op_kwargs={'message':'hello my friend!'},
    dag=etl_dag
)