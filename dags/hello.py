from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Gonzalo',
             'start_date': datetime(2024, 7, 18),
             'catch_up': False
}

dag = DAG('hello_world',
          default_args=default_args,
          schedule=timedelta(days=1))

task1 = BashOperator(
    task_id='hello_world',
    bash_command='echo "hello_world"'
)

task2 = BashOperator(
    task_id='hello_gonzalo',
    bash_command='echo "Aprende k8s, sera divertido, dijeron *******"',
    dag=dag
)

task1 >> task2