# ⏰ 내일 아침 10시 체크리스트
## 🗓️ 2026-06-08 (월) 오전 10:00 KST

> 📍 어떤 PC에서도 이 URL 하나로 바로 시작:
> **https://github.com/aigw2026-cpu/claude-mcp-workspace**

---

## ✅ 어제까지 완료된 것 (건드릴 필요 없음)

| 항목 | 상태 | 비고 |
|------|------|------|
| Smithery MCP 152 tools | ✅ 완료 | Gmail/Calendar/Drive/Sheets/Notion |
| GitHub 레포 구조화 | ✅ 완료 | 20+ 파일, 자동화 중 |
| GitHub Actions 자동화 | ✅ 가동 중 | 매일 자정 Obsidian 동기화 |
| SMITHERY_API_KEY Secret | ✅ 등록 완료 | 어제 직접 입력 완료 |
| Obsidian Sync Plus | ✅ Active | aigw2026@gmail.com, 갱신 06-24 |

---

## 🔴 오늘 할 것 2가지 (총 15분)

---

### ① Claude Desktop 설치 (8분)

**Step 1.** 다운로드
```
https://claude.ai/download
```
→ macOS 또는 Windows 버전 다운로드 & 설치

**Step 2.** 설정 파일 적용
```bash
# macOS 터미널에서:
cp ~/Downloads/claude_desktop_config.json    ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

또는 GitHub에서 직접 복사:
```
https://github.com/aigw2026-cpu/claude-mcp-workspace/blob/main/claude_desktop_config.json
```
→ Raw 클릭 → 전체 복사 → 파일로 저장

**Step 3.** API 키 교체
파일 안의 `YOUR_SMITHERY_API_KEY_HERE` 부분을:
```
9c893b26-d0b2-4ae0-8fe3-1517a42d283f
```
로 교체 (어제 GitHub Secret에 넣은 것과 동일한 키)

**Step 4.** Claude Desktop 재시작 후 테스트
```
"오늘 Gmail 읽지 않은 이메일 3개 요약해줘"
"오늘 Google Calendar 일정 알려줘"
"Notion 워크스페이스 페이지 목록 보여줘"
```

---

### ② Slack 인증 (5분)

**조건**: 최신 Chrome 브라우저 사용 (Chrome 116 이하 불가)

**Step 1.** 최신 Chrome에서 접속:
```
https://smithery.run/aigw2026/slack/setup
```

**Step 2.** Slack 워크스페이스 이메일 입력:
```
aigw2026@gmail.com
```

**Step 3.** Slack 로그인 → **Allow** 클릭

**Step 4.** 완료 확인:
```
https://smithery.ai/console/toolbox
```
→ Slack: 0 tools → 완료 시 tools 생김

---

## 🔗 핵심 링크 모음 (북마크 추천)

| 서비스 | URL |
|--------|-----|
| 📁 **GitHub 레포** | https://github.com/aigw2026-cpu/claude-mcp-workspace |
| 🤖 **Smithery Toolbox** | https://smithery.ai/console/toolbox |
| 🔑 **API Keys** | https://smithery.ai/console/api-keys |
| 📊 **GitHub Actions** | https://github.com/aigw2026-cpu/claude-mcp-workspace/actions |
| 📓 **Obsidian 계정** | https://obsidian.md/account |
| 🔒 **GitHub Secrets** | https://github.com/aigw2026-cpu/claude-mcp-workspace/settings/secrets/actions |
| ⬇️ **Claude Desktop** | https://claude.ai/download |
| 📋 **이 체크리스트** | https://github.com/aigw2026-cpu/claude-mcp-workspace/blob/main/TOMORROW-10AM-CHECKLIST.md |

---

## 📋 완료 후 전체 시스템 상태

```
Claude Desktop (로컬 앱)
    │
    └── Smithery MCP Toolbox
            ├── Gmail        ✅ 23 tools
            ├── Calendar     ✅ 28 tools
            ├── Drive        ✅ 51 tools
            ├── Sheets       ✅ 36 tools
            ├── Notion       ✅ 14 tools
            └── Slack        ← 오늘 완료 예정

GitHub Actions (매일 자정 자동)
    └── Obsidian Vault 자동 동기화
            └── Obsidian Sync Plus (모든 기기)
```

---

## 💡 완료 후 첫날 해볼 것

```
아침 브리핑 (Claude Desktop에서):
"Gmail 오늘 읽지 않은 이메일 요약하고,
 Google Calendar 오늘 일정 알려주고,
 Notion에 오늘 날짜로 일일 계획 페이지 만들어줘"
```

---

## 🆘 막히면?

Claude에게 물어보면서 이 체크리스트 URL 공유:
```
https://github.com/aigw2026-cpu/claude-mcp-workspace/blob/main/TOMORROW-10AM-CHECKLIST.md
```

---

*작성: 2026-06-07 | Claude AI 🤖 | aigw2026-cpu/claude-mcp-workspace*
