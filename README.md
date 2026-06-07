# 🤖 Claude MCP Workspace

> **Claude AI + Smithery MCP 커넥터 연결 완전 가이드**
> 계정: `aigw2026` | 생성일: 2026-06-07 | 상태: 5/6 연결 완료

---

## 📊 연결 현황

| 서비스 | 상태 | 기능 | 인증 방식 |
|---|---|---|---|
| Gmail | ✅ 완료 | 읽기, 초안 작성, 라벨 관리 | Google OAuth |
| Google Calendar | ✅ 완료 | 일정 조회/생성/수정 | Composio OAuth |
| Google Drive | ✅ 완료 | 파일 읽기/쓰기/검색 | Composio OAuth |
| Google Sheets | ✅ 완료 | 시트 읽기/쓰기/수식 | Composio OAuth |
| Notion | ✅ 완료 | 페이지 읽기/작성/검색 | Notion OAuth |
| Slack | ⏳ 수동 필요 | 메시지 읽기/전송 | Slack OAuth |

---

## 🚀 빠른 시작 (5분 설정)

### 1단계: Claude Desktop 앱 설치
```bash
# https://claude.ai/download 에서 다운로드
```

### 2단계: MCP 설정 파일 복사
macOS/Linux:
```bash
cp claude_desktop_config.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Windows:
```bash
copy claude_desktop_config.json %APPDATA%\Claude\claude_desktop_config.json
```

### 3단계: API 키 입력
`claude_desktop_config.json` 파일에서 `YOUR_SMITHERY_API_KEY_HERE` 부분을 실제 키로 교체:
- Smithery API 키 확인: https://smithery.ai/console/api-keys

### 4단계: Claude Desktop 재시작
앱을 재시작하면 모든 커넥터가 자동으로 연결됩니다.

---

## 📁 파일 구조

```
claude-mcp-workspace/
├── README.md                    # 이 파일 (전체 가이드)
├── claude_desktop_config.json   # Claude Desktop MCP 설정
├── connectors/
│   ├── gmail_examples.md        # Gmail 활용 예제 프롬프트
│   ├── calendar_examples.md     # Calendar 활용 예제
│   ├── sheets_examples.md       # Sheets 활용 예제
│   ├── notion_examples.md       # Notion 활용 예제
│   └── slack_setup.md           # Slack 수동 설정 가이드
├── scripts/
│   ├── setup.sh                 # 자동 설정 스크립트 (macOS)
│   └── test_connection.py       # 연결 상태 테스트 스크립트
└── workflows/
    ├── morning_briefing.md      # 아침 브리핑 자동화 워크플로우
    ├── email_assistant.md       # 이메일 관리 워크플로우
    └── daily_notes.md           # Notion 일일 노트 자동화
```

---

## 💡 활용 예제

### 아침 브리핑 자동화
Claude에게 다음과 같이 요청하세요:
```
오늘 Google Calendar 일정 확인하고, 읽지 않은 중요 Gmail 요약해줘.
Notion에 오늘 날짜로 일일 계획 페이지 만들어줘.
```

### 이메일 → Notion 정리
```
오늘 받은 Gmail 중 답장 필요한 것들을 Notion "받은업무" 데이터베이스에 추가해줘.
우선순위: 높음/중간/낮음으로 분류해줘.
```

### Google Sheets 데이터 분석
```
"2026매출데이터" 시트에서 이번 달 데이터 가져와서 
월별 트렌드 분석하고 요약해줘.
```

---

## 🔧 MCP 엔드포인트 정보

| 항목 | 값 |
|---|---|
| MCP URL | `https://mcp.smithery.run/aigw2026` |
| Smithery 네임스페이스 | `aigw2026` |
| Toolbox 대시보드 | https://smithery.ai/console/toolbox |
| API Keys 관리 | https://smithery.ai/console/api-keys |

---

## 📚 참고 자료

- [MCP 공식 문서](https://modelcontextprotocol.io)
- [Smithery 서버 목록](https://smithery.ai/servers) — 200개+ 커넥터
- [Claude Desktop 다운로드](https://claude.ai/download)
- [Smithery Toolbox 관리](https://smithery.ai/console/toolbox)

---

## 🔑 Slack 수동 설정 (마지막 단계)

1. 최신 Chrome 브라우저에서 https://smithery.run/aigw2026/slack/setup 접속
2. Slack 워크스페이스 URL 또는 이메일(`aigw2026@gmail.com`) 입력
3. Slack 로그인 → Composio "Allow" 클릭
4. `smithery.ai/oauth-callback?success=true` 확인
5. [Smithery Toolbox](https://smithery.ai/console/toolbox)에서 "0 servers need attention" 확인

---

*이 레포지토리는 Claude AI와 함께 자동으로 생성되었습니다 🤖*
*Last updated: 2026-06-07*
