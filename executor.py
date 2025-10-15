from __future__ import annotations
import os, json, shutil
from pathlib import Path
from typing import Dict, Any

ARTIFACTS_DIR = Path('storage/artifacts')
EVIDENCE_DIR = Path('storage/evidence')
REPORTS_DIR = Path('reports')

for d in (ARTIFACTS_DIR, EVIDENCE_DIR, REPORTS_DIR):
    d.mkdir(parents=True, exist_ok=True)

class Executor:
    """
    실행 유형
    - write_file: 파일/보고서/템플릿 쓰기
    - save_artifact: 산출물 저장(파일 복사/스냅샷)
    - notify: 알림 훅(추후 adapters/notifier 연동)
    - web_capture: 증빙 저장(추후 adapters/web_capture 연동)
    """
    def run(self, job: Dict[str, Any]) -> Dict[str, Any]:
        kind = (job.get('type') or '').lower()
        if kind == 'write_file':
            path = Path(job['path'])
            path.parent.mkdir(parents=True, exist_ok=True)
            data = job.get('content','')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(data)
            return {'ok': True, 'path': str(path)}
        elif kind == 'save_artifact':
            src = Path(job['src'])
            dst = ARTIFACTS_DIR / Path(job.get('dst', src.name)).name
            if src.exists():
                shutil.copy2(src, dst)
                return {'ok': True, 'artifact': str(dst)}
            return {'ok': False, 'reason': 'src_not_found'}
        elif kind == 'notify':
            payload = {k:v for k,v in job.items() if k!='type'}
            log = REPORTS_DIR / 'notify.log'
            with open(log, 'a', encoding='utf-8') as w:
                w.write(json.dumps(payload, ensure_ascii=False) + '\n')
            return {'ok': True, 'logged': str(log)}
        elif kind == 'web_capture':
            return {'ok': True, 'info': 'captured_stub'}
        else:
            return {'ok': True, 'info': 'noop'}

if __name__ == '__main__':
    ex = Executor()
    print(ex.run({'type':'write_file','path':'reports/test.md','content':'hello'}))
