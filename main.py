from fastmcp import FastMCP, Context
from pydantic import Field
from lib.list_packages import list_packages

mcp = FastMCP(name="Python Code Sandbox MCP Server")


@mcp.tool(name="python.list_packages")
async def list_packages_tool(
    ctx: Context,
) -> str:
    """List all available python packages in the sandbox."""

    packages = list_packages()
    return packages


@mcp.tool(name="python.exec")
async def list_packages_tool(
    ctx: Context,
    code=Field(
        ...,
        description=""" Valid python code to run on the sandbox. Example: import numpy as np\narr = np.array([[1, 2], [3, 4]])\nprint(arr.shape) """,
    ),
) -> str:
    """Execute python code using exec() function."""

    try:
        import io
        import sys

        output = io.StringIO()
        sys.stdout = output
        exec(code)
        sys.stdout = sys.__stdout__
        return output.getvalue()
    except Exception as e:
        return f"Error executing code: {e}"
