import json, time
from pathlib import Path
from strategy_runner import StrategyRunner

TASKS = Path('queues/tasks.jsonl')
EVENTS = Path('queues/events.jsonl')

class AutoFixLoop:
    def __init__(self):
        self.runner = StrategyRunner()

    def tick(self):
        if not TASKS.exists():
            return 0
        done = 0
        for line in TASKS.read_text(encoding='utf-8').splitlines():
            try:
                task = json.loads(line)
            except Exception:
                continue
            ok = self.runner.run(task)
            if not ok:
                time.sleep(1)
                ok = self.runner.run(task)
            done += 1 if ok else 0
        return done

if __name__ == '__main__':
    loop = AutoFixLoop()
    print({'processed': loop.tick()})
