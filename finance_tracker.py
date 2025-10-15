import csv
from pathlib import Path
from typing import Dict, List

DATA_DIR = Path('storage/finance')
DATA_DIR.mkdir(parents=True, exist_ok=True)

class FinanceTracker:
    def __init__(self):
        self.rows: List[Dict] = []

    def add(self, date: str, income: float, expense: float, memo: str = '') -> None:
        self.rows.append({'date': date, 'income': income, 'expense': expense, 'memo': memo})

    def load_csv(self, pattern: str = '*.csv') -> int:
        cnt = 0
        for p in DATA_DIR.glob(pattern):
            with p.open('r', encoding='utf-8') as r:
                for row in csv.DictReader(r):
                    try:
                        self.rows.append({
                            'date': row.get('date') or row.get('날짜'),
                            'income': float(row.get('income') or row.get('수입') or 0),
                            'expense': float(row.get('expense') or row.get('지출') or 0),
                            'memo': row.get('memo') or row.get('메모') or ''
                        })
                        cnt += 1
                    except Exception:
                        continue
        return cnt

    def summary(self) -> Dict:
        inc = sum(x['income'] for x in self.rows)
        exp = sum(x['expense'] for x in self.rows)
        net = inc - exp
        return {'income': inc, 'expense': exp, 'net': net}
