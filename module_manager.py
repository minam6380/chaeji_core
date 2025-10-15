class ModuleManager:
    def __init__(self):
        self.enabled = set()
    def enable(self, name: str):
        self.enabled.add(name)
    def list(self):
        return sorted(self.enabled)
