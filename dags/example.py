from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Define a simple Python function for the PythonOperator
def print_current_time():
    """This function prints the current time in UTC."""
    print(f"The current time is {pendulum.now('UTC')}")

with DAG(
    dag_id="large_dag_with_no_dependencies",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    catchup=False,
    schedule="@daily",
    tags=["example", "large"],
    doc_md="""
    ### Large DAG with No Dependencies

    This DAG demonstrates a larger workflow with multiple independent tasks.
    It includes `EmptyOperator`, `BashOperator`, and `PythonOperator` tasks.
    Since no dependencies are set, all tasks can run in parallel.
    """,
) as dag:
    # Task 1: An EmptyOperator as a starting point
    start_task = EmptyOperator(task_id="start_task")

    # Task 2: A BashOperator to print the date
    print_date_task = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    # Task 3: A BashOperator that sleeps for 5 seconds
    sleep_task = BashOperator(
        task_id="sleep_for_5_seconds",
        bash_command="sleep 5",
    )

    # Task 4: A PythonOperator to execute a Python function
    python_task_1 = PythonOperator(
        task_id="print_current_utc_time",
        python_callable=print_current_time,
    )

    # Task 5: Another PythonOperator using a lambda function
    python_task_2 = PythonOperator(
        task_id="say_hello",
        python_callable=lambda: print("Hello from a Python lambda function!"),
    )

    # Task 6: A final EmptyOperator
    end_task = EmptyOperator(task_id="end_task")
