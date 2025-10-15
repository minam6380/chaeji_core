from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Dict

ART_DIR = Path('storage/artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATE = '# {title}

[결론]
- 핵심 메시지 3줄 정리

[핵심 근거]
- 근거1
- 근거2
- 근거3

[적용 절차]
1) 
2) 
3) 

[주의점]
- 

(생성시각: {ts})
'

def run(topic: str = '블로그/뉴스레터 자동생산') -> Dict:
    ts = datetime.now().strftime('%Y%m%d_%H%M')
    title = f'콘텐츠 초안 — {topic}'
    body = TEMPLATE.format(title=title, ts=ts)
    out = ART_DIR / f'content_{ts}.md'
    out.write_text(body, encoding='utf-8')
    return {'pipeline':'content_factory','artifact': str(out)}
