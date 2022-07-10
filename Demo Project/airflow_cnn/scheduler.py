from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import date, timedelta
from datetime import datetime
import os

wd = '/Users/sing/Desktop/demo_cases/airflow_cnn'

with DAG('sample', 
                schedule_interval='@hourly',
                description='Sample of airflow',
                start_date = datetime(2022,6,17),
                catchup=False) as dag:
    data_path = os.path.join(wd, 'dataset')
    log_path = os.path.join(wd, 'log')
    model_path = os.path.join(wd, 'model')
    
    t1 = BashOperator(task_id='preprocess', bash_command=f'python3 {wd}/data_preprocessing.py {data_path}')

    #user template varaible ds to extract the datetime
    t2 = BashOperator(task_id='train', bash_command=f'python3 {wd}/train.py {{ds}} {data_path} {model_path} {log_path}')
    t1 >> t2


