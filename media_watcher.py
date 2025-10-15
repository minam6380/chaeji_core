# 언론·SNS·블로그 언급 감시 스텁
class MediaWatcher:
    def mentions(self, keyword: str):
        return [{'source':'news','title':'테스트 기사','sentiment':'+1'}]
