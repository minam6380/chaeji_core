from dataclasses import dataclass
import time
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None

RULES_PATH = Path('rules/writing_rules.yml')

@dataclass
class EthicsReport:
    ok: bool
    banned_hits: list
    notes: list

class EthicsGuard:
    DEFAULT_BANNED = ['아카이브','레버리지','시너지','패러다임']

    def __init__(self):
        self.banned = set(self.DEFAULT_BANNED)
        if RULES_PATH.exists() and yaml:
            try:
                data = yaml.safe_load(RULES_PATH.read_text(encoding='utf-8')) or {}
                add = data.get('banned_words') or []
                self.banned.update(add)
            except Exception:
                pass

    def scan_text(self, text: str) -> EthicsReport:
        lower = (text or '').lower()
        hits = [w for w in self.banned if w.lower() in lower]
        return EthicsReport(ok=(len(hits)==0), banned_hits=hits, notes=([] if not hits else ['금지어 포함']))

    def issue_delete_token(self, target: str) -> str:
        return f'DEL-{int(time.time())}'

    def verify_delete_token(self, token: str, max_age_sec: int = 600) -> bool:
        try:
            _, ts = token.split('-')
            return (time.time() - int(ts)) <= max_age_sec
        except Exception:
            return False
