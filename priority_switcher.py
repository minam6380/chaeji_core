# 우선순위 전환 스위처
class PrioritySwitcher:
    def choose(self, signals: dict) -> str:
        # 예: 신호에 따라 wealth/authority/reputation 중 택1
        return signals.get('prefer','wealth')
