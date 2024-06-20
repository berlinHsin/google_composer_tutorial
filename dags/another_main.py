import datetime

from airflow import models
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import pandas as pd

default_dag_args = {
    "start_date": datetime.datetime(2024, 6, 18),
}

# Define a DAG (directed acyclic graph) of tasks.
# Any task you create within the context manager is automatically added to the
# DAG object.
with models.DAG(
    "tester",
    schedule_interval=datetime.timedelta(hours=1),
    default_args=default_dag_args,
) as dag:
    
    def greeting():
        import logging
        df = pd.DataFrame({'name': ['Berlin']})
        logging.info(df)
        logging.info("Hello World!")

    # An instance of an operator is called a task. In this case, the
    # hello_python task calls the "greeting" Python function.
    hello_python = PythonOperator(
        task_id="hello", python_callable=greeting
    )

    # Likewise, the goodbye_bash task calls a Bash script.
    goodbye_bash = BashOperator(
        task_id="bye", bash_command="echo Goodbye."
    )
    
    hello_python >> goodbye_bash