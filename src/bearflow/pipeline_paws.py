"""
Dagster pipeline with two sequential operations.

Defines a job (bear_pipeline) that executes task_a and task_b as ops.
Run with: python pipeline_paws.py or via dagster dev UI
"""
# 🧩 Dagster
from dagster import job, op


@op
def task_a():
    print("Dagster: Task A complete")


@op
def task_b():
    print("Dagster: Task B complete")


@job
def bear_pipeline():
    task_a()
    task_b()


if __name__ == "__main__":
    bear_pipeline.execute_in_process()
