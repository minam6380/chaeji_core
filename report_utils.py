from __future__ import annotations
from datetime import datetime
from pathlib import Path
DAILY = Path('reports/daily_status.md')
WEEKLY = Path('reports/weekly_kpi.md')
ANOM = Path('reports/anomalies.md')
DAILY.parent.mkdir(parents=True, exist_ok=True)

def append_daily(line: str):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(DAILY, 'a', encoding='utf-8') as w:
        w.write('- ['+ts+'] '+line+'\n')

def append_weekly(line: str):
    ts = datetime.now().strftime('%Y-%m-%d')
    with open(WEEKLY, 'a', encoding='utf-8') as w:
        w.write('- ['+ts+'] '+line+'\n')

def append_anomaly(line: str):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(ANOM, 'a', encoding='utf-8') as w:
        w.write('- ['+ts+'] '+line+'\n')
