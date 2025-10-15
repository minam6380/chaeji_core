from __future__ import annotations
from datetime import datetime
from typing import Dict, Any, List

class Scheduler:
    """
    스케줄링 규칙과 트리거 결정을 담당.
    """
    DAILY = [{'time': '07:30'}, {'time': '23:30'}]
    WEEKLY = [{'dow': 'Mon', 'time': '09:00'}]
    MONTHLY = [{'day': 1, 'time': '09:00'}]

    @staticmethod
    def should_run(now: datetime, rule: Dict[str, Any]) -> bool:
        t = rule.get('time')
        if t and now.strftime('%H:%M') == t:
            if 'dow' in rule and rule['dow'] != now.strftime('%a'):
                return False
            if 'day' in rule and rule['day'] != now.day:
                return False
            return True
        return False

if __name__ == '__main__':
    now = datetime.now().replace(hour=7, minute=30)
    print(Scheduler.should_run(now, {'time':'07:30'}))
