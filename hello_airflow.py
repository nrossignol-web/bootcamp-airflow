from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def print_hello(ti=None):
    print("hello Airflow")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily"
)
:
    task1 = PythonOperator(
        task_id="print_hello",
        pyhone_callable=print_hello
    )
    
task1













