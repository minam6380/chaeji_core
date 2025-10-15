from datetime import datetime
import json
from pathlib import Path
from report_utils import write_weekly_kpi, append_anomaly, thresholds

LOG = Path('logs/perf.log')
LOG.parent.mkdir(exist_ok=True)

class DailyGoalEvaluator:
    def evaluate(self, snapshot: dict) -> dict:
        th = thresholds().get('thresholds', {})
        out = {'ok': True, 'violations': []}
        # 기준: outputs_per_day, error_autofix_rate, writing_quality
        if snapshot.get('outputs', 0) < th.get('outputs_per_day', 15):
            out['ok'] = False; out['violations'].append('outputs')
        if snapshot.get('autofix', 0) < th.get('error_autofix_rate', 0.9):
            out['ok'] = False; out['violations'].append('autofix')
        if snapshot.get('quality', 0) < th.get('writing_quality', 4.5):
            out['ok'] = False; out['violations'].append('quality')
        with open(LOG, 'a', encoding='utf-8') as w:
            w.write(json.dumps({'ts': datetime.now().isoformat(timespec='minutes'), 'snapshot': snapshot, 'result': out}, ensure_ascii=False) + '
')
        # 주간 KPI 파일 갱신
        write_weekly_kpi(snapshot)
        # 위반시 이상 보고 적재
        if not out['ok']:
            append_anomaly('KPI 위반: ' + ','.join(out['violations']))
        return out
