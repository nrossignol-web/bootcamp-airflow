from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
catchup=False,
tags=['hello_airflow']
):

    print_hello = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Bonjour depuis Airflow'",
    )
    
print_hello












