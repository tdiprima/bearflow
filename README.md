# 🐻 Bearflow: Workflow Orchestration Playground

Welcome to **Bearflow**, where pipelines roam free and tasks get tamed.  
This repo is a mini playground for exploring different **workflow management systems** — from the classics to the shiny new ones.  

It's not production. It's **proof-of-concept territory**.  
Bring snacks, curiosity, and maybe Redis.  

## 🗺️ What's Inside

Each folder/file is a tiny POC showing a 2-task workflow:

Task A → Task B → "Flow complete!"

| Framework | Filename | Vibe | Notes |
|------------|-----------|------|-------|
| 🌀 **Prefect** | `bearflow_prefect.py` | smooth, modern | Pythonic, easy orchestration |
| ⚙️ **Celery** | `celery_den.py` | old reliable | Great for async queues, needs broker |
| 🧩 **Dagster** | `dagster_den.py` | data-pipeline friendly | strong typing + observability |
| ⏳ **Temporal** | `temporal_cave.py` | next-gen vibes | durable, resilient workflows |

## 🧰 Setup

If you're using [`uv`](https://github.com/astral-sh/uv) (and you should), grab the dependencies you need:

### Install them all

```bash
uv sync
# or
uv add prefect celery dagster temporalio redis
```

## 🧪 Running the POCs

Each script can be run locally:

### Prefect

```bash
uv run bearflow_prefect.py
```

### Celery

```bash
# Terminal A: start redis
./redisctl.sh up
# Or
redis-server

# Terminal 1: start worker
celery -A celery_den worker --loglevel=info

# Terminal 2: trigger tasks
uv run celery_trigger.py
```

### Dagster

```bash
uv run dagster_den.py
```

### Temporal

```bash
# Terminal 1: Start Temporal server
temporal server start-dev

# Terminal 2: Run the worker
uv run temporal_cave.py

# Terminal 3: Trigger the workflow
uv run temporal_trigger.py
```

## 🧠 Quick Comparison

| Framework    | Setup Effort | Learning Curve | Maintenance   | Scalability   | Bear's Hot Take                                    |
| ------------ | ------------ | -------------- | ------------- | ------------- | -------------------------------------------------- |
| **Prefect**  | ⭐⭐           | 🧩 Smooth      | 🌿 Low        | 🚀 High       | *Feels like the future of "just works" workflows*  |
| **Celery**   | ⭐            | 🪓 Moderate    | 🧱 Medium     | 🚀 High       | *Still the champ for simple queues, but dusty*     |
| **Dagster**  | ⭐⭐           | 📈 Steep       | 🌱 Manageable | 🚀 High       | *Data teams love it — structured and robust*       |
| **Temporal** | ⭐⭐⭐          | 🧩 Medium      | 🌿 Low        | 🚀🚀🚀 Insane | *Resilient, future-proof, but needs infra love*    |

## 🪄 Future Ideas

* Add async workflows for Celery & Prefect
* Compare logging/monitoring tools (Prefect Cloud vs Dagit vs Temporal UI)
* Dockerize everything for local orchestration lab
* Write a wrapper script (`run_all_bears.py`) to test all flows together

## 🐻 Closing Thoughts

"Workflows are just glorified to-do lists for machines."  
— Bear, probably

This repo exists so you can explore what feels **right-sized** for your team — whether it's a tiny Python job runner or a full-blown orchestrator.

No pressure, no vendor lock-in, just vibes.

**License:** MIT  
**Maintainer:** 🧸 Bear  
**Mood:** ✨ mildly chaotic but organized

<br>
