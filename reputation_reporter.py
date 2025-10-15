from pathlib import Path
from typing import Dict

LOG = Path('logs/reputation_report.log')
LOG.parent.mkdir(exist_ok=True)

class ReputationReporter:
    def build_monthly_index(self, mentions: int, posts: int, awards: int) -> Dict:
        score = mentions*0.5 + posts*0.3 + awards*0.2
        data = {'mentions': mentions, 'posts': posts, 'awards': awards, 'index': round(score,2)}
        with open(LOG, 'a', encoding='utf-8') as w:
            w.write(str(data)+'\n')
        return data
