from __future__ import annotations
from datetime import datetime
from typing import Optional
from task_injector import TaskInjector
from schedule_rules import due_tasks

# 매 분 실행 가정: 현재 시각에 해당하는 규칙만 태스크로 넣음
class LocalDecisionLoop:
    def __init__(self):
        self.injector = TaskInjector()

    def tick(self, now: Optional[datetime] = None) -> int:
        now = now or datetime.now()
        tasks = due_tasks(now)
        for t in tasks:
            self.injector.add(t['pipeline'], {})
        return len(tasks)

if __name__ == '__main__':
    print({'enqueued': LocalDecisionLoop().tick()})
