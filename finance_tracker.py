from dataclasses import dataclass
from typing import List, Dict, Any

# 💰 Wealth Core
@dataclass
class CashFlow:
    date: str
    income: float
    expense: float
    memo: str = ''

class FinanceTracker:
    def __init__(self):
        self.records: List[CashFlow] = []

    def add(self, date: str, income: float = 0.0, expense: float = 0.0, memo: str = ''):
        self.records.append(CashFlow(date, income, expense, memo))

    def summary(self) -> Dict[str, Any]:
        income = sum(r.income for r in self.records)
        expense = sum(r.expense for r in self.records)
        return {
            'net': income - expense,
            'income': income,
            'expense': expense,
            'count': len(self.records)
        }

if __name__ == '__main__':
    ft = FinanceTracker()
    ft.add('2025-10-15', income=1000000, memo='테스트')
    print('[Wealth] summary:', ft.summary())
