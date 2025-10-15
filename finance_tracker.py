from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime

STORAGE = Path('storage')
STORAGE.mkdir(parents=True, exist_ok=True)
ASSETS = STORAGE / 'artifacts'
ASSETS.mkdir(parents=True, exist_ok=True)

class FinanceTracker:
    def __init__(self):
        self.ledger = STORAGE / 'finance_ledger.jsonl'
        if not self.ledger.exists():
            self.ledger.write_text('', encoding='utf-8')

    def add_tx(self, ts: str, kind: str, amount: float, memo: str = ''):
        rec = {'ts': ts, 'kind': kind, 'amount': amount, 'memo': memo}
        with open(self.ledger, 'a', encoding='utf-8') as w:
            w.write(json.dumps(rec, ensure_ascii=False)+'
')
        return rec

    def snapshot(self):
        income = expense = 0.0
        for line in self.ledger.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            amt = float(rec.get('amount',0))
            if (rec.get('kind') or '').lower() in ('income','입금','수입'):
                income += amt
            else:
                expense += amt
        return {'income': income, 'expense': expense, 'net': income-expense, 'updated_at': datetime.now().isoformat(timespec='seconds')}
