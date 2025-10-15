class PositionManager:
    def __init__(self):
        self.positions = []  # [{title, org, start, end}]
    def add(self, title: str, org: str, start: str, end: str = ''):
        self.positions.append({'title': title, 'org': org, 'start': start, 'end': end})
        return True
