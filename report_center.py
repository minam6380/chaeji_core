from __future__ import annotations
from datetime import datetime
from typing import Dict

class ReportCenter:
    def build_daily(self, wealth: Dict, authority: Dict, reputation: Dict, state: Dict) -> str:
        now = state.get('now', datetime.now().strftime('%Y-%m-%d %H:%M'))
        lines = []
        lines.append('[CHAEEJI LIFE DASHBOARD]')
        lines.append('날짜: ' + now)
        lines.append('')
        lines.append('💰 자산현황')
        lines.append('- 총 평가액: ' + str(wealth.get('assets','-')) + ' (' + str(wealth.get('delta','')) + ')')
        lines.append('')
        lines.append('🏛 권위/직위')
        lines.append('- 활성 포지션: ' + str(authority.get('active','-')))
        lines.append('')
        lines.append('🌟 명예/브랜딩')
        lines.append('- 언급 추정: ' + str(reputation.get('mentions','-')) + '회')
        lines.append('')
        lines.append('🧠 윤리·감정: ' + str(state.get('mood','-')))
        return '\n'.join(lines)
