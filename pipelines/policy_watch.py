import yaml, feedparser
from typing import List, Dict

# rules/policy_sources.yml 를 읽어 상위 항목만 요약
def run(limit: int = 5) -> Dict:
    try:
        with open('rules/policy_sources.yml','r',encoding='utf-8') as f:
            conf = yaml.safe_load(f)
    except Exception:
        conf = {'sources': []}
    items: List[Dict] = []
    for src in conf.get('sources', []):
        if src.get('type') == 'rss':
            try:
                feed = feedparser.parse(src['url'])
                for e in feed.get('entries', [])[:2]:
                    items.append({'source': src['name'], 'title': e.get('title',''), 'link': e.get('link','')})
            except Exception:
                continue
        # html 타입은 추후 확장
        if len(items) >= limit:
            break
    return {'pipeline': 'policy_watch', 'count': len(items), 'items': items[:limit]}
