from datetime import datetime

class PerformanceMonitor:
    def kpi_snapshot(self) -> dict:
        # 스텁: 나중에 artifacts/ evidence/ 및 로그 기반 통계로 확장
        return {
            'outputs_per_day': 0,
            'error_autofix_rate': 0.0,
            'writing_quality': 0.0,
            'timestamp': datetime.now().isoformat()
        }
