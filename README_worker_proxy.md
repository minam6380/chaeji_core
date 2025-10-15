# Calendar Proxy (Cloudflare Workers → Google Apps Script)

Google Calendar에 일정을 자동 생성하기 위한 **프록시 워커** 코드입니다.

## 구조
You → ChatGPT → Cloudflare Worker → Apps Script(Web App) → Google Calendar

## 배포 절차(요약)
1. Cloudflare 대시보드 → Workers → Create → Quick edit
2. `worker.js` 붙여넣고 **Save/Deploy**
3. Settings → Variables 등록
   - `APPS_SCRIPT_URL` = Apps Script 웹앱 `/exec` URL
   - `SHARED_SECRET`   = Apps Script 코드와 동일한 시크릿
4. 발급된 워커 URL로 POST 전송하면 일정 생성됨

## 요청 JSON 예시
```json
{
  "title": "특허심판원 구술심리",
  "start": "2025-11-04T14:00:00+09:00",
  "end":   "2025-11-04T15:00:00+09:00",
  "location": "특허심판원",
  "desc": "오후 2시 구술심리. 신분증/자료 지참."
}
```

> 보안: `SHARED_SECRET`는 코드에 커밋하지 말고, Cloudflare Variables에만 저장하세요.
