from typing import Dict
from ethics_guard import EthicsGuard
from emotion_analyzer import EmotionAnalyzer
from priority_switcher import PrioritySwitcher

class ChaejiBrain:
    def __init__(self):
        self.ethics = EthicsGuard()
        self.emotion = EmotionAnalyzer()
        self.switcher = PrioritySwitcher()

    def route(self, event: Dict) -> Dict:
        text = event.get('text','')
        ethics = self.ethics.scan_text(text)
        mood = self.emotion.sense(text)
        target = self.switcher.choose(event.get('signals',{}))
        return {'target_loop': target, 'mood': mood, 'ethics_ok': ethics.ok, 'banned': ethics.banned_hits}
