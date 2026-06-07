---
date: 2026-06-07
tags: [obsidian, sync-plus, setup, active]
status: active
plan: Sync Plus
renewal: 2026-06-24
account: aigw2026@gmail.com
---

# 🔄 Obsidian Sync Plus 설정 완전 가이드
> 계정: aigw2026@gmail.com | 플랜: Sync Plus (월간) | 갱신: 2026-06-24

---

## ✅ 현재 구독 상태 (확인 완료 2026-06-07)

| 항목 | 값 |
|------|-----|
| **플랜** | Sync Plus ✅ Active |
| **갱신 주기** | 월간 (연간 전환 시 20% 절약) |
| **다음 갱신** | 2026-06-24 |
| **Vault 수** | 10개 |
| **총 저장용량** | 10 GB |
| **최대 파일 크기** | 200 MB |
| **버전 히스토리** | 12개월 |
| **기기 수** | 무제한 |
| **공유 Vault** | 지원 |

**관리 URL**: https://obsidian.md/account/sync

---

## 🏗️ 전체 연동 아키텍처

```
╔════════════════════════════════════════════════════════╗
║           aigw2026의 Obsidian 생태계                   ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  [PC/Mac Obsidian] ←──── Obsidian Sync Plus ────→ [iPhone/iPad]
║       │                    (E2E 암호화)               [Android]
║       │                    10GB / 무제한 기기           ║
║       │                                                ║
║       ↕ obsidian-git 플러그인                          ║
║       │ (30분마다 자동 push/pull)                       ║
║       │                                                ║
║  [GitHub 레포]  ←──── GitHub Actions ────────────────→ ║
║  claude-mcp-workspace    (매일 자정 자동 실행)          ║
║       │                  Claude MCP Bot 자동 커밋       ║
║       │                                                ║
║       ↕ Claude Desktop MCP                            ║
║       │                                                ║
║  [Smithery Toolbox]                                    ║
║  Gmail / Calendar / Drive / Sheets / Notion            ║
╚════════════════════════════════════════════════════════╝
```

---

## 📱 기기별 설정 가이드

### Step 1: Mac/PC에서 Obsidian Sync 활성화

```
1. Obsidian 앱 열기
2. 설정(⚙️) → 계정 → 로그인 (aigw2026@gmail.com)
3. 설정 → 코어 플러그인 → Sync → 활성화
4. 동기화 대상 vault 선택 or 새 remote vault 생성
5. 동기화 설정:
   - [x] 에디터 설정
   - [x] 외관 설정 (테마)  
   - [x] 플러그인 (obsidian-git 등)
   - [x] 단축키
   - [x] 이미지/첨부파일 (선택)
```

### Step 2: iPhone/iPad에서 동기화 연결

```
1. App Store에서 Obsidian 다운로드 (무료)
2. 앱 실행 → "Sign in to sync" 선택
3. aigw2026@gmail.com 로그인
4. "Connect" → PC와 같은 remote vault 선택
5. 동기화 자동 시작
```

### Step 3: obsidian-git 플러그인 설정 (GitHub 이중 백업)

```
Obsidian 설정 → Community plugins → obsidian-git → 설정:
- Auto pull interval: 30 (분)
- Auto push interval: 30 (분)  
- Commit message: "🔄 obsidian: auto-sync {{date}}"
- Pull on startup: ✅
- Push on startup: ✅
```

**GitHub Personal Access Token 생성:**
```
1. github.com → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. 권한: repo (전체), workflow
4. 생성된 토큰 → obsidian-git 플러그인 설정에 입력
```

---

## 🔐 보안 설정 (Sync Plus E2E 암호화)

Obsidian Sync Plus는 **AES-256 엔드투엔드 암호화** 사용:
- 암호화 키는 로컬에서만 생성
- Obsidian 서버에서도 내용 읽기 불가
- 새 기기 연결 시 **암호화 암호(Encryption password)** 필요

> ⚠️ 암호화 암호는 안전한 곳에 보관 (분실 시 복구 불가)

---

## 📂 현재 Vault 구조 (claude-mcp-workspace)

```
obsidian-vault/
├── 00-Dashboard/
│   └── Home.md              ← Dataview 메인 대시보드
├── 01-Daily-Notes/
│   └── 2026/                ← 일일 노트 (자동 생성)
├── 02-Claude-MCP/
│   └── MCP-Setup-Guide.md   ← MCP 아키텍처 가이드
├── 03-Connectors/           ← 커넥터별 사용 기록
├── 04-Workflows/            ← 자동화 워크플로우
├── 05-Templates/
│   └── Daily-Note-Template.md ← Templater 템플릿
├── 06-Claude-Sessions/
│   └── 2026-06-07-MCP-Setup-Complete.md ← 세션 기록
└── 07-Setup-Guides/
    └── Obsidian-Sync-Plus-Setup.md ← 이 파일
```

---

## 🔄 이중 동기화 전략 (Sync Plus + GitHub)

| 전략 | Obsidian Sync Plus | GitHub obsidian-git |
|------|-------------------|---------------------|
| **목적** | 실시간 기기 간 동기화 | 버전 관리 + 공개 백업 |
| **속도** | 즉시 (실시간) | 30분마다 |
| **암호화** | AES-256 E2E | 없음 (Public repo) |
| **히스토리** | 12개월 | 무제한 |
| **복구** | Sync 대시보드 | git checkout |
| **비용** | $8/월 (Sync Plus) | 무료 |

> 💡 **전략**: Sync Plus로 실시간 기기 동기화 + GitHub으로 영구 백업 + 버전 관리

---

## ⚡ 연간 전환 시 절약 계산

```
현재: Sync Plus 월간 = $8/월 × 12개월 = $96/년
연간 전환: $8 × 0.8 × 12 = $76.8/년 (약 ₩102,000/년)
절약: $19.2/년 (약 ₩25,000)

전환 URL: https://obsidian.md/account/sync → "Switch to yearly"
```

---

## 🎯 즉시 해야 할 체크리스트

### Mac/PC (1순위)
- [ ] Obsidian 앱에서 aigw2026@gmail.com 로그인 확인
- [ ] Core plugin: Sync 활성화
- [ ] Remote vault: "claude-mcp-workspace" 선택/생성
- [ ] obsidian-git 플러그인 설치 및 GitHub 토큰 입력

### iPhone/iPad (2순위)  
- [ ] App Store에서 Obsidian 설치
- [ ] 계정 로그인 → 같은 remote vault 연결
- [ ] 동기화 완료 확인

### 검증 (3순위)
- [ ] Mac에서 노트 작성 → iPhone에서 즉시 반영 확인
- [ ] obsidian-git 자동 커밋 확인 (GitHub Actions 연동)
- [ ] 00-Dashboard/Home.md Dataview 쿼리 정상 작동 확인

---

## 🔗 유용한 링크

- **계정 관리**: https://obsidian.md/account
- **Sync 설정**: https://obsidian.md/account/sync  
- **청구 관리**: https://obsidian.md/account/billing
- **사용 가이드**: https://help.obsidian.md/Obsidian+Sync/Introduction+to+Obsidian+Sync
- **GitHub 레포**: https://github.com/aigw2026-cpu/claude-mcp-workspace

---

*2026-06-07 Claude AI 자동 생성 🤖 | Obsidian Sync Plus Active ✅*
