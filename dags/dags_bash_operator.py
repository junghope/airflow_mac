from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False
) as dag: # dag에 대한 정의, 모든 dag마다 필요함
    
    bash_t1 = BashOperator(
        task_id="bash_t1",# bash 명과 task_id는 일치하도록!
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2",# bash 명과 task_id는 일치하도록!
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2