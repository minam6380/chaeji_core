import json, os, time
from pathlib import Path
from typing import Dict, Any, Iterable

QUEUES_DIR = Path('queues')
TASKS = QUEUES_DIR / 'tasks.jsonl'
EVENTS = QUEUES_DIR / 'events.jsonl'
LOGS_DIR = Path('logs')
LOGS_DIR.mkdir(exist_ok=True)

QUEUES_DIR.mkdir(exist_ok=True)
for f in (TASKS, EVENTS):
    if not f.exists():
        f.write_text('', encoding='utf-8')

# --- jsonl helpers ---
def append_jsonl(path: Path, obj: Dict[str, Any]) -> None:
    with path.open('a', encoding='utf-8') as w:
        w.write(json.dumps(obj, ensure_ascii=False) + '\n')

def read_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        return []
    with path.open('r', encoding='utf-8') as r:
        for line in r:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue

def rotate_log(name: str, max_keep: int = 5):
    files = sorted(LOGS_DIR.glob(f'{name}*.log'))
    while len(files) > max_keep:
        files[0].unlink(missing_ok=True)
        files = sorted(LOGS_DIR.glob(f'{name}*.log'))

__all__ = ['append_jsonl', 'read_jsonl', 'TASKS', 'EVENTS']
