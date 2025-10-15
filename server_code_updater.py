class ServerCodeUpdater:
    def deploy(self, stage: str = 'staging'):
        print({'deploy': stage})
        return True
    def rollback(self):
        print({'rollback': 'prev'})
        return True
