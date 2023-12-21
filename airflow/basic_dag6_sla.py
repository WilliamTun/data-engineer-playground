from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from datetime import timedelta


'''
SLA: Service level agreement
- it is the amount of time a task/DAG is required to run
- SLA miss is any time the task does NOT meet the expected timing
- if SLA is missed, an email is sent off / log is stored
- use "sla" argument in Operator
'''

default_arguments = {
    'owner': 'will',
    'email': 'will@gmail.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'email_on_success': True,
    'start_date': datetime(20, 1, 20)
}

etl_dag = DAG(
    dag_id="etl_pipeline",
    default_args=default_arguments
)

part1a = BashOperator(
    task_id="generate_rand_num",
    bash_comand="echo $RANDOM",
    dag=etl_dag,
    sla=timedelta(seconds=30) 
    #sla=timedelta(minutes=30) 
    #sla=timedelta(hours=30) 
    #sla=timedelta(days=30) 
)