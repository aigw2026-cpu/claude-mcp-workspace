# 🧪 검증 및 테스트 가이드
> Claude MCP Workspace 전체 시스템 검증 체크리스트 | 2026-06-07

---

## ✅ 검증 단계 1: GitHub 레포 구조 확인

### 파일 구조 검증
아래 URL에서 각 파일이 존재하는지 확인:
```
https://github.com/aigw2026-cpu/claude-mcp-workspace
```

**필수 파일 체크리스트:**
- [ ] README.md (전체 가이드)
- [ ] BUDGET-AND-COSTS.md (비용 분석)
- [ ] FREE-API-GUIDE.md (API 활용법)
- [ ] claude_desktop_config.json (MCP 설정)
- [ ] scripts/setup.sh (자동 설정)
- [ ] scripts/test_connection.py (연결 테스트)
- [ ] connectors/all_prompts.md (프롬프트 모음)
- [ ] workflows/morning_briefing.md (브리핑 자동화)
- [ ] .github/workflows/obsidian-sync.yml (자동화 핵심)
- [ ] obsidian-vault/ (Obsidian 볼트 폴더)
- [ ] archive/2026-week23-full-archive.md (이번 주 아카이브)

### GitHub Actions 검증
1. https://github.com/aigw2026-cpu/claude-mcp-workspace/actions 접속
2. "Obsidian Vault Sync" 워크플로우 확인
3. 최근 실행이 ✅ 녹색인지 확인
4. 커밋 기록에 "Claude MCP Bot" 자동 커밋 있는지 확인

---

## ✅ 검증 단계 2: Smithery Toolbox 확인

### 접속 URL
```
https://smithery.ai/console/toolbox
```

### 확인 항목
- [ ] **6 connectors** 표시 (상단)
- [ ] **152 tools** 표시 (상단)
- [ ] Gmail: ✅ 활성화 (23 tools)
- [ ] Google Calendar: ✅ 활성화 (28 tools)
- [ ] Google Drive: ✅ 활성화 (51 tools)
- [ ] Google Sheets: ✅ 활성화 (36 tools)
- [ ] Notion: ✅ 활성화 (14 tools)
- [ ] Slack: ⚠️ "Authenticate" 버튼 (미완)

### API 키 확인
```
https://smithery.ai/console/api-keys
```
- [ ] DEFAULT 키 (...3bd5) 활성화 상태
- [ ] my-secret-key (...3d13) 활성화 상태

---

## ✅ 검증 단계 3: Claude Desktop MCP 연결 테스트

### 설치 확인
1. https://claude.ai/download 에서 Claude Desktop 다운로드
2. 앱 설치 완료 확인

### MCP 설정
1. Smithery API 키 복사: https://smithery.ai/console/api-keys
2. claude_desktop_config.json 다운로드 또는 복사
3. YOUR_SMITHERY_API_KEY_HERE → 실제 키로 교체
4. 파일 위치:
   ```bash
   # macOS
   ~/Library/Application Support/Claude/claude_desktop_config.json
   
   # Windows
   %APPDATA%\Claude\claude_desktop_config.json
   ```
5. Claude Desktop 재시작

### 기능 테스트 프롬프트

**테스트 1: Gmail 연결 확인**
```
오늘 받은 이메일 중 읽지 않은 것 3개만 요약해줘
```
예상 결과: Claude가 Gmail에서 이메일 목록 가져와서 요약

**테스트 2: Calendar 연결 확인**
```
오늘 내 일정 알려줘
```
예상 결과: Google Calendar에서 오늘 일정 목록 반환

**테스트 3: Notion 연결 확인**
```
내 Notion 워크스페이스에 접근 가능한 페이지 목록 알려줘
```
예상 결과: Notion 페이지/데이터베이스 목록 반환

**테스트 4: Drive + Sheets 연결 확인**
```
내 Google Drive에서 최근 수정된 파일 5개 알려줘
```
예상 결과: Drive 파일 목록 반환

**테스트 5: 통합 자동화 테스트**
```
오늘 날짜로 Notion에 일일 계획 페이지 만들어줘.
페이지 제목: "2026-06-07 일일 계획"
내용에 오늘 Google Calendar 일정 포함시켜줘
```
예상 결과: Notion에 새 페이지 자동 생성, Calendar 일정 포함

---

## ✅ 검증 단계 4: GitHub Secret 등록 (중요!)

### 등록 방법
1. https://github.com/aigw2026-cpu/claude-mcp-workspace/settings/secrets/actions/new 접속
2. **Name**: `SMITHERY_API_KEY`
3. **Secret**: smithery.ai/console/api-keys 에서 DEFAULT 키(...3bd5) 전체 복사
4. "Add secret" 클릭

### 등록 후 확인
- [ ] https://github.com/aigw2026-cpu/claude-mcp-workspace/settings/secrets/actions 에서 SMITHERY_API_KEY 보임
- [ ] GitHub Actions 재실행 후 Obsidian 자동화 정상 작동

---

## ✅ 검증 단계 5: Obsidian 앱 연동

### Obsidian 설정
1. https://obsidian.md 에서 무료 다운로드
2. "Open folder as vault" → `claude-mcp-workspace` 폴더 선택
   (GitHub 클론한 로컬 폴더)
3. Community plugins 활성화:
   - Settings → Community plugins → Turn on community plugins
4. 필수 플러그인 설치:
   - **obsidian-git**: 30분마다 자동 GitHub 동기화
   - **dataview**: 대시보드 쿼리
   - **templater**: 템플릿 자동화

### 클론 명령어
```bash
git clone https://github.com/aigw2026-cpu/claude-mcp-workspace.git
cd claude-mcp-workspace
# obsidian-vault 폴더를 Obsidian에서 vault로 열기
```

### 검증 체크
- [ ] obsidian-vault/00-Dashboard/Home.md 열림
- [ ] obsidian-vault/01-Daily-Notes/2026/ 폴더 존재
- [ ] obsidian-vault/05-Templates/Daily-Note-Template.md 존재
- [ ] obsidian-git 플러그인 "Last sync" 표시

---

## 🔧 문제 해결 (Troubleshooting)

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| Claude Desktop에서 MCP 툴 안 보임 | 설정 파일 경로 오류 | JSON 파일 위치 재확인, 앱 재시작 |
| GitHub Actions 실패 | Secret 미등록 | SMITHERY_API_KEY Secret 등록 |
| Obsidian-git 동기화 안 됨 | Git 자격증명 없음 | GitHub Personal Access Token 설정 |
| Smithery 연결 끊김 | OAuth 토큰 만료 | Toolbox에서 "Reauthenticate" 클릭 |
| Notion 페이지 못 가져옴 | 권한 범위 제한 | Notion integration 재인증 |

---

## 📋 전체 체크리스트 요약

### 즉시 완료 가능 (지금 바로)
- [ ] GitHub Secret 등록 (SMITHERY_API_KEY)
- [ ] GitHub Actions 재실행 확인

### 1시간 내 완료
- [ ] Claude Desktop 설치 + API 키 설정
- [ ] MCP 기능 테스트 (5가지 프롬프트)

### 오늘 중 완료
- [ ] Obsidian 설치 + vault 연동
- [ ] 일일 노트 자동화 첫 실행 확인

### 이번 주 중
- [ ] Slack 인증 (최신 Chrome에서 직접)
- [ ] 아침 브리핑 루틴 시작

---

*2026-06-07 Claude AI 자동 생성 🤖 | aigw2026-cpu/claude-mcp-workspace*
