from report_utils import append_daily

class ContentPipeline:
    def publish(self, title: str, summary: str):
        append_daily(f'content: {title} — {summary[:60]}')
        return True
