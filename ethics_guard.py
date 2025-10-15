from pathlib import Path
import json, os, time
from dotenv import load_dotenv

load_dotenv()

MEMORY_PATH = Path('storage/chaeji_memory.json')
RULES_PATH = Path('rules/writing_rules.yml')

class EthicsGuard:
    HARD_ASK = ["외부개입 불허", "삭제 이중확인", "결정권자 유일"]
    def confirm_delete(self, target: str) -> bool:
        print(f"[ETHICS] 삭제 이중확인 대상: {target}")
        time.sleep(0.5)
        # 실제 환경에선 사용자 재확인 로직/타이머 적용
        return False

if __name__ == '__main__':
    print('[ETHICS] guard loaded')
