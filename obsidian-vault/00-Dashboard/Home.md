---
title: "🤖 Claude MCP Workspace — Obsidian Dashboard"
date: 2026-06-07
type: dashboard
tags: [dashboard, claude-mcp, home]
pinned: true
---

# 🤖 Claude MCP Workspace

> **계정**: aigw2026 | **MCP**: https://mcp.smithery.run/aigw2026
> 🔄 GitHub Actions로 자동 동기화 — push마다 최신 상태 유지

---

## 📊 커넥터 연결 현황

| 서비스 | 상태 | 기능 |
|---|---|---|
| Gmail | ✅ 완료 | 읽기, 초안 작성, 라벨 관리 |
| Google Calendar | ✅ 완료 | 일정 조회/생성/수정 |
| Google Drive | ✅ 완료 | 파일 읽기/쓰기/검색 |
| Google Sheets | ✅ 완료 | 데이터 읽기/쓰기/수식 |
| Notion | ✅ 완료 | 페이지 읽기/작성/검색 |
| Slack | ⏳ 설정 필요 | 메시지 읽기/전송 |

---

## 🗂️ Vault 구조

```
obsidian-vault/
├── 00-Dashboard/        ← 지금 여기
├── 01-Daily-Notes/      ← 날짜별 일일 노트 (자동생성)
├── 02-Claude-MCP/       ← MCP 설정 파일
├── 03-Connectors/       ← 커넥터별 프롬프트
├── 04-Workflows/        ← 자동화 워크플로우
├── 05-Templates/        ← 노트 템플릿
└── 06-Archive/          ← 보관된 노트
```

---

## ⚡ 자주 쓰는 Claude 프롬프트

### 아침 브리핑
```
오늘 캘린더 일정이랑 Gmail 중요 메일 요약해줘.
Notion에 오늘 날짜 일일 계획 페이지 만들어줘.
```

### 이메일 → Notion
```
오늘 Gmail에서 처리 필요한 메일을
Notion "받은업무" 데이터베이스에 추가해줘.
```

### 주간 리포트
```
이번 주 Calendar 일정 + Gmail + Notion 완료 항목으로
주간 리포트 Notion 페이지 만들어줘.
```

---

## 🔗 빠른 링크

- [[03-Connectors/all_prompts|📚 모든 프롬프트 모음]]
- [[04-Workflows/morning_briefing|🌅 아침 브리핑 가이드]]
- [[05-Templates/Daily-Note-Template|📝 일일 노트 템플릿]]
- [[05-Templates/Claude-Session-Template|🤖 Claude 세션 기록]]

---

## 📌 Dataview — 이번 주 일일 노트

```dataview
TABLE date, file.ctime as "생성시각"
FROM "01-Daily-Notes"
WHERE type = "daily-note"
SORT date DESC
LIMIT 7
```

---

## 📌 Dataview — Claude 세션 기록

```dataview
TABLE date, connectors-used as "사용 커넥터"
FROM "02-Claude-MCP" OR "03-Connectors"
WHERE type = "claude-session"
SORT date DESC
LIMIT 10
```

---

*🔄 자동 업데이트: GitHub Actions (push / 매일 자정)  
🐙 [GitHub 레포지토리](https://github.com/aigw2026-cpu/claude-mcp-workspace)*
