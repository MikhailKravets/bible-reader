import requests

from dataclasses import dataclass


DEFAULT_BIBLE_API_URL = "https://bible-api.com/"


@dataclass(frozen=True)
class Bible:
    reference: str
    translation_id: str
    translation_name: str
    translation_note: str
    text: str


class BibleReader:

    def __init__(self, url: str = DEFAULT_BIBLE_API_URL):
        self.url = url

    def get(self, book: str, chapter: int, verse: int):
        url = f"{DEFAULT_BIBLE_API_URL}{book}+{chapter}:{verse}"
        resp = requests.get(url, headers={'Content-Type': 'application/json'})

        data = resp.json()
        verses = data.pop('verses')
        # TODO: add verses to Bible dataclass
        return Bible(**data)
