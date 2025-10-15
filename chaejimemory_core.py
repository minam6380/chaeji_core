import json
from pathlib import Path

MEM = Path('storage/chaeji_memory.json')
MEM.parent.mkdir(parents=True, exist_ok=True)
if not MEM.exists():
    MEM.write_text('{"ethics":{},"style":{},"goals":[],"routines":{},"contacts":{},"events":{}}', encoding='utf-8')

class ChaejiMemoryCore:
    def load(self) -> dict:
        return json.loads(MEM.read_text(encoding='utf-8'))
    def save(self, data: dict):
        MEM.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        return True
