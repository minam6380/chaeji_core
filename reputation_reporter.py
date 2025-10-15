from report_utils import append_weekly

class ReputationReporter:
    def summarize(self, score: dict):
        append_weekly(f'reputation pos={score.get(''pos'',0)} neg={score.get(''neg'',0)} net={score.get(''net'',0)}')
        return True
