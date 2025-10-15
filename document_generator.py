from pathlib import Path

TEMPLATES = Path('storage/templates')
TEMPLATES.mkdir(parents=True, exist_ok=True)

class DocumentGenerator:
    def make_resume(self, name: str, roles: list) -> str:
        md = ['# 이력서', f'이름: {name}', '', '## 주요 역할'] + [f'- {r}' for r in roles]
        out = TEMPLATES / 'resume.md'
        out.write_text('
'.join(md), encoding='utf-8')
        return str(out)
