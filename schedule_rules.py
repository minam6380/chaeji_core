from __future__ import annotations
from datetime import datetime, time
from typing import List, Dict

# 간단 스케줄 규칙: (HH:MM, pipeline) 목록
RULES: List[Dict] = [
    {'at': '08:20', 'pipeline': 'policy_watch'},
    {'at': '23:30', 'pipeline': 'daily_goal_evaluator'},
]

def _hm(t: str) -> time:
    h, m = map(int, t.split(':'))
    return time(hour=h, minute=m)

def due_tasks(now: datetime) -> List[Dict]:
    out = []
    cur = now.time().replace(second=0, microsecond=0)
    for r in RULES:
        if _hm(r['at']) == cur:
            out.append({'type':'PIPELINE','pipeline': r['pipeline'], 'status':'QUEUED', 'retries':0})
    return out
