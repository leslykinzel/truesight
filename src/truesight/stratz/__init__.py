from sgqlc.endpoint.http import HTTPEndpoint
from typing import Any, Optional
from enum import Enum
from truesight.gql import Query, GQL


GRAPHQL_URL = "https://api.stratz.com/graphql"


class Language(Enum):
    ENGLISH    = "ENGLISH"
    BRAZILIAN  = "BRAZILIAN"
    BULGARIAN  = "BULGARIAN"
    CZECH      = "CZECH"
    DANISH     = "DANISH"
    DUTCH      = "DUTCH"
    FINNISH    = "FINNISH"
    FRENCH     = "FRENCH"
    GERMAN     = "GERMAN"
    GREEK      = "GREEK"
    HUNGARIAN  = "HUNGARIAN"
    ITALIAN    = "ITALIAN"
    JAPANESE   = "JAPANESE"
    KOREAN     = "KOREAN"
    KOREANA    = "KOREANA"
    NORWEGIAN  = "NORWEGIAN"
    POLISH     = "POLISH"
    PORTUGUESE = "PORTUGUESE"
    ROMANIAN   = "ROMANIAN"
    RUSSIAN    = "RUSSIAN"
    S_CHINESE  = "S_CHINESE"
    SPANISH    = "SPANISH"
    SWEDISH    = "SWEDISH"
    T_CHINESE  = "T_CHINESE"
    THAI       = "THAI"
    TURKISH    = "TURKISH"
    UKRAINIAN  = "UKRAINIAN"


class StratzAPIClient:
    """ Client to manage requests to api.stratz.com/graphql
    """

    def __init__(self, token: str):
        self._token = token
        self._header = StratzAPIClient.std_header(token)

    @staticmethod
    def std_header(token: Optional[str]):
        """ This is all that is required in the
            header according to stratz own docs
        """
        return {
            "Authorization": f"Bearer {token if token else 'your_token_here'}",
            "User-Agent": "STRATZ_API",
        }

    def send_query(self, query: str, vars: Optional[dict[str, Any]]) -> dict[str, Any]:
        """ Send a rendered GQL query to the stratz api
        """
        endpoint = HTTPEndpoint(GRAPHQL_URL, self._header)
        response = endpoint(query, vars)
        if response is None:
            response = {"data": {}, "headers": {}}
        return response

    def get_all_hero_metadata(self, dota2_version_id: int, lang: str = Language.ENGLISH.value):
        """ This returns a map can than be used to find hero names based on their in-game identifiers.

            - dota2_version_id: int - If you want 7.39, just pass 739.
            - lang: Language        - Doesn't seem to change much, depends what stratz bothers to record.
        """
        query = Query(
            GQL(
                "constants",
                fields=[
                    GQL(
                        name="heroes",
                        args={ "gameVersionId": dota2_version_id, "language": lang },
                        fields=[
                            GQL("id"),
                            GQL("name"),
                            GQL("displayName"),
                            GQL("shortName"),
                            GQL("aliases")
                        ]
                    )
                ]
            )
        )
        return self.send_query(query.render(), {})

