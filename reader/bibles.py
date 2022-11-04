from functools import lru_cache

import requests

from reader.constants import DEFAULT_BIBLE_API_URL, REQUEST_TIMEOUT, MAX_CACHE_SIZE
from reader.errors import APIError
from reader.models import Verse, Bible


class BibleReader:
    """Read bible verses from remote API

    Args:
        url: base url to read data from
    """

    def __init__(self, url: str = DEFAULT_BIBLE_API_URL):
        self.url = url

    @lru_cache(maxsize=MAX_CACHE_SIZE)
    def get(self, book: str, chapter: int, verse: int) -> Bible:
        """Get the data for the given book, chapter, and verse

        Args:
            book: bible book name
            chapter: chapter from bible
            verse: verse number

        Returns:
            Bible object containing the information
        """
        url = f"{DEFAULT_BIBLE_API_URL}{book}+{chapter}:{verse}"
        resp = requests.get(url, headers={'Content-Type': 'application/json'}, timeout=REQUEST_TIMEOUT)

        if not resp.ok:
            raise APIError(f"API error [{resp.status_code}]: {resp.json()}")

        data: dict = resp.json()
        data['verses'] = [Verse.from_dirty_dict(**v) for v in data['verses']]
        return Bible(**data)
