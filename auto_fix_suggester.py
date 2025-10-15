class AutoFixSuggester:
    def suggest(self, error: str) -> list:
        return [f'옵션A: {error[:60]} 처리 로직 완화', f'옵션B: 재시도 대기시간 +3s']
