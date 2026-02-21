from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `search_users`
        return "search_users"

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return "Tool to search for users based on various criteria"

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - name: str
        # - surname: str
        # - email: str
        # - gender: str
        # None of them are required (see UserClient.search_users method)
        return {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "First name of the user"},
                "surname": {"type": "string", "description": "Last name of the user"},
                "email": {"type": "string", "description": "Email address of the user"},
                "gender": {"type": "string", "description": "Gender of the user"}
            },
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # Call user_client search_users (with `**arguments`) and return its results (it is async, don't forget to await)
        result = await self._user_client.search_users(**arguments)
        return result