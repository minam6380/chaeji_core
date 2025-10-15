from __future__ import annotations
import json, traceback
from pathlib import Path
from datetime import datetime

from self_corrector import SelfCorrector
from report_utils import append_anomaly

try:
    from strategy_runner import run_pipeline
except Exception:
    def run_pipeline(name: str, inputs: dict | None = None):
        return {'ok': True, 'pipeline': name, 'result': 'noop'}

TASKS = Path('queues/tasks.jsonl')
EVENTS = Path('queues/events.jsonl')
TASKS.parent.mkdir(parents=True, exist_ok=True)
for f in (TASKS, EVENTS):
    if not f.exists():
        f.write_text('', encoding='utf-8')

MAX_RETRIES = 3

def _jsonl_read(path: Path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            yield json.loads(line)
        except Exception:
            continue

def _jsonl_append(path: Path, obj: dict):
    with open(path, 'a', encoding='utf-8') as w:
        w.write(json.dumps(obj, ensure_ascii=False) + '
')

def _load_next_queued():
    lines = list(_jsonl_read(TASKS))
    for it in lines:
        if it.get('status','QUEUED') == 'QUEUED':
            return it
    return None

def _rewrite_with_update(target_id: str, update: dict):
    lines = list(_jsonl_read(TASKS))
    out = []
    for it in lines:
        if it.get('task_id') == target_id:
            it.update(update)
        out.append(it)
    TASKS.write_text('
'.join(json.dumps(x, ensure_ascii=False) for x in out) + ('
' if out else ''), encoding='utf-8')

def consume_one():
    task = _load_next_queued()
    if not task:
        return {'ok': True, 'info': 'no queued task'}
    tid = task.get('task_id') or f"ad-hoc-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    retries = int(task.get('retries', 0))
    _rewrite_with_update(tid, {'status':'RUNNING', 'started_at': datetime.now().isoformat(timespec='seconds')})
    try:
        if task.get('type') == 'PIPELINE':
            res = run_pipeline(task.get('pipeline',''), task.get('inputs') or {})
        else:
            res = {'ok': True, 'result': 'noop'}
        _rewrite_with_update(tid, {'status':'DONE','finished_at': datetime.now().isoformat(timespec='seconds'),'result': res})
        _jsonl_append(EVENTS, {'ts': datetime.now().isoformat(), 'event':'TASK_DONE', 'task_id': tid})
        return {'ok': True, 'task_id': tid, 'result': res}
    except Exception as e:
        err = {'ts': datetime.now().isoformat(), 'event':'TASK_ERROR', 'task_id': tid, 'error': str(e), 'trace': traceback.format_exc()}
        _jsonl_append(EVENTS, err)
        retries += 1
        if retries <= MAX_RETRIES:
            _rewrite_with_update(tid, {'status':'QUEUED','retries': retries})
            return {'ok': False, 'task_id': tid, 'action':'retry', 'retries': retries}
        else:
            _rewrite_with_update(tid, {'status':'FAILED','retries': retries})
            SelfCorrector().recover(json.dumps(err, ensure_ascii=False))
            append_anomaly(f"TASK_FAILED after retries: {tid}")
            return {'ok': False, 'task_id': tid, 'action':'failed'}

if __name__ == '__main__':
    print(consume_one())
