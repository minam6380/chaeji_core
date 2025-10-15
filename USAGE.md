# 사용법

## 1) 가상환경 & 설치
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2) 일일 루프 1회 실행
```bash
python local_decision_loop.py
```

성공 시 `reports/daily_life_report.md`가 생성되고,
대시보드 텍스트가 들어간다.

## 3) 스케줄 연결(예시)
- Linux/systemd, pm2, Windows Task Scheduler 등으로
  매일 07:30 / 23:30에 `python local_decision_loop.py` 실행.

## 다음 단계
- Wealth/Authority/Reputation 각 모듈에 실제 데이터 연동(API/파일) 추가
- `report_center.py` 포맷 고도화, KPI 집계 연결
- 실패 자동 복구(SelfCorrector) 후 재시도 3회 구현
