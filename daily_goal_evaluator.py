from __future__ import annotations
from datetime import datetime
from report_utils import append_daily

class DailyGoalEvaluator:
    def run(self, stats: dict | None = None):
        s = stats or {}
        line = f"outputs={s.get('outputs',0)}, errors={s.get('errors',0)}, recovery={s.get('recovery_rate','-')}"
        append_daily('daily_goal_evaluator: '+line)
        return True

if __name__ == '__main__':
    DailyGoalEvaluator().run({'outputs':3,'errors':0,'recovery_rate':1.0})
