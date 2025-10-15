from __future__ import annotations
import yaml
from adapters.rss_reader import RSSReader

class PolicyFinanceMonitor:
    def __init__(self, rules_path: str = 'rules/policy_sources.yml'):
        self.conf = yaml.safe_load(open(rules_path, 'r', encoding='utf-8'))
        self.rss = RSSReader()

    def scan(self, per_source: int = 5):
        sources = [s for s in self.conf.get('sources', []) if s.get('type')=='rss']
        return self.rss.fetch_many(sources, per_source=per_source)
