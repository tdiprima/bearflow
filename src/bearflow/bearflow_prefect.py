# 🌀 Prefect
from prefect import flow, task


@task
def task_a():
    print("Prefect: Task A complete")


@task
def task_b():
    print("Prefect: Task B complete")


@flow
def bearflow():
    task_a()
    task_b()
    print("Prefect flow complete!")


if __name__ == "__main__":
    bearflow()
