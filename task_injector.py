from pathlib import Path
import json

TASKS = Path('queues/tasks.jsonl')
TASKS.parent.mkdir(parents=True, exist_ok=True)

class TaskInjector:
    def add(self, pipeline: str, inputs: dict = None):
        rec = {'pipeline': pipeline, 'inputs': inputs or {}, 'status': 'QUEUED'}
        with open(TASKS, 'a', encoding='utf-8') as f:
            f.write(json.dumps(rec, ensure_ascii=False) + '
')
        return rec
