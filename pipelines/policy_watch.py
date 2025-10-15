from adapters.rss_reader import RSSReader
from pathlib import Path
import yaml

class PolicyWatch:
    def __init__(self):
        self.sources = []
        p = Path('rules/policy_sources.yml')
        if p.exists():
            self.sources = yaml.safe_load(p.read_text(encoding='utf-8')).get('sources',[])
        self.rss = RSSReader()

    def run(self) -> list:
        return self.rss.fetch_many(self.sources, per_source=3)
