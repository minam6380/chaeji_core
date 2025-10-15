# 이력서/경력증명/위촉장 자동생성 스텁
class DocumentGenerator:
    def make_resume(self, profile: dict) -> str:
        return f"# 이력서\n이름: {profile.get('name','형')}"
