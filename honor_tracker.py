class HonorTracker:
    def renewals_due(self, items: list, days: int = 30) -> list:
        # items: [{'title','end_in_days': int}] (단순 스텁)
        return [x for x in items if int(x.get('end_in_days', 9999)) <= days]
