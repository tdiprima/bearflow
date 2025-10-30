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
