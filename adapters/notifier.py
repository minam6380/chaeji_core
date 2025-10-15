import json
from pathlib import Path

LOG = Path('logs/notify.log')
LOG.parent.mkdir(exist_ok=True)

class Notifier:
    def telegram(self, text: str, chat_id: str = 'LOCAL'):
        with open(LOG, 'a', encoding='utf-8') as w:
            w.write(json.dumps({'type':'telegram','chat_id':chat_id,'text':text}, ensure_ascii=False)+'
')
        return True

    def email(self, to: str, subject: str, body: str):
        with open(LOG, 'a', encoding='utf-8') as w:
            w.write(json.dumps({'type':'email','to':to,'subject':subject,'body':body}, ensure_ascii=False)+'
')
        return True
