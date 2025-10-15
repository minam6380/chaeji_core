class PerformanceMonitor:
    def record(self, metric: str, value):
        # stub: later persist to reports/ or DB
        print({'metric': metric, 'value': value})
        return True
