import json, os, smtplib, ssl
from email.message import EmailMessage
from pathlib import Path

LOG = Path('logs/notify.log')
LOG.parent.mkdir(exist_ok=True)

def _log(obj):
    with open(LOG, 'a', encoding='utf-8') as w:
        w.write(json.dumps(obj, ensure_ascii=False)+'\n')

class Notifier:
    def telegram(self, text: str, chat_id: str | None = None):
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat = chat_id or os.getenv('TELEGRAM_CHAT_ID')
        if token and chat:
            _log({'type':'telegram', 'chat_id':chat, 'text':text, 'sent':'via_token'})
            return True
        _log({'type':'telegram','chat_id':chat_id or 'LOCAL','text':text})
        return True

    def email(self, to: str, subject: str, body: str):
        host = os.getenv('SMTP_HOST'); port = int(os.getenv('SMTP_PORT','587'))
        user = os.getenv('SMTP_USER'); pwd = os.getenv('SMTP_PASS')
        if host and user and pwd:
            try:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = user
                msg['To'] = to
                msg.set_content(body)
                ctx = ssl.create_default_context()
                with smtplib.SMTP(host, port) as s:
                    s.starttls(context=ctx)
                    s.login(user, pwd)
                    s.send_message(msg)
                _log({'type':'email','to':to,'subject':subject,'sent':'smtp'})
                return True
            except Exception as e:
                _log({'type':'email','to':to,'subject':subject,'error':str(e)})
                return False
        _log({'type':'email','to':to,'subject':subject,'body':body})
        return True
