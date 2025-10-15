from __future__ import annotations
import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

TASKS = Path('queues/tasks.jsonl')
EVENTS = Path('queues/events.jsonl')
TASKS.parent.mkdir(parents=True, exist_ok=True)
EVENTS.parent.mkdir(parents=True, exist_ok=True)

app = FastAPI(title='Chaeji API')

class TaskIn(BaseModel):
    pipeline: str
    inputs: dict | None = None

class EventIn(BaseModel):
    text: str
    meta: dict | None = None

@app.post('/task')
async def add_task(t: TaskIn):
    rec = {'pipeline': t.pipeline, 'inputs': t.inputs or {}, 'status': 'QUEUED'}
    with open(TASKS, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False)+'
')
    return {'ok': True, 'queued': rec}

@app.post('/event')
async def add_event(e: EventIn):
    rec = {'text': e.text, 'meta': e.meta or {}}
    with open(EVENTS, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False)+'
')
    return {'ok': True}

@app.get('/status')
async def status():
    tasks = TASKS.read_text(encoding='utf-8').splitlines() if TASKS.exists() else []
    events = EVENTS.read_text(encoding='utf-8').splitlines() if EVENTS.exists() else []
    return {'tasks_queued': len([1 for _ in tasks if _]), 'events_logged': len([1 for _ in events if _])}
