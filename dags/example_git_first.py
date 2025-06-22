#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
### Airflow DAG with Independent Tasks

This DAG is designed to showcase a simple workflow where numerous tasks are defined
but none have any dependencies on each other. When this DAG is triggered, the Airflow
scheduler is free to execute all tasks concurrently, depending on the available
resources (executor slots) in the Airflow environment.
"""

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# Define the DAG
with DAG(
    dag_id="git_independent_tasks_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    schedule=None,  # This DAG runs only when manually triggered
    tags=["example", "independent"],
    doc_md=__doc__,
) as dag:
    # Task 1: A simple bash command
    task_1 = BashOperator(
        task_id="git_task_1_runs_report",
        bash_command="echo 'Running a daily sales report'",
    )

    # Task 2: Another independent bash command
    task_2 = BashOperator(
        task_id="git_task_2_cleans_temp_data",
        bash_command="echo 'Cleaning temporary directories...'",
    )

    # Task 3: Simulates checking an API status
    task_3 = BashOperator(
        task_id="git_task_3_checks_api_status",
        bash_command="echo 'Pinging external API for status...'",
    )

    # Task 4: Simulates a data backup
    task_4 = BashOperator(
        task_id="git_task_4_performs_backup",
        bash_command="echo 'Backing up critical database...'",
    )

    # Task 5: Data validation task
    task_5 = BashOperator(
        task_id="git_task_5_validates_data",
        bash_command="echo 'Validating yesterday's data ingestion.'",
    )

    # Task 6: A longer running task simulation
    task_6 = BashOperator(
        task_id="git_task_6_long_running_job",
        bash_command="echo 'Starting a long-running simulation...'; sleep 5",
    )

    # Task 7: User management task
    task_7 = BashOperator(
        task_id="git_task_7_syncs_users",
        bash_command="echo 'Syncing user permissions from LDAP.'",
    )

    # Task 8: Logging task
    task_8 = BashOperator(
        task_id="git_task_8_archives_logs",
        bash_command="echo 'Archiving old log files.'",
    )

    # Task 9: System health check
    task_9 = BashOperator(
        task_id="git_task_9_system_health_check",
        bash_command="echo 'Performing system health check.'",
    )

    # Task 10: Send a completion notification (in a real scenario, this would depend on others)
    # For this example, it's independent.
    task_10 = BashOperator(
        task_id="git_task_10_sends_notification",
        bash_command="echo 'Notification: All independent startup tasks have been triggered.'",
    )

    # In this DAG, no dependencies are set.
    # We do not use bitshift operators (>> or <<) to link tasks.
    # Therefore, all defined tasks will be scheduled to run in parallel.
