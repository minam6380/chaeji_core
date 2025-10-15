class PrioritySwitcher:
    def choose(self, signals: dict) -> str:
        for d in signals.get('deadlines', []):
            if d.get('d_minus', 999) <= 7:
                return 'authority'
        market = signals.get('market') or {}
        if market.get('volatility') == 'high' or market.get('alert') == 'risk':
            return 'wealth'
        return 'reputation'
