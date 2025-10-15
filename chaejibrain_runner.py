import json, time
from ethics_guard.py import EthicsGuard

class Judge:
    def route(self, event):
        t = event.get('type')
        if t == 'PIPELINE':
            return event['pipeline']
        return 'content_factory'

if __name__ == '__main__':
    j = Judge()
    print('[JUDGE] test route:', j.route({'type':'PIPELINE','pipeline':'policy_watch'}))
