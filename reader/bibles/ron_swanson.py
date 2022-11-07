import typing
from functools import lru_cache

from reader.bibles import BaseReader
from reader.constants import MAX_CACHE_SIZE, DEFAULT_RON_SWANSON_API_URL
from reader.models import Bible, Verse


class RonSwansonReader(BaseReader):
    """Read Ron Swanson quites from remote API

    Args:
        url: base url to read data from
    """

    def __init__(self, url: str = DEFAULT_RON_SWANSON_API_URL):
        super().__init__(url)

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def get(self, term: str):
        url = self.prepare_url(term)
        return self.request(url)

    def prepare_url(self, term: str):
        return f"{self.url}/{term}"

    def prepare_response(self, data: typing.List[str]):
        return Bible(
            reference="Ron Swanson",
            translation_id=None,
            translation_name=None,
            translation_note="original",
            text=data[0] if len(data) else None,
            verses=[Verse(chapter=0, verse=0, text=v) for v in data]
        )
