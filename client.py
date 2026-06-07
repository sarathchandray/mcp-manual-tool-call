import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (
        read_stream,
        write_stream,
    ):

        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("\nAvailable Tools:")
            for tool in tools.tools:
                print(tool.name)

            result = await session.call_tool(
                "add",
                {
                    "a": 10,
                    "b": 20
                }
            )

            print("\nResult:")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())