from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


def _print_hello(ti=None):
    print("hello Airflow")

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily"
,
catchup=False,
tags=['hello_airflow']
)
:
    print_hello = PythonOperator(
        task_id="print_hello",
        pyhone_callable=print_hello
    )
    
task1













