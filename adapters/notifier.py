import os

class Notifier:
    def __init__(self):
        self.telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')

    def send(self, channel: str, text: str):
        # stub: implement Telegram/Slack in future
        print(f'[{channel}] {text}')
        return True
