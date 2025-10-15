class InvestmentBrain:
    def analyze(self, market: dict) -> dict:
        # 매우 단순한 경보 로직 (stub)
        vol = market.get('volatility','low')
        risk = 'HIGH' if vol == 'high' else 'LOW'
        picks = market.get('watch', ['CHZ','ONDO','DOGE'])
        return {'risk': risk, 'watch': picks}
