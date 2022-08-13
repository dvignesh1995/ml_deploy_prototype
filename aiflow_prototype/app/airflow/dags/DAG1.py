
import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG('dag_1', description='pipeline 1',
          schedule_interval=datetime.timedelta(minutes=2),
          start_date=datetime.datetime(2017, 3, 20), catchup=False,
          is_paused_upon_creation=False)

f1 = BashOperator(task_id='fucntion1', \
    bash_command= "/opt/conda/envs/venv/bin/python /opt/app/functions/f1.py", dag=dag)
f2 = BashOperator(task_id='fucntion2', \
    bash_command= "/opt/conda/envs/venv/bin/python /opt/app/functions/f2.py", dag=dag)
f3 = BashOperator(task_id='fucntion3', \
    bash_command= "/opt/conda/envs/venv/bin/python /opt/app/functions/f3.py", dag=dag)

[f1,f2] >> f3