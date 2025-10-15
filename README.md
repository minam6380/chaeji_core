# chaeji_core

자율 루프: 판단 → 생성 → 검증 → 실행 → 보고.

## 구조
- 모듈 맵과 폴더는 README 및 각 파일 상단 주석 참고.
- 최소 실행 단위: `local_decision_loop.py`

## 빠른 시작
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python local_decision_loop.py --once
```

## KPI 대시보드
- `reports/daily_status.md`, `reports/weekly_kpi.md`를 갱신
- `performance_monitor.py`가 집계

## 보안
- `.env`에 비밀키, 토큰 저장 (예: `API_KEY`, `TELEGRAM_TOKEN`)
- `storage/secret/`은 gitignore 처리
