from fastmcp import FastMCP, Context
from pydantic import Field
from lib.list_packages import list_packages
import textwrap

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
        description=textwrap.dedent(
            """ Valid python code to run on the sandbox. 
        - Use \n to represent every line break in the code
        - Maintain exact indentation using spaces or tabs
        - Escape double quotes as \" inside JSON strings
        Example 1: for i in range(2):\n    if i > 0:\n        print(i)
        Example 2: import numpy as np\narr = np.array([[1, 2], [3, 4]])\nprint(arr.shape) """
        ),
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
