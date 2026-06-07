---
date: 2026-06-07
tags: [claude, mcp, obsidian, integration, workflow]
status: active
obsidian_plan: Sync Plus
smithery_tools: 152
---

# 🤖 Claude MCP + Obsidian Sync Plus 완전 통합 가이드
> aigw2026 | 2026-06-07 | 구축 완료 및 운영 중

---

## 🏆 통합 목표

Claude AI가 Obsidian vault를 직접 읽고 쓰는 완전 자동화 시스템:
1. **Claude → Obsidian**: 대화 중 생성된 내용을 Obsidian에 자동 저장
2. **Obsidian → Claude**: vault의 노트를 컨텍스트로 활용
3. **GitHub Actions**: 매일 자동 동기화 + 일일 노트 생성
4. **Obsidian Sync Plus**: 모든 기기에서 즉시 접근

---

## ⚙️ 현재 구성된 자동화 레이어

### Layer 1: GitHub Actions (서버사이드 자동화)
```yaml
트리거: 매일 자정(KST) + 수동 실행
작업:
  - 오늘 날짜 일일 노트 자동 생성
  - frontmatter 자동 주입 (date, tags, weather placeholder)
  - 대시보드 업데이트
  - Claude MCP Bot으로 커밋
결과: GitHub 레포에 자동 커밋
```

### Layer 2: Obsidian Sync Plus (기기 간 동기화)
```
GitHub 커밋 → obsidian-git 자동 pull → Obsidian Sync Plus → 모든 기기 반영
속도: 즉시 (Sync Plus 실시간) + 30분마다 (obsidian-git)
```

### Layer 3: Claude Desktop MCP (AI 제어)
```
Claude Desktop → Smithery Toolbox → 152개 툴
  ├── Gmail: 이메일 읽기/작성
  ├── Calendar: 일정 관리
  ├── Drive: 파일 접근
  ├── Sheets: 데이터 분석
  └── Notion: 페이지 관리
```

---

## 📋 실전 워크플로우 레시피

### 🌅 아침 루틴 (Claude Desktop 사용)
```
프롬프트 1개로 전체 실행:
"오늘 아침 브리핑:
1. Gmail 읽지 않은 이메일 중 중요한 것 요약
2. 오늘 Google Calendar 일정 목록
3. 오늘 날짜로 Obsidian 일일 노트에 위 내용 추가해줘
   파일: obsidian-vault/01-Daily-Notes/2026/2026-06-07.md"
```

### 📧 이메일 → Obsidian 정리
```
"오늘 받은 Gmail 중 답장 필요한 것들을
obsidian-vault/03-Connectors/Gmail-Tasks.md 파일에 추가해줘.
형식: - [ ] [발신자] 제목 (마감일 있으면 포함)"
```

### 📊 주간 리뷰 자동화
```
"이번 주 Google Calendar 일정과 완료된 Gmail을 분석해서
obsidian-vault/01-Daily-Notes/2026/2026-W23-Weekly-Review.md 로 작성해줘"
```

### 🗺️ Notion → Obsidian 이전
```
"내 Notion의 '할일' 데이터베이스에서 미완료 항목들을
obsidian-vault/08-Tasks/From-Notion.md 로 가져와줘"
```

---

## 🔧 기술 스택 상세

### obsidian-git 플러그인 설정값
```json
{
  "commitMessage": "🔄 obsidian: auto-sync {{date}}",
  "autoSaveInterval": 30,
  "autoPullInterval": 30,
  "autoPushInterval": 30,
  "pullBeforePush": true,
  "disablePopups": false,
  "listChangedFilesInMessageBody": true,
  "showStatusBar": true,
  "gitDir": "",
  "commitDateFormat": "YYYY-MM-DD HH:mm:ss"
}
```

### GitHub Actions 워크플로우 핵심
```python
# obsidian-sync.yml 에서 실행되는 Python 코드
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
now = datetime.now(KST)
date_str = now.strftime("%Y-%m-%d")

# 일일 노트 생성
note_content = f"""---
date: {date_str}
tags: [daily-note, auto-generated]
created_by: claude-mcp-bot
---

# {date_str} 일일 노트

## 📅 오늘의 계획
- [ ] 아침 브리핑 확인 (Claude Desktop)
- [ ] 주요 이메일 처리
- [ ] 일정 확인

## 📝 메모
(Claude Desktop으로 자동 채우기)

## 🌙 오늘의 회고
(저녁에 작성)
"""
```

---

## 📱 Obsidian Sync Plus 기기별 현황

| 기기 | 상태 | 연결 방법 |
|------|------|-----------|
| Mac/PC | 설정 필요 | Obsidian → 설정 → Sync 활성화 |
| iPhone | 설정 필요 | App Store → Obsidian → 로그인 |
| iPad | 설정 필요 | App Store → Obsidian → 로그인 |
| Android | 선택 | Google Play → Obsidian → 로그인 |

**모든 기기에서 같은 계정(aigw2026@gmail.com) 로그인 → 자동 동기화**

---

## 🚀 즉시 실행 가능한 것들

### 지금 바로 (GitHub Actions 자동화 이미 작동 중)
- ✅ 매일 자정 일일 노트 자동 생성
- ✅ 대시보드 자동 업데이트
- ✅ obsidian-vault 폴더에 자동 파일 추가

### Obsidian 앱 설치 후 즉시 사용
- obsidian-vault/00-Dashboard/Home.md → Dataview 대시보드
- obsidian-vault/01-Daily-Notes/2026/ → 자동 생성된 일일 노트
- obsidian-vault/06-Claude-Sessions/ → Claude 세션 기록

### Claude Desktop 설치 후 즉시 사용
- Gmail 읽기 + Obsidian 노트 작성 통합
- Calendar → 일일 노트 자동 채우기
- Sheets 데이터 → Obsidian 분석 노트 생성

---

## 💡 고급 활용: Dataview 쿼리 예시

### 미완료 할일 전체 조회
```dataview
TASK
WHERE !completed
SORT file.mtime DESC
LIMIT 20
```

### 이번 주 Claude 세션 기록
```dataview
TABLE date, tags, status
FROM "06-Claude-Sessions"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

### 커넥터 사용 현황
```dataview
TABLE status, smithery_tools
FROM "07-Setup-Guides"
SORT date DESC
```

---

## 📊 비용 요약

| 서비스 | 월 비용 | 역할 |
|--------|---------|------|
| Obsidian Sync Plus | $8/월 | 기기 간 실시간 동기화 |
| GitHub (Free) | $0 | 버전 관리 + Actions |
| Smithery (Beta) | $0 | Claude MCP 152 tools |
| **합계** | **$8/월** | 전체 자동화 생태계 |

> 연간 결제 전환 시: $6.4/월 × 12 = $76.8/년 (20% 절약)

---

*2026-06-07 Claude AI 자동 생성 🤖*
*다음 갱신: 2026-06-24 (Obsidian Sync Plus 월간)*
