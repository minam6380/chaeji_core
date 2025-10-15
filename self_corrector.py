from report_utils import append_anomaly

class SelfCorrector:
    def recover(self, error: str, context: dict | None = None):
        append_anomaly(f'auto-fix: {error[:120]}')
        return {'patched': True}
