class EmotionAnalyzer:
    POS = ['좋음','만족','OK','안정','행복','집중']
    NEG = ['피곤','짜증','분노','불안','우울']

    def sense(self, text: str) -> str:
        t = text or ''
        if any(w in t for w in self.NEG):
            return 'stressed'
        if any(w in t for w in self.POS):
            return 'stable'
        return 'neutral'

if __name__ == '__main__':
    e = EmotionAnalyzer()
    print(e.sense('오늘 컨디션 좋음'))
