from __future__ import annotations
import json, uuid
from pathlib import Path
from datetime import datetime
from schedule_rules import due_tasks

TASKS = Path('queues/tasks.jsonl')
TASKS.parent.mkdir(parents=True, exist_ok=True)
if not TASKS.exists():
    TASKS.write_text('', encoding='utf-8')

def enqueue(task: dict):
    task.setdefault('task_id', f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}")
    task.setdefault('status', 'QUEUED')
    task.setdefault('retries', 0)
    with open(TASKS, 'a', encoding='utf-8') as w:
        w.write(json.dumps(task, ensure_ascii=False) + '
')
    return task['task_id']

def inject_now(now: datetime | None = None):
    now = now or datetime.now()
    for t in due_tasks(now):
        enqueue(t)
    return True

if __name__ == '__main__':
    print(inject_now())
