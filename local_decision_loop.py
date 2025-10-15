import os, json
from datetime import datetime

# Core imports
from finance_tracker import FinanceTracker
from policy_finance_monitor import PolicyFinanceMonitor
from investment_brain import InvestmentBrain
from position_manager import PositionManager
from media_watcher import MediaWatcher
from report_center import ReportCenter

REPORT_PATH = 'reports/daily_life_report.md'

def run_daily_loop() -> str:
    """
    최소 실행 루프: 데이터 수집(스텁) → 요약 → 대시보드 MD 생성
    외부 API/키 없이 실행 가능. 실제 연동은 각 모듈 내부 확장.
    """
    # Wealth
    ft = FinanceTracker()
    ft.add(datetime.now().strftime('%Y-%m-%d'), income=0, expense=0, memo='bootstrap')
    wealth = {
        'assets': '₩xxx,xxx,xxx',
        'delta': '+0.0%',
        'policy': PolicyFinanceMonitor().scan(),
        'market': InvestmentBrain().brief(),
    }

    # Authority
    authority = {
        'active': len(PositionManager().list()),
        'renewals': [{'title':'멘토단','d_minus':28}],
    }

    # Reputation
    reputation = {
        'mentions': len(MediaWatcher().mentions('김영채'))
    }

    # State
    state = { 'now': datetime.now().strftime('%Y-%m-%d %H:%M') }

    # Build report text
    text = ReportCenter().build_daily(wealth, authority, reputation, state)

    # Write to file
    os.makedirs('reports', exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(text)

    return REPORT_PATH

if __name__ == '__main__':
    path = run_daily_loop()
    print('[OK] daily report written:', path)
