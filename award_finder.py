class AwardFinder:
    def shortlist(self, calls: list, profile: dict) -> list:
        return [c for c in calls if profile.get('field') in c.get('fields', [])]
