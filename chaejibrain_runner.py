from datetime import datetime
from emotion_analyzer import EmotionAnalyzer
from priority_switcher import PrioritySwitcher
from ethics_guard import EthicsGuard

class Judge:
    ""
    입력 이벤트 → 우선 코어 선택(wealth/authority/reputation) → 파이프라인 라우팅
    윤리 가드로 금지어/민감행위 사전 확인
    ""
    def __init__(self):
        self.emotions = EmotionAnalyzer()
        self.switcher = PrioritySwitcher()
        self.ethics = EthicsGuard()

    def decide(self, event: dict) -> dict:
        text = (event.get('text') or '')
        er = self.ethics.scan_text(text)
        if not er.ok:
            return {'ok': False, 'reason': 'banned_words', 'hits': er.banned_hits}

        signal = {
            'time': datetime.now().strftime('%H:%M'),
            'emotion': self.emotions.sense(text)
        }
        # 도메인 힌트 수집
        signal['deadlines'] = event.get('deadlines') or []
        signal['market'] = event.get('market') or {}

        core = self.switcher.choose(signal)
        pipeline = self._map_core_to_pipeline(core)
        return {'ok': True, 'core': core, 'pipeline': pipeline, 'signal': signal}

    def _map_core_to_pipeline(self, core: str) -> str:
        return {
            'wealth': 'policy_watch',
            'authority': 'content_factory',
            'reputation': 'content_factory'
        }.get(core, 'content_factory')

if __name__ == '__main__':
    j = Judge()
    print(j.decide({'text':'오늘 일정 정리'}))
