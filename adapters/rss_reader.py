import yaml, feedparser
from typing import List, Dict

class RSSReader:
    def fetch_many(self, sources: List[Dict], per_source: int = 2) -> List[Dict]:
        items: List[Dict] = []
        for src in sources:
            if src.get('type') != 'rss':
                continue
            try:
                feed = feedparser.parse(src['url'])
                for e in feed.get('entries', [])[:per_source]:
                    items.append({'source': src['name'], 'title': e.get('title',''), 'link': e.get('link','')})
            except Exception:
                continue
        return items
