import json
from report_utils import append_daily

class Executor:
    def run(self, action: dict):
        append_daily('execute: '+json.dumps(action, ensure_ascii=False)[:200])
        return True
