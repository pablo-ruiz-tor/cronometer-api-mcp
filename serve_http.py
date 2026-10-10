"""Serve the Cronometer MCP server over HTTP in one long-lived process."""

import os

from starlette.responses import PlainTextResponse

from cronometer_api_mcp.server import mcp


@mcp.custom_route("/healthz", methods=["GET"])
async def healthz(request):
    return PlainTextResponse("ok")


mcp.run(
    transport="streamable-http",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "8080")),
    streamable_http_path=os.environ["MCP_SECRET_PATH"],
    stateless_http=True,
)
