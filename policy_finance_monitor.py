import yaml, feedparser
from typing import List, Dict
from adapters.rss_reader import RSSReader

class PolicyFinanceMonitor:
    def __init__(self, sources_file: 'str' = 'rules/policy_sources.yml'):
        self.sources_file = sources_file
    def scan(self, limit: int = 5) -> List[Dict]:
        try:
            with open(self.sources_file,'r',encoding='utf-8') as f:
                conf = yaml.safe_load(f) or {}
        except Exception:
            conf = {'sources': []}
        srcs = conf.get('sources', [])
        items = RSSReader().fetch_many(srcs, per_source=2)
        return items[:limit]
