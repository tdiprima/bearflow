# Temporal workflow trigger
import asyncio

from temporalio.client import Client

from temporal_cave import BearFlow


async def trigger_workflow():
    # Connect to the Temporal server
    client = await Client.connect("localhost:7233")

    # Start the workflow
    print("Triggering BearFlow workflow...")
    handle = await client.start_workflow(
        BearFlow.run, id="bearflow-workflow-1", task_queue="bearflow"
    )

    print(f"Workflow started with ID: {handle.id}")

    # Wait for the workflow to complete
    result = await handle.result()
    print(f"Workflow completed with result: {result}")


if __name__ == "__main__":
    asyncio.run(trigger_workflow())
