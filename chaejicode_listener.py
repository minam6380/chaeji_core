class ChaejiCodeListener:
    def on_event(self, evt: dict):
        return {'ok': True, 'echo': evt}
