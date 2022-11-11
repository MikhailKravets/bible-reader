import typing
from functools import lru_cache

from reader.bibles import BaseReader
from reader.constants import MAX_CACHE_SIZE, DEFAULT_OFFICE_API_URL
from reader.models import Bible, Verse


class TheOfficeReader(BaseReader):

    def __init__(self, url: str = DEFAULT_OFFICE_API_URL):
        super().__init__(url)

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def get(self):
        url = self.prepare_url()
        return self.request(url)

    def prepare_url(self):
        return f"{self.url}/quotes/random"

    def prepare_response(self, data: typing.List[str]):
        """Use standard Bible model but fill
        the attribute ourselves

        Args:
            data: data to parse and to write into Bible

        Returns:
            Bible instance
        """
        return Bible(
            reference=f"{data['data']['character']['firstname']} {data['data']['character']['lastname']}",
            translation_id=data['data']['character']['_id'],
            translation_name=None,
            translation_note="original",
            text=data['data']['content'],
            verses=[Verse(chapter=0, verse=0, text=data['data']['content'])]
        )
