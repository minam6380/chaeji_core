from pipelines.policy_watch import PolicyWatch

class StrategyRunner:
    def run(self, task: dict) -> bool:
        t = (task or {}).get('pipeline')
        if t == 'policy_watch':
            pw = PolicyWatch()
            items = pw.run()
            print({'policy_watch': len(items)})
            return True
        return False
