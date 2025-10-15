class ChaejiLogGuardian:
    def compress(self, text: str) -> str:
        return (text or '')[:2000]
