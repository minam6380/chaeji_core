class PrioritySwitcher:
    def choose(self, signals: dict) -> str:
        # 마감이 임박하면 권위(Authority) 우선
        for d in signals.get('deadlines', []):
            if d.get('d_minus', 999) <= 7:
                return 'authority'
        # 시장 신호가 강하면 부(Wealth) 우선
        market = signals.get('market') or {}
        if market.get('volatility') == 'high' or market.get('alert') == 'risk':
            return 'wealth'
        # 기본: 명예(Reputation) 성장
        return 'reputation'

if __name__ == '__main__':
    s = PrioritySwitcher()
    print(s.choose({'deadlines':[{'d_minus':5}]}))
