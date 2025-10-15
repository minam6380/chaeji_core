import os, json, time
from datetime import datetime
from queue_io import read_jsonl, append_jsonl, TASKS
from report_center import ReportCenter
from self_corrector import SelfCorrector

MAX_RETRIES = 3

# 간단 실행기: 파이프라인 이름만 보고 더미 결과 생성
def _execute_pipeline(task: dict) -> dict:
    p = (task.get('pipeline') or '').lower()
    if p == 'policy_watch':
        from pipelines.policy_watch import run as run_policy
        return run_policy()
    elif p == 'content_factory':
        from pipelines.content_factory import run as run_content
        return run_content()
    else:
        return {'result': 'OK', 'info': 'noop'}

def run_once_from_queue() -> str | None:
    tasks = list(read_jsonl(TASKS))
    if not tasks:
        return None
    # 맨 앞 1건만 처리
    task = tasks[0]
    try:
        res = _execute_pipeline(task)
        # 결과를 보고서로도 남길 수 있음
        text = ReportCenter().build_daily(
            wealth={'assets':'-','delta':'0%'},
            authority={'active':0},
            reputation={'mentions':0},
            state={'now': datetime.now().strftime('%Y-%m-%d %H:%M')}
        )
        os.makedirs('reports', exist_ok=True)
        with open('reports/daily_life_report.md','w',encoding='utf-8') as f:
            f.write(text)
        return 'OK'
    except Exception as e:
        task['retries'] = int(task.get('retries',0)) + 1
        if task['retries'] <= MAX_RETRIES:
            SelfCorrector().recover(str(e))
            append_jsonl(TASKS, task)
        return None

if __name__ == '__main__':
    run_once_from_queue()
