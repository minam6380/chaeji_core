# 3루프 종합 리포트
class ReportCenter:
    def build_daily(self, wealth: dict, authority: dict, reputation: dict, state: dict) -> str:
        return (
            f"[CHAEEJI LIFE DASHBOARD]
"
            f"날짜: {state.get('now','')}\n\n"
            f"💰 자산현황\n- 총 평가액: {wealth.get('assets','-')} ({wealth.get('delta','')})\n\n"
            f"🏛 권위/직위\n- 유지: {authority.get('active','-')}건\n\n"
            f"🌟 명예/브랜딩\n- 언급: {reputation.get('mentions','-')}회\n"
        )
