class MediaWatcher:
    def score(self, mentions: list) -> dict:
        pos = sum(1 for m in mentions if m.get('sentiment')=='pos')
        neg = sum(1 for m in mentions if m.get('sentiment')=='neg')
        return {'pos': pos, 'neg': neg, 'net': pos-neg}
