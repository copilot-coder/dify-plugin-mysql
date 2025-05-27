from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class MysqlProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            from tools.db import DbManagerSingleton

            dbManager = DbManagerSingleton(
                host=credentials["host"],
                port=credentials["port"],
                user=credentials["user"],
                password=credentials["password"],
                database=credentials["database"],
            )
            dbManager.execute_sql("show tables")
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
