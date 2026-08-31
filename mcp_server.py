from fastmcp import FastMCP
import httpx

mcp = FastMCP("app_checkin")

SUPABASE_URL = "https://hgnwdttdbzhlbaxnfpgm.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhnbndkdHRkYnpobGJheG5mcGdtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODgxODcxNDIsImV4cCI6MjEwMzc2MzE0Mn0.hfEQln9GIy-ul6F4rlDVstmjhs0tSlpvwWkvhdZCwss"

@mcp.tool()
def query_app_usage(start: str, end: str) -> str:
    """查询某时间段内用户打开App的记录"""
    url = f"{SUPABASE_URL}/rest/v1/app_usage?ts=gte.{start}&ts=lte.{end}&select=app,event,ts&order=ts.asc"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    resp = httpx.get(url, headers=headers)
    return resp.text

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8001)
