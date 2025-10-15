from schedule_rules import due_tasks
from local_decision_loop import LocalDecisionLoop
from full_autonomous_fix_loop import AutoFixLoop

class Scheduler:
    def tick(self):
        enq = LocalDecisionLoop().tick()
        done = AutoFixLoop().tick()
        return {'enqueued': enq, 'processed': done}
