from report_utils import append_weekly

class WealthReporter:
    def summarize(self, net: float):
        trend = '▲' if net >= 0 else '▼'
        append_weekly(f'Wealth net {trend} {net:,.0f}')
        return True
