from __future__ import annotations
from datetime import datetime
from typing import List, Dict

# 스케줄 표준 (형 루틴 반영)
SCHEDULES: List[Dict] = [
    {'time':'08:20', 'task': {'type':'PIPELINE','pipeline':'policy_watch'}},
    {'time':'09:10', 'task': {'type':'PIPELINE','pipeline':'content_factory','inputs':{'topic':'crypto_brief(요약)'}}},
    {'time':'09:30', 'task': {'type':'PIPELINE','pipeline':'policy_watch','inputs':{'source':'하이브레인넷'}}},
    {'time':'11:00', 'task': {'type':'PIPELINE','pipeline':'book_writer','inputs':{'chapter':'금일 집필 1단위'}}},
    {'time':'14:00', 'task': {'type':'PIPELINE','pipeline':'content_factory','inputs':{'topic':'블로그 1 · 뉴스레터 1'}}},
    {'time':'17:30', 'task': {'type':'PIPELINE','pipeline':'policy_watch','inputs':{'mode':'delta'}}},
    {'time':'21:10', 'task': {'type':'PIPELINE','pipeline':'content_factory','inputs':{'topic':'crypto_brief(야간)'}}},
    {'time':'23:30', 'task': {'type':'PIPELINE','pipeline':'content_factory','inputs':{'topic':'daily_life_report'}}}
]

def due_tasks(now: datetime) -> List[Dict]:
    hhmm = now.strftime('%H:%M')
    return [x['task'] for x in SCHEDULES if x.get('time') == hhmm]
