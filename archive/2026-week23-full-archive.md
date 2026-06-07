# 📚 2026년 6월 1주차 (Week 23) 전체 작업 아카이브
> Claude AI + Smithery MCP 구축 완전 기록 | aigw2026 | 2026-06-07

---

## 📊 이번 주 작업 요약

| 항목 | 내용 |
|------|------|
| **작업 기간** | 2026-06-01 ~ 2026-06-07 |
| **핵심 목표** | Claude MCP(Smithery) 커넥터 설정 + GitHub 백업 + Obsidian 자동화 |
| **완료율** | 92% (Slack 인증만 미완) |
| **생성 파일** | 15+ 파일, 13개 커밋 |
| **자동화 성공** | GitHub Actions Obsidian Vault Sync ✅ |

---

## 🏆 완료된 주요 작업 목록

### Phase 1: Smithery MCP 커넥터 인증 (5/6)
- [x] **Gmail** - Google OAuth 인증 완료, 23개 툴 활성화
- [x] **Google Calendar** - Composio OAuth, 28개 툴 활성화
- [x] **Google Drive** - Composio OAuth, 51개 툴 활성화
- [x] **Google Sheets** - Composio OAuth, 36개 툴 활성화
- [x] **Notion** - Notion OAuth 완료, 14개 툴 활성화
- [ ] **Slack** - Chrome 116 제약으로 미완 (최신 Chrome 필요)

**총 연결된 툴: 152개**

### Phase 2: GitHub 레포지토리 구조화
- [x] 레포 생성: `aigw2026-cpu/claude-mcp-workspace`
- [x] README.md - 전체 가이드 (커넥터 현황 테이블 포함)
- [x] claude_desktop_config.json - MCP 설정 파일
- [x] scripts/setup.sh - macOS/Linux 자동 설정 스크립트
- [x] scripts/test_connection.py - Python 연결 테스트
- [x] connectors/all_prompts.md - 서비스별 프롬프트 모음
- [x] workflows/morning_briefing.md - 아침 브리핑 자동화
- [x] FREE-API-GUIDE.md - API 키 무료 최대 활용 TOP 10

### Phase 3: Obsidian 연동 자동화
- [x] .obsidian/community-plugins.json (8개 플러그인)
- [x] .obsidian/plugins/obsidian-git/data.json (30분 자동 동기화)
- [x] .github/workflows/obsidian-sync.yml (GitHub Actions 핵심)
- [x] obsidian-vault/00-Dashboard/Home.md (Dataview 대시보드)
- [x] obsidian-vault/05-Templates/Daily-Note-Template.md
- [x] obsidian-vault/02-Claude-MCP/MCP-Setup-Guide.md

### Phase 4: 자동화 검증
- [x] GitHub Actions 수동 실행 → ✅ **Success (12초)**
- [x] Claude MCP Bot 자동 커밋 확인
- [x] Obsidian vault 자동 생성 폴더 확인

---

## 🔑 핵심 연결 정보

```
MCP 엔드포인트: https://mcp.smithery.run/aigw2026
Smithery 계정: aigw2026
GitHub 레포: aigw2026-cpu/claude-mcp-workspace
Obsidian Vault: obsidian-vault/ (레포 내부)
API Key (DEFAULT): ...3bd5
API Key (my-secret-key): ...3d13
```

---

## 🐛 해결된 오류들

| 오류 | 원인 | 해결 방법 |
|------|------|-----------|
| GitHub Actions exit code 127 | heredoc 내 bash 변수치환 오류 | Python subprocess 방식으로 전환 |
| Slack UI 미렌더링 | Chrome 116 구버전 UA | 브라우저 제약, 사용자 직접 처리 필요 |
| CodeMirror 삽입 실패 | 에디터 API 차이 | textarea + execCommand fallback |
| zoneinfo 모듈 오류 | Python 버전 차이 | datetime.timezone으로 대체 |

---

## 💡 이번 주 배운 핵심 인사이트

### MCP(Model Context Protocol)란?
- AI가 외부 서비스와 직접 연결되는 표준 프로토콜
- Smithery = MCP 커넥터 마켓플레이스
- Claude Desktop에서 실시간으로 Gmail, Calendar 등 제어 가능

### 자동화 구조
```
Claude Desktop
    └── Smithery Toolbox (mcp.smithery.run/aigw2026)
            ├── Gmail (23 tools)
            ├── Calendar (28 tools)
            ├── Drive (51 tools)
            ├── Sheets (36 tools)
            └── Notion (14 tools)
```

### GitHub Actions 자동화 흐름
```
main 브랜치 push
    └── obsidian-sync.yml 트리거
            ├── Python으로 일일 노트 생성
            ├── 대시보드 업데이트
            └── Claude MCP Bot으로 자동 커밋
```

---

## 📅 다음 주 계획

- [ ] Slack 인증 완료 (최신 Chrome 사용)
- [ ] GitHub Secret에 실제 API 키 등록
- [ ] Claude Desktop 설치 및 MCP 연결 테스트
- [ ] Obsidian 앱에서 obsidian-git 플러그인 설치
- [ ] 일일 노트 자동화 실사용 검증
- [ ] 아침 브리핑 워크플로우 실행 테스트

---

## 💰 예상 비용 분석

### 현재 무료 사용 중인 서비스
| 서비스 | 무료 한도 | 현재 사용량 | 비용 |
|--------|-----------|-------------|------|
| Smithery API | 무료 플랜 (현재 beta) | 152 tools | $0 |
| GitHub | Free 플랜 | Public repo, Actions 2000분/월 | $0 |
| Google APIs | OAuth 무료 | Gmail/Calendar/Drive | $0 |
| Notion API | Free 플랜 | 1000 API calls/일 | $0 |
| Obsidian | 무료 (로컬) | 로컬 vault | $0 |
| Claude AI (브라우저) | 구독 플랜 | 대화 | 기존 구독 포함 |

**현재 추가 비용: $0 (기존 Claude 구독 외 없음)**

### 확장 시 예상 비용 (선택사항)
| 항목 | 가격 | 필요성 |
|------|------|--------|
| Smithery Pro | $20/월 | 고급 커넥터, 우선 지원 필요 시 |
| Obsidian Sync | $10/월 | 여러 기기 sync 원할 경우 |
| GitHub Pro | $4/월 | Private repo Actions 분 추가 |
| Claude Pro | $20/월 | 현재 사용 중이면 이미 포함 |

---

*이 아카이브는 Claude AI가 자동 생성했습니다 🤖 | 2026-06-07*
