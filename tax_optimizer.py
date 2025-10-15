class TaxOptimizer:
    def next_actions(self, month: int) -> list:
        plan = []
        if month in (1,4,7,10):
            plan.append('부가세 중간/확정신고 점검')
        if month == 5:
            plan.append('종합소득세 신고 준비')
        return plan
