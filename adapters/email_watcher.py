import email, os
from pathlib import Path

INBOX = Path('storage/emails')
INBOX.mkdir(parents=True, exist_ok=True)

class EmailWatcher:
    def scan(self, pattern='*.eml'):
        results = []
        for p in INBOX.glob(pattern):
            try:
                msg = email.message_from_binary_file(open(p,'rb'))
                results.append({'file': p.name, 'subject': msg.get('Subject'), 'from': msg.get('From')})
            except Exception:
                continue
        return results
