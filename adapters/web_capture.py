import hashlib, json
from datetime import datetime
from pathlib import Path

EVID = Path('storage/evidence')
EVID.mkdir(parents=True, exist_ok=True)

class WebCapture:
    def snapshot(self, url: str, html: str = ''):
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        h = hashlib.sha256((url+html).encode('utf-8')).hexdigest()[:12]
        meta = {'url': url, 'ts': ts, 'sha': h}
        (EVID / f'{ts}_{h}.meta.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
        (EVID / f'{ts}_{h}.html').write_text(html, encoding='utf-8')
        return meta
