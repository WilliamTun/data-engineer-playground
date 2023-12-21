'''
- Templates allow substitution of information
  to add added flexibility when defining tasks
- Created using Jinja templates
'''

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

templated_command = """
    echo "Reading {{ params.filename }}"
"""

part1 = BashOperator(
    task_id="template task",
    bash_comand=templated_command,
    params={'filename': 'file1.txt'}
    dag=etl_dag
)

part2 = BashOperator(
    task_id="template task",
    bash_comand=templated_command,
    params={'filename': 'file2.txt'}
    dag=etl_dag
)