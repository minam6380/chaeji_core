class ApplicationScheduler:
    def pick(self, calls: list, profile: dict) -> list:
        # calls: [{'title','req':['학력','지역',...]}]
        ok = []
        for c in calls:
            req = set(c.get('req', []))
            mine = set(profile.get('tags', []))
            if req.issubset(mine):
                ok.append(c)
        return ok
