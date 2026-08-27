from airflow.sdk import dag, Asset
from airflow.operators.bash import BashOperator
from airflow import dataset
from pendulum import datetime
from datetime import timedelta
import logging

mon_fichier = Asset('file:///tmp/mon_asset.txt')

@dag(
  start_date=datetime(2026,8,27, tz='UTC'),
  schedule=None,
  catchup=False,
  tags=['producer'],
)
def producer():

  @task(outlet=[mon_fichier])
  def write_to_file(**context):
    logical_date= context['logical_date']
    ts = logical_date.isoformat()
    logging.info(f"start {ts}")
    with open(mon_fichier.uti, 'w') as f:
        f.write('hello')
  wrtie_to_file()    

  producer_dag = producer()
  


  
