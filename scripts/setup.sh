#!/bin/bash
# ============================================================
# Claude MCP Workspace - 자동 설정 스크립트 (macOS/Linux)
# 사용법: chmod +x setup.sh && ./setup.sh
# ============================================================

set -e

echo "🤖 Claude MCP Workspace 설정 시작..."
echo ""

# ── 색상 코드 ──
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# ── 1. Node.js 확인 ──
echo "${BLUE}[1/5]${NC} Node.js 확인 중..."
if ! command -v node &> /dev/null; then
    echo "${RED}❌ Node.js가 없습니다.${NC}"
    echo "   brew install node 또는 https://nodejs.org 에서 설치하세요."
    exit 1
fi
NODE_VERSION=$(node --version)
echo "${GREEN}✅ Node.js ${NODE_VERSION} 확인${NC}"

# ── 2. Claude Desktop 설정 폴더 확인 ──
echo "${BLUE}[2/5]${NC} Claude Desktop 설정 폴더 확인 중..."
CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
if [ ! -d "$CLAUDE_CONFIG_DIR" ]; then
    mkdir -p "$CLAUDE_CONFIG_DIR"
    echo "${YELLOW}📁 폴더 생성: $CLAUDE_CONFIG_DIR${NC}"
else
    echo "${GREEN}✅ 폴더 존재: $CLAUDE_CONFIG_DIR${NC}"
fi

# ── 3. API 키 입력 ──
echo "${BLUE}[3/5]${NC} Smithery API 키 설정"
echo ""
echo "${YELLOW}📌 API 키 확인 방법:${NC}"
echo "   1. https://smithery.ai/console/api-keys 접속"
echo "   2. 'DEFAULT' 키 복사"
echo ""
read -p "Smithery API 키를 입력하세요: " SMITHERY_API_KEY
echo ""

# ── 4. 설정 파일 생성 ──
echo "${BLUE}[4/5]${NC} claude_desktop_config.json 생성 중..."
cat > "$CLAUDE_CONFIG_DIR/claude_desktop_config.json" << EOF
{
  "mcpServers": {
    "smithery-toolbox": {
      "command": "npx",
      "args": [
        "-y",
        "@smithery/cli@latest",
        "run",
        "@smithery/toolbox",
        "--key",
        "$SMITHERY_API_KEY"
      ],
      "env": {
        "SMITHERY_PROFILE": "aigw2026"
      }
    }
  }
}
EOF
echo "${GREEN}✅ 설정 파일 생성 완료${NC}"

# ── 5. 완료 ──
echo ""
echo "${BLUE}[5/5]${NC} 설정 완료!"
echo ""
echo "${GREEN}================================================${NC}"
echo "${GREEN}✅ Claude MCP Workspace 설정 완료!${NC}"
echo "${GREEN}================================================${NC}"
echo ""
echo "다음 단계:"
echo "  1. Claude Desktop 앱 재시작"
echo "  2. 새 대화에서 🔌 아이콘 확인"
echo "  3. '내 Gmail 읽어줘'로 테스트"
echo ""
echo "${YELLOW}📌 연결된 서비스:${NC}"
echo "  ✅ Gmail"
echo "  ✅ Google Calendar"
echo "  ✅ Google Drive"
echo "  ✅ Google Sheets"
echo "  ✅ Notion"
echo "  ⏳ Slack (수동 설정 필요: https://smithery.run/aigw2026/slack/setup)"
