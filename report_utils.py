from datetime import datetime
from pathlib import Path
import yaml

REPORT_DIR = Path('reports')
REPORT_DIR.mkdir(exist_ok=True)
WEEKLY = REPORT_DIR / 'weekly_kpi.md'
ANOM = REPORT_DIR / 'anomalies.md'

def write_weekly_kpi(snapshot: dict) -> str:
    lines = [
        '# WEEKLY KPI',
        '- 자동 생성 산출물/일 평균: ' + str(snapshot.get('outputs','-')),
        '- 오류 자동복구율: ' + str(snapshot.get('autofix','-')),
        '- 원고 품질 스코어: ' + str(snapshot.get('quality','-'))
    ]
    WEEKLY.write_text('
'.join(lines), encoding='utf-8')
    return str(WEEKLY)

def append_anomaly(note: str) -> str:
    with open(ANOM, 'a', encoding='utf-8') as w:
        w.write('- ' + datetime.now().strftime('%Y-%m-%d %H:%M') + ' — ' + note + '
')
    return str(ANOM)

def thresholds(path: str = 'rules/kpi_thresholds.yml') -> dict:
    try:
        return yaml.safe_load(open(path,'r',encoding='utf-8')) or {}
    except Exception:
        return {}
