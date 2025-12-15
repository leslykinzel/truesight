from sgqlc.endpoint.http import HTTPEndpoint
from typing import Any


GRAPHQL_URL = "https://api.stratz.com/graphql"


class APIClient:

    def __init__(self, token):
        self._token = token

    def send_query(self, query: str, vars: dict[str, Any]):
        headers = {
            "Authorization": f"Bearer {self._token}",
            "User-Agent": "STRATZ_API",
        }
        endpoint = HTTPEndpoint(GRAPHQL_URL, )
        result = endpoint(query, vars)
        # just return this for now I will test how
        # to catch errors later... :)
        return result
