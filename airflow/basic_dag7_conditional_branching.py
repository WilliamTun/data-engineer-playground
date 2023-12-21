from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import BranchPythonOperator
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

def branch_test(**kwargs):
    if int(kwargs['ds_nodash']) %2 == 0:
        return 'even_task'
    else:
        return 'odd_task'

start_task = BashOperator(
    task_id="generate_rand_num",
    bash_comand="start.sh",
    dag=etl_dag
)

odd_task = BashOperator(
    task_id="generate_rand_num",
    bash_comand="echo $RANDOM",
    dag=etl_dag
)

even_task = BashOperator(
    task_id="generate_rand_num",
    bash_comand="awk $RANDOM",
    dag=etl_dag
)

branch_task = BranchPythonOperator(
    task_id="branch_task",
    dag=etl_dag,
    provide_context=True,
    python_callable=branch_test # next task id / list of task ids
)


start_task >> branch_task >> even_task
branch_task >> odd_task