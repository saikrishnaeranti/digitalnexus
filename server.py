from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-company-server")

@mcp.tool()
def ping() -> str:
    """Health check — returns 'pong'."""
    return "pong"

if __name__ == "__main__":
    mcp.run()  # uses stdio transport by default
