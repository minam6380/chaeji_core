from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from queue_io import append_jsonl, TASKS, EVENTS

app = FastAPI(title="chaeji_core listener")

class Task(BaseModel):
    task_id: str | None = None
    type: str
    pipeline: str | None = None
    inputs: dict | None = None
    constraints: dict | None = None

@app.post('/task')
def add_task(t: Task):
    payload = t.dict()
    payload['task_id'] = payload.get('task_id') or f"task_{datetime.now().isoformat()}"
    payload['status'] = 'QUEUED'
    payload['retries'] = 0
    append_jsonl(TASKS, payload)
    return {'ok': True, 'task_id': payload['task_id']}

class Event(BaseModel):
    kind: str
    data: dict | None = None

@app.post('/event')
def add_event(e: Event):
    payload = {'ts': datetime.now().isoformat(), 'kind': e.kind, 'data': e.data or {}}
    append_jsonl(EVENTS, payload)
    return {'ok': True}

@app.get('/status')
def status():
    return {'ok': True, 'message': 'listener alive'}
