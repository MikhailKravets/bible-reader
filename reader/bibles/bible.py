import typing
from functools import lru_cache

from reader.bibles import BaseReader
from reader.constants import DEFAULT_BIBLE_API_URL, MAX_CACHE_SIZE
from reader.models import Bible, Verse


class BibleReader(BaseReader):
    """Read bible verses from remote API

    Args:
        url: base url to read data from
    """

    def __init__(self, url: str = DEFAULT_BIBLE_API_URL):
        super().__init__(url)

    def get(self, book: str, chapter: int, verse: int) -> Bible:
        """Get the data for the given book, chapter, and verse

        Args:
            book: bible book name
            chapter: chapter from bible
            verse: verse number

        Returns:
            Bible object containing the information
        """
        url = self.prepare_url(book, chapter, verse)
        return self.request(url)

    def prepare_url(self, book: str, chapter: int, verse: int):
        return f"{self.url}{book}+{chapter}:{verse}"

    def prepare_response(self, data: typing.Dict[str, typing.Any]):
        data['verses'] = [Verse.from_dirty_dict(**v) for v in data['verses']]
        return Bible(**data)
