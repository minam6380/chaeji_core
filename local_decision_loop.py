from datetime import datetime
from report_center import ReportCenter
from emotion_analyzer import EmotionAnalyzer
from pipelines import content_factory, book_writer, ip_finance_bridge, policy_watch

# 간단 동기 루프: 현재 시간 기준 스냅샷 생성 + 일일 보고

def run_once():
    # 1) 파이프라인 샘플 실행 (필요 시 주석 해제)
    cf = content_factory.run('일일 리포트 요소')
    bw = book_writer.run('금일 집필 1단위')
    # 2) 상태 스냅샷
    mood = EmotionAnalyzer().sense('집중')
    daily = ReportCenter().build_daily(
        wealth={'assets':'-','delta':'+'},
        authority={'active': 5},
        reputation={'mentions': 3},
        state={'mood': mood}
    )
    # 3) 파일로 저장
    from pathlib import Path
    out = Path('reports/daily_life_report.md')
    out.write_text(daily, encoding='utf-8')
    return {'daily_report': str(out), 'artifacts': [cf['artifact'], bw['artifact']]}

if __name__ == '__main__':
    print(run_once())
