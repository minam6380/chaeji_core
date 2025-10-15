from __future__ import annotations
from typing import Dict, Any

def run_pipeline(name: str, inputs: Dict[str, Any] | None = None) -> Dict[str, Any]:
    inputs = inputs or {}
    name = (name or '').strip().lower()
    if name == 'content_factory':
        from pipelines.content_factory import run
        return run(inputs.get('topic') or '자동 콘텐츠')
    if name == 'book_writer':
        from pipelines.book_writer import run
        return run(inputs.get('chapter') or '샘플 챕터')
    if name == 'ip_finance_bridge':
        from pipelines.ip_finance_bridge import run
        return run(inputs.get('ip_list') or None)
    if name == 'policy_watch':
        from policy_finance_monitor import PolicyFinanceMonitor
        return {'pipeline':'policy_watch', 'items': PolicyFinanceMonitor().scan(limit=5)}
    return {'ok': True, 'pipeline': name, 'result': 'noop'}