from collections.abc import Generator
from typing import Any
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from tools.db import DbManagerSingleton


class GetTableDefinitionTool(Tool):
    def __init__(self, runtime, session):
        super().__init__(runtime, session)
        self.dbManager = DbManagerSingleton(
            host=runtime.credentials["host"],
            port=runtime.credentials["port"],
            user=runtime.credentials["user"],
            password=runtime.credentials["password"],
            database=runtime.credentials["database"],
        )

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        table = tool_parameters["table"]
        sql = f"show create table {table}"
        yield self.create_text_message(self.dbManager.execute_sql(sql))
