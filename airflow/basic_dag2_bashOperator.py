from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
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

part1a = BashOperator(
    task_id="generate_rand_num",
    bash_comand="echo $RANDOM",
    dag=etl_dag
)

part1b = BashOperator(
    task_id="generate_rand_num",
    bash_comand="awk $RANDOM",
    dag=etl_dag
)

part2 = BashOperator(
    task_id="generate_rand_num",
    bash_comand="cleanup.sh",
    dag=etl_dag
)

# chain tasks
part1a >> part1b >> part2 

# one task with multiple dependecies
part1a >> part2 << part1b 

part1a >> part2 
part1b >> part2