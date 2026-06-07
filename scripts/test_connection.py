#!/usr/bin/env python3
"""
Claude MCP 연결 상태 테스트 스크립트
사용법: python3 test_connection.py --api-key YOUR_SMITHERY_API_KEY
"""

import json
import argparse
import urllib.request
import urllib.error
import sys

SMITHERY_PROFILE = "aigw2026"
TOOLBOX_API_URL = f"https://mcp.smithery.run/{SMITHERY_PROFILE}"

CONNECTORS = [
    {"name": "Gmail",            "id": "gmail"},
    {"name": "Google Calendar",  "id": "googlecalendar"},
    {"name": "Google Drive",     "id": "googledrive"},
    {"name": "Google Sheets",    "id": "googlesheets"},
    {"name": "Notion",           "id": "notion"},
    {"name": "Slack",            "id": "slack"},
]

def check_smithery_toolbox(api_key: str) -> dict:
    """Smithery Toolbox 상태 확인"""
    url = f"https://smithery.ai/api/v1/profiles/{SMITHERY_PROFILE}/toolbox"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def check_mcp_endpoint(api_key: str) -> bool:
    """MCP 엔드포인트 응답 확인"""
    url = TOOLBOX_API_URL
    headers = {"Authorization": f"Bearer {api_key}"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except Exception:
        return False

def print_status(name: str, ok: bool, detail: str = ""):
    icon = "✅" if ok else "❌"
    line = f"  {icon} {name}"
    if detail:
        line += f"  ({detail})"
    print(line)

def main():
    parser = argparse.ArgumentParser(description="Claude MCP 연결 테스트")
    parser.add_argument("--api-key", required=True, help="Smithery API 키")
    args = parser.parse_args()

    print()
    print("=" * 55)
    print("   🤖 Claude MCP Workspace - 연결 상태 테스트")
    print("=" * 55)
    print(f"   프로파일: {SMITHERY_PROFILE}")
    print(f"   MCP URL : {TOOLBOX_API_URL}")
    print("=" * 55)
    print()

    # ── MCP 엔드포인트 확인 ──
    print("🔌 MCP 엔드포인트 확인...")
    endpoint_ok = check_mcp_endpoint(args.api_key)
    print_status("Smithery MCP Endpoint", endpoint_ok, TOOLBOX_API_URL)
    print()

    # ── Toolbox 상태 확인 ──
    print("📦 Toolbox 서버 상태 확인...")
    toolbox_data = check_smithery_toolbox(args.api_key)
    if "error" in toolbox_data:
        print(f"  ⚠️  API 조회 실패: {toolbox_data['error']}")
        print(f"  💡 브라우저에서 직접 확인: https://smithery.ai/console/toolbox")
    else:
        servers = toolbox_data.get("servers", [])
        attention = [s for s in servers if s.get("needsAttention")]
        print_status("Toolbox 연결", True, f"서버 {len(servers)}개")
        if attention:
            print(f"  ⚠️  주의 필요: {[s['id'] for s in attention]}")
        else:
            print("  🎉 모든 서버 정상!")
    print()

    # ── 커넥터별 설정 안내 ──
    print("📋 커넥터 설정 가이드:")
    known_done = ["gmail", "googlecalendar", "googledrive", "googlesheets", "notion"]
    for c in CONNECTORS:
        is_done = c["id"] in known_done
        detail = "인증 완료" if is_done else "수동 설정 필요"
        setup_url = f"https://smithery.run/{SMITHERY_PROFILE}/{c['id']}/setup"
        print_status(c["name"], is_done, detail if is_done else setup_url)
    print()
    print("=" * 55)
    print("   다음 단계: Claude Desktop 앱 재시작 후 테스트")
    print("=" * 55)
    print()

if __name__ == "__main__":
    main()
