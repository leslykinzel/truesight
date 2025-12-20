from sgqlc.endpoint.http import HTTPEndpoint
from typing import Any


GRAPHQL_URL = "https://api.stratz.com/graphql"


class StratzAPIClient:

    def __init__(self, token: str):
        self._token = token

    def send_query(self, query: str, vars: dict[str, Any]) -> dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self._token}",
            "User-Agent": "STRATZ_API",
        }
        endpoint = HTTPEndpoint(GRAPHQL_URL, headers)
        response = endpoint(query, vars)
        if response is None:
            response = {"data": {}, "headers": {}}
        return response
