# Sensor 
# - operator that waits for a condition to be true
#   eg. creation of a file / upload to database / web response
# - we must define how often to check for condition status

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
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


makefile = BashOperator(
    task_id="generate_rand_num",
    bash_comand="echo $RANDOM >> random.txt",
    dag=etl_dag
)

file_sensor_task = FileSensor(
    task_id='file_sensor',
    filepath='random.txt',
    poke_interval=300, # how long to wait between checks
    timeout=1000, # how long to wait before failing
    dag=etl_dag
)

makefile >> file_sensor_task

'''
# Other type of sensors
ExternalTaskSensor - wait for a task in another DAG to complete
HttpSensor = Request a web URL and check for content
'''