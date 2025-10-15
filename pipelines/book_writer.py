from datetime import datetime
from pathlib import Path

ART_DIR = Path('storage/artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

BOOK_HEAD = '# {title}

'
SECTIONS = ['결론','핵심 근거','적용 절차','주의점']

def run(chapter='제도 중심 재테크서 — 샘플 챕터', sections=None):
    sections = sections or SECTIONS
    ts = datetime.now().strftime('%Y%m%d_%H%M')
    title = f'{chapter}'
    body = [BOOK_HEAD.format(title=title)]
    for s in sections:
        body.append(f'## {s}
')
        body.append('- 항목 1
- 항목 2
- 항목 3

')
    out = ART_DIR / f'book_{ts}.md'
    out.write_text(''.join(body), encoding='utf-8')
    return {'pipeline':'book_writer','artifact': str(out)}
